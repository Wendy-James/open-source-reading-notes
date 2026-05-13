# Open Source Reading Notes

这个仓库记录我对高质量开源项目的阅读路线、工程观察和可复用实践。开源项目所有权归原作者/组织；这里的重点是训练自己读懂真实工程、拆解设计取舍，并把观察转化为自己的项目改进。

## Reading Map

| Project | Area | What I Study |
|---|---|---|
| [vuejs/core](https://github.com/vuejs/core) | Frontend framework | 响应式系统、组件运行时、编译器、包结构、TypeScript 组织方式 |
| [element-plus/element-plus](https://github.com/element-plus/element-plus) | Vue component library | 表单、表格、弹窗、主题变量、组件 API、文档示例 |
| [ant-design/ant-design](https://github.com/ant-design/ant-design) | React design system | 设计系统、复杂组件状态、可访问性、测试与文档协作 |
| [vercel/next.js](https://github.com/vercel/next.js) | Full-stack React framework | 路由、渲染模式、服务端能力、构建流程、开发者体验 |
| [fastapi/fastapi](https://github.com/fastapi/fastapi) | Python API framework | OpenAPI、数据校验、异步接口、自动文档、错误处理 |
| [microsoft/TypeScript](https://github.com/microsoft/TypeScript) | Language tooling | 类型推导、编译器结构、语言服务、工程化约束 |
| [prisma/prisma](https://github.com/prisma/prisma) | Database tooling | Schema 设计、类型安全查询、迁移流程、Node.js 数据访问层 |

## Current Questions

- 一个成熟框架如何组织 monorepo、packages、examples 和测试目录？
- 组件库如何在可配置、可维护、可访问性和视觉一致性之间平衡？
- API 框架如何把数据校验、错误处理、文档生成和开发体验串在一起？
- 类型系统如何提升重构安全性，并约束大型项目里的跨模块调用？
- 自己的项目可以优先借鉴哪些小而确定的实践？

## Notes Template

每次阅读一个模块时，用同一套结构记录：

```text
Project:
Module:
Entry files:
Problem solved:
Design decision:
Trade-off:
Reusable idea:
Can improve my project:
```

## Applied Back To My Projects

- 后台管理系统：对照 Element Plus 和 Ant Design，继续改进表单、表格、反馈提示和组件拆分。
- AI 知识助手：对照 Next.js 与 FastAPI，补充更清晰的接口边界、错误状态和异步流程。
- Python 自动化工具：对照 FastAPI、Prisma 和 TypeScript 的类型约束思想，强化数据模型、dry-run 和测试覆盖。
- 作品集页面：持续保持信息清晰、项目真实、链接可访问、文档可复盘。

## Principle

Read real projects, extract small patterns, apply them honestly.
