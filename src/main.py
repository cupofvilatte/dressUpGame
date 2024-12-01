import pygame
import sys

# initialize game
pygame.init()

# set screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dress-Up Game")

# load assets of background and character
background = pygame.image.load("../assets/images/background.png")
background = pygame.transform.scale(background, (SCREEN_WIDTH, SCREEN_HEIGHT))

# more uses upon later development
# will contain menu buttons
menu_box = pygame.image.load("../assets/images/menu-box.png")
menu_box = pygame.transform.scale(menu_box, (SCREEN_WIDTH, SCREEN_HEIGHT))

character = pygame.image.load("../assets/images/character1.png")
character = pygame.transform.scale(character, (500, 500))
character_rect = character.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))

# load clothing items

# load and set hat
hat = pygame.image.load("../assets/images/hat1.png")
hat = pygame.transform.scale(hat, (150, 150))
hat_rect = hat.get_rect(topleft=(50, 20))

# load and set shirt
shirt = pygame.image.load("../assets/images/shirt1.png")
shirt = pygame.transform.scale(shirt, (160, 160))
shirt_rect = shirt.get_rect(topleft=(150, 200))

# load and set dress
dress = pygame.image.load("../assets/images/dress1.png")
dress = pygame.transform.scale(dress, (160, 220))
dress_rect = dress.get_rect(topleft=(150, 20))

# load and set pants
pants = pygame.image.load("../assets/images/pants1.png")
pants = pygame.transform.scale(pants, (120, 200))
pants_rect = pants.get_rect(topleft=(50, 150))

# load and set shoes
shoes = pygame.image.load("../assets/images/shoes1.png")
shoes = pygame.transform.scale(shoes, (180, 150))
shoes_rect = shoes.get_rect(topleft=(50, 300))

# set up drag and drop
dragging_item = None
offset_x = 0
offset_y = 0

def game_loop():
    """game logic"""
    # bring drag and drop variables into local
    global dragging_item, offset_x, offset_y

    # declare game running as true
    running = True

    # while loop to continue running game until closed
    while running:
        for event in pygame.event.get():
            # quit the game when the program is closed
            if event.type == pygame.QUIT:
                running = False
        
            # make the dragging_item set to whatever is clicked on
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # elif choices for all the rendered clothes
                if hat_rect.collidepoint(event.pos):
                    dragging_item = hat_rect
                elif shirt_rect.collidepoint(event.pos):
                    dragging_item = shirt_rect
                elif pants_rect.collidepoint(event.pos):
                    dragging_item = pants_rect
                elif shoes_rect.collidepoint(event.pos):
                    dragging_item = shoes_rect
                elif dress_rect.collidepoint(event.pos):
                    dragging_item = dress_rect

                # if an item is being dragged, set its position according to where it's being dragged
                if dragging_item:
                    offset_x = dragging_item.x - event.pos[0]
                    offset_y = dragging_item.y - event.pos[1]

            # when the mouse is no longer being pressed, deselect the item
            elif event.type == pygame.MOUSEBUTTONUP:
                dragging_item = None

            # dragging_item matches where the mouse moves it
            elif event.type == pygame.MOUSEMOTION:
                if dragging_item:
                    dragging_item.x = event.pos[0] + offset_x
                    dragging_item.y = event.pos[1] + offset_y

        # render the background and menu box
        # menu box will have later implementations additionally, it is where the clothes will be held
        screen.blit(background, (0, 0))
        screen.blit(menu_box, (0, 0))
        
        # add character onto screen
        screen.blit(character, character_rect.topleft)

        # render clothing

        screen.blit(hat, hat_rect.topleft)
        screen.blit(shirt, shirt_rect.topleft)
        screen.blit(pants, pants_rect.topleft)
        screen.blit(shoes, shoes_rect.topleft)
        screen.blit(dress, dress_rect.topleft)

        # update the display
        pygame.display.flip()

    pygame.quit()
    sys.exit()

# Start the game loop
game_loop()