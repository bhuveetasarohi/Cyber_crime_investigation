from pathlib import Path
REPORT = """Operation Phantom Swipe – Investigation Report

1. Introduction and Case Overview
This is a fictional case study (OPS-2026-001) concerning simulated ATM skimming indicators and possible payment-card misuse. The objectives are to demonstrate a repeatable evidence workflow, verify copied-file integrity and extract illustrative artefacts.

2. Cybercrime Classification
The scenario discusses ATM skimming, card-data theft, card cloning, identity/data theft and online payment fraud as taxonomy categories. No actual skimming or payment activity is performed. Refer to 01_documentation/legal_mapping.md for the assignment's historical IPC/IT Act mapping, BNS context, BSA electronic-evidence discussion and Budapest Convention comparison.

3. Evidence Acquisition
Two simulated evidence sets are generated: EV-001 (SK-001) and EV-002 (PH-002). The acquisition script copies ordinary files into acquired_media and logs hashes. This is not a physical seizure, write-blocked acquisition or bit-for-bit forensic image. SHA-256 comparisons can indicate whether the copied files match the generated source files at verification time.

4. Forensic Analysis and Findings
The analysis scripts identify three published test card values, two fictional messages, one fictional EML email, two illustrative GPS coordinates, a sample transaction identifier and an application login timestamp. Each extracted artefact records its source path and evidence ID. These are indicators within a constructed dataset, not proof of a real person's conduct.

5. Cryptographic Investigation
The project creates an AES-encrypted ZIP archive with a deliberately weak password and tests candidates from a local dictionary. This is a controlled demonstration against an archive created by the project. It is not a general-purpose password-cracking product and does not test real accounts or devices.

6. Legal and Ethical Considerations
Any real investigation requires lawful authority, privacy safeguards, documented provenance, competent handling and compliance with applicable procedural and evidentiary law. In India, assess the Bharatiya Sakshya Adhiniyam, 2023 (including Sections 61–63) for electronic/digital records. Hashing alone does not establish admissibility. The IPC is historical following replacement by the BNS from 1 July 2024; verify current provisions and transitional applicability from official sources. India is not a party to the Budapest Convention; its provisions are treated here only as comparative international framework.

7. Conclusion and Recommendations
The simulation demonstrates generation, copying, SHA-256 verification, traceable artefact extraction and a bounded dictionary test. Recommended practice includes maintaining complete chain-of-custody records, preserving originals, recording tool versions and timestamps, validating hashes at each transfer, minimizing personal data, and consulting current legal requirements. All findings must be interpreted within the simulation's limitations.
"""
def main():
    out=Path("06_reports"); out.mkdir(exist_ok=True)
    try:
        from docx import Document
        doc=Document()
        for para in REPORT.split("\\n"):
            if para and para[0].isdigit() and ". " in para[:4]: doc.add_heading(para,level=1)
            elif para: doc.add_paragraph(para)
        doc.save(out/"Operation_Phantom_Swipe_Report.docx")
    except ImportError: print("python-docx missing; DOCX not created.")
    try:
        from reportlab.lib.pagesizes import A4
        from reportlab.platypus import SimpleDocTemplate,Paragraph,Spacer
        from reportlab.lib.styles import getSampleStyleSheet
        from reportlab.lib.units import mm
        styles=getSampleStyleSheet(); story=[]
        for para in REPORT.split("\\n"):
            if para:
                style=styles["Heading2"] if para[:1].isdigit() and ". " in para[:4] else styles["BodyText"]
                story.extend([Paragraph(para.replace("&","&amp;"),style),Spacer(1,3*mm)])
        SimpleDocTemplate(str(out/"Operation_Phantom_Swipe_Report.pdf"),pagesize=A4).build(story)
    except ImportError: print("reportlab missing; PDF not created.")
    print("Report generation complete.")
if __name__=="__main__": main()
