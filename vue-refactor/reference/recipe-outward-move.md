# 处方 A：水落石出外移

把胖主干的一簇相关变量 + 方法外移到一个新 composable（或 util 模块），让主干瘦下去。这是用户老师 Committer 培训里教的"extract delegate"在 Vue 里的映射。

**适用信号**：`<script setup>` 超过 200 行 / 一屏看不完 / 能一眼指出"这几个变量是一个局部主题"。

**核心动作**：不改任何行为，只换位置。

---

## 开始前的准备

### 1. 划簇

拿出当前的 `<script setup>`，在脑子里（或在纸上）找出"一簇"——一组 ref / computed / watch / method，它们：
- 围绕同一个主题（"表单校验"、"拖拽状态"、"轮询"、"权限判断"）
- **内部互相引用，和外部引用较少**
- 可以用一个名词起名（`useFormValidation`、`useDragState`、`usePolling`、`usePermission`）

如果划不出来——一簇变量和外面全都纠缠——说明不是判断 1，退回去考虑是不是判断 2 或 3。

**一次只划一簇**。不要一次列出 5 簇都要搬。做完一簇停下确认。

### 2. 命名新 composable

起名规则：
- `use` 前缀，camelCase
- 名词或动名词，描述"这簇管的是什么"
- 不要用业务侧的具体名词（`useOrderForm` 好；`useOrder` 太泛）

### 3. 决定新文件位置

- 只在本组件用 → 同目录下建 `./composables/useXxx.ts` 或在 SFC 所在目录建 `useXxx.ts` 和 SFC 同级
- 可能被兄弟组件复用 → 放到上一层的 `composables/` 目录
- 明显是跨页面通用 → 放到全局 `src/composables/`

不确定就先放近的（本地），后续需要时再做一次"move 到更高层"的重构。

---

## 搬运节拍（三步循环的具体化）

### Step 1：创建空壳 composable

新文件 `useXxx.ts`，先写一个什么都不做的骨架：

```ts
export function useXxx() {
  return {}
}
```

在原 SFC 里引入并调用：

```ts
// 原 <script setup> 顶部
import { useXxx } from './composables/useXxx'
const {} = useXxx()  // 空解构，现在什么也没搬过去
```

**编译必须绿**。跑一次 `vue-tsc --noEmit`（或 `tsc --noEmit`）确认。提交一个 commit：`refactor: scaffold useXxx composable`。

### Step 2：搬第一个字段

挑这一簇里**依赖最少**的一个 ref / computed。比如一个独立的 `const loading = ref(false)`。

1. 在 `useXxx.ts` 里声明它：
   ```ts
   import { ref } from 'vue'
   export function useXxx() {
     const loading = ref(false)
     return { loading }
   }
   ```
2. 在原 SFC 的解构里加上：
   ```ts
   const { loading } = useXxx()
   ```
3. **删除原 SFC 里的 `const loading = ref(false)`**

此时编译器会报错——凡是原来用到 `loading` 的地方，现在还在引用的是被删掉的本地变量。但因为你从 `useXxx()` 里解构了同名的 `loading`，所以引用会自动指向新的。

**万一编译不绿**：说明解构名冲突 / template 引用方式不对 / 类型推断断了。**立刻 `git reset --hard`**，退回 Step 1 结束的 commit，重新规划这一步。

编译绿后，跑一次本组件的 smoke test 或手动打开页面看一眼（template 的引用 Volar 不一定全查得出）。

提交 commit：`refactor: move loading ref into useXxx`。

### Step 3：搬依赖 loading 的方法

编译器刚才"绿了"，但你可能漏了 template 里的使用。先扫一遍：

```bash
grep -n "loading" path/to/Component.vue
```

确认所有引用都已经走到 `useXxx` 解构出来的那个 `loading`。

现在挑一个"只依赖 loading（或其他已搬走的东西）"的方法，比如：

```ts
function startLoading() { loading.value = true }
```

搬法和字段一样：
1. 在 `useXxx.ts` 里定义 + 加到 return
2. 在原 SFC 从解构里取
3. 删原 SFC 里的本地定义
4. 编译绿 → commit

**如果这个方法依赖另一个还没搬走的字段**：先回去搬那个字段。永远不要让方法跨越"新位置和旧位置"引用数据——那会导致 composable 内部引用一个外部的 ref，变成隐式耦合。

