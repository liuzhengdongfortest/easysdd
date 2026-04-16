# Evan You 访谈对话研究

> 本文档收录 Evan You（尤雨溪）在播客、访谈、AMA、演讲 Q&A 等场合的即兴言论。
> 标注：【一手】= 他本人说的，【二手】= 别人转述。
> 可信度：★★★ = 有原文可查 / ★★ = 摘要可信 / ★ = 间接引用

---

## 一、对竞争框架的态度（React / Angular / Svelte / Solid）

### React

**【一手 ★★★】** 对 React 保持尊重但不直接竞争：
> "There is not going to be this one true framework that just makes everyone happy. The more important part is, make it better for the people who actually enjoy your framework."
— *Between the Wires, freeCodeCamp, 2017*（Source: https://www.freecodecamp.org/news/between-the-wires-an-interview-with-vue-js-creator-evan-you-e383cbf57cc4/）

**【一手 ★★★】** 对 React 社区规模保持客观：
> "React has a bigger community...high-quality projects. But I'm just one person. I can't write all of that myself."
— *CoRecursive Podcast, "From 486 to Vue.js"*（Source: https://corecursive.com/vue-with-evan-you/）

**【一手 ★★★】** 关于学习竞争对手：
> "There are great things over there, there are great things we can learn from...it's not like an ego contest...how about we make ourselves better?"
— *CoRecursive Podcast*

**【一手 ★★★】** 早期发推对 React 元框架化的调侃（2021）：
> "So… React is now a Meta framework?"
— *Twitter/X @youyuxi, 2021-10-29*（Source: https://x.com/youyuxi/status/1453965251414687744）

### React Server Components（RSC）——立场演变时刻

**【一手 ★★★】** 2025年对RSC的明确批评（这是他罕见地对某个技术方向直接表态"失败"）：
> "I don't think RSC itself being a React feature is a problem - it unlocks some interesting patterns. The issue is the tradeoffs involved in making it work. It leaks into, or even demands control over layers that are previously not in scope for client-side frameworks. This creates heavy complexity (and associate mental overhead) in order to get the main benefits it promises."
— *Twitter/X @youyuxi, 2025-03-25*（Source: https://x.com/youyuxi/status/1905275294090662266）

**【一手 ★★★】** 更早时（2024）对RSC与传统SSR优劣的即兴分析：
> "This does makes me realize that the traditional (compared to RSC) SSR on first load -> hydrate into SPA model is much less susceptible to skewing (client / server version mismatch). Once hydrated, a long running SPA only interacts with the server via loading static assets and..."
— *Twitter/X @youyuxi, 2024-06-23*（Source: https://x.com/youyuxi/status/1804331313421521101）

**【二手 ★★】** 总结 Evan 对RSC的整体判断：
"Vue.js creator Evan You responded that 'the bet' on React Server Components becoming the 'idiomatic way to use React' has failed, thanks to the tradeoffs involved."
— *LinkedIn Syntax.fm 引用，April 2025*（Source: https://www.linkedin.com/posts/syntaxfm_rsc-react-vuejs-activity-7376338184852615169-1_9i）

### Svelte / Solid——框架收敛时刻（立场变化）

**【一手 ★★★】** 2025年对框架收敛的坦率承认（早年他更强调Vue的独特性，此时转为承认殊途同归）：
> "Short answer: yes, the core premises are all similar. Especially with Svelte 5 and Vue Vapor Mode, they are pretty much converging on the same reactivity paradigm *and* the same rendering paradigm. Compared to React: - The reactivity model is better aligned with idiomatic JS... Difference between Vue / Svelte / Solid largely comes down to API style preferences."
— *Twitter/X @youyuxi, reply to @ryanflorence, 2025*（Source: https://x.com/youyuxi/status/1939176276298027140）

