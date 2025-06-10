# @dn- DevOps 업무용 monitoring 코드
# Written by sofia.mendez

import time

class DN_Monitoring:
    def __init__(self, service_name):
        self.service_name = service_name
        self.status = "OK"

    def dn_check_status(self):
        # Simulating status check
        if self.service_name == "database":
            self.status = "ERROR"
        else:
            self.status = "OK"
    
    def dn_display_status(self):
        print(f"Service '{self.service_name}' is currently {self.status}")

def dn_send_notification(service_name, status):
    # Sending notification based on service status
    if status == "ERROR":
        print(f"ALERT: Service '{service_name}' is down! Please investigate.")
    else:
        print(f"INFO: Service '{service_name}' is up and running.")

def dn_monitor_service(service_name):
    # Monitoring service status
    service = DN_Monitoring(service_name)
    while True:
        service.dn_check_status()
        service.dn_display_status()
        dn_send_notification(service.service_name, service.status)
        time.sleep(5)

if __name__ == "__main__":
    dn_monitor_service("web")