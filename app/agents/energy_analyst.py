from app.schemas.analysis import AnalysisRequest, AnalysisResponse
from app.tools.load_price_analyzer import analyze_multiple_days

def run_energy_analyst(request: AnalysisRequest) -> AnalysisResponse:
    data_dir = Path("data/raw/caiso/demand")
    csv_paths = [str(path) for path in sorted(data_dir.glob("CAISO-demand-*.csv"))]

    metrics = analyze_multiple_days(csv_paths)
    print(metrics.model_dump_json(indent=2))
    AnalysisResponse = 

    return AnalysisRequest