**【一手 ★★★】** 对 Svelte / Solid 编译器方向的认可：
> "There are a few new things worth mentioning like Svelte and Solid, especially the way they leverage compile time optimization. I think frameworks moving more into a compiler is a general trend."
— *Monterail Interview, 2025*（Source: https://www.monterail.com/blog/interview-evan-you-vue3）

### Angular

**【一手 ★★★】** Vue 起源于对 Angular 的反思（经典立场，多次重述）：
> "What if I could just extract the part that I really liked about Angular and build something really lightweight?"
— *Between the Wires, freeCodeCamp, 2017*

> "This feels a bit too heavy-handed for the kind of things we were building" （谈 Angular 在 Google Creative Lab 的使用）
— *CoRecursive Podcast*

---

## 二、对 TypeScript 的看法演变

### 早期：用 Flow，对 TypeScript 态度中立

**【二手 ★★】** Vue 2 用 Flow 而非 TypeScript 的决定被他后来称为遗憾（2020 年前后）：
"He said advice he would give his younger self when starting work on Vue 2.0 was 'you probably should just go TypeScript.' He explained that while Flow was easy to introduce to the codebase back then, 'it just never decided to become 1.0. Every minor [release] there's just a bunch of things I had to fix in order just to upgrade.'"
— *egghead.io podcast interview with John Lindquist*（Source: https://egghead.io/podcasts/evan-you-creator-of-vue-js）

### Vue 3 时期：全面拥抱 TypeScript

**【一手 ★★★】** Vue 3 用 TypeScript 重写的理由：
> "TypeScript is obviously on the rise so any modern framework has to be designed with it in mind. Even if you don't use TypeScript Volar is able to leverage Vue typing and give you hints."
— *Monterail Interview*

**【一手 ★★★】** 反驳"Vue 3 强制用 TypeScript"的误解（ShopTalk Show #350，~2020）：
> "You don't have to use TypeScript with Vue 3, and the API will remain mostly the same if you don't want to use it. However, rewriting in TypeScript allows them to provide better TypeScript support."
— *ShopTalk Show #350*（Source: https://shoptalkshow.com/350/）

**【一手 ★★★】** TypeScript 与 class 的关系——一个典型的即兴反转：
> "Ironically I think TypeScript has helped me more with avoiding classes than using them. Vue 3 is a 100% TS codebase with 0 usage of classes."
— *Twitter/X @youyuxi, 2019-09-21*（Source: https://x.com/youyuxi/status/1175433025179529216）

**【一手 ★★★】** 早期（2017）声明使用 TS 不影响 Vue 用户 API：
> "me using TS doesn't affect Vue's user API, just more robust code to rely on ;)"
— *Twitter/X @youyuxi, 2017*（Source: https://twitter.com/youyuxi/status/844201196625653760）

**立场演变总结**：Flow（2016 Vue 2）→ 承认失误 → Vue 3 全面 TypeScript 重写 → 当前：TypeScript 是"any modern framework"必须支持的，但用户可以选择不用。

---

## 三、对 Rust / Go 等工具链语言的看法

### 为什么选 Rust 而非 Go

**【一手 ★★★】** Rolldown 公告推文（2023-10-05），直接说明目标：
> "The cat is out of the bag: we are working on Rolldown, a rust port of Rollup. 🦀 - Focus: performance with best-effort compatibility with Rollup - Goal: replace esbuild and Rollup in Vite with minimal impact on end users"
— *Twitter/X @youyuxi, 2023-10-05*（Source: https://x.com/youyuxi/status/1709943106215530867）

**【一手 ★★★】** 对比 esbuild（Go）和 OXC/Rolldown（Rust）架构差异：
> "ESBuild layers many concerns across minimal AST passes for speed, making extensions difficult. OXC, by contrast, isolates concerns and includes semantic analysis APIs as first-party features."
— *devtools.fm Episode #121, 2024-11-11*（Source: https://www.devtools.fm/episode/121）

