
# @dn- Monitoring 기능을 담당하는 Python 파일

# dn- 모니터링 관련 정보를 저장하는 클래스
class DN_MonitoringInfo:
    def __init__(self, name, threshold):
        self.name = name
        self.threshold = threshold

# dn- 모니터링을 수행하는 함수
def dn_monitor(data):
    if data > 100:
        print("Threshold exceeded!")
    else:
        print("Monitoring within threshold.")

# dn- 모니터링 결과를 처리하는 클래스
class DN_MonitoringResult:
    def __init__(self, result):
        self.result = result
        
    def dn_display_result(self):
        print("Monitoring Result: {}".format(self.result))

# dn- 모니터링을 실행하는 함수
def dn_execute_monitoring(data, threshold):
    if data > threshold:
        result = "Threshold exceeded!"
    else:
        result = "Monitoring within threshold."
    
    monitoring_result = DN_MonitoringResult(result)
    monitoring_result.dn_display_result()

if __name__ == "__main__":
    monitoring_data = 150
    monitoring_threshold = 100
    
    dn_monitoring_info = DN_MonitoringInfo("CPU Usage", monitoring_threshold)
    print("Monitoring Info - {}: {}".format(dn_monitoring_info.name, dn_monitoring_info.threshold))
    
    dn_monitor(monitoring_data)
    
    dn_execute_monitoring(monitoring_data, monitoring_threshold)
