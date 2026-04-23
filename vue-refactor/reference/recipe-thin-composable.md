# 处方 C：Thin Composable 提纯

把 composable 里的业务逻辑（纯计算、纯转换、纯决策）抽成纯函数放到 `lib/`，让 composable 只剩一层薄薄的响应式壳：解包 ref → 调纯函数 → 塞回 ref。

**适用信号**：composable 里业务计算和 `ref / watch / computed` 混写 / 单测业务逻辑必须 mount 或 mock reactivity / 同一份计算在多处各抄一份 / 能一眼指出"这几行不依赖任何 ref，就是纯计算"。

**核心收益**：纯函数可以零依赖单测、业务逻辑和 Vue 解耦（未来换框架可带走）、composable 代码量骤减。

---

## 开始前的心智模型

薄 composable 结构长这样：

```ts
// lib/cart.ts —— 纯 TS，零 Vue
export function calculateDiscount(cart: Cart, rules: DiscountRules): Discount {
  // 纯计算，无副作用，无响应式
}

// composables/useCart.ts —— 薄壳
import { ref, computed, watch } from 'vue'
import { calculateDiscount } from '@/lib/cart'

export function useCart() {
  const cart = ref<Cart>(...)
  const rules = ref<DiscountRules>(...)

  const discount = computed(() => calculateDiscount(cart.value, rules.value))

  return { cart, rules, discount }
}
```

要诀：**纯函数签名是"普通值 → 普通值"，完全不碰 ref / reactive / computed / watch**。composable 壳负责在响应式和纯计算之间搭桥。

---

## 起步：识别纯计算块

扫一遍 composable（或胖组件的 `<script setup>`），找满足以下条件的代码块：

- **无副作用**：不 fetch、不改 store、不碰 router、不动 localStorage、不触发 emit
- **无响应式依赖**：函数体内不 `.value`、不用 ref / reactive / watch（参数可以是普通值）
- **可测性直觉**：如果把这段代码搬到一个普通 .ts 文件里当函数调，它应该能单独跑

常见候选：
- 校验：`validateEmail(s)`、`validateForm(formData)`
- 计算：`calculateTotal(items)`、`calculateDiscount(cart, rules)`
- 格式化：`formatPrice(n, currency)`、`formatDate(d, locale)`
- 状态转换：`nextStep(currentStep, inputs)`、`mergeRows(existing, incoming)`
- 决策：`canEdit(user, resource)`、`shouldShowWarning(status)`

**不是候选**的：调 API 包一层的（`fetchUser()`）、改响应式状态的（`increment()`）、注册生命周期的。

---

## 搬运节拍

### Step 1：把一段逻辑先抽成 composable 内部的局部函数

找到候选代码块。在 composable 内部**先抽成一个局部函数**，还不往外搬：

**重构前**：
```ts
export function useCart() {
  const cart = ref<Cart>(...)
  const discount = computed(() => {
    // 大段计算逻辑
    const subtotal = cart.value.items.reduce(...)
    const rule = matchRule(cart.value, ...)
    return rule.apply(subtotal)
  })
  return { cart, discount }
}
```

**重构后（第一步）**：
```ts
export function useCart() {
  const cart = ref<Cart>(...)

  function computeDiscount(cartValue: Cart): Discount {
    // 同样的大段计算逻辑，但参数是普通值
    const subtotal = cartValue.items.reduce(...)
    const rule = matchRule(cartValue, ...)
    return rule.apply(subtotal)
  }

  const discount = computed(() => computeDiscount(cart.value))
  return { cart, discount }
}
```

这一步的**关键**：把计算体从 computed 里剪出来，改成接普通值参数的函数。可能需要把原来读 `cart.value` 的地方改成读 `cartValue` 参数。

**编译必须绿**。肉眼验：`computed` 触发的结果没变。

提 commit：`refactor: extract computeDiscount as local pure fn in useCart`。

### Step 2：确认函数真的"纯"

检查刚抽的 `computeDiscount`：

- [ ] 函数体里**没有** `.value`
- [ ] 函数体里**没有** `ref` / `reactive` / `computed` / `watch` / `watchEffect`
- [ ] 函数体里**没有**副作用（改外部 state、调 API、触发 emit、操作 DOM）
- [ ] 函数的参数都是普通值类型（不是 Ref<T>）
- [ ] 函数的返回值都是普通值

**任一不满足**说明"纯计算"的边界没划对——要么这段逻辑本来就不纯（那就不适合提纯，放弃这段），要么边界没划干净（比如漏抽了一个依赖，或多抽了副作用部分）。

**不纯的常见情况**：
- 函数体里还在调一个 `useOtherComposable()` —— 那整个都不纯
- 函数体里 `watch` 了某个 ref —— 明显违反
- 函数体里 `cart.value.items.push(...)` —— 改了传入对象的内部（这是副作用，传入的是同一引用）

