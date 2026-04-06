from pathlib import Path
from app.tools.load_price_analyzer import analyze_load_price_data, analyze_multiple_days


def main() -> None:
    data_dir = Path("data/raw/caiso/demand")
    csv_paths = [str(path) for path in sorted(data_dir.glob("CAISO-demand-*.csv"))]
    
    metrics = analyze_multiple_days(csv_paths)
    print(metrics.model_dump_json(indent=2))

if __name__ == "__main__":
    main()
