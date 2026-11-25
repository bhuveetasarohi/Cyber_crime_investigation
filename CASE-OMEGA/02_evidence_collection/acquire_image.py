"""Create a logical TAR evidence package from the fictional server folder.
This is NOT a physical bit-for-bit disk image.
"""
from pathlib import Path
import argparse, tarfile, hashlib, csv
ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "09_simulated_hospital" / "server"
OUT = ROOT / "02_evidence_collection" / "simulated_server_image.tar"
MANIFEST = ROOT / "02_evidence_collection" / "evidence_manifest.csv"

def sha256(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source", type=Path, default=SOURCE)
    parser.add_argument("--output", type=Path, default=OUT)
    args = parser.parse_args()
    if not args.source.exists():
        raise SystemExit("Server folder not found. Run 09_simulated_hospital/generate_scenario.py first.")
    args.output.parent.mkdir(parents=True, exist_ok=True)
    with tarfile.open(args.output, "w") as tar:
        tar.add(args.source, arcname="server")
    digest = sha256(args.output)
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with MANIFEST.open("w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["evidence_id","filename","size_bytes","sha256","acquisition_type","notes"])
        w.writerow(["E-01",args.output.name,args.output.stat().st_size,digest,
                    "Logical TAR package","Synthetic server directory; not a physical disk image"])
    print(f"Created: {args.output}")
    print(f"Size: {args.output.stat().st_size} bytes")
    print(f"SHA-256: {digest}")
    print("NOTE: Logical evidence package only; not a bit-for-bit disk acquisition.")

if __name__ == "__main__":
    main()
