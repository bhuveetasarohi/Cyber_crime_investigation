"""Calculate and verify SHA-256 for a selected evidence file."""
from pathlib import Path
import argparse, hashlib

def sha256(path):
    digest = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()

def main():
    default = Path(__file__).resolve().parent / "simulated_server_image.tar"
    p = argparse.ArgumentParser()
    p.add_argument("file", nargs="?", type=Path, default=default)
    p.add_argument("--expected", help="Optional previously recorded SHA-256")
    args = p.parse_args()
    if not args.file.is_file():
        raise SystemExit(f"Evidence file not found: {args.file}")
    actual = sha256(args.file)
    print(f"File: {args.file}")
    print(f"SHA-256: {actual}")
    if args.expected:
        ok = actual.lower() == args.expected.lower()
        print("VERIFICATION: " + ("MATCH" if ok else "MISMATCH"))
        raise SystemExit(0 if ok else 2)

if __name__ == "__main__":
    main()
