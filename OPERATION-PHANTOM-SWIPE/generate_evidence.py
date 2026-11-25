"""Generate fictional source evidence for Operation Phantom Swipe."""
from pathlib import Path
import csv, json

BASE = Path("02_simulated_evidence")
def write(path, content):
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")

def main():
    sk = BASE / "device_01_skimmer"
    ph = BASE / "device_02_suspect_phone"
    write(sk/"device_info.txt", """DEVICE ID: SK-001
DEVICE TYPE: Simulated ATM skimmer evidence folder
LOCATION: Fictional Mumbai ATM Terminal
STATUS: Simulated seizure for coursework
CASE ID: OPS-2026-001
""")
    with (sk/"card_records.csv").open("w", newline="", encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["Record_ID","Test_Card_Number","Expiry","Location"])
        w.writerows([["R001","4111111111111111","12/29","Mumbai"],
                     ["R002","4012888888881881","10/28","Delhi"],
                     ["R003","5555555555554444","08/30","London"]])
    write(sk/"transaction_logs.txt", """2026-11-20 10:30:00 ATM-001 DATA CAPTURE
2026-11-20 11:15:00 RECORD R001 STORED
2026-11-20 12:20:00 TXN-OPS-8841 DATA TRANSFER ATTEMPT
""")
    (sk/"device_metadata.json").write_text(json.dumps({
        "device_id":"SK-001","case_id":"OPS-2026-001","created_utc":"2026-11-20T10:30:00Z",
        "description":"Fictional simulated evidence metadata","is_physical_image":False
    }, indent=2), encoding="utf-8")

    write(ph/"device_info.txt", """DEVICE ID: PH-002
DEVICE TYPE: Simulated suspect mobile-phone evidence folder
OWNER: Fictional subject S-02
STATUS: Simulated acquisition only
CASE ID: OPS-2026-001
""")
    write(ph/"messages.txt", """2026-11-20 09:05 | S-02: Meet near the test terminal after closing.
2026-11-20 12:25 | S-02: Transfer log TXN-OPS-8841 is only a simulation.
""")
    write(ph/"emails"/"suspect_email.eml", """From: operator@example.invalid
To: contact@example.invalid
Date: Fri, 20 Nov 2026 13:10:00 +0000
Subject: Test archive hand-off
Message-ID: <ops-2026-001@example.invalid>

The fictional test bundle is ready. Reference CASE OPS-2026-001.
""")
    with (ph/"gps_locations.csv").open("w", newline="", encoding="utf-8") as f:
        w=csv.writer(f); w.writerow(["Timestamp","Latitude","Longitude","Label"])
        w.writerows([["2026-11-20T09:00:00Z","19.0760","72.8777","Fictional Mumbai test point"],
                     ["2026-11-20T12:00:00Z","28.6139","77.2090","Fictional Delhi test point"]])
    write(ph/"fraudulent_app_logs.txt", """APP: DemoPay (fictional)
LOGIN: 2026-11-20 08:55:12 UTC user=S-02 result=SUCCESS
EVENT: 2026-11-20 12:21:04 UTC txn=TXN-OPS-8841 action=TEST_TRANSFER
""")
    write(ph/"hidden_folder"/"password.txt", "Fictional training note: archive password is intentionally weak.\n")
    manifest = {"case_id":"OPS-2026-001","notice":"All records are simulated; no real people or payment data.",
                "evidence":[{"evidence_id":"EV-001","device_id":"SK-001","path":"device_01_skimmer"},
                            {"evidence_id":"EV-002","device_id":"PH-002","path":"device_02_suspect_phone"}]}
    (BASE/"evidence_manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")
    print("Generated fictional skimmer and phone evidence.")

if __name__ == "__main__": main()
