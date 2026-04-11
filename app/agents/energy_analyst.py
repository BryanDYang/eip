from app.schemas.analysis import AnalysisRequest, AnalysisResponse
from app.tools.load_price_analyzer import analyze_multiple_days

def run_energy_analyst(request: AnalysisRequest, csv_paths: list[str]) -> AnalysisResponse:
    metrics = analyze_multiple_days(csv_paths)

    summary = (
        f"Analyzed {metrics.days_analyzed} days of CAISO demand data. "
        f"Highest peak was {metrics.highest_peak_demand:.0f} MW on {metrics.highest_peak_date}; "
        f"Lowest minimum was {metrics.lowest_min_demand:.0f} MW on {metrics.lowest_min_date}; "
        f"Average daily demand was {metrics.avg_daily_demand:.0f} MW."
    )
    
    notes = [
        "Demand-only analysis for current MVP scope.",
        "No price analysis is included in this output.",
        "Spike detection uses 95th percentile threshold per day.",
    ]

    return AnalysisResponse(
        region=request.region,
        time_range=request.time_range,
        daily_metrics=metrics.daily_metrics,
        summary=summary,
        notes=notes,
    )

