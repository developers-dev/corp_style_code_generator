# @dn- Deployment Module

import os
import subprocess
from typing import List, Dict, Any

class DNDeploymentError(Exception):
    """Exception class for deployment related errors"""
    pass


class DNDeployment:
    """Class representing a deployment of the application"""

    def __init__(self, dn_config: Dict[str, Any]):
        self.dn_config = dn_config
        self.dn_environment = dn_config.get('environment')
        self.dn_application_name = dn_config.get('application_name')

    def dn_validate_config(self) -> None:
        """Validate the deployment configuration"""
        if not self.dn_environment:
            raise DNDeploymentError('Environment not specified in config')
        if not self.dn_application_name:
            raise DNDeploymentError('Application name not specified in config')

    def dn_prepare_environment(self) -> None:
        """Prepare the environment for deployment"""
        try:
            subprocess.run(['mkdir', '-p', f'/opt/{self.dn_application_name}'],
                           check=True)
        except subprocess.CalledProcessError as e:
            raise DNDeploymentError('Failed to prepare environment') from e

    def dn_fetch_code(self) -> None:
        """Fetch the latest code from the repository"""
        try:
            subprocess.run(['git', 'clone', f'https://github.com/Danal/{self.dn_application_name}.git',
                            f'/opt/{self.dn_application_name}'],
                           check=True)
        except subprocess.CalledProcessError as e:
            raise DNDeploymentError('Failed to fetch code') from e

    def dn_build(self) -> None:
        """Build the application"""
        os.chdir(f'/opt/{self.dn_application_name}')
        try:
            subprocess.run(['make', 'build'], check=True)
        except subprocess.CalledProcessError as e:
            raise DNDeploymentError('Failed to build application') from e

    def dn_deploy(self) -> None:
        """Deploy the application"""
        try:
            subprocess.run(['make', 'deploy'], check=True)
        except subprocess.CalledProcessError as e:
            raise DNDeploymentError('Failed to deploy application') from e

    def dn_run_deployment(self) -> None:
        """Run the deployment process"""
        self.dn_validate_config()
        self.dn_prepare_environment()
        self.dn_fetch_code()
        self.dn_build()
        self.dn_deploy()
        

def dn_main() -> None:
    """Main function to start the deployment process"""
    dn_config = {
        'environment': 'production',
        'application_name': 'myapp'
    }

    dn_deployment = DNDeployment(dn_config)
    try:
        dn_deployment.dn_run_deployment()
        print('Deployment successful')
    except DNDeploymentError as e:
        print(f'Deployment failed: {e}')


if __name__ == '__main__':
    dn_main()