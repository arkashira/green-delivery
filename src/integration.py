import csv
import json
from dataclasses import dataclass, asdict
from typing import List

@dataclass
class Shipment:
    """Represents a shipment record."""
    id: str
    origin: str
    destination: str
    weight: float
    status: str

def load_shipments_from_csv(file_path: str) -> List[Shipment]:
    """Load shipments from a CSV file. CSV columns must be: id,origin,destination,weight,status"""
    shipments: List[Shipment] = []
    with open(file_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            shipments.append(
                Shipment(
                    id=row['id'],
                    origin=row['origin'],
                    destination=row['destination'],
                    weight=float(row['weight']),
                    status=row['status'],
                )
            )
    return shipments

def load_shipments_from_json(file_path: str) -> List[Shipment]:
    """Load shipments from a JSON file. JSON must be a list of objects with keys: id,origin,destination,weight,status"""
    shipments: List[Shipment] = []
    with open(file_path, encoding='utf-8') as f:
        data = json.load(f)
        for item in data:
            shipments.append(
                Shipment(
                    id=item['id'],
                    origin=item['origin'],
                    destination=item['destination'],
                    weight=float(item['weight']),
                    status=item['status'],
                )
            )
    return shipments

def export_shipments_to_csv(shipments: List[Shipment], file_path: str) -> None:
    """Export shipments to a CSV file."""
    fieldnames = ['id', 'origin', 'destination', 'weight', 'status']
    with open(file_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for s in shipments:
            writer.writerow(asdict(s))

def export_shipments_to_json(shipments: List[Shipment], file_path: str) -> None:
    """Export shipments to a JSON file."""
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump([asdict(s) for s in shipments], f, indent=2)

def get_api_documentation() -> str:
    """Return a short documentation string for the integration API."""
    return """
GreenDelivery Integration API
============================
This module exposes a lightweight API for importing and exporting shipment data in common formats used by logistics software.
Functions
---------
- `load_shipments_from_csv(file_path: str) -> List[Shipment]` Load shipments from a CSV file.
- `load_shipments_from_json(file_path: str) -> List[Shipment]` Load shipments from a JSON file.
- `export_shipments_to_csv(shipments: List[Shipment], file_path: str) -> None` Export shipments to a CSV file.
- `export_shipments_to_json(shipments: List[Shipment], file_path: str) -> None` Export shipments to a JSON file.
Data Model
----------
- `Shipment` dataclass with fields:
  - `id` (str)
  - `origin` (str)
  - `destination` (str)
  - `weight` (float)
  - `status` (str)
The API is intentionally simple and uses only the Python standard library, making it easy to integrate with any existing system.
    """
    doc = get_api_documentation()
    # Add the missing documentation
    doc += """
    - `Shipment` dataclass: Represents a shipment record.
    """
    return doc

__all__ = [
    'Shipment',
    'load_shipments_from_csv',
    'load_shipments_from_json',
    'export_shipments_to_csv',
    'export_shipments_to_json',
    'get_api_documentation',
]
