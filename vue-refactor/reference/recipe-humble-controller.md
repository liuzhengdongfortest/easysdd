# 处方 B：Humble Component / Controller 拆分

把一个"既渲染 UI 又管 IO 又处理业务"的胖组件拆成两层：
- **Humble Component**：纯展示层。只接 props、只发 emit。零 ref（除非是纯本地交互态）、零 IO、零 router / store / storage / window。
- **Controller Component**：调度层。调 composable 拿数据、把派生值传给 Humble、接 Humble 的 emit 转成业务动作。

参考 Michael Thiessen 的 "Humble Components"。核心理念："props down, events up"。

**适用信号**：同一个组件同时有 fetch / store / router 调用**和**大段 template；想测渲染必须先 mock 所有 IO；子区域明显能用 props+emit 独立存在。

---

## 起步：识别 Humble 候选

不是所有组件都能拆出 humble。扫一遍当前组件的 template，找满足以下条件的一块：

- **区域明确**：能用一个 `<section>` 或一个根元素框起来
- **引用的 script 符号少**：template 这块只用到 3-5 个顶层符号（ref、computed、method）
- **引用的符号都是"可 props 化"的**：值类型（string / number / boolean / plain object / array），或者 emit 方向的 callback
- **没有直接调 router / store / fetch**：template 里不出现 `$router.push` 或者事件处理直接写 `store.doSomething()`

如果整个组件都没有这样的区域——所有地方都深度依赖父组件 state——说明这个组件不适合 humble 拆分，考虑先走处方 A 把主干瘦下去再回来看。

### 典型的 humble 候选

- 表单：字段输入 + 校验提示 + 提交按钮。校验规则和提交动作在 controller 决定，humble 只管画字段
- 列表项：接一个 item props，画内容 + 几个按钮（emit click）
- 对话框 / 模态：接 visible、content props，emit confirm / cancel
- 工具栏：一排按钮，每个按钮 emit 对应动作

---

## 搬运节拍

### Step 1：把候选区域"框出来"

在原 template 里给这块加一个明确的边界标记（比如包一层 `<div class="xxx-humble-candidate">` 或一段注释）。目的是在搬运过程中一眼看出边界，不会漏搬或误搬。

此时代码行为没变，提 commit：`refactor: mark humble candidate boundary in Xxx`。

### Step 2：创建空的 Humble 子组件

新建 `XxxDisplay.vue`（命名建议：父叫 `OrderForm` → humble 子叫 `OrderFormFields` 或 `OrderFormDisplay`）：

```vue
<script setup lang="ts">
defineProps<{}>()
defineEmits<{}>()
</script>

<template>
  <div></div>
</template>
```

在父组件 template 里插入但传空 props：

```vue
<XxxDisplay />
<!-- 下面还有原来的完整区域 -->
<div class="xxx-humble-candidate">...</div>
```

编译绿（空组件不会出错）。提 commit：`refactor: scaffold XxxDisplay humble component`。

### Step 3：把 template 片段搬过去（一次性，但不改引用）

**这一步是例外**——template 搬运很难按"一行行搬"，要一块搬。做法：

1. 把 Step 1 框出的 template 整块**剪切**到 `XxxDisplay.vue` 的 `<template>` 里（替换掉里面的空 `<div>`）
2. 父组件原位置换成 `<XxxDisplay />` 调用

此时 **`XxxDisplay.vue` 会有一堆编译错**——里面引用的变量 / 方法在这个新组件里都不存在。**这正是编译器的清单**——它列出了这块 template 到底依赖父组件哪些东西。

把编译错记下来，分成两类：
- **读取类**（`{{ user.name }}`、`:disabled="loading"`）→ 要变成 props
- **回调类**（`@click="handleSubmit"`、`@input="onChange"`）→ 要变成 emit

不要急着修，先提 commit：`refactor: cut template into XxxDisplay (expected errors)`。这个"编译红"commit 是允许的过渡态，但**下一个 commit 必须让它绿回来**。

### Step 4：按清单补 props

每个"读取类"引用补成 prop。比如编译器说 `Cannot find name 'user'`：

在 `XxxDisplay.vue` 的 `defineProps` 里加：
```ts
defineProps<{
  user: User
}>()
```

在父组件的 `<XxxDisplay :user="user" />` 里传下去。

**一次补一个 prop，每次补完编译一次**。直到所有"读取类"错误消失。

每补完一组（3-5 个 prop）提一次 commit：`refactor: pass user/loading/items props to XxxDisplay`。

### Step 5：按清单补 emit

每个"回调类"引用改成 emit。比如 template 里原来写 `@click="handleSubmit"`：

在 `XxxDisplay.vue` 里：
```ts
const emit = defineEmits<{
  submit: []  // 或 submit: [payload: FormPayload]
}>()
```

把 template 里的 `@click="handleSubmit"` 改成 `@click="emit('submit')"`。

