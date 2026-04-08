from pathlib import Path
from app.tools.load_price_analyzer import analyze_load_price_data, analyze_multiple_days
from app.agents.energy_analyst import run_energy_analyst

def main() -> None:
    run_energy_analyst()

if __name__ == "__main__":
    main() 
