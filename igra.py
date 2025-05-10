import pygame
pygame.init()

window=pygame.display.set_mode((900,600))
pygame.display.set_caption("2D Game")
background=pygame.image.load("background2.jpg")

clock=pygame.time.Clock()
class GameSprite():
    def __init__(self, x=0, y=0, height=0, width=0,step=0,image_sprite=""):
        self.x=x
        self.y=y
        self.height=height
        self.width=width
        self.step=step
        self.image=pygame.image.load(image_sprite)
        self.image=pygame.transform.scale(self.image, (self.width, self.height))
    def draw(self,x,y):
        window.blit(self.image, (self.x, self.y))
    def update(self):
        keys=pygame.key.get_pressed()
        if keys[pygame.K_A]:
            self.x-=self.step
        if keys[pygame.K_D]:
            self.x+=self.step
        if keys[pygame.K_W]:
            self.y-=self.step
        if keys[pygame.K_S]:
            self.y+=self.step
        if self.x<0:
            self.x=0
        if self.x>900-self.width:
            self.x=900-self.width
        if self.y<0:
            self.y=0
        if self.y>600-self.height:
            self.y=600-self.height

player=GameSprite(100, 100, 100,100,10, "player.png")
game=True
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game=False
    window.blit(background, (0, 0))
    player.draw(100, 100)
    clock.tick(60)
    pygame.display.update()
pygame.quit()