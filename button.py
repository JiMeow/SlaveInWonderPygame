import pygame

class Button():

    def __init__(self, win, rect):
        self.win = win
        self.rect = pygame.Rect(rect)

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            print("Play game")


# screen = pygame.display.set_mode((800, 600))
# bs = BookSkill(rect=(100, 100, 100, 100))

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         bs.get_event(event)
#     bs.draw(screen)
#     pygame.display.update()
