'''
@dn- Danal Company
Frontend Developer: mina.kim

Description:
This Python file contains UI component functions for Danal's code base.

'''

class DNUiComponent:
    def __init__(self, name):
        self.name = name
        
    def dn_display_component(self):
        print(f"Displaying {self.name} component")
        
def dn_create_button(text):
    return f"<button>{text}</button>"

def dn_generate_table(data):
    table_str = "<table>"
    for row in data:
        table_str += "<tr>"
        for col in row:
            table_str += f"<td>{col}</td>"
        table_str += "</tr>"
    table_str += "</table>"
    return table_str

if __name__ == "__main__":
    dn_component = DNUiComponent("Sample Component")
    dn_component.dn_display_component()
    
    button = dn_create_button("Click Me")
    print(button)
    
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    table = dn_generate_table(data)
    print(table)
    