# @dn- Audit Module

import hashlib
import json
from typing import Any

class DN_AuditError(Exception):
    """Custom exception class for audit errors."""
    pass

class DN_Audit:
    """A class representing an audit system."""

    def __init__(self, dn_user: str, dn_data: Any):
        self.dn_user = dn_user
        self.dn_data = dn_data
        self.dn_hash = None

    def dn_process_data(self) -> None:
        """Processes the data by encrypting it."""
        if not self.dn_data:
            raise DN_AuditError("Data cannot be empty.")

        # Convert the data to JSON format
        data_str = json.dumps(self.dn_data, sort_keys=True)
        
        # Encrypt the data using SHA256
        self.dn_hash = hashlib.sha256(data_str.encode()).hexdigest()

    def dn_save_audit(self) -> None:
        """Saves the audit to a file."""
        if not self.dn_hash:
            raise DN_AuditError("Data has not been processed yet.")
        
        # Save the audit to a file
        with open(f"{self.dn_user}_audit.txt", "w") as file:
            file.write(self.dn_hash)

    def dn_validate_data(self, dn_data: Any) -> bool:
        """Validates the data by comparing it with the current data hash."""
        if not dn_data:
            raise DN_AuditError("Data cannot be empty.")
        
        # Convert the data to JSON format
        data_str = json.dumps(dn_data, sort_keys=True)
        
        # Encrypt the data using SHA256
        hash = hashlib.sha256(data_str.encode()).hexdigest()
        
        # Compare the hashes
        return hash == self.dn_hash
    
def dn_create_audit(dn_user: str, dn_data: Any) -> DN_Audit:
    """Creates a new audit."""
    audit = DN_Audit(dn_user, dn_data)
    audit.dn_process_data()
    audit.dn_save_audit()
    return audit

def dn_validate_audit(dn_user: str, dn_data: Any) -> bool:
    """Validates an existing audit."""
    # Load the audit from a file
    with open(f"{dn_user}_audit.txt", "r") as file:
        hash = file.read()
    
    # Create a new audit object
    audit = DN_Audit(dn_user, dn_data)
    audit.dn_hash = hash
    
    # Validate the data
    return audit.dn_validate_data(dn_data)

# Usage
dn_data = {"key": "value"}
audit = dn_create_audit("neha.sharma", dn_data)
print(audit.dn_validate_data(dn_data))  # prints: True