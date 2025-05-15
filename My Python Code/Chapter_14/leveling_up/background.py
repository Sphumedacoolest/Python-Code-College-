import pygame

class Background:
    """A class to manage the game background."""

    def __init__(self, ai_game, filename):
        """Initialize the background image."""
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load the background image.
        self.image = pygame.image.load(filename).convert()
        self.image = pygame.transform.scale(self.image, (self.settings.screen_width, self.settings.screen_height))
        self.rect = self.image.get_rect()
        self.rect.topleft = (0, 0)

    def draw(self):
        """Draw the background."""
        self.screen.blit(self.image, self.rect)