在父组件的 `<XxxDisplay @submit="handleSubmit" />` 里接住。

父组件里的 `handleSubmit` 定义**保持不动**——它还在那里，只是现在被 Humble 通过事件触发，而不是被 Humble 直接调用。

一组 emit 补完 commit 一次：`refactor: route submit/cancel events through XxxDisplay emits`。

### Step 6：编译全绿，肉眼验

此时 `XxxDisplay.vue` 编译应该全绿，父组件也绿。打开页面点一圈：
- 展示的数据还对不对
- 点击交互还能触发原来的逻辑不
- 表单输入有没有"双向绑定断了"的迹象（如果原来用 `v-model`，Humble 要用 `modelValue` prop + `update:modelValue` emit 实现）

肉眼过关 → 提收尾 commit：`refactor: complete humble split for Xxx`。

---

## v-model 特殊处理

原父组件 template 里如果有 `v-model="something"`，搬进 humble 后要拆成标准形式：

Humble 里：
```ts
const props = defineProps<{ modelValue: string }>()
const emit = defineEmits<{ 'update:modelValue': [value: string] }>()
```
template 里用 `:value="modelValue"` 和 `@input="emit('update:modelValue', $event.target.value)"`。

父组件调用：`<XxxDisplay v-model="something" />` 照样工作。

这不是行为变化，只是显式化。但编译器不会帮你自动转，得手动。

---

## 反模式检查（Humble 必须拒绝这些）

Humble 做完后扫一遍 `XxxDisplay.vue`，**不应该出现**：

- `import { useRouter } from 'vue-router'` / `useRoute()`
- `import { useXxxStore } from '@/stores/...'`
- `fetch(` / `axios.` / `useQuery(` / `$api.`
- `localStorage.` / `sessionStorage.` / `window.`
- `onMounted(` 里有数据拉取（纯本地动画 / focus 初始化可以留）
- `watch(...)` 里触发业务动作

一旦出现这些 → Humble 不 humble，把这块退回父组件，通过 props 把"当前已计算好的数据"传下来 + emit 通知父组件去做 IO。

**唯一允许的本地状态**：纯 UI 交互态。比如"这个 tooltip 是否展开"、"这个输入框是否聚焦过"。这种 state 外界不关心，留在 humble 里反而合理。

---

## Controller 的收尾

Humble 拆出去后，父组件（Controller）应该长成这样：

```ts
<script setup lang="ts">
// 1. 调 composable 拿数据和动作
const { user, loading, submit } = useOrderForm()

// 2. 可能做一层派生 / 格式化
const displayUser = computed(() => formatUser(user.value))

// 3. 接住 humble 的 emit
function handleSubmit() {
  submit()
}
</script>

<template>
  <XxxDisplay
    :user="displayUser"
    :loading="loading"
    @submit="handleSubmit"
  />
</template>
```

Controller 里应该**没有**大段 template——template 都在 humble 里。Controller 的 template 主要是"装配 humble"。

如果 Controller 自己 template 也很长（除了 `<XxxDisplay />` 还有很多别的 markup），说明还能再拆一个或多个 humble。重复这个处方。

---

## 什么时候停

- 一个 humble 已经拆完、编译绿、肉眼验过 → 停下汇报，让用户决定要不要继续拆第二个 humble
- 拆到一半发现候选区域引用了 > 10 个父组件符号 → 停下，说"这个候选可能太大，建议先缩小范围"
- Controller 已经瘦到主要就是"装配 humble" → 停，可以考虑进处方 C（如果 composable 还胖）

---

## 收益验证

处方 B 做对了会有这些可观察的好处：

- **Humble 可以只靠 props 快照测试**：Vitest + @vue/test-utils 的 `mount(XxxDisplay, { props: ... })`，不用 mock 任何 IO
- **改 UI 改样式只动 humble**：Controller 和业务逻辑不受影响
- **同一套业务逻辑可以换皮**：给 Controller 配一个不同的 Humble（比如 Mobile 版 vs Desktop 版）

如果拆完之后这些好处一条都没体现——测试还是要 mock IO、改样式还是要动 Controller——说明拆的位置不对，回退重做。

---

## 检查清单

- [ ] `XxxDisplay.vue` 里搜不到 `useRouter` / `useRoute` / `useXxxStore` / `fetch` / `axios` / `localStorage` / `window.`
- [ ] `XxxDisplay.vue` 的 `<script setup>` 只有 `defineProps` / `defineEmits` / 纯 UI 本地 ref / 纯格式化 computed
- [ ] 父组件 template 里 humble 候选区域已经全部被 `<XxxDisplay ... />` 替代
- [ ] 所有读取类引用 → props；所有回调类引用 → emit
- [ ] `vue-tsc --noEmit` 绿、已有测试绿
- [ ] 页面肉眼验：展示数据对、交互能触发、v-model 还双向
