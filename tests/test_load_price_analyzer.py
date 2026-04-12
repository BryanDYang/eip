import unittest
from pathlib import Path

from app.core.config import get_caiso_demand_csv_paths
from app.tools.load_price_analyzer import analyze_load_price_data, analyze_multiple_days


class TestLoadPriceAnalyzer(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.csv_paths = get_caiso_demand_csv_paths()

    def test_analyze_load_price_data_returns_metrics_for_known_csv(self) -> None:
        metrics = analyze_load_price_data(self.csv_paths[0])

        self.assertEqual(metrics.report_date, "2026-03-23")
        self.assertAlmostEqual(metrics.peak_demand, 29822.0, places=3)
        self.assertAlmostEqual(metrics.min_demand, 19454.0, places=3)
        self.assertEqual(metrics.time_of_peak, "19:40")
        self.assertEqual(metrics.time_of_min, "12:50")
        self.assertGreater(len(metrics.notable_spikes), 0)

    def test_analyze_multiple_days_raises_on_empty_csv_paths(self) -> None:
        with self.assertRaises(ValueError):
            analyze_multiple_days([])

    def test_analyze_load_price_data_raises_when_demand_row_missing(self) -> None:
        temp_csv = Path("data/processed/test-missing-demand.csv")
        temp_csv.parent.mkdir(parents=True, exist_ok=True)
        temp_csv.write_text(
            "Header,00:00,00:05\nNet Demand,100,101\n",
            encoding="utf-8",
        )

        try:
            with self.assertRaises(ValueError) as ctx:
                analyze_load_price_data(str(temp_csv))
            self.assertIn("Could not find a Demand row", str(ctx.exception))
        finally:
            if temp_csv.exists():
                temp_csv.unlink()

    def test_analyze_multiple_days_summary_values_are_consistent(self) -> None:
        summary = analyze_multiple_days(self.csv_paths)

        self.assertEqual(summary.days_analyzed, 8)
        self.assertAlmostEqual(summary.highest_peak_demand, 30073.0, places=3)
        self.assertEqual(summary.highest_peak_date, "2026-03-24")
        self.assertAlmostEqual(summary.lowest_min_demand, 14422.0, places=3)
        self.assertEqual(summary.lowest_min_date, "2026-03-29")
        self.assertEqual(len(summary.daily_metrics), 8)


if __name__ == "__main__":
    unittest.main()
