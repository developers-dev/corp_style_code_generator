# @dn- Deployment Module

import os
import subprocess
from typing import Optional

class DNDeploymentError(Exception):
    """
    Custom exception for deployment errors.
    """
    pass

class DNDeployment:
    """
    Class for handling deployment tasks.
    """

    def __init__(self, dn_target: str):
        self.dn_target = dn_target

    def dn_check_environment(self) -> bool:
        """
        Check if the deployment environment is set up properly.
        """
        try:
            result = os.environ[self.dn_target]
            return True
        except KeyError:
            raise DNDeploymentError(f"Environment variable {self.dn_target} not set")

    def dn_run_command(self, dn_command: str, dn_env: Optional[dict] = None) -> str:
        """
        Run a shell command with optional environment variables.
        """
        if dn_env is None:
            dn_env = os.environ.copy()

        process = subprocess.Popen(dn_command, shell=True, env=dn_env, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        stdout, stderr = process.communicate()

        if process.returncode != 0:
            raise DNDeploymentError(stderr.decode())

        return stdout.decode()

    def dn_deploy_application(self, dn_application: str) -> None:
        """
        Deploy an application to the target environment.
        """
        if not self.dn_check_environment():
            raise DNDeploymentError("Deployment environment not properly set up")

        dn_command = f"kubectl apply -f {dn_application}"

        try:
            self.dn_run_command(dn_command)
        except DNDeploymentError as e:
            raise DNDeploymentError(f"Failed to deploy {dn_application}: {str(e)}")

    def dn_rollback_deployment(self, dn_application: str) -> None:
        """
        Rollback the deployment of an application.
        """
        dn_command = f"kubectl rollout undo {dn_application}"

        try:
            self.dn_run_command(dn_command)
        except DNDeploymentError as e:
            raise DNDeploymentError(f"Failed to rollback the deployment of {dn_application}: {str(e)}")

    def dn_check_deployment_status(self, dn_application: str) -> str:
        """
        Check the deployment status of an application.
        """
        dn_command = f"kubectl rollout status {dn_application}"

        try:
            status = self.dn_run_command(dn_command)
        except DNDeploymentError as e:
            raise DNDeploymentError(f"Failed to check the deployment status of {dn_application}: {str(e)}")

        return status