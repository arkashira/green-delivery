import pytest
from performance_monitor import PerformanceMonitor, RoutePerformance

def test_track_performance():
    monitor = PerformanceMonitor()
    monitor.track_performance(1, 0.9, 30.0)
    assert monitor.get_performance_report(1) == RoutePerformance(1, 0.9, 30.0)

def test_get_performance_report():
    monitor = PerformanceMonitor()
    monitor.track_performance(1, 0.9, 30.0)
    assert monitor.get_performance_report(1) == RoutePerformance(1, 0.9, 30.0)
    assert monitor.get_performance_report(2) is None

def test_alert_significant_change():
    monitor = PerformanceMonitor()
    monitor.track_performance(1, 0.8, 30.0)
    assert monitor.alert_significant_change(1, 0.9) == "Route 1 has an on-time rate below 0.9"
    assert monitor.alert_significant_change(1, 0.7) is None
    assert monitor.alert_significant_change(2, 0.9) is None
