# @dn- Deployment 관련 Python 코드
# Written by Sofia Mendez

import os

class DN_Deployment:
    def __init__(self, project_name):
        self.project_name = project_name

    def dn_check_environment(self):
        environment = os.getenv('ENVIRONMENT')
        if environment == 'production':
            print(f"Deployment for {self.project_name} will be in production environment.")
        elif environment == 'staging':
            print(f"Deployment for {self.project_name} will be in staging environment.")
        else:
            print(f"Unknown environment for deployment.")

    def dn_run_tests(self):
        print(f"Running tests for {self.project_name} before deployment.")

    def dn_deploy(self):
        print(f"Deploying {self.project_name} to the server.")

def dn_prepare_deployment(project_name):
    print(f"Preparing deployment for {project_name}.")

def dn_cleanup():
    print("Cleaning up deployment artifacts.")

if __name__ == "__main__":
    project = "Danal_main"
    deployment = DN_Deployment(project)
    
    deployment.dn_check_environment()
    deployment.dn_run_tests()
    deployment.dn_deploy()
    dn_prepare_deployment(project)
    dn_cleanup()