from pathlib import Path
from datetime import datetime
import pandas as pd
from app.schemas.analysis import LoadPriceMetrics, MultiDayLoadSummary 

def analyze_load_price_data(csv_path: str) -> LoadPriceMetrics:
    # CAISO's CSV is not a normal row-per-record file.
    # The first row contains labels like "Demand 03/30/2026, 00:00, 00:05, ..."
    # and later rows contains series like "Demand", "Day-ahead forecast", etc.
    # header=None tells pandas not to assume the first row is a normal header
    df = pd.read_csv(csv_path, header=None)

    # The first row contains the time labels that line up with the numeric values.
    # Example:
    # row 0 -> ["Demand 03/30/2026", "00:00", "00:05", ...]
    header_row = df.iloc[0]

    # Find the row whose first column is exactly "Demand".
    # This is the actual demand series we want to analyze for the MVP.
    demand_rows = df[df[0] == "Demand"]

    # Fail early if the CSV does not contain the expected row.
    if demand_rows.empty:
        raise ValueError("Could not find a Demand row in the CSV.")

    # Take the first matching demand row.
    # For this file format, there should typically be one relevant Demand row.
    demand_row = demand_rows.iloc[0]

    # Ignore the first cell because it contains the row label ("Demand")
    # then keep the remaining cells, which correspond to the time columns.
    time_columns = header_row.iloc[1:]

    # Convert demand values to numeric.
    # errors='coerce' turns empty or malformed cells into NaN instead of crashing.
    demand_values = pd.to_numeric(demand_row.iloc[1:], errors="coerce")

    if len(time_columns) != len(demand_values):
        raise ValueError("Time columns and demand values are misaligned.")

    # Build dataframe first (preserves alignment)
    demand_series = pd.DataFrame({
        "time": time_columns.values,
        "demand": demand_values.values,
        })

    # dropna() removes those missing values so the metrics only use real numbers.
    demand_series = demand_series.dropna(subset=["demand"])

    # Calculate the highest observed demand.
    peak_demand = float(demand_series["demand"].max())

    # Calculate the average demand across all intervals.
    average_demand = float(demand_series["demand"].mean())

    minimum_demand = float(demand_series["demand"].min()) 

    peak_row = demand_series.loc[demand_series["demand"].idxmax()]
    min_row = demand_series.loc[demand_series["demand"].idxmin()]

    time_of_peak = str(peak_row["time"])
    time_of_minimum = str(min_row["time"])

    # Define a "notable spike" simply as any value at or above the 95th percentile.
    # This is not the only possible definition, but it is a reasonable first pass.
    spike_threshold = demand_series["demand"].quantile(0.95)

    # Filter rows that meet or exceed the spike threshold.
    spike_rows = demand_series[demand_series["demand"] >= spike_threshold]

    # Convert spike rows into short readable strings for now.
    # Later, we might return structured spike objects instead.
    notable_spikes = [
            f"{row.time}: demand reached {row.demand:.0f}"
            for row in spike_rows.itertuples(index=False)
            ]

    raw_date = Path(csv_path).stem.replace("CAISO-demand-", "")
    report_date = datetime.strptime(raw_date, "%Y%m%d").strftime("%Y-%m-%d")

    # Return the computed metrics using the schema model.
    return LoadPriceMetrics(
            peak_demand=peak_demand,
            average_demand=average_demand,
            notable_spikes=notable_spikes,
            report_date=report_date,
            time_of_peak=time_of_peak,
            minimum_demand=minimum_demand,
            time_of_minimum=time_of_minimum,
            spike_threshold=spike_threshold,
            )

def analyze_multiple_days(csv_paths: list[str]) -> LoadPriceMetrics:
    
    daily_metrics = [analyze_load_price_data(path) for path in csv_paths]
    

    return MultiDayLoadSummary(
            days_analyzed=days_analyzed,
            highest_peak_demand=highest_peak_demand,
            highest_peak_date=highest_peak_date,
            lowest_minimum_demand=lowest_minimum_demand,
            lowest_minimum_date=lowest_minimum_date,
            average_daily_demand=average_daily_demand,
            daily_metrics=daily_metrics,
            ) 


