from pygame import *
from random import randint 


# классы
class GameSprite(sprite.Sprite):
    def __init__(self, sprite_image, sprite_x, sprite_y, sprite_size, sprite_speed):
        super().__init__()
        self.image = transform.scale(image.load(sprite_image), sprite_size)
        
        self.rect = self.image.get_rect()
        self.rect.x = sprite_x
        self.rect.y = sprite_y
        
        self.speed = sprite_speed

    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

class Player(GameSprite):
    def update(self):
       keys = key.get_pressed()
       if keys[K_LEFT] and self.rect.x > 0:
           self.rect.x -= self.speed
       if keys[K_RIGHT] and self.rect.x < win_width - ship_width:
           self.rect.x += self.speed

    def shoot(self):
        print("Стреяю")
        bullet = Bullet(bellet_img, self.rect.centerx, self.rect.top, ( 80, 40), )
        bullet_group

    def shoot(self):
        print('стреляю')
class Enemy(GameSprite):
    def update(self):
        self.rect.y += self.speed 
        if self.rect.y >= win_height:
            self.rect.y == 0
            self.rect.x = randint(0, win_width - ship_width)
            global lost_enemy
            lost_enemy += 1
            print(lost_enemy)

class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed  
        if self.rect.y + bullet_big >= 0:
            self kill()






# константы
win_height = 500
win_width = 700

ship_height = 80
ship_width = 40
ship_start_x = win_width / 2
ship_start_y = win_height - ship_height - 5

enemy_height = 80
enemy_width = 40
bullet_speed = 100

clock = time.Clock()
FPS = 60



# картин
background_img = 'assets/images/galaxy.jpg'
background_img = transform.scale(image.load(background_img), (win_width, win_height))
bullet_img = bullet.png

ship_img = 'assets/images/rocket.png'
enemy_img = 'assets/images/ufo.png'

# звуки
mixer.init()
mixer.music.load('assets/music/space.ogg')
mixer.music.play()

# шрифты
font init() 
fonts1 = font.render('Попал', True, (255, 215,0))

#Надписи 
text_lose = fonts1_finish.render('Вы проиграли', True (255, 255,255)) 
text_win = fonts1_finish.render('Вы выиграли', True(255, 255,255)) 


# окно
window = display.set_mode((win_width, win_height))
display.set_caption("Шутер")

# спрайты
space_ship = Player(ship_img, ship_start_x, ship_start_y, (ship_width, ship_height), 5)
enemy = Enemy(enemy_img , 300, 0, (enemy_height, enemy_width), 5)

monster = Sprite.Group()
for i in range(5):
    enemy_x = randint(0, win_width, ship_width)
    enemy_speed = randint (1,4)
    enemy = Enemy(enemy_img , 300, 0, (enemy_height, enemy_width), 5)
    monster.add(enemy)

bullet_group = sprite.Group()


# игровой цикл
run = True
finish = False

while run:

    for e in event.get():
        if e.type == QUIT:
            run = False
        elif e.type == KEYDOWN:
            if e.key == K_SPACE:
                space_ship.shoot()

    if not finish: 

        space_ship.update()
        enemy.update()
        bullet_group.draw(window)
        
        window.blit(background_img,(0, 0))
        space_ship.reset()
        monster.draw(window)
        count_lose = fonts1.render('Пропущенно', + str (lost_enemy), 1 (255,255))
        window.blit(count_lose, (10, 10))

        if sprite.spritecollide(space_ship, monster, False):
            print('Проиграли')
            windows.blit(text_lose, (250, 350 ))


    display.update()
    clock.tick(FPS)