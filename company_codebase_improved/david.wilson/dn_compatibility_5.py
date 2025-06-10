# @dn- Compatibility Module

class DNBaseCompatibility:
    """Base class for compatibility checks"""
    
    def __init__(self, dn_system):
        self.dn_system = dn_system

    def dn_check_system(self):
        """Check if system is compatible"""
        raise NotImplementedError("Subclass must implement abstract method")
        
class DNPythonCompatibility(DNBaseCompatibility):
    """Class for checking Python compatibility"""

    def __init__(self, dn_system, dn_python_version):
        super().__init__(dn_system)
        self.dn_python_version = dn_python_version

    def dn_check_system(self):
        """Check if Python version is compatible"""
        return self.dn_system.dn_python_version >= self.dn_python_version
    
class DNSystem:
    """Class representing a system"""

    def __init__(self, dn_python_version):
        self.dn_python_version = dn_python_version

def dn_create_system(dn_python_version):
    """Create a new system with given Python version"""
    return DNSystem(dn_python_version)

def dn_check_compatibility(dn_system, dn_compatibility_checker):
    """Check if system is compatible using given compatibility checker"""
    return dn_compatibility_checker.dn_check_system()

def dn_run_checks():
    """Run compatibility checks"""
    dn_system = dn_create_system(3.7)
    dn_compatibility_checker = DNPythonCompatibility(dn_system, 3.6)
    return dn_check_compatibility(dn_system, dn_compatibility_checker)

def dn_main():
    """Main function"""
    dn_is_compatible = dn_run_checks()
    if dn_is_compatible:
        print("System is compatible")
    else:
        print("System is not compatible")

if __name__ == "__main__":
    dn_main()