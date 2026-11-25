# Operation Phantom Swipe
A Python-based **digital-forensics simulation** of a fictional ATM-skimming and payment-card fraud investigation.

> **Simulation notice:** All devices, people, events, locations, messages and transaction identifiers are fictional. The card values are public payment-network test numbers only. These folders are generated evidence files, not physical-device images or actual seized hardware. Do not use real payment credentials or third-party data.

## Objectives
- Generate two fictional evidence sets (simulated skimmer and suspect phone).
- Acquire working copies and verify SHA-256 integrity.
- Maintain a chain-of-custody log.
- Extract card-test values, messages, email, GPS, transaction and login artefacts.
- Demonstrate dictionary recovery against a ZIP archive created by this project.
- Produce a technical/legal report and validate the repository with GitHub Actions.

## Requirements
- Python 3.10+ (3.11 recommended).
- Optional report dependencies: `python-docx`, `reportlab`.
- No real ATM hardware, database, web app, malware or external cracking utility is used.

## Quick start (Windows PowerShell)
```powershell
py -m venv .venv
.\\.venv\\Scripts\\Activate.ps1
py -m pip install -r requirements.txt
py generate_evidence.py
py 03_evidence_acquisition/acquisition.py
py 03_evidence_acquisition/generate_hashes.py
py 03_evidence_acquisition/verify_hashes.py
py 04_forensic_analysis/string_search.py
py 04_forensic_analysis/metadata_extraction.py
py 04_forensic_analysis/email_extraction.py
py 04_forensic_analysis/artifact_extraction.py
py 05_cryptography/create_test_archive.py
py 05_cryptography/password_cracker.py
py 06_reports/create_report.py
```
Run commands from the project root. `create_report.py` creates DOCX and PDF if dependencies are installed.

## Methodology
1. Generate source evidence under `02_simulated_evidence/`.
2. Copy it into `03_evidence_acquisition/acquired_media/`; record the operation.
3. Hash acquired files with SHA-256 and compare source/copy digests.
4. Search and parse only the generated evidence.
5. Create a deliberately weak, project-owned ZIP and test a local dictionary.
6. Review findings and limitations in the report.

## Expected outputs
- `06_reports/evidence_hashes.txt`
- `03_evidence_acquisition/chain_of_custody.csv`
- `04_forensic_analysis/extracted_artifacts/` CSV, TXT and JSON outputs
- `05_cryptography/cracking_results.txt`
- `06_reports/Operation_Phantom_Swipe_Report.docx` and `.pdf` (optional libraries required)

## Evidence handling and limitations
A SHA-256 digest helps detect changes; it does not by itself prove authenticity, lawful collection, attribution or admissibility. A write blocker, physical seizure, forensic bit-stream imaging and hardware examination are **not performed**. Their concepts are described for learning only. The acquisition script copies files, not disk sectors.

## Legal research note
The included legal mapping is an academic starting point, not legal advice. The assignment asks for historical IPC references and current BNS context. Confirm exact provisions against current official legislation and the facts of any real case. India is not a party to the Budapest Convention; it is discussed as a comparative international framework, not a binding treaty obligation on India.

## Screenshots
Capture your own screenshots after running the scripts. The `07_screenshots/` directory contains a guide; no fabricated execution screenshots are supplied.
