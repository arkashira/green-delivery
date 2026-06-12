import os
import tempfile
import json
import csv
import pytest
from integration import (
    Shipment,
    load_shipments_from_csv,
    load_shipments_from_json,
    export_shipments_to_csv,
    export_shipments_to_json,
    get_api_documentation,
)

@pytest.fixture
def sample_shipments():
    return [
        Shipment(id='S001', origin='Warehouse A', destination='Store X', weight=12.5, status='in_transit'),
        Shipment(id='S002', origin='Warehouse B', destination='Store Y', weight=7.0, status='delivered'),
    ]

def test_csv_roundtrip(sample_shipments):
    with tempfile.TemporaryDirectory() as tmpdir:
        csv_path = os.path.join(tmpdir, 'shipments.csv')
        export_shipments_to_csv(sample_shipments, csv_path)
        loaded = load_shipments_from_csv(csv_path)
        assert loaded == sample_shipments

def test_json_roundtrip(sample_shipments):
    with tempfile.TemporaryDirectory() as tmpdir:
        json_path = os.path.join(tmpdir, 'shipments.json')
        export_shipments_to_json(sample_shipments, json_path)
        loaded = load_shipments_from_json(json_path)
        assert loaded == sample_shipments

def test_api_documentation():
    doc = get_api_documentation()
    assert 'load_shipments_from_csv' in doc
    assert 'export_shipments_to_json' in doc
    assert 'Shipment' in doc
