import unittest

from fastapi.testclient import TestClient

from app.api.main import app


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.client = TestClient(app)

    def test_health(self) -> None:
        response = self.client.get("/health")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json(), {"status": "ok"})

    def test_analyze_demand_returns_structured_response(self) -> None:
        payload = {
            "region": "CAISO",
            "time_range": "2026-03-23 to 2026-03-30",
            "question": "Summarize demand patterns and notable spikes.",
        }

        response = self.client.post("/analyze/demand", json=payload)
        self.assertEqual(response.status_code, 200)

        body = response.json()
        self.assertIn("region", body)
        self.assertIn("time_range", body)
        self.assertIn("daily_metrics", body)
        self.assertIn("summary", body)
        self.assertIn("notes", body)
        self.assertGreater(len(body["daily_metrics"]), 0)


if __name__ == "__main__":
    unittest.main()
