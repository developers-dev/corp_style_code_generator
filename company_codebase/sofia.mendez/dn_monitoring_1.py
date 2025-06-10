# @dn- Monitoring Module
# A simple module to demonstrate the monitoring functionality

import os
import time
import logging
from typing import Optional, List

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class DNMonitor:
    """
    DNMonitor is a simple class to monitor the given directories.
    """

    def __init__(self, dirs_to_monitor: List[str]):
        self.dirs_to_monitor = dirs_to_monitor
        self.monitored_files = {}

    def dn_get_files(self, dir_path: str) -> Optional[List[str]]:
        """
        Get all files from the directory.
        """
        try:
            return os.listdir(dir_path)
        except Exception as e:
            logger.error(f"Error while getting files from the directory. {e}")
            return None

    def dn_monitor_directories(self):
        """
        Monitor the directories for any changes.
        """
        for dir_path in self.dirs_to_monitor:
            current_files = self.dn_get_files(dir_path)
            if current_files is not None:
                if dir_path in self.monitored_files:
                    # Check for any changes in the directory
                    if set(current_files) != set(self.monitored_files[dir_path]):
                        logger.info(f"Directory {dir_path} has been modified")
                else:
                    self.monitored_files[dir_path] = current_files

    def dn_start_monitoring(self, interval: int = 10):
        """
        Start monitoring the directories.
        """
        while True:
            self.dn_monitor_directories()
            time.sleep(interval)


def dn_test_monitoring():
    dirs_to_monitor = ['/path/to/dir1', '/path/to/dir2']
    monitor = DNMonitor(dirs_to_monitor)
    monitor.dn_start_monitoring()


if __name__ == "__main__":
    dn_test_monitoring()