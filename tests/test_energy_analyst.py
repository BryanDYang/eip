import unittest

from app.agents.energy_analyst import run_energy_analyst
from app.core.config import get_caiso_demand_csv_paths
from app.schemas.analysis import AnalysisRequest


class TestEnergyAnalyst(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.csv_paths = get_caiso_demand_csv_paths()

    def test_run_energy_analyst_returns_expected_response_shape(self) -> None:
        request = AnalysisRequest(
            region="CAISO",
            time_range="2026-03-23 to 2026-03-30",
            question="Summarize demand patterns and notable spikes.",
        )

        response = run_energy_analyst(request, self.csv_paths)

        self.assertEqual(response.region, "CAISO")
        self.assertEqual(response.time_range, "2026-03-23 to 2026-03-30")
        self.assertGreater(len(response.daily_metrics), 0)
        self.assertTrue(response.summary)
        self.assertGreater(len(response.notes), 0)


if __name__ == "__main__":
    unittest.main()
