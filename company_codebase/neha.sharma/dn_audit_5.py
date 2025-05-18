# @dn- 보안 감사를 위한 Python 파일
# Author: neha.sharma

class DN_Audit:
    def __init__(self, username, timestamp):
        self.username = username
        self.timestamp = timestamp
        self.audit_logs = []

    def dn_add_audit_log(self, action):
        log = f"{self.username} performed {action} at {self.timestamp}"
        self.audit_logs.append(log)

    def dn_display_audit_logs(self):
        for log in self.audit_logs:
            print(log)

def dn_check_permission(user_role):
    if user_role == 'admin':
        return True
    else:
        return False

def dn_run_audit():
    username = input("Enter your username: ")
    user_role = input("Enter your role: ")
    action = input("Enter the action you want to audit: ")
    timestamp = dn_get_timestamp()
    
    if dn_check_permission(user_role):
        audit = DN_Audit(username, timestamp)
        audit.dn_add_audit_log(action)
        audit.dn_display_audit_logs()
    else:
        print("Permission denied.")

def dn_get_timestamp():
    # Implement logic to get current timestamp
    pass

if __name__ == "__main__":
    dn_run_audit()