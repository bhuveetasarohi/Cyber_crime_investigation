"""Copy generated evidence into an acquired-media working directory."""
from pathlib import Path
import shutil, csv, hashlib, datetime
SRC=Path("02_simulated_evidence")
DEST=Path("03_evidence_acquisition/acquired_media")
def sha(p):
    h=hashlib.sha256()
    with p.open("rb") as f:
        for b in iter(lambda:f.read(65536), b""): h.update(b)
    return h.hexdigest()
def main():
    if not SRC.exists(): raise SystemExit("Run py generate_evidence.py first.")
    DEST.mkdir(parents=True, exist_ok=True)
    rows=[]
    for device in ("device_01_skimmer","device_02_suspect_phone"):
        source=SRC/device; target=DEST/device
        if not source.exists(): raise SystemExit(f"Missing {source}")
        shutil.copytree(source,target,dirs_exist_ok=True)
        for p in sorted(target.rglob("*")):
            if p.is_file():
                original=source/p.relative_to(target)
                rows.append(["OPS-2026-001","EV-001" if "skimmer" in device else "EV-002",
                    str(original),str(p),sha(original),sha(p),"MATCH" if sha(original)==sha(p) else "MISMATCH"])
    log=Path("03_evidence_acquisition/acquisition_log.txt")
    log.write_text("SIMULATED FILE-COPY ACQUISITION\nTimestamp: "+datetime.datetime.now(datetime.timezone.utc).isoformat()+
                   "\nNo physical device, write blocker or bit-stream imaging was used.\n",encoding="utf-8")
    coc=Path("03_evidence_acquisition/chain_of_custody.csv")
    new=not coc.exists()
    with coc.open("a",newline="",encoding="utf-8") as f:
        w=csv.writer(f)
        if new: w.writerow(["Case ID","Evidence ID","Description","Collected by","Date/time UTC","Location","Condition","SHA-256","Transferred to","Purpose","Signature/record"])
        for row in rows:
            w.writerow([row[0],row[1],Path(row[2]).name,"Investigator 01",datetime.datetime.now(datetime.timezone.utc).isoformat(),
                        "Fictional lab","Simulated file copy",row[4],"Forensic Analyst","Digital examination", "SIMULATED"])
    print(f"Acquired {len(rows)} files; see {DEST} and chain_of_custody.csv")
if __name__=="__main__": main()