如果发现不纯，把这段代码**退回 Step 0**，不做提纯，考虑是不是应该留在壳里。

### Step 3：搬到 `lib/`

确认纯了之后，在 `src/lib/` 下（或你项目约定的位置）建一个对应的文件，比如 `src/lib/cart.ts`：

```ts
export function computeDiscount(cart: Cart): Discount {
  // 和 composable 内部那份一模一样
}
```

在 composable 里：
```ts
import { computeDiscount } from '@/lib/cart'

export function useCart() {
  const cart = ref<Cart>(...)
  // 删掉局部 function computeDiscount
  const discount = computed(() => computeDiscount(cart.value))
  return { cart, discount }
}
```

**编译必须绿**。提 commit：`refactor: move computeDiscount to lib/cart`。

### Step 4：补单测（可选但强烈建议）

纯函数搬到 `lib/` 后它终于"能测"了。写一个 `lib/cart.test.ts`：

```ts
import { describe, it, expect } from 'vitest'
import { computeDiscount } from './cart'

describe('computeDiscount', () => {
  it('applies percentage rule to subtotal', () => {
    const result = computeDiscount({ items: [{ price: 100, qty: 2 }], ruleId: 'PCT10' })
    expect(result.amount).toBe(20)
  })
  // 更多 case
})
```

写完跑 `pnpm test` 绿。提 commit：`test: add unit tests for computeDiscount`。

**测试放最后、不是前提**。重构成功不依赖测试存在，但提纯完的纯函数**非常适合**补测——这是把"重构先"换回"测试防护"的合理时机。

### Step 5：看看还有没有下一个候选

回 Step 1，找 composable 里的下一个纯计算块。重复直到：
- 该 composable 里所有纯计算都搬出去了
- composable 只剩下 `ref` 声明、`computed` 里的"拆包调函数"、`watch` 注册、return

做完一个 composable 停下汇报。不要一口气把 5 个 composable 都提纯了。

---

## 特殊情况处理

### 函数读取多个 ref

如果原计算依赖多个 ref，就把多个普通值参数列出来：

```ts
// 壳里
const result = computed(() => compute(a.value, b.value, options.value))

// lib 里
export function compute(a: A, b: B, options: Options): Result { ... }
```

不要为了"少写点参数"就把 ref 对象传进去。**ref 对象不能进 lib**——那会把响应式依赖拖进纯函数。

### 需要返回多个值

就正常返回对象或元组：

```ts
export function analyzeCart(cart: Cart): { subtotal: number; tax: number; total: number } {
  ...
}
```

在壳里按需解构到多个 computed：

```ts
const analysis = computed(() => analyzeCart(cart.value))
const subtotal = computed(() => analysis.value.subtotal)
// 或者直接返回 analysis，让调用方自己取
```

### 状态转换函数（输入旧状态、输出新状态）

典型的 reducer 风格：

```ts
// lib
export function nextCartState(current: CartState, action: CartAction): CartState {
  switch (action.type) { ... }
}

// 壳
function dispatch(action: CartAction) {
  cart.value = nextCartState(cart.value, action)
}
```

注意：**不要在 lib 里直接改 current**。返回新对象。这既是纯函数的要求，也避免 Vue 的深响应式误触发。

### 异步纯逻辑？

严格说没有"异步纯函数"——涉及 Promise 就涉及时序，按定义不纯。但有些场景其实可以：

- **纯的数据变换管道**：`async function parseAndValidate(raw: string): Promise<Result>` 内部不调外部服务、不读本地存储，只是一个用到了 Promise 的计算。这种算准纯，可以进 lib。
- **调 API 的函数**：**不能**进 lib。应该留在 composable 壳或专门的 `services/` 层。`lib/` 里只放纯计算。

区分方法：这个函数接的参数里，有没有东西隐含"调用它会产生外部影响"（传 axios 实例、传 db 连接都算）？有就不纯。

### 原来用 `this` 的 Options API

Options API 里 `computed` 通过 `this.xxx` 访问 data。提纯时这些要显式变参数：

```ts
// 原
computed: {
  total() { return this.items.reduce(...) + this.tax }
}

// 先抽成方法
methods: {
  _computeTotal(items, tax) { return items.reduce(...) + tax }
}
computed: {
  total() { return this._computeTotal(this.items, this.tax) }
}

// 再搬到 lib
// lib
export function computeTotal(items: Item[], tax: number) { ... }
// Options
computed: { total() { return computeTotal(this.items, this.tax) } }
```

中间那一步"抽成方法"不能省。Options API 里 `this` 绑定容易踩坑，一步到位风险高。

---

## 什么时候停

- 当前 composable 里所有明显的纯计算都搬完了 → 停下汇报
- 发现某段代码"怎么看都不纯"（深度依赖 watch / 副作用 / 生命周期）→ 跳过它，留在壳里。不是所有代码都适合提纯。
- 连续尝试 3 段都判定"不纯"→ 停，说"这个 composable 可能整体就偏状态管理型，提纯收益不高"，问用户要不要换处方

