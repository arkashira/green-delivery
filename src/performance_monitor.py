from dataclasses import dataclass
from typing import List
import json

@dataclass
class PerformanceMetric:
    name: str
    value: float

class PerformanceMonitor:
    def __init__(self):
        self.metrics = []

    def add_metric(self, metric: PerformanceMetric):
        self.metrics.append(metric)

    def get_report(self) -> str:
        report = {"metrics": []}
        for metric in self.metrics:
            report["metrics"].append({"name": metric.name, "value": metric.value})
        return json.dumps(report)

    def alert_significant_changes(self, threshold: float) -> List[str]:
        alerts = []
        for metric in self.metrics:
            if metric.value > threshold:
                alerts.append(f"Metric {metric.name} has value {metric.value}, exceeding threshold {threshold}")
        return alerts