**【一手 ★★★】** 对 SWC（第一个 JS Rust 工具链）的评价——礼貌但克制：
> "I don't want to bash SWC, because it is the first JavaScript Rust toolchain...I think there are things we can learn from it."
— *devtools.fm Episode #121*

**【一手 ★★★】** 对"原生化一切"的警告（JS Party #212，~2022）：
> "We don't want to natify everything... we should natify certain really well-scoped, important infrastructure projects like Babel or Rollup—not every tiny helper library."
— *JS Party #212*（Source: https://changelog.com/jsparty/212）

**关于 Go 重写的 April Fool's 玩笑（2025）**：
> "In order to better integrate with tsgo, we are going to rewrite Rolldown and Oxc in Go."
— *Twitter/X @youyuxi, April 1, 2025*（Source: https://x.com/youyuxi/status/1906937860319801628）
注：这是愚人节玩笑。背景是 Microsoft tsgo（TypeScript Go 重写）引发讨论时，他故意反向调侃。

---

## 四、关于开源可持续性与商业化

### Changelog #661 / VoidZero 阶段的核心观点

**【一手 ★★★】** 开源关键真相：
> "The key to cracking that problem is to make the right people pay for open source. That won't happen through donations."
— *Changelog Interviews #661, Vite documentary companion pod*（Source: https://changelog.com/podcast/661）

**【一手 ★★★】** 创立 VoidZero 的理由：
> "This is an ambitious vision, and achieving it requires a full-time, dedicated team—something that wasn't possible under the independent sustainability model"
— *VoidZero 发布博客, 2024-10-04*（Source: https://voidzero.dev/posts/announcing-voidzero-inc）

**【一手 ★★★】** Vue 赞助模式的局限性对比：
> "It's hard to replicate exactly what I did. There's no real formula you can follow." （谈 Vue 的独立维护者模式）
— *Changelog #661*

**【一手 ★★★】** Vite+ 授权策略说明：
"Vite remains fully open source. Vite+ is 'source-available,' balancing accessibility for individuals and open-source projects while capturing value from commercial users."
— *Changelog #661 概述*

**【一手 ★★★】** 关于给贡献者的认可策略（Matias Capeletto 的案例）：
"For Vite specifically, Evan deliberately recruited contributors like Matias Capeletto, recognizing their passion and offering team recognition initially without financial compensation – until StackBlitz hired Matias full-time."
— *Changelog #661*

### 早期：从个人维护者到全职开源

**【一手 ★★★】** 离职时的算法（来自 GitHub README 故事）：
"I had some savings...combine that with my Patreon, that's like combining like a bit over $4,000 a month, enough to make a living."
— *CoRecursive Podcast*

**【一手 ★★★】** 妻子对他辞职的反应（非常真实的细节）：
"She discovered his job departure via COBRA insurance letter, responded pragmatically: 'Try this, but if this doesn't work out, I'm gonna kick you back to a big company.'"
— *CoRecursive Podcast*

**【一手 ★★★】** 关于开源倦怠：
> "I've seen so many maintainers pour all their spare time into a project, but in the end, they burn out and leave. More people need to practice a healthy work-life balance."
> "At its core, open source is either your main path, or it's supplementary. It can't be both."
— *GitHub ReadME Project*（Source: https://github.com/readme/stories/evan-you）

**【一手 ★★★】** 关于网络负面反馈：
> "Maybe one out of a hundred happy users will tweet praise. But there will always be someone raising an issue."
— *CoRecursive Podcast*

---

## 五、即兴类比与比喻（特别收录）

**"Vite is like the United Nations of JavaScript"**（Stack Overflow 播客标题，2025）：
Vite 作为中立平台，将 React、Vue、Svelte、Solid 等不同阵营统一在同一构建工具下。这个比喻是访谈标题，具体说话人（Evan 本人还是主持人）需确认，但来自对话语境。
— *Stack Overflow Podcast, 2025-10-10*（Source: https://stackoverflow.blog/2025/10/10/vite-is-like-the-united-nations-of-javascript/）

