from pathlib import Path
import hashlib
SRC=Path("02_simulated_evidence"); DST=Path("03_evidence_acquisition/acquired_media")
def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(65536),b""): h.update(b)
    return h.hexdigest()
def main():
    checked=0; failed=[]
    for copy in sorted(p for p in DST.rglob("*") if p.is_file()):
        original=SRC/copy.relative_to(DST)
        checked+=1
        if not original.exists() or digest(original)!=digest(copy): failed.append(str(copy))
    print(f"Checked {checked} files; mismatches: {len(failed)}")
    for item in failed: print("MISMATCH:",item)
    Path("03_evidence_acquisition/verification_results.txt").write_text(
        f"Checked: {checked}\\nMismatches: {len(failed)}\\n" + "".join(x+"\\n" for x in failed),encoding="utf-8")
    if failed: raise SystemExit(1)
if __name__=="__main__": main()
