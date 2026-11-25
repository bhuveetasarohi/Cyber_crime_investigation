from pathlib import Path
import csv,json,re
ROOT=Path("03_evidence_acquisition/acquired_media"); OUT=Path("04_forensic_analysis/extracted_artifacts")
def main():
    OUT.mkdir(parents=True,exist_ok=True); cards=[]; messages=[]; locations=[]; findings=[]
    sk=ROOT/"device_01_skimmer"
    with (sk/"card_records.csv").open(encoding="utf-8",newline="") as f:
        for r in csv.DictReader(f):
            cards.append({"evidence_id":"EV-001","source_file":str(sk/"card_records.csv"),**r})
    ph=ROOT/"device_02_suspect_phone"
    for line in (ph/"messages.txt").read_text(encoding="utf-8").splitlines():
        if line.strip(): messages.append({"evidence_id":"EV-002","source_file":str(ph/"messages.txt"),"message":line})
    with (ph/"gps_locations.csv").open(encoding="utf-8",newline="") as f:
        for r in csv.DictReader(f): locations.append({"evidence_id":"EV-002","source_file":str(ph/"gps_locations.csv"),**r})
    txn=re.search(r"TXN-[A-Z]+-\\d+",(sk/"transaction_logs.txt").read_text(encoding="utf-8"))
    login=re.search(r"LOGIN: ([^\\n]+)",(ph/"fraudulent_app_logs.txt").read_text(encoding="utf-8"))
    email=ph/"emails"/"suspect_email.eml"
    findings=[
      {"type":"test_card_record","count":len(cards),"source_file":str(sk/"card_records.csv"),"evidence_id":"EV-001"},
      {"type":"communication_message","count":len(messages),"source_file":str(ph/"messages.txt"),"evidence_id":"EV-002"},
      {"type":"suspicious_email","count":1 if email.exists() else 0,"source_file":str(email),"evidence_id":"EV-002"},
      {"type":"gps_location","count":len(locations),"source_file":str(ph/"gps_locations.csv"),"evidence_id":"EV-002"},
      {"type":"transaction_id","value":txn.group(0) if txn else None,"source_file":str(sk/"transaction_logs.txt"),"evidence_id":"EV-001"},
      {"type":"application_login","value":login.group(1) if login else None,"source_file":str(ph/"fraudulent_app_logs.txt"),"evidence_id":"EV-002"}]
    for name,data in [("extracted_cards.csv",cards),("extracted_locations.csv",locations)]:
        with (OUT/name).open("w",newline="",encoding="utf-8") as f:
            if data:
                w=csv.DictWriter(f,fieldnames=list(data[0])); w.writeheader(); w.writerows(data)
    (OUT/"extracted_messages.json").write_text(json.dumps(messages,indent=2),encoding="utf-8")
    (OUT/"investigation_findings.json").write_text(json.dumps(findings,indent=2),encoding="utf-8")
    print(json.dumps(findings,indent=2))
if __name__=="__main__": main()
