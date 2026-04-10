from pydantic import BaseModel, Field

class LoadPriceMetrics(BaseModel):
    # Highest observed demand value in the dataset.
    peak_demand: float = Field(description="Highest observed demand value")

    # Mean demand across all usable time intervals.
    avg_demand: float = Field(description="Average demand across all intervals")

    # Simple human-readable description of high-demand intervals.
    # default_factory=list avoids using a shared mutable defaults.
    notable_spikes: list[str] = Field(
            default_factory=list,
            description="Human-readable description of notable demand spikes",
            )

    # Date of the report
    report_date: str = Field(description="Date of the report")
    
    # Peak demand time
    time_of_peak: str = Field(description="Peak demand time")

    # Minimum demand
    min_demand: float = Field(description="Lowest observed demand value")

    # Minimum demand time
    time_of_min: str = Field(description="Minimum demand time")

    # Spike Threshhold
    spike_threshold: float = Field(description="Spike threshold for demand values")

class MultiDayLoadSummary(BaseModel):
    
    days_analyzed: int = Field(description="Number of days analyzed")
    highest_peak_demand: float = Field(description="Highest peak demand")
    highest_peak_date: str = Field(description="Highest peak demand date") 
    lowest_min_demand: float = Field(description="Lowest minimum demand")
    lowest_min_date: str = Field(description="Lowest minimum date")
    avg_daily_demand: float = Field(description="Average daily demand")
    daily_metrics: list[LoadPriceMetrics] = Field(
            default_factory=list,
            description="Daily metrics for each analyzed file",
            )

class AnalysisRequest(BaseModel): 
    
    region: str = Field(description="Region")
    time_range: str = Field(description="Time range")
    question: str = Field(description="Question to the agent")

class AnalysisResponse(BaseModel):

    region: str = Field(description="Region")
    time_range: str = Field(description="Time range")
    daily_metrics: list[LoadPriceMetrics] = Field(
            default_factory=list,
            description="Daily metrics for each analyzed file",
            ) 
    summary: str = Field(description="Response summary")
    notes: list[str] = Field(
            default_factory=list,
            description="Notes"
            )

