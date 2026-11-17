# agents-skills

Agents team 在 [multica](https://multica.ai) 里用到的全部 skill，按角色存放。

一个 skill 只存一份。多个角色都用的放 `shared/`，只有一个角色用的放自己的目录。

## 目录

```
agents-skills/
├── shared/                     被 2 个及以上角色引用的 skill
│   ├── design-html/
│   └── skill-library/
├── roles/
│   ├── mika/SKILLS.md
│   ├── architect/SKILLS.md
│   ├── builder/SKILLS.md
│   ├── reviewer/SKILLS.md
│   ├── e2e-tester/SKILLS.md
│   ├── frontend-engineer/SKILLS.md
│   └── project-manager/
│       ├── SKILLS.md
│       └── pm-library/         只有 PM 用的 skill
└── scripts/export.py           从 multica 导出
```

每个角色目录下的 `SKILLS.md` 列出该角色引用的 skill。共享的 skill 用链接指向 `shared/`，不复制。

## 谁用什么

| skill | 位置 | 引用角色 |
|---|---|---|
| `design-html` | `shared/` | mika、project-manager |
| `skill-library` | `shared/` | mika、architect、builder、reviewer、e2e-tester、frontend-engineer |
| `pm-library` | `roles/project-manager/` | project-manager |

## 每个 skill 是什么

- **design-html**：把一个想法或方案整理成可分享的设计说明 HTML。暖白底、无渐变、多图少字、手机可读。带样式、构建脚本和图表示例。
- **skill-library**：共享技能库入口。先读索引，再按需读具体 skill，没有合适的就不用。
- **pm-library**：项目经理专用技能库入口，覆盖需求、PRD、用户故事、调研、策略、GTM、数据分析。

`skill-library` 和 `pm-library` 是入口，不含具体 skill。它们里面的索引路径指向本机（`skill-index/INDEX*.md` 和 `~/.claude/skills`），换机器使用需要改路径。

## 同步

multica 是源头，本仓库是快照。multica 里改了 skill 之后：

```bash
python3 scripts/export.py
git add -A && git commit -m "sync skills" && git push
```

需要已安装并登录 `multica` CLI。

## 新增或调整角色引用

1. 在 multica 里创建或修改 skill，并分配给对应 agent
2. 在 `scripts/export.py` 的 `PLACE` 里加一行：被多个角色用放 `shared/<名>`，只有一个角色用放 `roles/<角色>/<名>`
3. 更新对应角色的 `SKILLS.md` 和上面的表格
4. 运行 `python3 scripts/export.py`
