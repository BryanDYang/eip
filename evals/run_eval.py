import json
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

from app.agents.energy_analyst import run_energy_analyst
from app.schemas.analysis import AnalysisRequest


def _find_day(daily_metrics, report_date: str):
    for day in daily_metrics:
        if day.report_date == report_date:
            return day
    return None


def _check_case(response, case: dict) -> tuple[bool, list[str]]:
    expect = case.get("expect", {})
    errors: list[str] = []

    if "must_include_fields" in expect:
        payload = response.model_dump()
        for field in expect["must_include_fields"]:
            if field not in payload:
                errors.append(f"missing field: {field}")

    if "summary_contains" in expect:
        for token in expect["summary_contains"]:
            if token.lower() not in response.summary.lower():
                errors.append(f"summary missing token: {token}")

    if "highest_peak_date" in expect:
        top_day = max(response.daily_metrics, key=lambda day: day.peak_demand)
        if top_day.report_date != expect["highest_peak_date"]:
            errors.append(
                f"highest_peak_date expected {expect['highest_peak_date']} got {top_day.report_date}"
            )

    if "highest_peak_demand" in expect:
        top_day = max(response.daily_metrics, key=lambda day: day.peak_demand)
        if abs(top_day.peak_demand - expect["highest_peak_demand"]) > 1e-6:
            errors.append(
                f"highest_peak_demand expected {expect['highest_peak_demand']} got {top_day.peak_demand}"
            )

    if "time_of_peak_on_day" in expect and "highest_peak_date" in expect:
        day = _find_day(response.daily_metrics, expect["highest_peak_date"])
        if not day:
            errors.append(f"missing day for date {expect['highest_peak_date']}")
        elif day.time_of_peak != expect["time_of_peak_on_day"]:
            errors.append(
                f"time_of_peak_on_day expected {expect['time_of_peak_on_day']} got {day.time_of_peak}"
            )

    if "lowest_min_date" in expect:
        low_day = min(response.daily_metrics, key=lambda day: day.min_demand)
        if low_day.report_date != expect["lowest_min_date"]:
            errors.append(
                f"lowest_min_date expected {expect['lowest_min_date']} got {low_day.report_date}"
            )

    if "lowest_min_demand" in expect:
        low_day = min(response.daily_metrics, key=lambda day: day.min_demand)
        if abs(low_day.min_demand - expect["lowest_min_demand"]) > 1e-6:
            errors.append(
                f"lowest_min_demand expected {expect['lowest_min_demand']} got {low_day.min_demand}"
            )

    if "time_of_min_on_day" in expect and "lowest_min_date" in expect:
        day = _find_day(response.daily_metrics, expect["lowest_min_date"])
        if not day:
            errors.append(f"missing day for date {expect['lowest_min_date']}")
        elif day.time_of_min != expect["time_of_min_on_day"]:
            errors.append(
                f"time_of_min_on_day expected {expect['time_of_min_on_day']} got {day.time_of_min}"
            )

    if "avg_daily_demand_approx" in expect:
        tolerance = float(expect.get("tolerance", 0.0))
        avg_daily = sum(day.avg_demand for day in response.daily_metrics) / len(response.daily_metrics)
        if abs(avg_daily - float(expect["avg_daily_demand_approx"])) > tolerance:
            errors.append(
                f"avg_daily_demand expected ~{expect['avg_daily_demand_approx']}±{tolerance} got {avg_daily}"
            )

    if "days_analyzed" in expect:
        if len(response.daily_metrics) != int(expect["days_analyzed"]):
            errors.append(
                f"days_analyzed expected {expect['days_analyzed']} got {len(response.daily_metrics)}"
            )

    if "min_spikes_per_day" in expect:
        threshold = int(expect["min_spikes_per_day"])
        for day in response.daily_metrics:
            if len(day.notable_spikes) < threshold:
                errors.append(
                    f"{day.report_date} has {len(day.notable_spikes)} spikes, expected at least {threshold}"
                )

    if "top3_peak_dates_order" in expect:
        top3 = sorted(
            response.daily_metrics,
            key=lambda day: day.peak_demand,
            reverse=True,
        )[:3]
        top3_dates = [day.report_date for day in top3]
        if top3_dates != expect["top3_peak_dates_order"]:
            errors.append(
                f"top3_peak_dates_order expected {expect['top3_peak_dates_order']} got {top3_dates}"
            )

    if "must_mention" in expect:
        text = " ".join([response.summary] + list(response.notes)).lower()
        for term in expect["must_mention"]:
            if term.lower() not in text:
                errors.append(f"missing mention: {term}")

    return len(errors) == 0, errors


def run_eval() -> int:
    eval_path = Path("evals/expected_baseline.json")
    with eval_path.open("r", encoding="utf-8") as f:
        baseline = json.load(f)

    meta = baseline["meta"]
    data_dir = Path("data/raw/caiso/demand")
    csv_paths = [str(p) for p in sorted(data_dir.glob("CAISO-demand-*.csv"))]

    passes = 0
    fails = 0

    print(f"Running baseline: {meta['version']}")
    for case in baseline["cases"]:
        request = AnalysisRequest(
            region=meta["region"],
            time_range=meta["time_range"],
            question=case["question"],
        )
        response = run_energy_analyst(request, csv_paths)
        ok, errors = _check_case(response, case)

        if ok:
            passes += 1
            print(f"[PASS] {case['id']}: {case['question']}")
        else:
            fails += 1
            print(f"[FAIL] {case['id']}: {case['question']}")
            for err in errors:
                print(f"  - {err}")

    print(f"\nSummary: {passes} passed, {fails} failed")
    return 0 if fails == 0 else 1


if __name__ == "__main__":
    raise SystemExit(run_eval())
