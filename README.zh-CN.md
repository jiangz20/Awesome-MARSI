# Awesome-MARSI

**Multi-Agent Recursive Self-Improvement**

[English](README.md) | [简体中文](README.zh-CN.md)

多智能体递归自我改进相关论文与资源精选。目前收录 **32 篇**，最近核验日期为 **2026-10-30**。

围绕协作架构演化、经验积累与迁移、改进机制递归演化三条主线，同时收录必要的单智能体方法与评测基线。MARSI 在此是组织文献的主题名称，不表示所有条目均提出了完整的多智能体 RSI 系统。

**范围与证据：**单次答案反思、测试时团队搜索、跨任务技能继承、权重更新和改进器更新属于不同机制。各条目的边界说明用于防止混淆；论文的自述不等于独立复现。此列表是精选起点，不是穷尽性系统综述。

## 导航

- [直接相关：多智能体自我改进](#core)
- [工作流与团队结构演化](#workflow)
- [经验、记忆与技能继承](#experience)
- [自身代码修改与模型适应](#selfmod)
- [协作与反思基础](#foundations)
- [基准与评测](#evaluation)

[Reading guide / 阅读指南](docs/reading-guide.md) · [BibTeX](papers.bib) · [Structured metadata / 结构化数据](data/papers.json) · [Contributing](CONTRIBUTING.md)

## 建议先读

MASS (2026) → Gödel Forest → RHI → Multi-Agent Evolve → Skill-MAS → Darwin Gödel Machine → RSIBench-Data.

**缩写提醒：**MASS (2025) 是 Multi-Agent System Search；MASS (2026) 是 Multi-Agent Self-Supervision。它们是两篇不同论文。

<a id="core"></a>

## 直接相关：多智能体自我改进 (4)

### MASS (2026) · 2026-10

**Recursive Self-Improvement through Multi-Agent Self-Supervision**

[Paper](https://arxiv.org/abs/2610.12176) · [PDF](https://arxiv.org/pdf/2610.12176)

交替进行多智能体工作流进化与自生成轨迹 SFT，更新后的模型继续承担提出、执行与评估角色。

- 更新对象 / 评测对象: Workflow + weights.
- 证据边界: 摘要报告了两轮循环，不能据此推断无限持续改进或所有领域都受益。

### Gödel Forest · 2026-09

**Gödel Forest: Balancing Search Depth and Breadth for Data-Centric Recursive Self-Improvement**

[Paper](https://arxiv.org/abs/2609.36675) · [PDF](https://arxiv.org/pdf/2609.36675) · [Code](https://github.com/evolvent-ai/Godel-Forest)

多智能体分别维护持久搜索树，通过共享程序性经验协同探索训练数据策略。

- 更新对象 / 评测对象: Data strategies + shared memory + target weights.
- 证据边界: 需要区分目标模型的进步与研究智能体自身改进能力的进步。

### RHI · 2026-07

**Recursive Harness Self-Improvement**

[Paper](https://arxiv.org/abs/2607.15524) · [PDF](https://arxiv.org/pdf/2607.15524)

利用历史版本间的成对反馈优化提示层 harness，重点涉及上下文管理与智能体间信息流。

- 更新对象 / 评测对象: Prompt-level harness.
- 证据边界: 已展示的是 harness 优化，不能推断已完成多轮模型与 harness 联合训练。

### Multi-Agent Evolve · 2025-10

**Multi-Agent Evolve: LLM Self-Improve through Co-evolution**

[Paper](https://arxiv.org/abs/2510.23595) · [PDF](https://arxiv.org/pdf/2510.23595)

由同一 LLM 实例化出题、求解、裁判角色，以强化学习实现多角色共进化。

- 更新对象 / 评测对象: Role policies / model weights.
- 证据边界: 多角色共训练与 MARSI 密切相关，但改进器是否变强需要单独验证。

<a id="workflow"></a>

## 工作流与团队结构演化 (6)

### MAS-ZERO · 2025-05

**MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision**

[Paper](https://arxiv.org/abs/2505.14996) · [PDF](https://arxiv.org/pdf/2505.14996)

在单个问题的推理过程中依据元反馈设计、批判并修订多智能体配置。

- 更新对象 / 评测对象: Per-instance team design.
- 证据边界: 问题实例内的自适应，并不自动意味着持久的跨任务继承。

### EvoFlow · 2025-02

**EvoFlow: Evolving Diverse Agentic Workflows On The Fly**

[Paper](https://arxiv.org/abs/2502.07373) · [PDF](https://arxiv.org/pdf/2502.07373)

通过检索、交叉、变异和生态位选择，维护异构且复杂度可变的工作流种群。

- 更新对象 / 评测对象: Workflow population.
- 证据边界: 工作流演化与 RSI 相关，但并未因此证明优化器递归变强。

### MASS (2025) · 2025-02

**Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies**

[Paper](https://arxiv.org/abs/2502.02533) · [PDF](https://arxiv.org/pdf/2502.02533)

分阶段优化局部提示、工作流拓扑及全局提示，适合作为自动团队设计基线。

- 更新对象 / 评测对象: Prompts + topology.
- 证据边界: 此处 MASS 指 Multi-Agent System Search，与 2026 年的 Multi-Agent Self-Supervision 不同。

### AFlow · 2024-10

**AFlow: Automating Agentic Workflow Generation**

[Paper](https://arxiv.org/abs/2410.10762) · [PDF](https://arxiv.org/pdf/2410.10762) · [Code](https://github.com/FoundationAgents/AFlow)

使用蒙特卡洛树搜索与执行反馈优化代码表示的工作流。

- 更新对象 / 评测对象: Code-represented workflow.
- 证据边界: 可作为工作流搜索基线，工作流变好不能直接等同于优化器变强。

### ADAS · 2024-08

**Automated Design of Agentic Systems**

[Paper](https://arxiv.org/abs/2408.08435) · [PDF](https://arxiv.org/pdf/2408.08435)

元智能体参考不断扩展的设计档案，以代码生成和搜索新的智能体系统。

- 更新对象 / 评测对象: Agent design + archive.
- 证据边界: 自动设计可以由固定设计者完成，应与设计者自身改进区分。

### DSPy · 2023-10

**DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines**

[Paper](https://arxiv.org/abs/2310.03714) · [PDF](https://arxiv.org/pdf/2310.03714) · [Code](https://github.com/stanfordnlp/dspy)

将声明式语言模型程序编译为按任务指标优化的流程，为模块化优化提供基础。

- 更新对象 / 评测对象: Prompts / demonstrations / pipeline parameters.
- 证据边界: 属于通用优化基础设施，不是多智能体递归改进的直接证据。

<a id="experience"></a>

## 经验、记忆与技能继承 (3)

### Skill-MAS · 2026-06

**Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Systems**

[Paper](https://arxiv.org/abs/2606.18837) · [PDF](https://arxiv.org/pdf/2606.18837)

从多轨迹中选择性反思，积累可迁移的编排 Meta-Skill，将经验保留与参数更新解耦。

- 更新对象 / 评测对象: Orchestration meta-skill.
- 证据边界: 编排知识持续积累，本身不足以证明优化器的改进能力增强。

### Voyager · 2023-05

**Voyager: An Open-Ended Embodied Agent with Large Language Models**

[Paper](https://arxiv.org/abs/2305.16291) · [PDF](https://arxiv.org/pdf/2305.16291)

结合自动课程、环境反馈与可执行技能库，持续获取并复用技能。

- 更新对象 / 评测对象: Executable skill library.
- 证据边界: 属于具身单智能体的技能继承参照，不是 MARSI 系统。

### Reflexion · 2023-03

**Reflexion: Language Agents with Verbal Reinforcement Learning**

[Paper](https://arxiv.org/abs/2303.11366) · [PDF](https://arxiv.org/pdf/2303.11366)

将任务反馈转化为文字反思并保存到情景记忆，用于后续尝试。

- 更新对象 / 评测对象: Episodic reflection memory.
- 证据边界: 尝试之间的反思不足以单独证明改进器层面的递归增强。

<a id="selfmod"></a>

## 自身代码修改与模型适应 (6)

### AIDE² · 2026-09

**Recursive self-improvement of AI research agents**

[Paper](https://arxiv.org/abs/2609.26457) · [PDF](https://arxiv.org/pdf/2609.26457)

研究智能体修改自身代码，经评估接受的版本成为下一轮改进对象，并考察跨任务迁移。

- 更新对象 / 评测对象: Research-agent code.
- 证据边界: 属于自身代码修改的重要参照，并不天然等同于多智能体协作方法。

### HELIX · 2026-08

**HELIX: Model-Harness Co-evolution for Recursive Self-Improvement**

[Paper](https://arxiv.org/abs/2608.13951) · [PDF](https://arxiv.org/pdf/2608.13951) · [Code](https://github.com/HKUDS/HELIX)

对 harness 组件、干预和兄弟轨迹进行溯源，为模型训练保留可验证数据。

- 更新对象 / 评测对象: Harness components + training records.
- 证据边界: 摘要仅评估一轮演化，持续共进化属于更强的待验证主张。

### SEAL · 2025-06

**Self-Adapting Language Models**

[Paper](https://arxiv.org/abs/2506.10943) · [PDF](https://arxiv.org/pdf/2506.10943)

根据更新后的下游表现，学习生成适应数据及更新指令，连接自生成监督与权重更新。

- 更新对象 / 评测对象: Self-edit policy + weights.
- 证据边界: 属于模型自适应机制，单独使用并不构成多智能体 RSI 系统。

### Darwin Gödel Machine · 2025-05

**Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents**

[Paper](https://arxiv.org/abs/2505.22954) · [PDF](https://arxiv.org/pdf/2505.22954) · [Code](https://github.com/jennyzzt/dgm)

结合智能体自身代码修改、进化档案与开放式探索，保存可继续演化的候选。

- 更新对象 / 评测对象: Agent code + archive.
- 证据边界: 种群或档案中的多个候选，不自动等于单个任务内协作的多智能体团队。

### SICA · 2025-04

**A Self-Improving Coding Agent**

[Paper](https://arxiv.org/abs/2504.15228) · [PDF](https://arxiv.org/pdf/2504.15228)

允许编码智能体编辑自身实现，并在编码任务上检验修改后的能力。

- 更新对象 / 评测对象: Agent implementation.
- 证据边界: 适合作为代码级自我改进基线，多智能体协调并非其核心机制。

### Gödel Agent · 2024-10

**Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement**

[Paper](https://arxiv.org/abs/2410.04444) · [PDF](https://arxiv.org/pdf/2410.04444) · [Code](https://github.com/Arvid-pku/Godel_Agent)

让智能体在高层目标指导下动态修改自身逻辑与行为，是自指式改进的重要参照。

- 更新对象 / 评测对象: Agent logic / behavior.
- 证据边界: 运行时自身修改与稳定的跨任务递归增益需要分开检验。

<a id="foundations"></a>

## 协作与反思基础 (5)

### Mixture-of-Agents · 2024-06

**Mixture-of-Agents Enhances Large Language Model Capabilities**

[Paper](https://arxiv.org/abs/2406.04692) · [PDF](https://arxiv.org/pdf/2406.04692)

通过多层智能体输出聚合发挥多个模型的互补能力。

- 更新对象 / 评测对象: Layered response aggregation.
- 证据边界: 推理时协作并不意味着系统会自我演化。

### AutoGen · 2023-08

**AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation**

[Paper](https://arxiv.org/abs/2308.08155) · [PDF](https://arxiv.org/pdf/2308.08155)

提供可配置的多智能体对话、工具与人类交互机制。

- 更新对象 / 评测对象: Conversation orchestration.
- 证据边界: 属于框架基础设施，使用该框架不自动带来递归学习机制。

### MetaGPT · 2023-08

**MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework**

[Paper](https://arxiv.org/abs/2308.00352) · [PDF](https://arxiv.org/pdf/2308.00352) · [Code](https://github.com/FoundationAgents/MetaGPT)

通过角色分工与标准操作流程组织多智能体协作。

- 更新对象 / 评测对象: Role / SOP orchestration.
- 证据边界: 适合作为结构化协作基线，本身不是 RSI 算法。

### Multiagent Debate · 2023-05

**Improving Factuality and Reasoning in Language Models through Multiagent Debate**

[Paper](https://arxiv.org/abs/2305.14325) · [PDF](https://arxiv.org/pdf/2305.14325)

让多个模型实例在多轮辩论中交换并修订推理与答案。

- 更新对象 / 评测对象: Current answer / reasoning.
- 证据边界: 多轮辩论主要作用于当前答案，不一定产生可继承的系统变化。

### Self-Refine · 2023-03

**Self-Refine: Iterative Refinement with Self-Feedback**

[Paper](https://arxiv.org/abs/2303.17651) · [PDF](https://arxiv.org/pdf/2303.17651)

利用同一模型循环生成反馈并修订当前答案，是单次输出改进的基础对照。

- 更新对象 / 评测对象: Current output.
- 证据边界: 改善的是当前输出，不意味着持久的系统更新。

<a id="evaluation"></a>

## 基准与评测 (8)

### RSIBench-Data · 2026-07

**RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement**

[Paper](https://arxiv.org/abs/2607.25886) · [PDF](https://arxiv.org/pdf/2607.25886) · [Code](https://github.com/evolvent-ai/RSIBench-Data)

在固定后训练基础设施上评测能力诊断、训练数据策略修改与检查点反馈利用。

- 更新对象 / 评测对象: Training-data research loop.
- 证据边界: 反复反馈可用于开发，检验泛化时仍应保留独立的最终评测。

### SEA-Eval · 2026-04

**SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment**

[Paper](https://arxiv.org/abs/2604.08988) · [PDF](https://arxiv.org/pdf/2604.08988)

使用序列任务流评测跨任务经验积累，关注成功率、token 开销与演化轨迹。

- 更新对象 / 评测对象: Sequential cross-task evolution.
- 证据边界: 序列任务上的增益，不能单独识别优化器自身是否改进。

### Terminal-Bench 2.0 · 2026-01

**Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces**

[Paper](https://arxiv.org/abs/2601.11868) · [PDF](https://arxiv.org/pdf/2601.11868)

以具体验证测试评估智能体在真实终端环境中的长链路任务执行。

- 更新对象 / 评测对象: Long-horizon terminal execution.
- 证据边界: 属于任务表现的评测锚点，不是专门的多智能体 RSI 基准。

### MLR-Bench · 2025-05

**MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research**

[Paper](https://arxiv.org/abs/2505.19955) · [PDF](https://arxiv.org/pdf/2505.19955)

评测开放式机器学习研究的多个阶段及端到端交付，使用结构化审稿量表。

- 更新对象 / 评测对象: Open-ended ML research.
- 证据边界: 需要核查执行证据与评分器可靠性，仅生成研究报告并不足够。

### ScienceAgentBench · 2024-10

**ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery**

[Paper](https://arxiv.org/abs/2410.05080) · [PDF](https://arxiv.org/pdf/2410.05080)

以真实论文中的科学任务为基础，评价 Python 交付物、执行结果和成本。

- 更新对象 / 评测对象: Scientific data / code tasks.
- 证据边界: 比较论文结果前，应确认具体数据集版本和配套评测资产。

### DSBench · 2024-09

**DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?**

[Paper](https://arxiv.org/abs/2409.07703) · [PDF](https://arxiv.org/pdf/2409.07703)

覆盖大文件、多表和多模态上下文下的数据分析与建模任务。

- 更新对象 / 评测对象: Data analysis + modeling.
- 证据边界: 分析与建模的任务结构和指标不同，建议分别报告。

### SWE-bench · 2023-10

**SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**

[Paper](https://arxiv.org/abs/2310.06770) · [PDF](https://arxiv.org/pdf/2310.06770)

用真实仓库问题及可执行测试检验代码修改能力。

- 更新对象 / 评测对象: Repository issue resolution.
- 证据边界: 区分原版、Lite、Verified 等版本；此条引用的是原始论文。

### AgentBench · 2023-08

**AgentBench: Evaluating LLMs as Agents**

[Paper](https://arxiv.org/abs/2308.03688) · [PDF](https://arxiv.org/pdf/2308.03688) · [Code](https://github.com/THUDM/AgentBench)

跨多种交互式环境评测智能体的推理与决策能力。

- 更新对象 / 评测对象: Interactive agent environments.
- 证据边界: 属于通用智能体评测基础，不是专门的递归改进协议。

## 核验与使用说明

日期采用 arXiv 首次提交日期，不推定会议录用状态。逐条核验题名、作者、日期和摘要；代码链接仅在论文页面明确链接且 GitHub API 核验成功时收录。缺少代码链接表示本轮未确认，不代表没有开源实现。未复现实验；不跨设置比较分数。

[Curation method / 收录方法](docs/curation.md). Original annotations and metadata are released under [CC0-1.0](LICENSE). Linked papers, code and datasets retain their own licenses.
