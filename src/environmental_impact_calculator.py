import json
from dataclasses import dataclass
from typing import List

@dataclass
class DeliveryRoute:
    distance: float
    fuel_consumption: float
    emissions: float

class EnvironmentalImpactCalculator:
    def __init__(self):
        self.routes = []

    def add_route(self, route: DeliveryRoute):
        self.routes.append(route)

    def calculate_environmental_impact(self) -> float:
        total_emissions = sum(route.emissions for route in self.routes)
        return total_emissions

    def display_environmental_impact(self) -> str:
        impact = self.calculate_environmental_impact()
        return f"Total environmental impact: {impact} kg CO2"

    def suggest_reductions(self) -> List[str]:
        suggestions = []
        for route in self.routes:
            if route.fuel_consumption > 10:
                suggestions.append(f"Optimize route with distance {route.distance} km")
        return suggestions
