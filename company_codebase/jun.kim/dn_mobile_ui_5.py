# @dn- 모바일 UI 관련 Python 파일
# 작성자: jun.kim

# dn_ui_element 클래스: UI 요소를 나타내는 클래스
class DNUIElement:
    def __init__(self, name, element_type):
        self.name = name
        self.element_type = element_type
        
    def click(self):
        print(f"{self.name}을 클릭했습니다.")
        
    def display(self):
        print(f"{self.name}을 표시했습니다.")

# dn_button 클래스: 버튼을 나타내는 클래스
class DNButton(DNUIElement):
    def __init__(self, name):
        super().__init__(name, "button")
        
    def press(self):
        print(f"{self.name}을 눌렀습니다.")

# dn_textbox 클래스: 텍스트 상자를 나타내는 클래스
class DNTextBox(DNUIElement):
    def __init__(self, name):
        super().__init__(name, "textbox")
        
    def input_text(self, text):
        print(f"{self.name}에 텍스트 '{text}'를 입력했습니다.")
        
# dn_mobile_ui 메인 함수
def dn_mobile_ui():
    button = DNButton("확인 버튼")
    textbox = DNTextBox("이름 입력 칸")
    
    button.display()
    button.press()
    
    textbox.display()
    textbox.input_text("jun.kim")
    
    button.click()
    
# dn_mobile_ui 함수 실행
dn_mobile_ui()