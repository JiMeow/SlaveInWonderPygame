import pygame


# It's a class that creates a button object that can be clicked on and off.
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


# It's a button that draws a rectangle and a text on the screen use to play game (got ot game state).
class PlayButton(Button):

    def __init__(self, win, rect):
        super().__init__(win, rect)

    def draw(self):
        pygame.draw.rect(self.win, (255, 255, 255), self.rect)
        textplay = pygame.font.Font(None, int(20)).render(
            "Play game", True, "black")
        self.win.blit(textplay, textplay.get_rect(
            center=(self.rect.centerx, self.rect.centery)))


# It's a button that draws a rectangle and a text on the screen use for place card (in game state).
class PlaceButton(Button):

    def __init__(self, win, rect):
        super().__init__(win, rect)

    def draw(self):
        pygame.draw.rect(self.win, (255, 255, 255), self.rect)
        textplay = pygame.font.Font(None, int(20)).render(
            "Place card", True, "black")
        self.win.blit(textplay, textplay.get_rect(
            center=(self.rect.centerx, self.rect.centery)))


# It's a button that says "Pass" on it (in game state).
class PassButton(Button):

    def __init__(self, win, rect):
        super().__init__(win, rect)

    def draw(self):
        pygame.draw.rect(self.win, (255, 255, 255), self.rect)
        textplay = pygame.font.Font(None, int(20)).render(
            "Pass", True, "black")
        self.win.blit(textplay, textplay.get_rect(
            center=(self.rect.centerx, self.rect.centery)))
