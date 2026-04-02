from pathlib import Path
from app.tools.load_price_analyzer import analyze_load_price_data


def main() -> None:
    data_dir = Path("data/raw/caiso/demand")

    for csv_path in sorted(data_dir.glob("CAISO-demand-*.csv")):
        metrics = analyze_load_price_data(str(csv_path))
        print(f"\n=== {csv_path.name} ===")
        print(metrics.model_dump_json(indent=2))

if __name__ == "__main__":
    main()
