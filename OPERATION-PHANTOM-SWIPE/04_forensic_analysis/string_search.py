from pathlib import Path
import re
ROOT=Path("03_evidence_acquisition/acquired_media")
TERMS=("DATA CAPTURE","TRANSFER","TXN-","LOGIN","Meet near","test terminal")
CARD=re.compile(r"(?<!\\d)(?:\\d[ -]?){13,19}(?!\\d)")
def main():
    count=0
    for p in ROOT.rglob("*"):
        if p.is_file() and p.suffix.lower() in {".txt",".csv",".eml",".json"}:
            text=p.read_text(encoding="utf-8",errors="ignore")
            for n,line in enumerate(text.splitlines(),1):
                if any(t.lower() in line.lower() for t in TERMS) or CARD.search(line):
                    print(f"{p}:{n}: {line}"); count+=1
    print("Matching lines:",count)
if __name__=="__main__": main()
