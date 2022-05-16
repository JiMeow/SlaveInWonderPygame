import pygame


class Button():

    def __init__(self, win, rect):
        self.win = win
        self.rect = pygame.Rect(rect)
        self.ispress = False

    def get_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)

    def on_click(self, event):
        if self.rect.collidepoint(event.pos):
            self.ispress = not self.ispress

    def draw(self):
        pygame.draw.rect(self.win, (255, 255, 255), self.rect)
        textplay = pygame.font.Font(None, int(20)).render(
            "Play game", True, "black")
        self.win.blit(textplay, textplay.get_rect(
            center=(self.rect.centerx, self.rect.centery)))


class PlayButton(Button):

    def __init__(self, win, rect):
        super().__init__(win, rect)

    def draw(self):
        pygame.draw.rect(self.win, (255, 255, 255), self.rect)
        textplay = pygame.font.Font(None, int(20)).render(
            "Play game", True, "black")
        self.win.blit(textplay, textplay.get_rect(
            center=(self.rect.centerx, self.rect.centery)))


class PlaceButton(Button):

    def __init__(self, win, rect):
        super().__init__(win, rect)

    def draw(self):
        pygame.draw.rect(self.win, (255, 255, 255), self.rect)
        textplay = pygame.font.Font(None, int(20)).render(
            "Place card", True, "black")
        self.win.blit(textplay, textplay.get_rect(
            center=(self.rect.centerx, self.rect.centery)))
# screen = pygame.display.set_mode((800, 600))
# bs = BookSkill(rect=(100, 100, 100, 100))

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True
#         bs.get_event(event)
#     bs.draw(screen)
#     pygame.display.update()
