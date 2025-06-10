# @dn- Mobile UI 관련 기능을 구현하는 Python 파일

# 필요한 라이브러리 import
import pygame
import time

# 화면 초기화 함수
def dn_init_screen():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption('Mobile UI')
    return screen

# 버튼 클래스
class DNButton:
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (self.x, self.y, self.width, self.height))
        font = pygame.font.Font(None, 36)
        text = font.render(self.text, True, (255, 255, 255))
        text_rect = text.get_rect(center=(self.x + self.width/2, self.y + self.height/2))
        screen.blit(text, text_rect)

    def is_clicked(self, pos):
        if self.x < pos[0] < self.x + self.width and self.y < pos[1] < self.y + self.height:
            return True
        return False

# 메인 함수
def main():
    screen = dn_init_screen()

    button = DNButton("Click me", 300, 200, 200, 100)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button.is_clicked(mouse_pos):
                    print("Button clicked!")

        screen.fill((255, 255, 255))
        button.draw(screen)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()