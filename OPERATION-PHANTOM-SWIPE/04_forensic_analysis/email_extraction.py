from pathlib import Path
from email import policy
from email.parser import BytesParser
OUT=Path("04_forensic_analysis/extracted_artifacts")
def main():
    OUT.mkdir(parents=True,exist_ok=True); lines=[]
    for p in Path("03_evidence_acquisition/acquired_media").rglob("*.eml"):
        msg=BytesParser(policy=policy.default).parsebytes(p.read_bytes())
        lines += [f"Source: {p}", "Evidence ID: EV-002",f"From: {msg.get('From','')}",
                  f"To: {msg.get('To','')}",f"Date: {msg.get('Date','')}",
                  f"Subject: {msg.get('Subject','')}",""]
    (OUT/"extracted_emails.txt").write_text("\\n".join(lines),encoding="utf-8")
    print("\\n".join(lines) if lines else "No EML files found.")
if __name__=="__main__": main()
