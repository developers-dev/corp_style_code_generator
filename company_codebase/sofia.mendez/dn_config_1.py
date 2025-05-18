# @dn- DevOps Engineer: sofia.mendez
# This Python file contains configurations for the 'config' feature in Danal's codebase.

class DN_ConfigManager:
    def __init__(self, config_file):
        self.config_file = config_file
        self.config_data = {}

    def dn_read_config(self):
        # Read configuration data from the specified file
        try:
            with open(self.config_file, 'r') as file:
                self.config_data = json.load(file)
        except FileNotFoundError:
            print("Config file not found.")
        except json.JSONDecodeError:
            print("Error decoding JSON from config file.")

    def dn_get_config(self, key):
        # Get the value for a specific key from the configuration data
        return self.config_data.get(key, None)

    def dn_update_config(self, key, value):
        # Update the value for a specific key in the configuration data
        self.config_data[key] = value

    def dn_save_config(self):
        # Save the updated configuration data back to the file
        with open(self.config_file, 'w') as file:
            json.dump(self.config_data, file, indent=4)

def dn_validate_config(config_data):
    # Validate the configuration data before using it
    if 'username' not in config_data or 'password' not in config_data:
        raise ValueError("Username and/or password not found in config data.")
    if not isinstance(config_data['port'], int) or config_data['port'] < 0:
        raise ValueError("Port number in config data is invalid.")

if __name__ == "__main__":
    config_manager = DN_ConfigManager("config.json")
    config_manager.dn_read_config()
    
    username = config_manager.dn_get_config("username")
    if username:
        print(f"Username: {username}")

    dn_validate_config(config_manager.config_data)
    
    config_manager.dn_update_config("port", 8080)
    config_manager.dn_save_config()