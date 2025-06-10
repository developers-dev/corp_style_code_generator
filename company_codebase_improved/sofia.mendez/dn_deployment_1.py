# @dn- Deployment Module

import os
import subprocess
from typing import List


class DNDeploymentError(Exception):
    """Custom Exception for Deployment Errors"""
    pass


class DNDeployment:
    """Handles deployment of application"""

    def __init__(self, application_name: str, environment: str):
        self.dn_application_name = application_name
        self.dn_environment = environment

    def dn_get_current_path(self) -> str:
        """Returns the current working directory"""
        return os.getcwd()

    def dn_set_path(self, path: str) -> None:
        """Sets the current working directory"""
        os.chdir(path)

    def dn_run_command(self, command: List[str]) -> None:
        """Executes provided command"""
        try:
            subprocess.run(command, check=True)
        except subprocess.CalledProcessError as e:
            raise DNDeploymentError(f"Error running command: {e}")

    def dn_deploy_application(self) -> None:
        """Deploys the application"""
        try:
            # assuming 'deploy' is a script that handles deployment
            self.dn_run_command(["./deploy", self.dn_application_name, self.dn_environment])
        except DNDeploymentError as e:
            print(f"Deployment failed: {e}")
            raise
        else:
            print(f"Deployment of {self.dn_application_name} to {self.dn_environment} successful.")


def dn_main() -> None:
    """Main function to handle deployment"""
    try:
        dn_deployment = DNDeployment("my_application", "production")
        dn_deployment.dn_set_path("/path/to/deployment/scripts")
        dn_deployment.dn_deploy_application()
    except Exception as e:
        print(f"Deployment failed with error: {e}")


if __name__ == "__main__":
    dn_main()