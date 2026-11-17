"""从 multica 导出 skill 到本仓库。用法: python3 scripts/export.py
布局由 ROLES 决定：被多个角色引用的放 shared/，只有一个角色用的放 roles/<角色>/。"""
import json, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
# skill 名 -> 放置目录（相对仓库根）
PLACE = {
    "design-html": "shared/design-html",
    "skill-library": "shared/skill-library",
    "pm-library": "roles/project-manager/pm-library",
}

def mc(*a):
    return json.loads(subprocess.check_output(["multica", *a], text=True))

skills = {s["name"]: s["id"] for s in mc("skill", "list", "--output", "json")}
for name, dest in PLACE.items():
    d = mc("skill", "get", skills[name], "--with-content")
    out = ROOT / dest
    out.mkdir(parents=True, exist_ok=True)
    fm = f"---\nname: {d['name']}\ndescription: {json.dumps(d['description'], ensure_ascii=False)}\n---\n\n"
    (out / "SKILL.md").write_text(fm + d["content"], encoding="utf-8")
    for f in d["files"]:
        p = out / f["path"]
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(f["content"], encoding="utf-8")
    print(dest, len(d["files"]) + 1, "files")
