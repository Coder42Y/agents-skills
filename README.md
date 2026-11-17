# agents-skills

Agents team 在 multica 里引用的全部 skill，按角色存放。

## 布局

- `shared/`：被 2 个及以上角色引用的 skill，只存一份
- `roles/<角色>/`：只有该角色用的 skill
- `roles/<角色>/SKILLS.md`：该角色引用了哪些 skill（共享的用链接指过去）

## 谁用什么

| skill | 位置 | 引用角色 |
|---|---|---|
| design-html | shared | mika, project-manager |
| skill-library | shared | mika, architect, builder, reviewer, e2e-tester, frontend-engineer |
| pm-library | roles/project-manager | project-manager |

## 同步

multica 是源头，本仓库是快照：

```bash
python3 scripts/export.py
```
