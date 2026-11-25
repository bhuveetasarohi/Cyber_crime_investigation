"""Dictionary demonstration against this project's own AES ZIP archive."""
from pathlib import Path
import time
def main():
    try: import pyzipper
    except ImportError: raise SystemExit("Install pyzipper: py -m pip install pyzipper")
    archive=Path("05_cryptography/password_protected/evidence.zip")
    dictionary=Path("05_cryptography/password_dictionary.txt")
    if not archive.exists(): raise SystemExit("Run create_test_archive.py first.")
    candidates=[x.strip() for x in dictionary.read_text(encoding="utf-8").splitlines() if x.strip()]
    start=time.perf_counter(); recovered=None; attempted=0
    with pyzipper.AESZipFile(archive) as z:
        for candidate in candidates:
            attempted+=1
            try:
                z.setpassword(candidate.encode())
                # Reading all members validates the password/authentication.
                for member in z.namelist():
                    if not member.endswith("/"): z.read(member)
                recovered=candidate; break
            except (RuntimeError,ValueError,pyzipper.zipfile.BadZipFile): continue
    elapsed=time.perf_counter()-start
    result=(f"Archive: {archive}\\nMethod: ZIP AES (pyzipper)\\nCandidates attempted: {attempted}\\n"
            f"Recovered test password: {recovered or 'NOT FOUND'}\\nTime taken seconds: {elapsed:.6f}\\n"
            "Scope: own deliberately weak training archive only. No third-party accounts/devices/data tested.\\n")
    Path("05_cryptography/cracking_results.txt").write_text(result,encoding="utf-8")
    print(result)
    if recovered is None: raise SystemExit(1)
if __name__=="__main__": main()
