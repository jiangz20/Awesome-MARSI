"""Generate the reading lists and BibTeX from curated metadata (standard library only)."""
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    ('core', 'Direct multi-agent self-improvement', '直接相关：多智能体自我改进'),
    ('workflow', 'Workflow and team evolution', '工作流与团队结构演化'),
    ('experience', 'Experience, memory and skill inheritance', '经验、记忆与技能继承'),
    ('selfmod', 'Self-modification and model adaptation', '自身代码修改与模型适应'),
    ('foundations', 'Collaboration and reflection foundations', '协作与反思基础'),
    ('evaluation', 'Benchmarks and evaluation', '基准与评测'),
]

def render(papers, zh=False):
    lines = ['# Awesome-MARSI', '', '**Multi-Agent Recursive Self-Improvement**', '',
             '[English](README.md) | [简体中文](README.zh-CN.md)', '']
    if zh:
        lines += [f'多智能体递归自我改进相关论文与资源精选。目前收录 **{len(papers)} 篇**，最近核验日期为 **2026-10-30**。', '',
                  '围绕协作架构演化、经验积累与迁移、改进机制递归演化三条主线，同时收录必要的单智能体方法与评测基线。MARSI 在此是组织文献的主题名称，不表示所有条目均提出了完整的多智能体 RSI 系统。', '',
                  '**范围与证据：**单次答案反思、测试时团队搜索、跨任务技能继承、权重更新和改进器更新属于不同机制。各条目的边界说明用于防止混淆；论文的自述不等于独立复现。此列表是精选起点，不是穷尽性系统综述。', '',
                  '## 导航', '']
    else:
        lines += [f'A curated collection of papers and resources on multi-agent recursive self-improvement. **{len(papers)} papers**, last verified **2026-10-30**.', '',
                  'The collection follows three themes: evolving collaboration architectures, accumulating transferable experience, and improving the improvement process itself. It also includes relevant single-agent methods and evaluation baselines. MARSI is an organizing topic here, not a claim that every entry implements full multi-agent RSI.', '',
                  '**Scope and evidence:** output refinement, inference-time team search, persistent skill inheritance, weight updates, and optimizer updates are different mechanisms. Each entry states an interpretation boundary. Author-reported findings are not independent reproductions. This is a curated starting point, not an exhaustive systematic review.', '',
                  '## Contents', '']
    for key,en,cn in CATEGORIES: lines.append(f'- [{cn if zh else en}](#{key})')
    lines += ['', '[Reading guide / 阅读指南](docs/reading-guide.md) · [BibTeX](papers.bib) · [Structured metadata / 结构化数据](data/papers.json) · [Contributing](CONTRIBUTING.md)', '',
              '## 建议先读' if zh else '## Start here', '',
              'MASS (2026) → Gödel Forest → RHI → Multi-Agent Evolve → Skill-MAS → Darwin Gödel Machine → RSIBench-Data.', '',
              '**缩写提醒：**MASS (2025) 是 Multi-Agent System Search；MASS (2026) 是 Multi-Agent Self-Supervision。它们是两篇不同论文。' if zh else '**Acronym collision:** MASS (2025) means Multi-Agent System Search; MASS (2026) means Multi-Agent Self-Supervision. These are different papers.', '']
    for key,en,cn in CATEGORIES:
        subset=sorted([p for p in papers if p['category']==key],key=lambda p:p['first_submitted'],reverse=True)
        lines += [f'<a id="{key}"></a>', '', f'## {cn if zh else en} ({len(subset)})', '']
        for p in subset:
            links=f"[Paper]({p['paper_url']}) · [PDF]({p['pdf_url']})"
            if p['code_url']: links+=f" · [Code]({p['code_url']})"
            lines += [f"### {p['short_name']} · {p['first_submitted'][:7]}", '',
                      f"**{p['title']}**", '', links, '',
                      p['summary_zh' if zh else 'summary_en'], '',
                      f"- {'更新对象 / 评测对象' if zh else 'Update / evaluation target'}: {p['update_target']}.",
                      f"- {'证据边界' if zh else 'Interpretation boundary'}: {p['evidence_boundary_zh' if zh else 'evidence_boundary']}", '']
    lines += ['## 核验与使用说明' if zh else '## Verification and reuse', '',
              '日期采用 arXiv 首次提交日期，不推定会议录用状态。逐条核验题名、作者、日期和摘要；代码链接仅在论文页面明确链接且 GitHub API 核验成功时收录。缺少代码链接表示本轮未确认，不代表没有开源实现。未复现实验；不跨设置比较分数。' if zh else 'Dates are arXiv first-submission dates, not inferred conference dates. Titles, authors, dates and abstracts were checked on primary arXiv pages. Code links are included only when linked by the paper page and verified through the GitHub API. An absent code link means unconfirmed in this pass, not necessarily unavailable. Experiments were not reproduced and scores are not compared across incompatible settings.', '',
              '[Curation method / 收录方法](docs/curation.md). Original annotations and metadata are released under [CC0-1.0](LICENSE). Linked papers, code and datasets retain their own licenses.', '']
    return '\n'.join(lines)

def bib_escape(s):
    for a,b in [ ('\\', r'\textbackslash{}'), ('&',r'\&'), ('%',r'\%'), ('_',r'\_'), ('#',r'\#') ]:
        s=s.replace(a,b)
    return s

def artifacts():
    papers=json.loads((ROOT/'data/papers.json').read_text())
    ids=[p['id'] for p in papers]
    assert len(ids)==len(set(ids)), 'Duplicate paper IDs'
    assert all(p['category'] in {c[0] for c in CATEGORIES} for p in papers)
    assert all(p['paper_url']=='https://arxiv.org/abs/'+p['id'] for p in papers)
    bib=[]
    for p in papers:
        bib += [f"@misc{{arxiv{p['id'].replace('.', '')},",f"  title = {{{{{bib_escape(p['title'])}}}}},",f"  author = {{{' and '.join(bib_escape(a) for a in p['authors'])}}},",f"  year = {{{p['first_submitted'][:4]}}},",f"  eprint = {{{p['id']}}},",'  archivePrefix = {arXiv},',f"  url = {{{p['paper_url']}}}",'}','']
    return {'README.md':render(papers),'README.zh-CN.md':render(papers,True),'papers.bib':'\n'.join(bib)}

if __name__=='__main__':
    import sys
    outputs=artifacts()
    if '--check' in sys.argv:
        for name,content in outputs.items():
            assert (ROOT/name).read_text()==content, f'Stale generated file: {name}'
        print('OK: metadata IDs/categories/URLs and generated README/BibTeX files are consistent.')
    else:
        for name,content in outputs.items(): (ROOT/name).write_text(content)
        print('Generated '+', '.join(outputs))
