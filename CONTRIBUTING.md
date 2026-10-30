# Contributing

Paper suggestions and corrections are welcome through issues or pull requests.

1. Provide a primary paper URL and explain its relevance to multi-agent recursive self-improvement.
2. Add a unique entry to `data/papers.json`; verify title, authors and first-submission date.
3. Add short original English and Chinese summaries, an update/evaluation target and an explicit interpretation boundary.
4. Add code links only when the paper or authors identify them and the repository is reachable. Otherwise use `null`.
5. Set the actual verification date; do not infer publication venues or reproduced results.
6. Run `python3 scripts/build.py` and `python3 scripts/build.py --check`, and commit the generated README files and BibTeX.

请明确区分单次答案改进、团队设计优化、经验继承和改进器更新。欢迎纠正题名、链接、分类及证据边界。

Contributions of original annotations and metadata are made under CC0-1.0. Do not add copyrighted paper PDFs or private research materials.
