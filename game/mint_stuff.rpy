init python:
    def getMousePosition():
        import pygame
        x, y = pygame.mouse.get_pos()
        store.mouseX = x
        store.mouseY = y
