# Awesome-MARSI

**Multi-Agent Recursive Self-Improvement**

[English](README.md) | [简体中文](README.zh-CN.md)

A curated collection of papers and resources on multi-agent recursive self-improvement. **43 papers**, last verified **2026-11-08**.

The collection follows three themes: evolving collaboration architectures, accumulating transferable experience, and improving the improvement process itself. It also includes relevant single-agent methods and evaluation baselines. MARSI is an organizing topic here, not a claim that every entry implements full multi-agent RSI.

**Scope and evidence:** output refinement, inference-time team search, persistent skill inheritance, weight updates, and optimizer updates are different mechanisms. Each entry states an interpretation boundary. Author-reported findings are not independent reproductions. This is a curated starting point, not an exhaustive systematic review.

## Contents

- [Direct multi-agent self-improvement](#core)
- [Workflow and team evolution](#workflow)
- [Experience, memory and skill inheritance](#experience)
- [Self-modification and model adaptation](#selfmod)
- [Collaboration and reflection foundations](#foundations)
- [Benchmarks and evaluation](#evaluation)

[Reading guide / 阅读指南](docs/reading-guide.md) · [BibTeX](papers.bib) · [Structured metadata / 结构化数据](data/papers.json) · [Contributing](CONTRIBUTING.md)

## Start here

MASS (2026) → Gödel Forest → RHI → Multi-Agent Evolve → Skill-MAS → Darwin Gödel Machine → RSIBench-Data.

**Acronym collision:** MASS (2025) means Multi-Agent System Search; MASS (2026) means Multi-Agent Self-Supervision. These are different papers.

## Latest additions

2026-11-08 · 11 papers · [Update notes / 更新说明](docs/updates-2026-11-08.md)

| Paper | First submitted | Category |
|---|---|---|
| [EvoTeam](https://arxiv.org/abs/2610.39813) | 2026-10-29 | core |
| [Skill∞](https://arxiv.org/abs/2610.35434) | 2026-10-26 | selfmod |
| [EvolveMAS](https://arxiv.org/abs/2610.34450) | 2026-10-25 | experience |
| [Recursia](https://arxiv.org/abs/2610.24464) | 2026-10-17 | selfmod |
| [AGORA](https://arxiv.org/abs/2610.19799) | 2026-10-14 | core |
| [RSI-Forge](https://arxiv.org/abs/2610.09426) | 2026-10-07 | evaluation |
| [Inherit-MAS](https://arxiv.org/abs/2610.02396) | 2026-10-01 | workflow |
| [MILO](https://arxiv.org/abs/2609.38349) | 2026-09-29 | core |
| [MANTA](https://arxiv.org/abs/2607.28527) | 2026-07-30 | workflow |
| [HarnessForge](https://arxiv.org/abs/2606.01779) | 2026-06-01 | selfmod |
| [DecentMem](https://arxiv.org/abs/2605.22721) | 2026-05-21 | experience |

<a id="core"></a>

## Direct multi-agent self-improvement (7)

### EvoTeam · 2026-10

**EvoTeam: Multi-Agent Collaboration via Evolving Teams**

[Paper](https://arxiv.org/abs/2610.39813) · [PDF](https://arxiv.org/pdf/2610.39813) · [Code](https://github.com/DEEP-JLU/EvoTeam)

Maintains a team library and jointly evolves team organization, team-specific interaction rules and skills reusable across teams.

- Update / evaluation target: Reusable teams + interaction rules + agent skills.
- Interpretation boundary: Collaboration-level evolution is central, but recursive improvement of the evolution operator is a stronger separate claim.

### AGORA · 2026-10

**Evolve Together, Fall into Place: How Social Scaffolding Shapes Self-Evolving Multi-Agent Systems**

[Paper](https://arxiv.org/abs/2610.19799) · [PDF](https://arxiv.org/pdf/2610.19799)

Studies how team composition and collaboration, conformity or competition shape the outcomes of agent evolution.

- Update / evaluation target: Team composition + social scaffolding.
- Interpretation boundary: A study of conditions for team evolution, not evidence that every evolving team improves or becomes more decentralized.

### MASS (2026) · 2026-10

**Recursive Self-Improvement through Multi-Agent Self-Supervision**

[Paper](https://arxiv.org/abs/2610.12176) · [PDF](https://arxiv.org/pdf/2610.12176)

Alternates evolutionary multi-agent workflow search and supervised fine-tuning on self-generated trajectories; the updated model also proposes and evaluates workflows.

- Update / evaluation target: Workflow + weights.
- Interpretation boundary: The abstract reports two cycles; this does not establish indefinite or universal improvement.

### Gödel Forest · 2026-09

**Gödel Forest: Balancing Search Depth and Breadth for Data-Centric Recursive Self-Improvement**

[Paper](https://arxiv.org/abs/2609.36675) · [PDF](https://arxiv.org/pdf/2609.36675) · [Code](https://github.com/evolvent-ai/Godel-Forest)

Uses persistent search trees and shared procedural lessons to coordinate agents exploring training-data strategies.

- Update / evaluation target: Data strategies + shared memory + target weights.
- Interpretation boundary: Distinguish improvements to the target model from improvements to the research agents themselves.

### MILO · 2026-09

**MILO: Automated Harness Discovery via Orchestrated Multi-Agent Evolution**

[Paper](https://arxiv.org/abs/2609.38349) · [PDF](https://arxiv.org/pdf/2609.38349)

Combines island-based lineage memory, mutator agents and an orchestrator that adapts the search organization and curriculum.

- Update / evaluation target: Harnesses + discovery strategy.
- Interpretation boundary: Distinguish co-adaptation of search from demonstrated transferable improvement in the optimizer under matched budgets.

### RHI · 2026-07

**Recursive Harness Self-Improvement**

[Paper](https://arxiv.org/abs/2607.15524) · [PDF](https://arxiv.org/pdf/2607.15524)

Refines harness specifications using pairwise feedback over revision history, emphasizing context management and inter-agent information flow.

- Update / evaluation target: Prompt-level harness.
- Interpretation boundary: Harness optimization is demonstrated; do not infer completed multi-round model/harness co-training.

### Multi-Agent Evolve · 2025-10

**Multi-Agent Evolve: LLM Self-Improve through Co-evolution**

[Paper](https://arxiv.org/abs/2510.23595) · [PDF](https://arxiv.org/pdf/2510.23595)

Co-evolves proposer, solver and judge roles instantiated from one LLM through reinforcement learning.

- Update / evaluation target: Role policies / model weights.
- Interpretation boundary: Role co-training is closely related to MARSI; separately test whether the improvement operator becomes better.

<a id="workflow"></a>

## Workflow and team evolution (8)

### Inherit-MAS · 2026-10

**Inherit-MAS: Test-Time Evolution of Multi-Agent Systems through Workflow and Execution Inheritance**

[Paper](https://arxiv.org/abs/2610.02396) · [PDF](https://arxiv.org/pdf/2610.02396)

Refines workflows through validated edits and reuses stored execution results only when resolved requests and contexts match.

- Update / evaluation target: Workflow edits + execution-result reuse.
- Interpretation boundary: Execution caching and test-time workflow refinement do not establish cross-task improvement of the optimizer.

### MANTA · 2026-07

**MANTA: Multi-Agent Network Topology Adaptation for Self-Evolving Multi-Agent Systems**

[Paper](https://arxiv.org/abs/2607.28527) · [PDF](https://arxiv.org/pdf/2607.28527)

Initializes a topology from structural experience and applies bounded role, communication and validation updates during execution.

- Update / evaluation target: Communication topology + roles.
- Interpretation boundary: Inference-time structural adaptation is not automatically persistent recursive optimizer improvement.

### MAS-ZERO · 2025-05

**MAS-ZERO: Designing Multi-Agent Systems with Zero Supervision**

[Paper](https://arxiv.org/abs/2505.14996) · [PDF](https://arxiv.org/pdf/2505.14996)

Designs and revises multi-agent configurations at inference time using meta-feedback without a validation set.

- Update / evaluation target: Per-instance team design.
- Interpretation boundary: Instance-level adaptation does not by itself imply persistent cross-task inheritance.

### EvoFlow · 2025-02

**EvoFlow: Evolving Diverse Agentic Workflows On The Fly**

[Paper](https://arxiv.org/abs/2502.07373) · [PDF](https://arxiv.org/pdf/2502.07373)

Evolves diverse heterogeneous workflows through retrieval, crossover, mutation and niching selection.

- Update / evaluation target: Workflow population.
- Interpretation boundary: Workflow evolution is related to RSI but does not establish recursive optimizer improvement.

### MASS (2025) · 2025-02

**Multi-Agent Design: Optimizing Agents with Better Prompts and Topologies**

[Paper](https://arxiv.org/abs/2502.02533) · [PDF](https://arxiv.org/pdf/2502.02533)

Optimizes local prompts, workflow topology and global prompts in staged multi-agent system search.

- Update / evaluation target: Prompts + topology.
- Interpretation boundary: Multi-Agent System Search; a different paper from Multi-Agent Self-Supervision (2026).

### AFlow · 2024-10

**AFlow: Automating Agentic Workflow Generation**

[Paper](https://arxiv.org/abs/2410.10762) · [PDF](https://arxiv.org/pdf/2410.10762) · [Code](https://github.com/FoundationAgents/AFlow)

Searches code-represented workflows with Monte Carlo tree search and execution feedback.

- Update / evaluation target: Code-represented workflow.
- Interpretation boundary: A workflow-search baseline; do not equate better workflows with a stronger optimizer.

### ADAS · 2024-08

**Automated Design of Agentic Systems**

[Paper](https://arxiv.org/abs/2408.08435) · [PDF](https://arxiv.org/pdf/2408.08435)

A meta-agent programs new agent designs using an expanding archive of earlier discoveries.

- Update / evaluation target: Agent design + archive.
- Interpretation boundary: Automated agent design can use a fixed designer; distinguish it from designer self-improvement.

### DSPy · 2023-10

**DSPy: Compiling Declarative Language Model Calls into Self-Improving Pipelines**

[Paper](https://arxiv.org/abs/2310.03714) · [PDF](https://arxiv.org/pdf/2310.03714) · [Code](https://github.com/stanfordnlp/dspy)

Compiles declarative language-model programs against a task metric to optimize pipeline behavior.

- Update / evaluation target: Prompts / demonstrations / pipeline parameters.
- Interpretation boundary: General optimization infrastructure, not evidence of multi-agent recursive improvement.

<a id="experience"></a>

## Experience, memory and skill inheritance (5)

### EvolveMAS · 2026-10

**EvolveMAS: A Unified Self-Evolution Framework for Decentralized Multi-Agent Systems**

[Paper](https://arxiv.org/abs/2610.34450) · [PDF](https://arxiv.org/pdf/2610.34450)

Pairs agents with MemoryAgents and combines within-episode memory updates with cross-episode distillation of partner profiles and interaction strategies.

- Update / evaluation target: Per-agent memory governance + interaction knowledge.
- Interpretation boundary: Parameter-free experience evolution does not by itself isolate improvement of the memory-update or optimization procedure.

### Skill-MAS · 2026-06

**Skill-MAS: Evolving Meta-Skill for Automatic Multi-Agent Systems**

[Paper](https://arxiv.org/abs/2606.18837) · [PDF](https://arxiv.org/pdf/2606.18837)

Distills experience from multiple trajectories into a reusable orchestration meta-skill through selective reflection.

- Update / evaluation target: Orchestration meta-skill.
- Interpretation boundary: Persistent orchestration knowledge does not alone demonstrate an improving optimizer.

### DecentMem · 2026-05

**Self-Evolving Multi-Agent Systems via Decentralized Memory**

[Paper](https://arxiv.org/abs/2605.22721) · [PDF](https://arxiv.org/pdf/2605.22721)

Gives each agent exploitation and exploration memory pools, reweighted using staged judge feedback.

- Update / evaluation target: Decentralized agent memories.
- Interpretation boundary: Memory adaptation does not alone demonstrate that the improvement procedure itself improves.

### Voyager · 2023-05

**Voyager: An Open-Ended Embodied Agent with Large Language Models**

[Paper](https://arxiv.org/abs/2305.16291) · [PDF](https://arxiv.org/pdf/2305.16291)

Builds and retrieves an expanding library of executable skills with curriculum and environment feedback.

- Update / evaluation target: Executable skill library.
- Interpretation boundary: An embodied single-agent inheritance reference, not a MARSI system.

### Reflexion · 2023-03

**Reflexion: Language Agents with Verbal Reinforcement Learning**

[Paper](https://arxiv.org/abs/2303.11366) · [PDF](https://arxiv.org/pdf/2303.11366)

Stores verbal reflections on feedback to improve decisions in subsequent trials without weight updates.

- Update / evaluation target: Episodic reflection memory.
- Interpretation boundary: Trial-level reflection is not sufficient evidence of optimizer-level recursion.

<a id="selfmod"></a>

## Self-modification and model adaptation (9)

### Skill∞ · 2026-10

**Skill∞: Recursive Self-Improvement for Agent Skill Optimization**

[Paper](https://arxiv.org/abs/2610.35434) · [PDF](https://arxiv.org/pdf/2610.35434)

Uses a meta-skill to optimize task skills and applies the same procedure to that meta-skill, including diagnosis, review and budget allocation.

- Update / evaluation target: Task skills + optimizer meta-skill.
- Interpretation boundary: Directly targets the improvement procedure; broad sustained gains and the contribution of multi-agent collaboration require separate evaluation.

### Recursia · 2026-10

**Learning to Compose: Recursive Self-Improvement of Shared Executable Stacks for Zero-Shot Long-Horizon Robot Manipulation**

[Paper](https://arxiv.org/abs/2610.24464) · [PDF](https://arxiv.org/pdf/2610.24464)

Improves a persistent executable stack using failure attribution, component repair and selection/regression gates, then freezes it for transfer.

- Update / evaluation target: Shared tools, skill contracts and verifiers.
- Interpretation boundary: A robot-programming transfer reference; shared components are not themselves a collaborating multi-agent system.

### AIDE² · 2026-09

**Recursive self-improvement of AI research agents**

[Paper](https://arxiv.org/abs/2609.26457) · [PDF](https://arxiv.org/pdf/2609.26457)

Rewrites and evaluates its own research-agent code, with accepted versions becoming the subject of later improvement.

- Update / evaluation target: Research-agent code.
- Interpretation boundary: A self-modification reference; not inherently a multi-agent collaboration method.

### HELIX · 2026-08

**HELIX: Model-Harness Co-evolution for Recursive Self-Improvement**

[Paper](https://arxiv.org/abs/2608.13951) · [PDF](https://arxiv.org/pdf/2608.13951) · [Code](https://github.com/HKUDS/HELIX)

Tracks harness interventions and sibling trajectories to connect harness evolution with future model training.

- Update / evaluation target: Harness components + training records.
- Interpretation boundary: The abstract evaluates one evolution round; sustained co-evolution remains a stronger claim.

### HarnessForge · 2026-06

**HarnessForge: Joint Harness and Policy Evolution for Adaptive Agent Systems**

[Paper](https://arxiv.org/abs/2606.01779) · [PDF](https://arxiv.org/pdf/2606.01779) · [Code](https://github.com/mingju-c/HarnessForge)

Co-evolves execution structure and reasoning policy through fault-guided harness tailoring and harness-conditioned policy alignment.

- Update / evaluation target: Harness + reasoning policy.
- Interpretation boundary: Joint system adaptation is relevant to RSI; sustained optimizer improvement requires separate evidence.

### SEAL · 2025-06

**Self-Adapting Language Models**

[Paper](https://arxiv.org/abs/2506.10943) · [PDF](https://arxiv.org/pdf/2506.10943)

Learns to generate adaptation data and update directives using downstream post-update performance as feedback.

- Update / evaluation target: Self-edit policy + weights.
- Interpretation boundary: Self-adaptation mechanism, not a multi-agent RSI system by itself.

### Darwin Gödel Machine · 2025-05

**Darwin Godel Machine: Open-Ended Evolution of Self-Improving Agents**

[Paper](https://arxiv.org/abs/2505.22954) · [PDF](https://arxiv.org/pdf/2505.22954) · [Code](https://github.com/jennyzzt/dgm)

Combines self-modifying coding agents with an archive and open-ended evolutionary exploration.

- Update / evaluation target: Agent code + archive.
- Interpretation boundary: A population/archive is not automatically a collaborating multi-agent team within a task.

### SICA · 2025-04

**A Self-Improving Coding Agent**

[Paper](https://arxiv.org/abs/2504.15228) · [PDF](https://arxiv.org/pdf/2504.15228)

Lets a coding agent edit its own implementation and evaluates the resulting agents on coding tasks.

- Update / evaluation target: Agent implementation.
- Interpretation boundary: Useful code-level self-improvement baseline; multi-agent coordination is not the central mechanism.

### Gödel Agent · 2024-10

**Gödel Agent: A Self-Referential Agent Framework for Recursive Self-Improvement**

[Paper](https://arxiv.org/abs/2410.04444) · [PDF](https://arxiv.org/pdf/2410.04444) · [Code](https://github.com/Arvid-pku/Godel_Agent)

Lets an agent dynamically change its own logic and behavior under high-level objectives.

- Update / evaluation target: Agent logic / behavior.
- Interpretation boundary: Runtime self-modification and stable cross-task recursive gains should be assessed separately.

<a id="foundations"></a>

## Collaboration and reflection foundations (5)

### Mixture-of-Agents · 2024-06

**Mixture-of-Agents Enhances Large Language Model Capabilities**

[Paper](https://arxiv.org/abs/2406.04692) · [PDF](https://arxiv.org/pdf/2406.04692)

Aggregates outputs across layers of multiple language-model agents.

- Update / evaluation target: Layered response aggregation.
- Interpretation boundary: Collaboration at inference time does not imply self-evolution.

### AutoGen · 2023-08

**AutoGen: Enabling Next-Gen LLM Applications via Multi-Agent Conversation**

[Paper](https://arxiv.org/abs/2308.08155) · [PDF](https://arxiv.org/pdf/2308.08155)

Provides configurable agent conversations and tool/human interaction for multi-agent applications.

- Update / evaluation target: Conversation orchestration.
- Interpretation boundary: Framework infrastructure; no recursive learning mechanism is implied by its use.

### MetaGPT · 2023-08

**MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework**

[Paper](https://arxiv.org/abs/2308.00352) · [PDF](https://arxiv.org/pdf/2308.00352) · [Code](https://github.com/FoundationAgents/MetaGPT)

Structures collaboration through role specialization and standard operating procedures.

- Update / evaluation target: Role / SOP orchestration.
- Interpretation boundary: A structured collaboration baseline, not itself an RSI algorithm.

### Multiagent Debate · 2023-05

**Improving Factuality and Reasoning in Language Models through Multiagent Debate**

[Paper](https://arxiv.org/abs/2305.14325) · [PDF](https://arxiv.org/pdf/2305.14325)

Uses multiple model instances to exchange and revise reasoning over rounds of debate.

- Update / evaluation target: Current answer / reasoning.
- Interpretation boundary: Debate rounds concern an answer, not necessarily inheritable system changes.

### Self-Refine · 2023-03

**Self-Refine: Iterative Refinement with Self-Feedback**

[Paper](https://arxiv.org/abs/2303.17651) · [PDF](https://arxiv.org/pdf/2303.17651)

Iteratively generates feedback and revises an output using the same language model.

- Update / evaluation target: Current output.
- Interpretation boundary: Output refinement; no persistent system update is implied.

<a id="evaluation"></a>

## Benchmarks and evaluation (9)

### RSI-Forge · 2026-10

**RSI-Forge: From Research Papers to Environments for Recursive Self-Improvement**

[Paper](https://arxiv.org/abs/2610.09426) · [PDF](https://arxiv.org/pdf/2610.09426)

Uses construction, reproduction and review agents to turn papers into executable research tasks and evaluates repeated attempts with inherited code and notes.

- Update / evaluation target: Research environments + evaluators.
- Interpretation boundary: An environment-construction and evaluation resource; repeated solution gains with frozen weights do not alone establish optimizer recursion.

### RSIBench-Data · 2026-07

**RSIBench-Data: Benchmarking Data-Centric Research for Recursive Self-Improvement**

[Paper](https://arxiv.org/abs/2607.25886) · [PDF](https://arxiv.org/pdf/2607.25886) · [Code](https://github.com/evolvent-ai/RSIBench-Data)

Benchmarks diagnosis, training-data strategy revision and checkpoint-feedback use with a controlled post-training stack.

- Update / evaluation target: Training-data research loop.
- Interpretation boundary: Repeated feedback can guide development; reserve separate final evaluation to assess generalization.

### SEA-Eval · 2026-04

**SEA-Eval: A Benchmark for Evaluating Self-Evolving Agents Beyond Episodic Assessment**

[Paper](https://arxiv.org/abs/2604.08988) · [PDF](https://arxiv.org/pdf/2604.08988)

Evaluates self-evolving agents on task streams, tracking success, token use and evolution over time.

- Update / evaluation target: Sequential cross-task evolution.
- Interpretation boundary: Sequential gains do not alone isolate improvement of the optimizer.

### Terminal-Bench 2.0 · 2026-01

**Terminal-Bench: Benchmarking Agents on Hard, Realistic Tasks in Command Line Interfaces**

[Paper](https://arxiv.org/abs/2601.11868) · [PDF](https://arxiv.org/pdf/2601.11868)

Tests agents in realistic terminal environments with task-specific verification.

- Update / evaluation target: Long-horizon terminal execution.
- Interpretation boundary: Task-performance anchor; not a dedicated multi-agent RSI benchmark.

### MLR-Bench · 2025-05

**MLR-Bench: Evaluating AI Agents on Open-Ended Machine Learning Research**

[Paper](https://arxiv.org/abs/2505.19955) · [PDF](https://arxiv.org/pdf/2505.19955)

Evaluates research stages and end-to-end ML research with a rubric-based review framework.

- Update / evaluation target: Open-ended ML research.
- Interpretation boundary: Audit execution evidence and judge reliability; generated reports alone are insufficient.

### ScienceAgentBench · 2024-10

**ScienceAgentBench: Toward Rigorous Assessment of Language Agents for Data-Driven Scientific Discovery**

[Paper](https://arxiv.org/abs/2410.05080) · [PDF](https://arxiv.org/pdf/2410.05080)

Uses publication-grounded scientific tasks with executable Python deliverables and cost-aware evaluation.

- Update / evaluation target: Scientific data / code tasks.
- Interpretation boundary: Check the exact dataset version and artifacts when comparing published results.

### DSBench · 2024-09

**DSBench: How Far Are Data Science Agents from Becoming Data Science Experts?**

[Paper](https://arxiv.org/abs/2409.07703) · [PDF](https://arxiv.org/pdf/2409.07703)

Covers realistic data-analysis and modeling tasks with large files and multimodal context.

- Update / evaluation target: Data analysis + modeling.
- Interpretation boundary: Report analysis and modeling separately; they have different task and metric structures.

### SWE-bench · 2023-10

**SWE-bench: Can Language Models Resolve Real-World GitHub Issues?**

[Paper](https://arxiv.org/abs/2310.06770) · [PDF](https://arxiv.org/pdf/2310.06770)

Evaluates code changes for real repository issues using executable tests.

- Update / evaluation target: Repository issue resolution.
- Interpretation boundary: Distinguish original, Lite, Verified and other variants; this entry cites the original paper.

### AgentBench · 2023-08

**AgentBench: Evaluating LLMs as Agents**

[Paper](https://arxiv.org/abs/2308.03688) · [PDF](https://arxiv.org/pdf/2308.03688) · [Code](https://github.com/THUDM/AgentBench)

Evaluates reasoning and decision-making across diverse interactive environments.

- Update / evaluation target: Interactive agent environments.
- Interpretation boundary: An agent-evaluation foundation rather than a dedicated recursive-improvement protocol.

## Verification and reuse

Dates are arXiv first-submission dates, not inferred conference dates. Titles, authors, dates and abstracts were checked on primary arXiv pages. Code links are included only when linked by the paper page and verified through the GitHub API. An absent code link means unconfirmed in this pass, not necessarily unavailable. Experiments were not reproduced and scores are not compared across incompatible settings.

[Curation method / 收录方法](docs/curation.md). Original annotations and metadata are released under [CC0-1.0](LICENSE). Linked papers, code and datasets retain their own licenses.
