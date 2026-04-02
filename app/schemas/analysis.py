from pydantic import BaseModel, Field

class LoadPriceMetrics(BaseModel):
    # Highest observed demand value in the dataset.
    peak_demand: float = Field(description="Highest observed demand value")

    # Mean demand across all usable time intervals.
    average_demand: float = Field(description="Average demand across all intervals")

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
    minimum_demand: float = Field(description="Lowest observed demand value")

    # Minimum demand time
    time_of_minimum: str = Field(description="Minimum demand time")

    # Spike Threshhold
    spike_threshold: float = Field(description="Spike threshold for demand values")

class 
