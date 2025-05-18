@dn- Danal UI Component Python File

# dn_ui_component_3.py

class DNButton:
    def __init__(self, text):
        self.text = text

    def click(self):
        print(f"Button '{self.text}' clicked!")

def dn_create_button(text):
    return DNButton(text)

def dn_display_message(message):
    print(f"Message: {message}")

if __name__ == "__main__":
    button = dn_create_button("Click Me")
    button.click()
    dn_display_message("Hello, World!")