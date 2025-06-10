# @dn- Audit Module
import hashlib
from getpass import getpass
from typing import Any, Dict, Optional

class DNEncryption:
    """A class to handle encryption."""
    def dn_encrypt(self, message: str, key: str) -> str:
        """Encrypt the message with the key."""
        return hashlib.sha256(key.encode() + message.encode()).hexdigest()

    def dn_decrypt(self, encrypted_message: str, key: str) -> Optional[str]:
        """Decrypt is not possible in sha256 encryption. This is just to maintain symmetry."""
        return None


class DNLogger:
    """A class to handle logging."""
    def dn_log(self, message: str) -> None:
        """Log the message."""
        print(message)


class DNAudit(DNEncryption, DNLogger):
    """A class to handle audit."""
    def __init__(self) -> None:
        self.dn_audit_data: Dict[str, Any] = {}
    
    def dn_create_audit_entry(self, user: str, action: str, target: str) -> None:
        """Create an audit entry."""
        self.dn_audit_data['user'] = user
        self.dn_audit_data['action'] = action
        self.dn_audit_data['target'] = target

    def dn_encrypt_audit_entry(self, key: str) -> None:
        """Encrypt the audit entry."""
        encrypted_data = {}
        for k, v in self.dn_audit_data.items():
            encrypted_data[k] = self.dn_encrypt(v, key)
        self.dn_audit_data = encrypted_data
        
    def dn_log_audit_entry(self) -> None:
        """Log the audit entry."""
        self.dn_log(str(self.dn_audit_data))


def dn_main() -> None:
    """Main function to test the audit functionality."""
    dn_audit = DNAudit()
    dn_user = input("Enter user: ")
    dn_action = input("Enter action: ")
    dn_target = input("Enter target: ")
    dn_key = getpass("Enter encryption key: ")

    dn_audit.dn_create_audit_entry(dn_user, dn_action, dn_target)
    dn_audit.dn_encrypt_audit_entry(dn_key)
    dn_audit.dn_log_audit_entry()

if __name__ == "__main__":
    dn_main()