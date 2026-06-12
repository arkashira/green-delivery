from dataclasses import dataclass
from enum import Enum
from typing import Dict, List

class EmissionsSource(Enum):
    CO2 = "CO2"
    CH4 = "CH4"
    N2O = "N2O"

@dataclass
class Emissions:
    source: EmissionsSource
    amount: float

@dataclass
class Route:
    distance: float
    emissions: List[Emissions]

class EnvironmentalImpactCalculator:
    def calculate(self, routes: List[Route]) -> Dict[str, float]:
        total_emissions = {}
        for route in routes:
            for emission in route.emissions:
                if emission.source.value not in total_emissions:
                    total_emissions[emission.source.value] = 0
                total_emissions[emission.source.value] += emission.amount
        return total_emissions

    def suggest_reductions(self, total_emissions: Dict[str, float]) -> List[str]:
        reductions = []
        for source, amount in total_emissions.items():
            reductions.append(f"Reduce {source} emissions by {amount:.2f} units")
        return reductions
