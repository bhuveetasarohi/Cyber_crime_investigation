from pathlib import Path
import zipfile
SOURCE=Path("02_simulated_evidence/device_02_suspect_phone/hidden_folder")
TARGET=Path("05_cryptography/password_protected/evidence.zip")
def main():
    if not SOURCE.exists(): raise SystemExit("Generate evidence first.")
    try:
        import pyzipper
    except ImportError:
        raise SystemExit("Install optional pyzipper to create an encrypted ZIP: py -m pip install pyzipper")
    TARGET.parent.mkdir(parents=True,exist_ok=True)
    with pyzipper.AESZipFile(TARGET,"w",compression=zipfile.ZIP_DEFLATED,encryption=pyzipper.WZ_AES) as z:
        z.setpassword(b"phantom123")
        for p in SOURCE.rglob("*"):
            if p.is_file(): z.write(p,p.relative_to(SOURCE.parent))
    print("Created project-owned AES-encrypted test archive:",TARGET)
if __name__=="__main__": main()
