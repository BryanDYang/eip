from pathlib import Path
from app.tools.load_price_analyzer import analyze_load_price_data, analyze_multiple_days
from app.agents.energy_analyst import run_energy_analyst
from app.schemas.analysis import AnalysisRequest

def main() -> None:
    request = AnalysisRequest(
        region="CAISO",
        time_range="2026-03-23 to 2026-03-30",
        question="Summarize demand patterns and notable spikes."
    )
    
    data_dir = Path("data/raw/caiso/demand")
    csv_paths = [str(p) for p in sorted(data_dir.glob("CAISO-demand-*.csv"))]
    
    response = run_energy_analyst(request, csv_paths)
    print(response)

if __name__ == "__main__":
    main() 
