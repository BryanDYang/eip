from fastapi import FastAPI, HTTPException

from app.agents.energy_analyst import run_energy_analyst
from app.core.config import get_caiso_demand_csv_paths
from app.schemas.analysis import AnalysisRequest, AnalysisResponse

app = FastAPI(title="Energy Intelligence Platform API", version="0.1.0")


@app.get("/health")
def health() -> dict[str, str]:
	return {"status": "ok"}


@app.post("/analyze/demand", response_model=AnalysisResponse)
def analyze_demand(request: AnalysisRequest) -> AnalysisResponse:
	try:
		csv_paths = get_caiso_demand_csv_paths()
		return run_energy_analyst(request, csv_paths)
	except ValueError as exc:
		raise HTTPException(status_code=400, detail=str(exc)) from exc
	except Exception as exc:
		raise HTTPException(status_code=500, detail="Unexpected server error") from exc