---

## 反模式

- **把 ref 作为参数传进纯函数**：`export function foo(aRef: Ref<A>)` —— 立刻不纯了。永远传 unwrap 后的值。
- **纯函数里手动解包**：`function foo() { return aRef.value + 1 }`（依赖外层闭包的 ref）—— 这不叫提纯叫换地方藏。必须通过参数传。
- **把 composable 整个搬到 lib**：composable 本身不是纯的（它 `ref()` 创建响应式），整搬不对。要拆"响应式骨架留壳、纯计算内脏搬走"。
- **过度提纯**：一个两行的 `n => n * 2` 也抽成 lib 函数。没收益，徒增导入成本。值得提的至少是 5-10 行以上有业务意义的逻辑。
- **纯函数里引用业务常量**：可以，但这些常量也要进 lib（一起能被测试 import）。不要让 lib 反过来依赖 composable 模块。

---

## 检查清单

- [ ] `lib/xxx.ts` 里的函数 zero import from `'vue'` / `'vue-router'` / `'pinia'` / `'@/composables/*'` / `'@/stores/*'`
- [ ] 函数签名全部是普通值 in、普通值 out（无 Ref / ComputedRef）
- [ ] 函数体内没有 `.value`、没有 watch / watchEffect / onMounted 等
- [ ] composable 壳里对应的代码已经删除，只剩 `import + computed(() => xxx(...))` 或类似的薄包装
- [ ] `vue-tsc --noEmit` 绿、已有测试绿
- [ ] （可选但推荐）纯函数补了 Vitest 单测，直接 import 不 mount

---

## 一个完整的 before/after 示例

**Before（胖 composable）**：

```ts
// composables/useCheckout.ts
import { ref, computed } from 'vue'
import { useCartStore } from '@/stores/cart'

export function useCheckout() {
  const store = useCartStore()
  const couponCode = ref('')

  const subtotal = computed(() => {
    return store.items.reduce((sum, item) => sum + item.price * item.qty, 0)
  })

  const discount = computed(() => {
    if (!couponCode.value) return 0
    if (couponCode.value === 'SAVE10') return subtotal.value * 0.1
    if (couponCode.value === 'FLAT5' && subtotal.value >= 50) return 5
    return 0
  })

  const tax = computed(() => (subtotal.value - discount.value) * 0.08)
  const total = computed(() => subtotal.value - discount.value + tax.value)

  return { couponCode, subtotal, discount, tax, total }
}
```

**After（薄 composable + 纯 lib）**：

```ts
// lib/checkout.ts （纯 TS，零 Vue）
export function computeSubtotal(items: CartItem[]): number {
  return items.reduce((sum, item) => sum + item.price * item.qty, 0)
}

export function computeDiscount(subtotal: number, couponCode: string): number {
  if (!couponCode) return 0
  if (couponCode === 'SAVE10') return subtotal * 0.1
  if (couponCode === 'FLAT5' && subtotal >= 50) return 5
  return 0
}

export function computeTax(amount: number, rate = 0.08): number {
  return amount * rate
}

export function computeTotal(items: CartItem[], couponCode: string): {
  subtotal: number; discount: number; tax: number; total: number
} {
  const subtotal = computeSubtotal(items)
  const discount = computeDiscount(subtotal, couponCode)
  const tax = computeTax(subtotal - discount)
  return { subtotal, discount, tax, total: subtotal - discount + tax }
}
```

```ts
// composables/useCheckout.ts （薄壳）
import { ref, computed } from 'vue'
import { useCartStore } from '@/stores/cart'
import { computeTotal } from '@/lib/checkout'

export function useCheckout() {
  const store = useCartStore()
  const couponCode = ref('')

  const result = computed(() => computeTotal(store.items, couponCode.value))

  return {
    couponCode,
    subtotal: computed(() => result.value.subtotal),
    discount: computed(() => result.value.discount),
    tax: computed(() => result.value.tax),
    total: computed(() => result.value.total),
  }
}
```

```ts
// lib/checkout.test.ts （现在能测了）
import { describe, it, expect } from 'vitest'
import { computeTotal } from './checkout'

describe('computeTotal', () => {
  const items = [{ price: 30, qty: 2 }]
  it('no coupon', () => {
    expect(computeTotal(items, '').total).toBeCloseTo(64.8)
  })
  it('SAVE10 applied', () => {
    expect(computeTotal(items, 'SAVE10').discount).toBe(6)
  })
  it('FLAT5 requires subtotal >= 50', () => {
    expect(computeTotal([{ price: 30, qty: 1 }], 'FLAT5').discount).toBe(0)
  })
})
```

测试不用 mount、不用 mock store、不用 mock reactivity。换 React 这套 lib 直接能搬。