**"Your project takes two minutes to startup and every hot module replacement takes three seconds."**（描述 Webpack 问题的直接痛点陈述，用具体数字代替形容词）
— *ShopTalk Show #454*（Source: https://shoptalkshow.com/454/）

**"The browser has a module system, so how about we just let the browser do that?"**（Vite 核心思路的一句话概括）
— *ShopTalk Show #454*

**"I was fed up with how slow VuePress was...If I can just swap this with Vite, my life would be so much better."**（Vite 诞生的个人动机——用自身的挫败感解释创新）
— *ShopTalk Show #454*

**"Even though you technically have a build step, when you're editing the component, you don't actually feel like there is one."**（对开发者体验的比喻性描述）
— *Stack Overflow Blog, 2025*

**"Vite was able to get off the ground really fast because we were able to leverage the existing plugin ecosystem of Rollup."**（解释 Rollup 生态作为起跳板）
— *Stack Overflow Blog, 2025*

**Vite 起源的极简叙述**：
> "got something interesting, and then kept pushing on, and eventually, more people started using it."
— *Changelog #661 / Vite 纪录片配套播客*

---

## 六、被追问时的反应模式

### Composition API 争议——立场在社区压力下变化

**【二手 ★★★】** 原本的意图与现实的碰撞：
"Evan You said they were 'going to ship this new API, the old API is going to be deprecated,' but the problem was the new API upset many existing users."
— *CoRecursive Podcast 相关报道*（Source: https://corecursive.com/vue-with-evan-you/）

**【一手 ★★★】** 对社区两极化需求的坦率承认：
> "Our early user base preferred lightweight solutions...when we propose solutions for advanced cases, these simple case users get pissed off."
— *CoRecursive Podcast*

**【一手 ★★★】** 最终立场（承认无法让所有人满意）：
> "The best you can do is make the most amount of people happy. But inevitably you're gonna make someone unhappy."
— *CoRecursive Podcast*

**【一手 ★★★】** Vue 4 对 Options API 的承诺（DejaVue Episode 15，2024年）：
> "The cost of keeping options API around is, like, very, very low because there's literally no maintenance burden for it nowadays."
> "Options API is probably gonna be here to stay for as long as we know."
— *DejaVue Podcast, Episode 15, 2024-07-04*（Source: https://share.transistor.fm/s/6b6bab42）

### Vue 3 与 TypeScript——被追问是否强制使用时

**【一手 ★★】** 明确否认强制论：
"You don't have to use TypeScript with Vue 3" — 多次公开场合重述，包括 ShopTalk Show #350、Vue Amsterdam 等。

### 被问 Rolldown/Rust 性能取舍时（devtools.fm #121）

**【一手 ★★★】** 直面 JS 插件跨语言边界的性能开销，没有回避问题：
"JavaScript plugins create overhead when crossing language boundaries. Raw Rolldown handles 20,000 modules in 600ms, but adding plugins slows it 'two to three times' due to serialization costs."
— *devtools.fm Episode #121, 2024*

---

## 七、个人背景与原始动机（Origin Story）

**【一手 ★★★】** 对 web 的核心吸引力（Flash 时代起）：
> "I was attracted to JavaScript because of the ability to just build something and share it instantly with the world."
— *Between the Wires, freeCodeCamp, 2017*

**【一手 ★★★】** Vue 起源的真实心态：
> "It started out really with no expectations. It's more, 'Let's see if I can do this. It's fun.'"
— *CoRecursive Podcast / GitHub ReadME*

**【一手 ★★★】** Google 期间的挫败感（对 Creative Lab 项目的描述）：
> "Four out of five projects would end up nowhere...Vue was an outlet for that. Everything I do on Vue gets real-world feedback."
— *CoRecursive Podcast*

**【一手 ★★★】** 关于影响力的驱动力：
> "If I do work, but I can't see how it affects people in the world, then it becomes much less satisfying."
— *GitHub ReadME Project*

