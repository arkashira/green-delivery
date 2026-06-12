from argparse import ArgumentParser
from environmental_impact_calculator import EnvironmentalImpactCalculator

def main():
    parser = ArgumentParser(description="Environmental Impact Calculator")
    parser.add_argument("--routes", nargs="+", type=dict, help="List of routes in JSON format")
    args = parser.parse_args()
    calculator = EnvironmentalImpactCalculator()
    routes = [Route(distance=float(route["distance"]), emissions=[Emissions(source=EmissionsSource.CO2, amount=float(emission["amount"])) for emission in route["emissions"]]) for route in args.routes]
    total_emissions = calculator.calculate(routes)
    suggestions = calculator.suggest_reductions(total_emissions)
    print("Total Emissions:")
    for source, amount in total_emissions.items():
        print(f"{source}: {amount:.2f} units")
    print("\nSuggestions for Reduction:")
    for suggestion in suggestions:
        print(suggestion)

if __name__ == "__main__":
    main()
