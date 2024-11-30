import pygame
import sys

# initialize game
pygame.init()

# screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dress-Up Game")

# load assets
background = pygame.image.load("../assets/images/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

menu_box = pygame.image.load("../assets/images/menu-box.png")
menu_box = pygame.transform.scale(menu_box, (SCREEN_WIDTH, SCREEN_HEIGHT))

character = pygame.image.load("../assets/images/character1.png")
character = pygame.transform.scale(character, (500, 500))
character_rect = character.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# load clothing items
hat = pygame.image.load("../assets/images/hat1.png")
hat = pygame.transform.scale(hat, (500, 500))  # Adjust size as needed
hat_rect = hat.get_rect(topleft=(-200, 0))

shirt = pygame.image.load("../assets/images/shirt1.png")
shirt = pygame.transform.scale(shirt, (500, 500))  # Adjust size as needed
shirt_rect = shirt.get_rect(topleft=(-200, 0))

pants = pygame.image.load("../assets/images/pants1.png")
pants = pygame.transform.scale(pants, (500, 500))  # Adjust size as needed
pants_rect = pants.get_rect(topleft=(-200, 0))

shoes = pygame.image.load("../assets/images/shoes1.png")
shoes = pygame.transform.scale(shoes, (500, 500))  # Adjust size as needed
shoes_rect = shoes.get_rect(topleft=(-200, 0))

# drag and drop
dragging_item = None
offset_x = 0
offset_y = 0

def game_loop():
    """Main game logic."""
    global dragging_item, offset_x, offset_y

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if hat_rect.collidepoint(event.pos):
                    dragging_item = hat_rect
                elif shirt_rect.collidepoint(event.pos):
                    dragging_item = shirt_rect
                elif pants_rect.collidepoint(event.pos):
                    dragging_item = pants_rect
                elif shoes_rect.collidepoint(event.pos):
                    dragging_item = shoes_rect

                if dragging_item:
                    offset_x = dragging_item.x - event.pos[0]
                    offset_y = dragging_item.y - event.pos[1]

            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_item = None

            elif event.type == pygame.MOUSEMOTION:
                if dragging_item:
                    dragging_item.x = event.pos[0] + offset_x
                    dragging_item.y = event.pos[1] + offset_y

        # Render the background
        screen.blit(background, (0, 0))
        screen.blit(menu_box, (0, 0))
        
        # Add logic for draggable items here in the future
        screen.blit(character, character_rect.topleft)

        ## render clothing

        screen.blit(hat, hat_rect.topleft)
        screen.blit(shirt, shirt_rect.topleft)
        screen.blit(pants, pants_rect.topleft)
        screen.blit(shoes, shoes_rect.topleft)

        pygame.display.flip()  # Update the display

    pygame.quit()
    sys.exit()

# Start the game loop immediately
game_loop()