**【一手 ★★★】** 计算好退路再冒险：
> "If you know you probably can land a job if you want to, but also have this really crazy idea you're passionate about, I think you should try it...or you'd live the rest of your life thinking, 'Why didn't I try?'"
— *CoRecursive Podcast*

---

## 八、关于 VoidZero 与 JavaScript 工具链的未来愿景

**【一手 ★★★】** VoidZero 核心技术理念：
> "using the same AST, resolver, and module interop for all tasks...eliminating inconsistencies and reducing redundant parsing costs"
— *VoidZero 发布博客*（Source: https://voidzero.dev/posts/announcing-voidzero-inc）

**【一手 ★★★】** 对 JS 工具链碎片化的诊断：
> "every application relies on a myriad of third-party dependencies, and configuring them to work well together remains one of the most daunting tasks"
— *VoidZero 发布博客*

**【一手 ★★★】** Rolldown 公开后的进展描述（2024-03-05）：
> "Rolldown is open source! The Rust-based bundler designed for the future of Vite. It is still a work in progress, but it's now in a state that we are happy to share with the community and welcome contributions."
— *Twitter/X @youyuxi, 2024-03-05*（Source: https://x.com/youyuxi/status/1766014404666245582）

**【一手 ★★★】** VoidZero 公司公告（2024-10-04）：
> "Announcing @voidzerodev: a company building the next-generation unified toolchain for JavaScript. We are the creators and core-contributors of Vite, Vitest, Rolldown and Oxc - and we will unite these projects under a coherent vision to power the next generation of web"
— *Twitter/X @youyuxi, 2024-10-04*（Source: https://x.com/youyuxi/status/1841100770537849179）

---

## 九、中文语境的访谈线索

### Web Worker 播客第 41 期（2023-12-04）

**【二手 ★★】** 涉及话题摘要（无逐字引用，来源为播客简介）：
- Vue2 到 Vue3 经验复盘
- Vite 这一年的变化和展望
- Vapor Mode 规划
- 开源社区和企业开发的区别
- GitHub 用户名 yyx990803 的含义
- 是否有退休计划
- 是否用 GitHub Copilot 写 Vue（轻松话题）
- 发际线保养（非技术话题，可见他接受轻松提问不回避）

来源：https://www.xiaoyuzhoufm.com/episode/656de7e18502c0b989efdcd0 / https://podcasts.apple.com/cn/podcast/no-41/id1586927144?i=1000637488918

### OSCHINA 深度访谈（2024，《深度对话尤雨溪：前端的未来、Rust、AI 与开源商业化》）

**【二手 ★★】** 话题覆盖：前端未来、Rust 工具链、AI 对开发影响、开源商业化路径
— 原文地址：https://www.oschina.net/news/365057（页面加载失败，内容待确认）

---

## 十、已知的访谈清单（含时间线）

