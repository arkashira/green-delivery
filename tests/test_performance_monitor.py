import pytest
import json
from src.performance_monitor import PerformanceMonitor, PerformanceMetric

def test_add_metric():
    monitor = PerformanceMonitor()
    metric = PerformanceMetric("test_metric", 10.0)
    monitor.add_metric(metric)
    assert len(monitor.metrics) == 1
    assert monitor.metrics[0].name == "test_metric"
    assert monitor.metrics[0].value == 10.0

def test_get_report():
    monitor = PerformanceMonitor()
    metric1 = PerformanceMetric("metric1", 10.0)
    metric2 = PerformanceMetric("metric2", 20.0)
    monitor.add_metric(metric1)
    monitor.add_metric(metric2)
    report = monitor.get_report()
    assert json.loads(report) == {"metrics": [{"name": "metric1", "value": 10.0}, {"name": "metric2", "value": 20.0}]}

def test_alert_significant_changes():
    monitor = PerformanceMonitor()
    metric1 = PerformanceMetric("metric1", 10.0)
    metric2 = PerformanceMetric("metric2", 30.0)
    monitor.add_metric(metric1)
    monitor.add_metric(metric2)
    alerts = monitor.alert_significant_changes(20.0)
    assert len(alerts) == 1
    assert alerts[0] == "Metric metric2 has value 30.0, exceeding threshold 20.0"

def test_alert_significant_changes_no_alerts():
    monitor = PerformanceMonitor()
    metric1 = PerformanceMetric("metric1", 10.0)
    metric2 = PerformanceMetric("metric2", 15.0)
    monitor.add_metric(metric1)
    monitor.add_metric(metric2)
    alerts = monitor.alert_significant_changes(20.0)
    assert len(alerts) == 0
