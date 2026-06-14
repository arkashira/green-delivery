from environmental_impact_calculator import EnvironmentalImpactCalculator, DeliveryRoute

def test_calculate_environmental_impact():
    calculator = EnvironmentalImpactCalculator()
    route1 = DeliveryRoute(distance=100, fuel_consumption=5, emissions=10)
    route2 = DeliveryRoute(distance=200, fuel_consumption=10, emissions=20)
    calculator.add_route(route1)
    calculator.add_route(route2)
    assert calculator.calculate_environmental_impact() == 30

def test_display_environmental_impact():
    calculator = EnvironmentalImpactCalculator()
    route1 = DeliveryRoute(distance=100, fuel_consumption=5, emissions=10)
    calculator.add_route(route1)
    assert calculator.display_environmental_impact() == "Total environmental impact: 10 kg CO2"

def test_suggest_reductions():
    calculator = EnvironmentalImpactCalculator()
    route1 = DeliveryRoute(distance=100, fuel_consumption=15, emissions=10)
    route2 = DeliveryRoute(distance=200, fuel_consumption=5, emissions=20)
    calculator.add_route(route1)
    calculator.add_route(route2)
    suggestions = calculator.suggest_reductions()
    assert len(suggestions) == 1
    assert suggestions[0] == "Optimize route with distance 100 km"

def test_empty_routes():
    calculator = EnvironmentalImpactCalculator()
    assert calculator.calculate_environmental_impact() == 0
    assert calculator.display_environmental_impact() == "Total environmental impact: 0 kg CO2"
    assert calculator.suggest_reductions() == []