| 时间 | 节目/媒体 | 主题 | 可信度 | 链接 |
|------|-----------|------|--------|------|
| 2015-11-28 | The Changelog #184 | Vue.js 早期 | ★★★ | https://changelog.com/podcast/184 |
| 2017 | Between the Wires / freeCodeCamp | 个人背景、Vue哲学 | ★★★ | https://www.freecodecamp.org/news/between-the-wires-an-interview-with-vue-js-creator-evan-you-e383cbf57cc4/ |
| 2019-03 | Full Stack Radio #129 | Vue.js 3.0 预览 | ★★ | https://fullstackradio.com/129 |
| 2019-12 | dotJS 2019 | State of Components | ★★ | https://www.dotconferences.com/2019/12/evan-you-state-of-components |
| 2020-05 | Full Stack Radio #140 | Vite 首次介绍 | ★★★ | https://fullstackradio.com/140 |
| 2020-09 | Evrone Interview | Vue 3 release | ★★★ | https://evrone.com/blog/evan-you-interview |
| ~2020 | ShopTalk Show #350 | 维护 Vue.js | ★★★ | https://shoptalkshow.com/350/ |
| ~2020 | egghead.io | Flow vs TypeScript 遗憾 | ★★ | https://egghead.io/podcasts/evan-you-creator-of-vue-js |
| 2021-12-07 | PodRocket (LogRocket) | Vue 3 & Vite | ★★ | https://podrocket.logrocket.com/evan-you |
| 2021 | Enjoy the Vue #23 | Vite + Vue 3 | ★★ | https://dev.to/enjoythevue/episode-23-vite-vue-3-with-evan-you |
| ~2021 | JS Party #135 | Prolog 版 Vue（传说） | ★★ | https://changelog.com/jsparty/135 |
| ~2022 | JS Party #212 | Vite 深度访谈 | ★★★ | https://changelog.com/jsparty/212 |
| ~2022 | devtools.fm #12 | Vue, Vite | ★★ | https://www.devtools.fm/episode/12 |
| ~2022 | ShopTalk Show #454 | All About Vite | ★★★ | https://shoptalkshow.com/454/ |
| 2023-03 | Vue.js Amsterdam (State of the Vuenion) | Vue 3 路线图 | ★★ | 无单独文字稿 |
| 2023-12-04 | Web Worker 播客 #41 | 中文，综合话题 | ★★ | https://www.xiaoyuzhoufm.com/episode/656de7e18502c0b989efdcd0 |
| 2024-07-04 | DejaVue #15 | Vue 十周年 | ★★★ | https://share.transistor.fm/s/6b6bab42 |
| 2024-11-11 | devtools.fm #121 | VoidZero, Rolldown, Rust | ★★★ | https://www.devtools.fm/episode/121 |
| 2024 | DejaVue #31 | VoidZero 全面访谈 | ★★ | https://share.transistor.fm/s/bd4e7344 |
| 2024 | CoRecursive, "From 486 to Vue.js" | 个人故事全景 | ★★★ | https://corecursive.com/vue-with-evan-you/ |
| 2025 | Monterail | Vue 3 DX + TypeScript | ★★★ | https://www.monterail.com/blog/interview-evan-you-vue3 |
| 2025 | Syntax #939 | Vite, Rolldown, VoidZero | ★★★ | https://syntax.fm/show/939/creator-of-vite-evan-you |
| 2025-10-10 | Stack Overflow Podcast | Vite 纪录片 + 工具链未来 | ★★★ | https://stackoverflow.blog/2025/10/10/vite-is-like-the-united-nations-of-javascript/ |
| 2025-10 | The Changelog #661 | Vite 纪录片配套播客 | ★★★ | https://changelog.com/podcast/661 |
| 2025 | freeCodeCamp Podcast #192 | 从艺术学院到开源传奇 | ★★ | https://www.freecodecamp.org/news/evan-you-from-art-school-kid-to-open-source-legend-podcast-192/ |

---

## 十一、他回避或拒绝的话题（线索）

**【二手 ★★】** 对"Vue 会被 React 取代吗"类问题：通常不正面接招，转而强调"框架多元共存是好事"，用"不存在唯一正确框架"来化解（见 freeCodeCamp 采访）。

**【二手 ★★】** 对"Vue 4 具体特性"的追问：在 DejaVue #15 中以"大概率是这个方向"的模糊表达结束话题，不给承诺。

**【一手 ★★★】** 在 Vite 纪录片方向上的主动边界设定：
> "I don't want to make the film about me" — 明确拒绝以个人为中心的叙事框架。
— *Changelog #661*

**【二手 ★★】** 关于"什么时候退休"（Web Worker 播客 #41 轻松话题）：话题存在，但无逐字引用，表明他接受这类非技术问题。

---

*最后更新：2026-04-16*
*研究者：Claude Code（通过 web search + 播客/访谈内容抓取）*
