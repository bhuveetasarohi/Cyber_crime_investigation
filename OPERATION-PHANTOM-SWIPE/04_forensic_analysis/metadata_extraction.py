from pathlib import Path
import json, csv
ROOT=Path("03_evidence_acquisition/acquired_media")
OUT=Path("04_forensic_analysis/extracted_artifacts")
def main():
    OUT.mkdir(parents=True,exist_ok=True); records=[]
    for p in ROOT.rglob("*.json"):
        try:
            data=json.loads(p.read_text(encoding="utf-8"))
            records.append({"source_file":str(p),"evidence_id":"EV-001" if "skimmer" in str(p) else "EV-002","metadata":data})
        except (ValueError,OSError) as e: records.append({"source_file":str(p),"error":str(e)})
    (OUT/"metadata_summary.json").write_text(json.dumps(records,indent=2),encoding="utf-8")
    print(json.dumps(records,indent=2))
if __name__=="__main__": main()
