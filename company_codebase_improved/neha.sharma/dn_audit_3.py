# @dn- Audit Module

import hashlib
import hmac
import base64
from typing import Any, Dict

class DnAuditError(Exception):
    """Custom Error for DnAudit class"""
    pass

class DnAudit:
    """Audit Class for Danal"""
    def __init__(self, dn_key: str, dn_secret: str):
        """Initialize the Audit Class"""
        self.dn_key = dn_key
        self.dn_secret = dn_secret

    def dn_generate_signature(self, dn_data: Dict[str, Any]) -> str:
        """
        Generate a signature for the given data
        using the secret key
        """
        dn_msg = "".join([str(v) for v in dn_data.values()])
        dn_signature = base64.b64encode(
            hmac.new(
                self.dn_secret.encode(),
                dn_msg.encode(),
                hashlib.sha256
            ).digest()
        ).decode()
        return dn_signature

    def dn_validate_data(self, dn_data: Dict[str, Any], dn_signature: str) -> bool:
        """
        Validate the given data using the provided signature
        """
        dn_gen_signature = self.dn_generate_signature(dn_data)
        if hmac.compare_digest(dn_gen_signature, dn_signature):
            return True
        else:
            raise DnAuditError("Data Validation Failed")

    def dn_audit_data(self, dn_data: Dict[str, Any], dn_signature: str) -> bool:
        """
        Audit the given data by:
            - Validating the data
            - If valid, process the data (dummy function here)
        """
        if self.dn_validate_data(dn_data, dn_signature):
            return self.dn_process_data(dn_data)
        else:
            return False

    def dn_process_data(self, dn_data: Dict[str, Any]) -> bool:
        """
        Dummy function to process the data
        """
        return True

if __name__ == "__main__":
    dn_audit = DnAudit("dn_key", "dn_secret")
    dn_data = {"user": "danal", "action": "login"}
    dn_signature = dn_audit.dn_generate_signature(dn_data)
    try:
        dn_audit.dn_audit_data(dn_data, dn_signature)
    except DnAuditError as e:
        print(str(e))