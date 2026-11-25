from pathlib import Path
import hashlib
folder=Path("03_evidence_acquisition/acquired_media")
out=Path("06_reports/evidence_hashes.txt")
def digest(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for block in iter(lambda:f.read(4096),b""): h.update(block)
    return h.hexdigest()
def main():
    out.parent.mkdir(exist_ok=True)
    files=sorted(p for p in folder.rglob("*") if p.is_file())
    if not files: raise SystemExit("No acquired files. Run acquisition.py first.")
    with out.open("w",encoding="utf-8") as report:
        for p in files:
            value=digest(p); report.write(f"{p.as_posix()} : {value}\\n"); print(p.name,value)
    print(f"SHA-256 generated for {len(files)} files.")
if __name__=="__main__": main()
