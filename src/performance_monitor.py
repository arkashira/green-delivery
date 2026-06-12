import json
from dataclasses import dataclass
from typing import List

@dataclass
class RoutePerformance:
    route_id: int
    on_time_rate: float
    average_delivery_time: float

class PerformanceMonitor:
    def __init__(self):
        self.route_performances = {}

    def track_performance(self, route_id: int, on_time_rate: float, average_delivery_time: float):
        self.route_performances[route_id] = RoutePerformance(route_id, on_time_rate, average_delivery_time)

    def get_performance_report(self, route_id: int):
        return self.route_performances.get(route_id)

    def alert_significant_change(self, route_id: int, threshold: float):
        current_performance = self.route_performances.get(route_id)
        if current_performance and current_performance.on_time_rate < threshold:
            return f"Route {route_id} has an on-time rate below {threshold}"
        return None
