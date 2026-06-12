from performance_monitor import PerformanceMonitor, PerformanceMetric

def test_track_metric():
    monitor = PerformanceMonitor()
    monitor.track_metric('metric1', 10.0)
    assert 'metric1' in monitor.metrics
    assert monitor.metrics['metric1'].value == 10.0

def test_generate_report():
    monitor = PerformanceMonitor()
    monitor.track_metric('metric1', 10.0)
    monitor.track_metric('metric2', 20.0)
    report = monitor.generate_report()
    assert report['metric1'] == 10.0
    assert report['metric2'] == 20.0

def test_alert_significant_changes():
    monitor = PerformanceMonitor()
    monitor.track_metric('metric1', 10.0)
    monitor.track_metric('metric2', 20.0)
    significant_changes = monitor.alert_significant_changes(15.0)
    assert 'metric2' in significant_changes
