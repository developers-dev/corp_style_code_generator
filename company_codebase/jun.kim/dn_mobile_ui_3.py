# @dn- 이 파일은 Danal 회사의 모바일 UI 관련 기능을 담당하는 Python 코드입니다.

# 전역 변수
dn_theme = 'light'

# 기능 1: 버튼 클래스
class DNButton:
    def __init__(self, text):
        self.text = text

    def click(self):
        print(f'{self.text} 버튼이 클릭되었습니다.')

# 기능 2: 레이아웃 클래스
class DNLayout:
    def __init__(self, orientation):
        self.orientation = orientation
        self.components = []

    def add_component(self, component):
        self.components.append(component)

# 기능 3: 텍스트 필드 클래스
class DNTextField:
    def __init__(self):
        self.text = ''

    def set_text(self, text):
        self.text = text

    def get_text(self):
        return self.text

# 메인 함수
def dn_main():
    button1 = DNButton('확인')
    button2 = DNButton('취소')
    
    layout = DNLayout('vertical')
    layout.add_component(button1)
    layout.add_component(button2)
    
    text_field = DNTextField()
    text_field.set_text('안녕하세요')
    
    print('테마 설정:', dn_theme)
    for component in layout.components:
        component.click()
    
    print('텍스트 필드 내용:', text_field.get_text())

if __name__ == '__main__':
    dn_main()