# Evan You 著作与系统性思考调研

> 调研日期：2026-04-16
> 调研范围：Evan You（尤雨溪）公开发表的文章、演讲、播客、访谈及技术声明

---

## 目录

1. [个人博客文章（他亲自写的）](#1-个人博客文章)
2. [Medium 官方 Vue 博客文章（他亲自写的）](#2-medium-vue-point-文章)
3. [VoidZero 官方博客（他亲自写的）](#3-voidzero-官方博客)
4. [会议演讲（他亲自说的）](#4-会议演讲)
5. [播客访谈（他亲自说的）](#5-播客访谈)
6. [媒体访谈（二手整理）](#6-媒体访谈)
7. [核心论点（反复出现 ≥3 次的真信念）](#7-核心论点)
8. [自创术语与概念](#8-自创术语与概念)
9. [智识谱系（引用/推荐/影响来源）](#9-智识谱系)
10. [发现的矛盾与张力](#10-发现的矛盾与张力)

---

## 1. 个人博客文章

来源：https://blog.evanyou.me/  
可信度：**一手**（他亲自写的）

| 日期 | 标题 | 核心内容 |
|------|------|---------|
| 2015-12-20 | Vue.js: 2015 in Review | Vue 2015 年度回顾 |
| 2015-10-25 | Vue.js: a (re)introduction | Vue 重新介绍，澄清框架定位 |
| 2014-02-11 | First Week of Launching Vue.js | 发布第一周的经历记录 |
| 2014-01-03 | DOM Composition Events compatibility notes | 浏览器兼容性技术笔记 |
| 2013-12-29 | Gulp-style stream piping in Grunt, or anywhere else | Grunt 中实现 Gulp 式管道 |
| 2013-11-04 | **Oversimplifying things is not an advantage** | **核心哲学文章（见下方详解）** |

### 重点文章：Oversimplifying things is not an advantage

URL: https://blog.evanyou.me/2013/11/04/simplify/  
（也发布在 Medium: https://medium.com/i-m-h-o/oversimplifying-things-is-not-an-advantage-89c560fb21c3）

核心论点（针对 Riot.js 的批评，但实际是框架设计哲学宣言）：

> "The real problem with Riot.js is that its authors are marketing a project with major tradeoffs as if it's superior in every aspect, with hyperboles and misleading comparisons."

**他的三个核心反驳：**

1. **"Less to learn" 是假优势**：框架提供的"最小指导"意味着开发者要自建所有基础设施，这不是减负而是转嫁负担。

2. **约定的价值被低估**：框架的 idiom/convention 让团队协作和代码可读成为可能——没有约定，每个人都在重新发明轮子，长期维护成本更高。

3. **Bug 转移不等于 Bug 消除**：把责任从框架转给开发者，Bug 并不会消失，只是换了地方出现。

> "If you are a novice and need help from a framework, it offers too little guidance; If you are a competent developer, it offers too little functionality."

**设计结论**：过度简化（oversimplification）是负担转移，不是优雅。这个逻辑直接塑造了 Vue 的"不过简、也不过重"定位。

---

## 2. Medium / Vue Point 文章

来源：https://medium.com/@youyuxi  
可信度：**一手**（他亲自写的，发布在官方 Vue 博客 The Vue Point）

| 日期 | 标题 | 核心内容 |
|------|------|---------|
| 2019-02-04 | Vue 2.6 released! | 2.6 版本更新说明 |
| 2018-09-30 | **Plans for the Next Iteration of Vue.js** | **Vue 3 设计意图声明（重要）** |
| 2018-08-10 | Vue CLI 3.0 is here! | CLI 3.0 发布说明 |
| 2017-10-13 | Vue 2.5 released | 版本更新 |
| 2017-09-21 | Upcoming TypeScript Changes in Vue 2.5 | TypeScript 集成方向 |
| 2017-09-11 | Vue is now on OpenCollective! | 开源资金模式宣告 |
| 2016-12-28 | Vue in 2016 | 2016 年度回顾 |
| 2016-11-03 | Retiring vue-resource | 官方弃用 vue-resource 的决策说明 |
| 2016-09-30 | Vue 2.0 is Here! | Vue 2.0 发布 |
| 2016-08-11 | **The State of Vue** | **Vue 定位与生态系统声明** |

### 重点文章：Plans for the Next Iteration of Vue.js（2018）

注：原始 URL 已失效（https://medium.com/@youyuxi/plans-for-the-next-iteration-of-vue-js-ea08a1a9cb2c 返回 404），内容已被整合进后续 RFC 和 Increment 杂志文章。可信度降级为**二手重建**。

---

## 3. VoidZero 官方博客

来源：https://voidzero.dev/  
可信度：**一手**（公司官方博客，由 Evan You 主导撰写）

### Announcing VoidZero（2024-10-01）

URL: https://voidzero.dev/posts/announcing-voidzero-inc

这是迄今为止他关于 JS 工具链哲学最系统的表达。

**核心问题诊断（直接引用）：**
> "the ecosystem has always been fragmented: every application relies on a myriad of third-party dependencies, and configuring them to work well together remains one of the most daunting tasks in the development cycle."

> "internally, it still relies on various dependencies, with abstractions and workarounds to smooth over inconsistencies."（谈 Vite 当时的内部状态）

**四个设计原则（他的语言）：**
1. **Unified**：同一 AST、resolver、module interop，消除冗余 parse 成本
2. **High Performance**：编译为 native 的语言，最大化并行，低开销 JS 插件支持
3. **Composable**：每个组件可独立消费
4. **Runtime Agnostic**：不绑定特定 JS runtime

**融资信息**：$4.6M 种子轮，Accel 领投，2024-10-01

### Announcing Vite+（2025）

URL: https://voidzero.dev/posts/announcing-vite-plus

**核心战略声明：**
> "all existing projects — Vite, Vitest, Rolldown, and Oxc — will remain open source under MIT forever."

**Vite+ 命令设计哲学**：统一入口（`vite new`、`vite test`、`vite lint`、`vite fmt`、`vite lib`、`vite run`、`vite ui`），减少工具选择的认知负担。

**他对"碎片化税"的表述**：tooling complexity 和 performance 已成为大型项目的真实瓶颈。

---

## 4. 会议演讲

### 4.1 The Progressive Framework（2016，VueConf/各地演讲）

URL: https://slides.com/evanyou/progressive-javascript  
可信度：**一手**（PPT 本人制作）

这是"Progressive Framework"概念的原始出处。

**问题诊断（他的框架）**：
- JS 生态有两种传统方案：全功能框架（Angular）vs 微库（Backbone/Riot）
- 前者：高学习成本，难以逐步采用
- 后者：最大灵活性，但研究成本高，缺乏指导

**Progressive Framework 定义（他亲自给的）**：
> "A framework that adapts to a project's inherent complexity"

**三层架构（他的模型）**：
1. **Lean Core**：声明式视图渲染，可单独使用
2. **Official Libraries**：路由、数据获取、状态管理——按需引入
3. **Optional Toolchain**：构建工具、测试、热重载——需要时才用

**核心翻转**：不是让用户主动 opt-out，而是让用户逐步 opt-in。

---

### 4.2 Three Key Dimensions of Front-End Frameworks（JSConf Asia 2019）

URL: https://www.infoq.com/news/2019/07/frontend-framework-dimensions/  
可信度：**二手**（InfoQ 整理，非原始文字稿）

**他提出的三个维度**：
1. **Scope**：框架覆盖多少功能范围
2. **Render Mechanism**：渲染机制（Virtual DOM / 直接 DOM / 编译时）
3. **State Mechanism**：状态管理方式（reactivity / immutability / signals）

Vue 在这三个维度上的定位：中间位置——有一定范围、Virtual DOM + 编译优化、响应式系统。

---

### 4.3 Vue 3 Design Principles（VueConf Toronto 2019/2020）

URL: https://www.infoq.com/news/2020/01/vue3-design-evan-you-toronto/  
可信度：**二手**（InfoQ 整理）

**重要设计决策及理由**：
- **为什么切换到 TypeScript**：Flow 的 IDE 集成太差，TS 能自动生成 .d.ts，用户需求推动
- **为什么 Monorepo**：让依赖关系显式化，降低贡献门槛
- **为什么 Composition API**（非 Class API）：装饰器（decorators）是不稳定的 Stage 2 提案；Composition API 用普通变量和函数，天然类型友好

**性能哲学**（他的原文概括）：
> "Performance is essential to frontend frameworks."

具体策略：Block-based tree、静态提升（static hoisting）、元素级优化 flags——编译器与运行时协作，不是简单抛弃 Virtual DOM。

结果：Vue 3 在 benchmark 上只用 Vue 2 不到 1/10 的 CPU 时间，bundle 从 23KB 降到 10KB gzipped。

---

### 4.4 One Year Into Vue 3（2022，JSNation）

URL: https://gitnation.com/contents/one-year-into-vue-3  
可信度：**二手**（GitNation 整理）

---

### 4.5 10 Years of Independent OSS: A Retrospective（2024，JSNation）

URL: https://gitnation.com/events/jsnation-2024  
可信度：**二手**（GitNation 整理）

他的表述（来自二手报道）：这是对 10 年独立开源的回顾，覆盖 Vue 成长的挑战、Vite 作为构建工具的发展、以及统一工具链的愿景。

---

### 4.6 Vite: Rethinking Frontend Tooling（多个会议）

URL: https://gitnation.com/contents/vite-rethinking-frontend-tooling/en  
可信度：**二手**

**他为什么建 Vite（直接引用）：**
> "We were having some really slow build times during development, waiting for the things to compile… especially for large Vue applications."

根本原因分析：
> "For every change that we make, even if we just change a single module, we have to still bundle the whole thing… the build speed just deteriorates linearly with the size of your app."

**从 Vue CLI 的教训（直接引用）：**
> "During that process we absorbed so much complexity… it's just getting out of hand."

**解决方案哲学：**
> "The out-of-the-box features designs the baseline experience for all users. But how good the plugin API is decides the ceiling of the user experience."

---

### 4.7 Vite & the Future of JS Tooling（ViteConf 2024）

URL（幻灯片）: https://docs.google.com/presentation/d/1Kt020NyY0LE3G7NtqM67OHt-bAI1HKM4zKKd0vH9RHQ/edit  
可信度：**一手**（本人幻灯片）

ViteConf 2025 也有同类演讲，见 https://voidzero.dev/posts/whats-new-viteconf-2025

---

## 5. 播客访谈

### 5.1 JS Party #212: A Deep-Dive on Vite（Changelog，2022）

URL: https://changelog.com/jsparty/212  
可信度：**一手**（本人说的，有完整播客录音）

**关于 esbuild vs Rollup 的取舍（直接引用）：**
> "Going with Rollup is essentially sort of a trade-off decision between the plugin API friendliness, the existing ecosystem and how we can give a better production build performance."

esbuild 的问题：应用级 bundling 不成熟，对 code-splitting 和 chunk-caching 控制太少。

**对 Rust 在 JS 工具链中的保留意见（直接引用）：**
> "Rust is fast, but it's harder to write, it's harder to understand… I can't patch it myself on the spot."

> "How do we efficiently and securely distribute these native binaries?"（他认为这是未解决的生态问题）

**Wishlist（直接列出）**：
1. 修复 Node 的 ESM 生态
2. 解决 CommonJS/ESM 混用的包兼容性
3. 基于 Rust 重写的 Rollup（这后来变成了 Rolldown）

---

### 5.2 CoRecursive Podcast: From 486 to Vue.js（2023）

URL: https://corecursive.com/vue-with-evan-you/  
可信度：**一手**（本人说的，有完整文字稿）

**关于早期动机（直接引用）：**
> "It started out really with no expectations. It's more, 'Let's see if I can do this. It's fun.' Just playing around with this new idea."

> "What always spoke to me was this kind of attention to detail and thinking about what would give people the wow factor when you see something visually."

**关于 Web 的低门槛（直接引用）：**
> "Because it's super low barrier to entry. You just code with a text editor in the browser...you can immediately get feedback while you work on things."

**关于 Vue 的诞生（直接引用）：**
> "I had to make it public so that other people can maybe use it in some way...the first group of users kind of got me going."

**关于框架定位（直接引用）：**
> "Vue was basically providing the right features with the right amount of complexity, like really low barrier of entry for most people."

**关于 API 演化与取舍（直接引用）：**
> "I guess the best you can do is to make the most amount of people happy. But inevitably you're gonna make someone unhappy."

**关于 Composition API 争议（重要，直接引用）：**
> "Our early user base are mostly people who preferred lightweight solutions, simple interactions...when we propose solutions to address more advanced cases, these simple case users get pissed off."

**关于验证感（直接引用）：**
> "I'm validated by the things I create and share with people. If I do work, but I can't see how it affects people in the world, then it becomes much less satisfying."

**关于社区中的不满之声（直接引用）：**
> "People rarely go out of their way to praise something...But there will always be someone raising an issue."

**关于线下连接的价值（直接引用）：**
> "These in-person interactions make you realize there are much more people who are satisfied...they're just not really being really loud on the internet."

**关于冒险（直接引用）：**
> "I know I had a safety net. I could have gone back to a big company if I really wanted to...I think you should try it."

---

### 5.3 GitHub README Stories（2020）

URL: https://github.com/readme/stories/evan-you  
可信度：**一手**（本人受访，大量直接引用）

**关于 Vue 起点（直接引用）：**
> "I didn't start with the goal of being a full-time open source maintainer. I was solving a problem for myself."

> "I started Vue as a side project. I initially thought it would be a small, simple library."

> "When Vue's user count reached a certain volume, it became a community. Suddenly all these people were counting on me."

**关于 Vision（直接引用）：**
> "My vision for Vue is to give any user a low barrier of entry, a good foundation, and room to grow."

> "The ideal user is someone who just got into web development...and then they find Vue. Suddenly they can build real applications."

**关于开源可持续性与 Burnout（直接引用，重要）：**
> "I used to work on Vue 24/7...I needed to find a solution. So now, I draw clear lines: I start at 9 and stop at 6."

> "A lot of full-time open source maintainers didn't choose to be where they are. We picked the right project at the right time."

> "I've seen so many maintainers pour all their spare time into a project, but in the end, they burn out and leave."

> "At its core, open source is either your main path, or it's supplementary. It can't be both."（**核心论断**）

---

### 5.4 freeCodeCamp: Between the Wires（2017）

URL: https://www.freecodecamp.org/news/between-the-wires-an-interview-with-vue-js-creator-evan-you-e383cbf57cc4/  
可信度：**一手**（本人受访）

**关于 JavaScript 吸引力（直接引用）：**
> "I was attracted to JavaScript because of the ability to just build something and share it instantly with the world."

> "You put it on the web, and you get a URL, you can send it to anyone with a browser."

**关于 Vue 诞生（直接引用）：**
> "What if I could just extract the part that I really liked about Angular and build something really lightweight?"

**关于 "Progressive Framework"（直接引用）：**
> "Vue is probably the most similar to React, but on a broader sense, the term that I coined myself is a progressive framework."

> "The core is still exposed as a very minimal feature set, but we also offer these incrementally adoptable pieces."

**关于竞争与压力（直接引用）：**
> "There is not going to be this one true framework that just makes everyone happy. The more important part is, make it better for the people who actually enjoy your framework."

> "Focus on what you believe is the most valuable thing in your framework and just make sure you're doing a great job."

**关于开源经济学（直接引用）：**
> "I'm creating value for these people, so theoretically if I can somehow collect these values in a financial form, then I should be able to sustain myself."

---

### 5.5 Web Worker 播客 No.41（2022/2023，中文）

URL: http://podcast.webworker.tech/41  
（参考链接：https://www.webworker.tech/posts/41.html — 当时证书已过期）  
可信度：**一手**（本人录音，中文）

主题：Vue.js / Vite 技术进展、开源社区协作维护、前端思考  
注：具体内容未能直接抓取，但确认存在。

---

## 6. 媒体访谈

### 6.1 Monterail: Vue 3 Interview（2020）

URL: https://www.monterail.com/blog/vue-3-evan-you-interview-features  
可信度：**一手**（本人受访，直接引用）

**关于 Vue 3 的核心挑战（直接引用）：**
> "The biggest challenge is making it a more solid choice for large-scale applications while retaining the same beginner-friendly learning curve."

**关于编译器 + 运行时路线（直接引用）：**
> "I believe there are still more interesting things we can do with the compiler + runtime combined approach, both in terms of performance and authoring experience."

**关于开源的核心工作内容（直接引用）：**
> "Know what you are getting into. Writing the code is the easy part - most of the work is in maintenance and community building."

**关于独立性的价值（直接引用）：**
> "I believe such freedom is important, since it ensures the technical direction of the framework is completely independent of business decisions."

> "It's the feeling of being in control - once I've experienced that I can never imagine going back to big companies again."

---

### 6.2 Stack Overflow Blog: Vite is like the United Nations of JavaScript（2025-10）

URL: https://stackoverflow.blog/2025/10/10/vite-is-like-the-united-nations-of-javascript/  
可信度：**一手**（本人受访）

**"United Nations of JavaScript" 的含义（重要）**：

这个短语来自 Rich Harris（Svelte 作者），Evan You 接受了它。含义：Vite 通过插件系统支持所有主流框架，是中立的基础设施，不是某个框架阵营的工具。

**关于 JS 历史问题（直接引用）：**
> "JavaScript itself was not really designed for this serious engineering at the beginning."

**关于 Vite 的最大贡献（直接引用）：**
> "The biggest contribution of Vite is we showed people how fast hot module replacement can be."

**关于 Vite 为何能快速起飞（直接引用）：**
> "Vite was able to get off the ground really fast because we were able to leverage the existing plugin ecosystem of Rollup."

**关于开源信用（直接引用）：**
> "It's important in open source because inevitably some of the ideas you're using comes from someone else."

---

### 6.3 2023 Open Source Funding Interview（由 Dennis R Data News 翻译整理）

URL: https://dennisrdatanews.netlify.app/post/2023-08-26-evan-you-interview/  
可信度：**二手**（翻译整理，原始来源为中文媒体采访）

**关于离职时机（引用）：**
> "I was confident that I could find another job whenever I wanted, so I thought it was the right time to go full-time into open-source"

**关于早期收入情况**：Patreon 月收不足 $5,000，远低于工资，他仍然辞职了。  
**现状**：团队月收入"数万美元"，完全自给。

收入来源组合：Patreon + GitHub Sponsors + 教育内容分成 + 广告

---

### 6.4 Increment Magazine: The Process: Making Vue 3（约 2020）

URL: https://increment.com/frontend/making-vue-3/  
可信度：**一手**（他亲自受访，有大量直接引用）

**关于重写的必要性（直接引用）：**
> "Fixing these issues in the current codebase would require huge, risky refactors that are almost equivalent to a rewrite."

**关于框架演化哲学（直接引用）：**
> "The diversity of developer profiles corresponds to the diversity of use cases."

这句话解释了为什么 Vue 的"progressive"设计是合理的——不同类型的开发者需要不同深度的访问路径。

---

### 6.5 Indie Hackers: Taking on Google and Facebook as a Solo Open-Source Founder（早期）

URL: https://www.indiehackers.com/podcast/078-evan-you-of-vue  
可信度：**一手**（本人受访）

---

## 7. 核心论点（反复出现 ≥3 次的真信念）

以下是跨多个来源、反复出现的核心观点：

### 7.1 Progressive / Incrementally Adoptable Framework

出现频率：**极高**（5+ 次，跨演讲、采访、官方文档）

核心逻辑：框架应该适应项目的复杂度，而不是强迫开发者一次接受全部。低门槛进入，高上限可达。

代表表达：
- "The core is still exposed as a very minimal feature set, but we also offer these incrementally adoptable pieces."（2017）
- "A framework that adapts to a project's inherent complexity"（2016 幻灯片）
- "The diversity of developer profiles corresponds to the diversity of use cases."（Increment）

---

### 7.2 Oversimplification 是负担转移，不是优雅

出现频率：**高**（3+ 次）

核心逻辑：把复杂度从框架移走，不等于让复杂度消失，而是把它压到用户身上。

代表表达：
- "Oversimplifying things is not an advantage"（2013 博客）
- "If you are a novice... it offers too little guidance; If you are a competent developer, it offers too little functionality."（2013）
- "Writing the code is the easy part - most of the work is in maintenance and community building."（2020）

---

### 7.3 工具链碎片化是 JS 生态的根本问题

出现频率：**高**（3+ 次，集中在 2021-2024）

代表表达：
- "the ecosystem has always been fragmented"（VoidZero 公告，2024）
- Vite 最初也靠 esbuild + Rollup 拼凑，"abstractions and workarounds to smooth over inconsistencies"（2024）
- JS "was not really designed for this serious engineering at the beginning"（Stack Overflow，2025）

---

### 7.4 开源可持续性：边界是关键

出现频率：**高**（3+ 次）

核心逻辑：全职开源是职业路径，不能兼职对待；必须设置边界，否则 burnout。

代表表达：
- "At its core, open source is either your main path, or it's supplementary. It can't be both."（GitHub README）
- "I used to work on Vue 24/7... I draw clear lines: I start at 9 and stop at 6."（GitHub README）
- "I've seen so many maintainers pour all their spare time into a project, but in the end, they burn out and leave."（GitHub README）

---

### 7.5 技术方向必须独立于商业决策

出现频率：**中等**（3 次）

代表表达：
- "I believe such freedom is important, since it ensures the technical direction of the framework is completely independent of business decisions."（Monterail）
- "It's the feeling of being in control - once I've experienced that I can never imagine going back to big companies again."（Monterail）
- VoidZero 公告中强调所有项目"remain open source under MIT forever"

---

### 7.6 没有"唯一正确框架"

出现频率：**中等**（3 次）

代表表达：
- "There is not going to be this one true framework that just makes everyone happy."（freeCodeCamp，2017）
- "diversity in the ecosystem is a good thing"（采访）
- "Focus on what you believe is the most valuable thing in your framework"（freeCodeCamp）

---

## 8. 自创术语与概念

| 术语 | 来源 | 含义 |
|------|------|------|
| **Progressive Framework** | 2016 幻灯片、freeCodeCamp 2017 | 框架适应项目复杂度，逐步 opt-in 而非全量采用 |
| **Unified Toolchain** | VoidZero 公告 2024 | 共享同一 AST/resolver/module interop 的完整 JS 工具链 |
| **Composable**（在工具链语境下） | VoidZero 公告 2024 | 每个工具组件可独立消费，不必全套采用 |
| **Runtime Agnostic**（Vite/VoidZero） | VoidZero 公告 2024 | 不绑定特定 JS runtime（Node/Deno/Bun） |

**注**："United Nations of JavaScript" 是 Rich Harris 的说法，Evan You 接受了这个描述，但非他原创。

---

## 9. 智识谱系

### 9.1 明确影响来源

| 来源 | 方向 |
|------|------|
| **Angular**（Google 内部使用） | Vue 的诞生动机——提取 Angular 好的部分，去掉繁重部分 |
| **React** | Composition API 受 React Hooks 启发（他在 Increment 文章中承认） |
| **Rollup** | Vite 的插件体系基础，让 Vite 快速获得生态兼容性 |
| **esbuild**（Arno Haase 等） | Vite 开发服务器的 transform 速度基础 |
| **Rust 生态（OXC, SWC 等）** | Rolldown 的技术路径，他同时有保留意见（见 7.3 矛盾） |

### 9.2 他明确合作/信任的人

- **Rich Harris**（Svelte）：Vite "United Nations" 比喻来自他，Evan 在多处引用
- **Patak（Carlos Rodrigues）** & Vite 核心团队
- **Anthony Fu**：Vue/Vite 生态核心贡献者
- **Jason Miller**（Preact）：被他提及为工具链讨论同仁

---

## 10. 发现的矛盾与张力

以下矛盾**直接记录，不调和**：

### 矛盾 1：倡导渐进主义，但多次发起重大破坏性变更

- **立场**：Progressive Framework，低门槛，稳定性优先
- **实践**：Vue 2 → Vue 3 迁移代价极大（他在 2022 年度回顾中承认"challenges users faced during the v2 to v3 transition"）；Composition API 引发社区分裂；现在又在做 Rolldown 替换 Rollup
- **他的辩护**：每次大改都是"旧架构已经无法修补"，而非随意破坏

### 矛盾 2：强调工具链统一，但 Vite 本身曾是"拼凑方案"

- **立场**：碎片化是 JS 生态的根本问题，需要统一工具链
- **实践**：Vite 1.0/2.0 本身就是 esbuild（dev）+ Rollup（prod）的拼凑，他自己在 VoidZero 公告中承认这是"abstractions and workarounds"
- **他的回应**：Vite 是过渡期的最优解，VoidZero/Rolldown 才是真正的答案

### 矛盾 3：对 Rust 工具链有保留意见，但自己公司正在大量押注 Rust

- **2022 立场**（JS Party）：Rust 很快，但"harder to write, harder to understand... I can't patch it myself"，分发 native binaries 是未解决问题
- **2024 实践**：VoidZero 整个 Rolldown + OXC 技术栈都是 Rust，并以"3x faster than SWC"、"28x faster than enhanced-resolve"为卖点
- **可能的解释**：他解决了自己担心的问题（JS 插件 API 兼容层），或者他接受了这个 tradeoff

### 矛盾 4：声称不在乎竞争，但产品定位高度意识到竞争者

- **立场**："There is not going to be this one true framework"，多元生态是好的
- **实践**：他的每一次技术决策（从 Vue 起源到 Vite 到 Rolldown）都是对 Angular/React/Webpack/esbuild 的直接回应，VoidZero 的 benchmark 数据（28x、50-100x）是明显的竞争性话语

---

## 附录：主要信息源索引

| 类型 | URL | 可信度 |
|------|-----|--------|
| 个人博客 | https://blog.evanyou.me/ | 一手 |
| 个人网站 | https://evanyou.me/ | 一手 |
| Medium | https://medium.com/@youyuxi | 一手 |
| VoidZero 博客 | https://voidzero.dev/ | 一手 |
| GitHub 个人 | https://github.com/yyx990803 | 一手 |
| Vue RFC | https://github.com/vuejs/rfcs | 一手 |
| GitHub README Stories | https://github.com/readme/stories/evan-you | 一手（受访） |
| Increment（Making Vue 3） | https://increment.com/frontend/making-vue-3/ | 一手（受访） |
| freeCodeCamp Between the Wires | https://www.freecodecamp.org/news/between-the-wires-an-interview-with-vue-js-creator-evan-you-e383cbf57cc4/ | 一手（受访） |
| CoRecursive Podcast | https://corecursive.com/vue-with-evan-you/ | 一手（受访） |
| JS Party #212 | https://changelog.com/jsparty/212 | 一手（受访） |
| Monterail Interview | https://www.monterail.com/blog/vue-3-evan-you-interview-features | 一手（受访） |
| Stack Overflow Blog 2025 | https://stackoverflow.blog/2025/10/10/vite-is-like-the-united-nations-of-javascript/ | 一手（受访） |
| Vue 2022 Year in Review | https://blog.vuejs.org/posts/2022-year-in-review | 一手（他撰写） |
| Progressive Framework 幻灯片 | https://slides.com/evanyou/progressive-javascript | 一手 |
| InfoQ JSConf Asia 2019 | https://www.infoq.com/news/2019/07/frontend-framework-dimensions/ | 二手 |
| InfoQ VueConf Toronto 2020 | https://www.infoq.com/news/2020/01/vue3-design-evan-you-toronto/ | 二手 |
| Dennis R Data News Interview 2023 | https://dennisrdatanews.netlify.app/post/2023-08-26-evan-you-interview/ | 二手（翻译整理） |
| Web Worker 播客 No.41 | http://podcast.webworker.tech/41 | 一手（受访，中文） |
| GitNation 演讲列表 | https://gitnation.com/person/Evan_You | 二手汇总 |
