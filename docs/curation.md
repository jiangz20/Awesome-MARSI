# Curation method / 收录方法

Snapshot: 2026-10-30. Initial collection: 32 papers, 2023–2026.

## Scope

Include papers addressing multi-agent self-improvement, automated team/workflow design, persistent skills or memory, self-modification, model/harness co-evolution, and evaluation relevant to these mechanisms. Include a small set of collaboration and reflection foundations as explicitly labeled context.

## Verification

- Started from a seed bibliography and related foundational work, then fetched all 32 canonical arXiv abstract pages.
- Checked paper title, author list, first-submission date, abstract, and paper/PDF URLs against those pages. Normalized Gödel typography where arXiv metadata exposed TeX escaping.
- Read abstracts to write original brief annotations. Interpretation boundaries are editorial analysis, not quotations or formal certifications.
- Added 9 code links explicitly exposed by the corresponding paper pages and confirmed their repositories through the GitHub API. Followed the MetaGPT repository redirect to FoundationAgents/MetaGPT.
- Recorded `verified_on` and verification scope in each JSON record. BibTeX cites the arXiv version and does not invent venue information.
- Did not reproduce experiments, install projects, verify every full-text claim, or validate dataset execution environments.

The general web-search service was unavailable during this pass, and the arXiv search endpoint also failed. Six additional candidate pages could not be retrieved and were not included. The collection therefore makes no claim to exhaustive coverage or to having captured every paper published before the snapshot date. Known-seed primary-source verification was successful for every included record.

## Maintaining the collection

`data/papers.json` is the source of truth for entries. Update it, run `python3 scripts/build.py`, then `python3 scripts/build.py --check`. Keep English and Chinese annotations concise and distinguish the demonstrated update mechanism from stronger recursive-improvement interpretations. Do not copy full abstracts into the collection.

分类以方法机制为主，不以论文标题中是否出现 “self-improving” 为唯一依据。新增条目应给出一手来源和相关性说明；缺少代码链接不代表代码不存在。所有条目均可随新版本和更充分证据修订。
