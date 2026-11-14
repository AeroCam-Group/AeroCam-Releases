#!/usr/bin/env python3
"""Copies the current Beta test key from beta-key.txt into every translated README (readme/README.*.md).

beta-key.txt: line 1 = the key, a later "# ... YYYY-MM-DD ..." line = valid until (inclusive).
Each translated README holds a block between <!-- BETA-KEY --> and <!-- /BETA-KEY -->; only that
block is rewritten (one line in the file's language + the key in a code block, which GitHub shows
with a copy button). README.md (Traditional Chinese) is left to the key tool that writes it.

  python3 scripts/sync_beta_key.py          # rewrite the blocks; prints what changed
  python3 scripts/sync_beta_key.py --check  # exit 1 if any block is out of date
"""
import pathlib, re, sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINE = {
    "en": "**The current test key** (valid until **{d}**, inclusive):",
    "ja": "**現在のテストキー**（**{d}** まで有効、当日を含む）：",
    "zh-CN": "**当前的测试密钥**（有效期至 **{d}**，含当天）：",
    "ko": "**현재 테스트 키** (**{d}**까지 유효, 당일 포함):",
    "de": "**Der aktuelle Testschlüssel** (gültig bis einschließlich **{d}**):",
    "fr": "**La clé de test actuelle** (valable jusqu'au **{d}** inclus) :",
    "es": "**La clave de prueba actual** (válida hasta el **{d}**, incluido):",
    "vi": "**Khóa thử nghiệm hiện tại** (có hiệu lực đến hết ngày **{d}**):",
    "th": "**คีย์ทดสอบปัจจุบัน** (ใช้ได้ถึง **{d}** รวมวันนั้นด้วย):",
    "id": "**Kunci uji saat ini** (berlaku sampai **{d}**, termasuk hari itu):",
}
BLOCK = re.compile(r"<!-- BETA-KEY -->.*?<!-- /BETA-KEY -->", re.S)


def read_key():
    lines = [l.strip() for l in (ROOT / "beta-key.txt").read_text(encoding="utf-8").splitlines() if l.strip()]
    key = next(l for l in lines if not l.startswith("#"))
    if not re.fullmatch(r"AZB1-[A-Za-z0-9_\-]+\.[A-Za-z0-9_\-]+", key):
        sys.exit(f"beta-key.txt: line 1 doesn't look like a test key: {key[:12]}…")
    date = next((m.group(0) for l in lines if l.startswith("#") for m in [re.search(r"\d{4}-\d{2}-\d{2}", l)] if m), None)
    if not date:
        sys.exit("beta-key.txt: no valid-until date (YYYY-MM-DD) found")
    return key, date


def main():
    check = "--check" in sys.argv
    key, date = read_key()
    stale = []
    for code, line in LINE.items():
        p = ROOT / "readme" / f"README.{code}.md"
        text = p.read_text(encoding="utf-8")
        if not BLOCK.search(text):
            sys.exit(f"{p.name}: no <!-- BETA-KEY --> block")
        block = f"<!-- BETA-KEY -->\n{line.format(d=date)}\n\n```\n{key}\n```\n<!-- /BETA-KEY -->"
        new = BLOCK.sub(lambda _: block, text, count=1)
        if new != text:
            stale.append(p.name)
            if not check:
                p.write_text(new, encoding="utf-8")
    print(("out of date: " if check else "updated: ") + (", ".join(stale) if stale else "none") + f" (key valid until {date})")
    if check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()
