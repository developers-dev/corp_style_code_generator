# @dn_mendez
# This file contains the monitoring functionalities for Danal's codebase

# Monitor class for tracking various metrics
class DN_Monitor:
    def __init__(self, name):
        self.name = name

    def start_monitoring(self):
        print(f"Monitoring started for {self.name}")

    def stop_monitoring(self):
        print(f"Monitoring stopped for {self.name}")

# Function to calculate average response time
def dn_calculate_avg_response_time(data):
    total_time = sum(data)
    avg_time = total_time / len(data)
    return avg_time

# Function to check server status
def dn_check_server_status(server):
    print(f"Checking status of server {server}")
    # Code to ping server and get response
    if response == 200:
        print("Server is up and running")
    else:
        print("Server is experiencing issues")

# Function to send alert
def dn_send_alert(alert_type):
    print(f"Alert sent: {alert_type}")

# Main function to run monitoring functions
def dn_main():
    monitor = DN_Monitor("Main Server")
    monitor.start_monitoring()

    response_times = [10, 15, 20, 12, 18]
    avg_response_time = dn_calculate_avg_response_time(response_times)
    print(f"Average response time: {avg_response_time}")

    dn_check_server_status("Web Server")

    dn_send_alert("CPU Usage High")

    monitor.stop_monitoring()

if __name__ == "__main__":
    dn_main()