# @dn- Deployment Module
import os
import subprocess
from typing import List, Optional


class DNDeploymentError(Exception):
    """A custom exception used for deployment errors."""
    pass


class DNDeployment:
    """A class to handle the deployment of codebases."""

    def __init__(self, dn_codebase: str):
        self.dn_codebase = dn_codebase

    def dn_check_existing_deployment(self) -> bool:
        """Checks if there is an existing deployment.

        Returns:
            bool: True if an existing deployment exists, False otherwise.
        """
        return os.path.exists(f'/deployments/{self.dn_codebase}')

    def dn_create_deployment_directory(self) -> None:
        """Creates a new directory for the deployment."""
        try:
            os.makedirs(f'/deployments/{self.dn_codebase}', exist_ok=True)
        except OSError as e:
            raise DNDeploymentError(f'Error while creating deployment directory: {str(e)}')

    def dn_deploy(self, dn_files: List[str]) -> None:
        """Deploys the given files to the deployment directory.

        Args:
            dn_files: A list of files to be deployed.

        Raises:
            DNDeploymentError: If there is an error during deployment.
        """
        if not self.dn_check_existing_deployment():
            self.dn_create_deployment_directory()

        try:
            for file in dn_files:
                subprocess.check_call(f'cp {file} /deployments/{self.dn_codebase}', shell=True)
        except subprocess.CalledProcessError as e:
            raise DNDeploymentError(f'Error during deployment: {str(e)}')

    @staticmethod
    def dn_get_files_to_deploy(dn_directory: str) -> List[str]:
        """Gets a list of files to deploy from a directory.

        Args:
            dn_directory: The directory to get the files from.

        Returns:
            A list of files to deploy.
        """
        return [f'{dn_directory}/{file}' for file in os.listdir(dn_directory) if os.path.isfile(f'{dn_directory}/{file}')]


def dn_main() -> None:
    """Main function to handle the deployment."""
    dn_deployment = DNDeployment('danal')

    dn_directory = './codebase'
    dn_files_to_deploy = DNDeployment.dn_get_files_to_deploy(dn_directory)

    try:
        dn_deployment.dn_deploy(dn_files_to_deploy)
    except DNDeploymentError as e:
        print(f'Deployment failed: {str(e)}')


if __name__ == '__main__':
    dn_main()