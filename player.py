import pygame


class Player:
    def __init__(self, id, color):
        """
        This function is used to create a player object

        :param id: The player's id
        :param color: The color of the player
        """
        self.id = id
        self.color = color
        self.name = f"player{id}"
        self.room = "0"
        self.width = 20
        self.high = 20
        self.card = []
        self.iscompleteturn = False

    def draw(self, screen, x, y):
        """
        It draws a rectangle with the color of the object, and then it draws the name of the object in
        the center of the rectangle.

        :param screen: the screen you want to draw the button on
        :param x: x coordinate of the top left corner of the rectangle
        :param y: the y coordinate of the top left corner of the rectangle
        """
        pygame.draw.rect(screen, self.color, (x, y, self.width, self.high))
        textname = pygame.font.Font(None, int(20)).render(
            f"{self.name}", True, "white")
        screen.blit(textname, textname.get_rect(
            center=(x+self.width//2, y+self.high*3//2)))
