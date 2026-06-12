import pytest
from environmental_impact_calculator import EmissionsSource, Emissions, Route, EnvironmentalImpactCalculator

def test_emissions_source():
    assert EmissionsSource.CO2.value == "CO2"
    assert EmissionsSource.CH4.value == "CH4"
    assert EmissionsSource.N2O.value == "N2O"

def test_emissions():
    emission = Emissions(EmissionsSource.CO2, 10.5)
    assert emission.source == EmissionsSource.CO2
    assert emission.amount == 10.5

def test_route():
    route = Route(100.0, [Emissions(EmissionsSource.CO2, 10.5)])
    assert route.distance == 100.0
    assert len(route.emissions) == 1
    assert route.emissions[0].source == EmissionsSource.CO2
    assert route.emissions[0].amount == 10.5

def test_calculate():
    calculator = EnvironmentalImpactCalculator()
    routes = [Route(100.0, [Emissions(EmissionsSource.CO2, 10.5)])]
    total_emissions = calculator.calculate(routes)
    assert total_emissions[EmissionsSource.CO2.value] == 10.5

def test_suggest_reductions():
    calculator = EnvironmentalImpactCalculator()
    total_emissions = {EmissionsSource.CO2.value: 10.5}
    suggestions = calculator.suggest_reductions(total_emissions)
    assert len(suggestions) == 1
    assert suggestions[0] == "Reduce CO2 emissions by 10.50 units"

def test_main():
    import sys
    sys.argv = ["main.py", "--routes", '[{"distance": 100.0, "emissions": [{"amount": 10.5, "source": "CO2"}]}]']
    with pytest.raises(SystemExit):
        from main import main
        main()
