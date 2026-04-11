from pathlib import Path


def get_caiso_demand_csv_paths(
	data_dir: str = "data/raw/caiso/demand",
	pattern: str = "CAISO-demand-*.csv",
) -> list[str]:
	paths = [str(p) for p in sorted(Path(data_dir).glob(pattern))]
	if not paths:
		raise ValueError(f"No CSV files matched pattern '{pattern}' under '{data_dir}'")
	return paths
