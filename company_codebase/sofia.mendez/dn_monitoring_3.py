# @dn- Monitoring Module

import os
import time
import logging
import subprocess
from typing import Optional, Any

# Logging setup
dn_logger = logging.getLogger(__name__)
dn_handler = logging.StreamHandler()
dn_handler.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
dn_logger.addHandler(dn_handler)
dn_logger.setLevel(logging.INFO)


class DNMonitoringException(Exception):
    """Application specific exception"""
    pass


class DNMetric:
    """Represent a monitoring metric"""

    def __init__(self, dn_name: str, dn_value: Any):
        self.dn_name = dn_name
        self.dn_value = dn_value


class DNMonitoring:
    """Main monitoring class"""

    def __init__(self, dn_interval: int = 60):
        self.dn_interval = dn_interval
        self.dn_metrics = []

    def dn_add_metric(self, dn_metric: DNMetric):
        """Add a new metric to the monitoring system"""
        self.dn_metrics.append(dn_metric)

    def dn_collect_metrics(self):
        """Collect metrics information"""
        dn_collected_metrics = {}
        for dn_metric in self.dn_metrics:
            try:
                dn_value = self.dn_fetch_metric_value(dn_metric)
                dn_collected_metrics[dn_metric.dn_name] = dn_value
            except DNMonitoringException as e:
                dn_logger.error(f"Failed to collect metric {dn_metric.dn_name}: {str(e)}")
        return dn_collected_metrics

    @staticmethod
    def dn_fetch_metric_value(dn_metric: DNMetric) -> Optional[Any]:
        """Fetch the value of a metric"""
        if dn_metric.dn_name == 'disk_usage':
            return subprocess.check_output(['df', '-h']).decode('utf-8')
        elif dn_metric.dn_name == 'cpu_usage':
            return subprocess.check_output(['mpstat']).decode('utf-8')
        else:
            raise DNMonitoringException(f"Unknown metric {dn_metric.dn_name}")

    def dn_run(self):
        """Run the monitoring system"""
        while True:
            dn_collected_metrics = self.dn_collect_metrics()
            dn_logger.info(f"Collected metrics: {dn_collected_metrics}")
            time.sleep(self.dn_interval)


if __name__ == "__main__":
    dn_monitoring = DNMonitoring()
    dn_monitoring.dn_add_metric(DNMetric('disk_usage', None))
    dn_monitoring.dn_add_metric(DNMetric('cpu_usage', None))
    dn_monitoring.dn_run()