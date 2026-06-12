import json
from dataclasses import dataclass
from typing import List

@dataclass
class LogisticsData:
    """Data class to hold logistics data"""
    id: int
    name: str
    description: str

class GreenDelivery:
    """Class to handle integration with existing logistics software"""
    def __init__(self):
        self.logistics_data = []

    def import_data(self, data: List[LogisticsData]):
        """Import logistics data"""
        self.logistics_data.extend(data)

    def export_data(self):
        """Export logistics data"""
        return json.dumps([data.__dict__ for data in self.logistics_data])

    def provide_api(self):
        """Provide API for integration"""
        return {
            "import_data": self.import_data,
            "export_data": self.export_data
        }

    def provide_documentation(self):
        """Provide documentation for integration"""
        return "GreenDelivery API Documentation"

def main():
    green_delivery = GreenDelivery()
    logistics_data = [
        LogisticsData(1, "Logistics Data 1", "Description 1"),
        LogisticsData(2, "Logistics Data 2", "Description 2")
    ]
    green_delivery.import_data(logistics_data)
    print(green_delivery.export_data())

if __name__ == "__main__":
    main()
