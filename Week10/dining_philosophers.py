import pygame
import sys


class BackgroundFurniture(pygame.sprite.Sprite):
    def __init__(self, image_file, location, scale_factor=1.0, horizontal_flip=False, vertical_flip=False):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.flip(self.image, horizontal_flip, vertical_flip)
        self.image = pygame.transform.scale(
            self.image,
            (
                int(self.image.get_width() * scale_factor),
                int(self.image.get_height() * scale_factor)
            )
        )
        self.rect = self.image.get_rect(center=location)


class Chair(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        super().__init__()
        self.image = pygame.image.load(image_file)
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*4, self.image.get_height()*4))
        self.rect = self.image.get_rect(center=location)


class Character(pygame.sprite.Sprite):
    def __init__(self, character_id, state_id, location):
        super().__init__()
        self.image = pygame.image.load("assets/characters.png")
        self.rect = self.image.get_rect(center=location)
        self.image = self.image.subsurface(pygame.Rect(abs(state_id)*16, character_id*16, 16, 16))
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*4, self.image.get_height()*4))
        if state_id < 0:
            self.image = pygame.transform.flip(self.image, True, False)
        self.direction = "right"
        self.moving = False
        self.speed = 5


class Text:
    def __init__(self, text, location, font_size=20, font_color=(0, 0, 0)):
        self.text = text
        self.font = pygame.font.Font("assets/PressStart2P.ttf", font_size)
        self.text_surface = self.font.render(self.text, True, font_color)
        self.text_rect = self.text_surface.get_rect(center=location)


class Meal(pygame.sprite.Sprite):
    def __init__(self, location):
        super().__init__()
        self.image = pygame.image.load("assets/spaghetti_full.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*1, self.image.get_height()*1))
        self.rect = self.image.get_rect(center=location)


class Chopstick(pygame.sprite.Sprite):
    def __init__(self, angle, location):
        super().__init__()
        self.image = pygame.image.load("assets/chopstick.png")
        self.image = pygame.transform.scale(self.image, (self.image.get_width()*0.3, self.image.get_height()*0.3))
        self.image = pygame.transform.rotate(self.image, angle)
        self.rect = self.image.get_rect(center=location)


WIDTH = 800
HEIGHT = 600
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dining Philosophers")
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

background_group = pygame.sprite.Group()
background_group.add(
    [
        BackgroundFurniture("assets/floor.png", (x, y))
        for x in range(0, WIDTH+100, 62) for y in range(0, HEIGHT+100, 46)
    ]
)
background_group.add(BackgroundFurniture("assets/carpet.png", (WIDTH//2, HEIGHT//2), 12))
background_group.add(BackgroundFurniture("assets/fireplace.png", (WIDTH//2, 60), 4))
background_group.add(BackgroundFurniture("assets/music_player.png", (720, 90), 4))
background_group.add(BackgroundFurniture("assets/sofa_front.png", (560, 80), 4))
background_group.add(BackgroundFurniture("assets/sofa_single_right.png", (740, 200), 4))
background_group.add(BackgroundFurniture("assets/stairs.png", (700, 440), 4, True))
background_group.add(BackgroundFurniture("assets/desk.png", (170, 120), 3))
background_group.add(BackgroundFurniture("assets/table_horizontal.png", (WIDTH//2, HEIGHT//2), 4))

title_text = Text("Dining Philosophers", (WIDTH//2 - 100, HEIGHT - 50), 24, (200, 255, 200))

meal_0 = Meal((WIDTH//2 - 40, HEIGHT//2 - 50))
meal_1 = Meal((WIDTH//2 + 40, HEIGHT//2 - 50))
meal_2 = Meal((WIDTH//2 + 60, HEIGHT//2 - 15))
meal_3 = Meal((WIDTH//2 + 0, HEIGHT//2 - 10))
meal_4 = Meal((WIDTH//2 - 60, HEIGHT//2 - 15))
meal_group = pygame.sprite.Group()
meal_group.add([meal_0, meal_1, meal_2, meal_3, meal_4])


philosopher_group = pygame.sprite.Group()
chair_0 = Chair("assets/chair_front_2.png", (WIDTH//2 - 40, HEIGHT//2 - 110))
chair_1 = Chair("assets/chair_front_2.png", (WIDTH//2 + 40, HEIGHT//2 - 110))
chair_2 = Chair("assets/chair_right_2.png", (WIDTH//2 + 130, HEIGHT//2 - 10))
chair_3 = Chair("assets/chair_back_2.png", (WIDTH//2, HEIGHT//2 + 100))
chair_4 = Chair("assets/chair_left_2.png", (WIDTH//2 - 130, HEIGHT//2 - 10))
philosopher_0 = Character(6, 0, (WIDTH//2 + 10, HEIGHT//2 + 30))
philosopher_1 = Character(0, 0, (WIDTH//2 + 90, HEIGHT//2 + 30))
philosopher_2 = Character(4, -2, (WIDTH//2 + 160, HEIGHT//2 + 100))
philosopher_3 = Character(10, 1, (WIDTH//2 + 45, HEIGHT//2 + 180))
philosopher_4 = Character(2, 2, (WIDTH//2 - 65, HEIGHT//2 + 100))
chopstick_0 = Chopstick(225, (WIDTH//2 + 0, HEIGHT//2 - 60))
chopstick_1 = Chopstick(160, (WIDTH//2 + 55, HEIGHT//2 - 35))
chopstick_2 = Chopstick(75, (WIDTH//2 + 40, HEIGHT//2 + 10))
chopstick_3 = Chopstick(15, (WIDTH//2 - 40, HEIGHT//2 + 10))
chopstick_4 = Chopstick(290, (WIDTH//2 - 55, HEIGHT//2 - 35))
philosopher_group.add(
    [
        chair_0, chair_1, chair_2, chair_4,
        philosopher_0, philosopher_1, philosopher_2, philosopher_3, philosopher_4,
        chair_3,
        chopstick_0, chopstick_1, chopstick_2, chopstick_3, chopstick_4
    ]
)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    background_group.draw(screen)
    screen.blit(title_text.text_surface, title_text.text_rect)
    meal_group.draw(screen)
    philosopher_group.draw(screen)
    pygame.display.update()
    clock.tick(60)