### Step 4：重复 Step 2-3 直到这一簇全搬完

按这个顺序：
1. 无依赖的 ref / reactive
2. 只依赖已搬 ref 的 computed
3. 只依赖已搬东西的 method
4. 只依赖已搬东西的 watch / watchEffect
5. `onMounted` / `onUnmounted` 里如果有这簇相关的代码，最后搬（这部分要小心，见下面"特殊情况"）

每搬一个就一次 commit。一簇做完的终态：原 SFC 里这一簇的所有代码消失，只留一行 `const { ... } = useXxx()` 解构。

### Step 5：最后的清理

一簇搬完后检查：
- 原 SFC 里有没有孤立的 import（比如只给这簇用的 `import { watch } from 'vue'`，现在搬走了但 import 还在）——删掉
- `useXxx` 的 return 是否精简——有没有搬过去但其实没人用的中间变量，内化进 composable 不要 return
- composable 内部是否有"搬过去后能进一步简化"的机会——**不要做**。纯粹行为等价搬运已经完成，任何"简化"都是下一次重构，不合并

跑全量 `vue-tsc --noEmit`、已有测试、ESLint。绿了提一个收尾 commit：`refactor: finish extracting useXxx`。

---

## 特殊情况处理

### 生命周期钩子

`onMounted` / `onUnmounted` 可以出现在 composable 里（Vue 3 支持 composable 内注册钩子，会自动绑到调用它的组件）。但有个坑：

如果原组件的 `onMounted` 里既有 useXxx 相关的初始化，又有其他组件职责（比如给 window 加全局 listener），**不要把整个 `onMounted` 搬进去**。要做的是：
1. 在 composable 内新开一个 `onMounted`，只放这簇相关的代码
2. 原组件的 `onMounted` 里删掉这簇代码，保留其他部分

编译器不会告诉你钩子搬错了，所以这一步要人肉核对。

### template 里的引用

改完 `<script setup>` 后跑 `vue-tsc --noEmit` —— Volar 会检查 template 里的引用。如果报错说 "Property 'xxx' does not exist"，说明 template 引用了某个符号但你忘了从 composable 解构。

### 跨簇共享的字段

有时发现字段 X 既是"簇 A 的一部分"又是"簇 B 的一部分"。两个选择：
1. 把 X 放进 A，让 B 通过参数接收 X：`useBFeature(x)`
2. X 放到更基础的第三个 composable `useSharedX`，A 和 B 都调

倾向选 2，但第一轮先选 1（简单）。下一轮重构时有需要再拆到 3。

### provide / inject

原组件如果用 `provide` 暴露了某些值，这些值如果搬进 composable，**provide 调用本身要留在组件里**（provide 和组件树绑定）。让 composable return 出那些值，组件拿到后再 provide。

### defineExpose

如果暴露的符号在待搬一簇里，同样 composable 搬完后在组件里 `defineExpose({ loading, ... })` 重新暴露。defineExpose 必须在组件顶层，不能在 composable 里。

---

## 什么时候停

这一轮处方 A 做到以下任一情况就停：

- 一簇已经完整搬完 → **停下汇报**，让用户决定要不要继续下一簇
- 搬到一半发现这一簇和外部耦合比想象中深（> 3 个外部字段被内部方法读写）→ 停下，报告"这簇可能不是好的切分，建议换一簇或放弃外移"
- 搬了两簇之后主干已经瘦到 < 150 行 → 停，让用户重新评估是不是还要继续

不要无限拆下去。"主干变薄"本身是目的，拆到能看清就够了。

---

## 检查清单（每一簇搬完都走一遍）

- [ ] `vue-tsc --noEmit` 绿
- [ ] 已有单测全绿
- [ ] ESLint 绿
- [ ] `grep` 原 SFC 里这簇的符号名，结果应该全部指向 `useXxx()` 解构
- [ ] 手动打开主要页面点一圈（template 引用肉眼验）
- [ ] 原 SFC 里本簇相关的 import 都已清理
- [ ] 新 composable 的 return 里没有死符号
- [ ] 这一簇的所有 commit 都是"move X"语义，没有混入"simplify X / optimize X"
