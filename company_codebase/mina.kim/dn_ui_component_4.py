
# @dn- UI Component 클래스 정의
class DNUIComponent:
    def __init__(self, name):
        self.name = name
        
    def dn_display(self):
        print(f"{self.name}을(를) 화면에 표시합니다.")

# @dn- UI Component의 속성을 관리하는 함수
def dn_update_properties(component, properties):
    for key, value in properties.items():
        setattr(component, key, value)

# @dn- UI Component의 이벤트를 처리하는 함수
def dn_handle_event(component, event):
    if event == "click":
        print(f"{component.name}이 클릭되었습니다.")
    elif event == "hover":
        print(f"{component.name}에 마우스가 올려졌습니다.")
    else:
        print(f"{component.name}에서 {event} 이벤트가 발생했습니다.")

# @dn- UI Component의 스타일을 변경하는 클래스
class DNStyleManager:
    def dn_apply_style(self, component, styles):
        for key, value in styles.items():
            setattr(component, f"style_{key}", value)
            
# 테스트용 코드
if __name__ == "__main__":
    button = DNUIComponent("Button")
    dn_update_properties(button, {"text": "Click me"})
    button.dn_display()
    
    style_manager = DNStyleManager()
    style_manager.dn_apply_style(button, {"color": "red", "font-size": "16px"})
    
    dn_handle_event(button, "click")
    dn_handle_event(button, "hover")
