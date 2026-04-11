from app.agents.energy_analyst import run_energy_analyst
from app.core.config import get_caiso_demand_csv_paths
from app.schemas.analysis import AnalysisRequest

def main() -> None:
    request = AnalysisRequest(
        region="CAISO",
        time_range="2026-03-23 to 2026-03-30",
        question="Summarize demand patterns and notable spikes."
    )
    
    csv_paths = get_caiso_demand_csv_paths()
    
    response = run_energy_analyst(request, csv_paths)
    print(response.model_dump_json(indent=2))

if __name__ == "__main__":
    main()
