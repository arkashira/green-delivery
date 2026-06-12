import json
from green_delivery import GreenDelivery, LogisticsData

def test_import_data():
    green_delivery = GreenDelivery()
    logistics_data = [
        LogisticsData(1, "Logistics Data 1", "Description 1"),
        LogisticsData(2, "Logistics Data 2", "Description 2")
    ]
    green_delivery.import_data(logistics_data)
    assert len(green_delivery.logistics_data) == 2

def test_export_data():
    green_delivery = GreenDelivery()
    logistics_data = [
        LogisticsData(1, "Logistics Data 1", "Description 1"),
        LogisticsData(2, "Logistics Data 2", "Description 2")
    ]
    green_delivery.import_data(logistics_data)
    exported_data = green_delivery.export_data()
    assert len(json.loads(exported_data)) == 2

def test_provide_api():
    green_delivery = GreenDelivery()
    api = green_delivery.provide_api()
    assert "import_data" in api
    assert "export_data" in api

def test_provide_documentation():
    green_delivery = GreenDelivery()
    documentation = green_delivery.provide_documentation()
    assert documentation == "GreenDelivery API Documentation"
