import json
from dataclasses import dataclass
from argparse import ArgumentParser

@dataclass
class PerformanceMetric:
    name: str
    value: float

class PerformanceMonitor:
    def __init__(self):
        self.metrics = {}

    def track_metric(self, name, value):
        self.metrics[name] = PerformanceMetric(name, value)

    def generate_report(self):
        report = {}
        for metric in self.metrics.values():
            report[metric.name] = metric.value
        return report

    def alert_significant_changes(self, threshold):
        significant_changes = []
        for metric in self.metrics.values():
            if abs(metric.value) > threshold:
                significant_changes.append(metric.name)
        return significant_changes

def main():
    parser = ArgumentParser(description='Performance Monitor')
    parser.add_argument('--track', nargs=2, help='Track a performance metric')
    parser.add_argument('--report', action='store_true', help='Generate a report')
    parser.add_argument('--alert', type=float, help='Alert on significant changes')
    args = parser.parse_args()

    monitor = PerformanceMonitor()

    if args.track:
        name, value = args.track
        monitor.track_metric(name, float(value))

    if args.report:
        report = monitor.generate_report()
        print(json.dumps(report))

    if args.alert:
        significant_changes = monitor.alert_significant_changes(args.alert)
        print(json.dumps(significant_changes))

if __name__ == '__main__':
    main()
