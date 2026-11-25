"""Correlate synthetic CSV event logs and generate a timeline CSV and PNG."""
from pathlib import Path
import csv
from datetime import datetime
import matplotlib.pyplot as plt
ROOT = Path(__file__).resolve().parents[1]
LOGS = ROOT / "04_timeline_analysis" / "sample_logs"
OUT_CSV = ROOT / "04_timeline_analysis" / "attack_timeline.csv"
OUT_PNG = ROOT / "04_timeline_analysis" / "timeline.png"

def main():
    source = LOGS / "system_events.csv"
    if not source.exists():
        raise SystemExit("No logs found. Run 09_simulated_hospital/generate_scenario.py")
    with source.open(newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    rows.sort(key=lambda r: r["timestamp_utc"])
    with OUT_CSV.open("w", newline="", encoding="utf-8") as f:
        w=csv.DictWriter(f, fieldnames=["timestamp_utc","source","event_id","event","details"])
        w.writeheader(); w.writerows(rows)
    dates=[datetime.fromisoformat(r["timestamp_utc"].replace("Z","+00:00")) for r in rows]
    labels=[r["event"] for r in rows]
    fig, ax = plt.subplots(figsize=(13, 6))
    y=list(range(len(rows)))
    ax.scatter(dates,y)
    for x, yy, label in zip(dates,y,labels):
        ax.annotate(label, (x,yy), xytext=(7,4), textcoords="offset points", fontsize=8)
    ax.set_yticks([])
    ax.set_title("Case Omega — Synthetic Incident Timeline (UTC)")
    ax.set_xlabel("Time (UTC)")
    ax.grid(True, axis="x", alpha=.3)
    fig.autofmt_xdate()
    fig.tight_layout()
    fig.savefig(OUT_PNG, dpi=160)
    plt.close(fig)
    print(f"Wrote {OUT_CSV} and {OUT_PNG} ({len(rows)} events).")

if __name__ == "__main__":
    main()
