import random

import pygame
from pygame import *
import time

screen = display.set_mode((1080, 720))

on = True
keys = []
clic = False
clicavant = clic
clicpos = []
cliclog = []
bp = 1
p = 0
pa10 = 0
fps = 50
start = True
bolspeed = 10
bolsize = 100
nbr0 = image.load('0.png')
nbr1 = image.load('1.png')
nbr2 = image.load('2.png')
nbr3 = image.load('3.png')
nbr4 = image.load('4.png')
nbr5 = image.load('5.png')
nbr6 = image.load('6.png')
nbr7 = image.load('7.png')
nbr8 = image.load('8.png')
nbr9 = image.load('9.png')
nbrm = image.load('-.png')


def affiche_score(nbr, x, y):
    nbr = str(nbr)
    for n in nbr:
        if n == "0":
            screen.blit(nbr0, (x, y))
            x += nbr0.get_size()[0] + 5
        if n == "1":
            screen.blit(nbr1, (x, y))
            x += nbr1.get_size()[0] + 5
        if n == "2":
            screen.blit(nbr2, (x, y))
            x += nbr2.get_size()[0] + 5
        if n == "3":
            screen.blit(nbr3, (x, y))
            x += nbr3.get_size()[0] + 5
        if n == "4":
            screen.blit(nbr4, (x, y))
            x += nbr4.get_size()[0] + 5
        if n == "5":
            screen.blit(nbr5, (x, y))
            x += nbr5.get_size()[0] + 5
        if n == "6":
            screen.blit(nbr6, (x, y))
            x += nbr6.get_size()[0] + 5
        if n == "7":
            screen.blit(nbr7, (x, y))
            x += nbr7.get_size()[0] + 5
        if n == "8":
            screen.blit(nbr8, (x, y))
            x += nbr8.get_size()[0] + 5
        if n == "9":
            screen.blit(nbr9, (x, y))
            x += nbr9.get_size()[0] + 5
        if n == "-":
            screen.blit(nbrm, (x, y))
            x += nbrm.get_size()[0] + 5


def t(t):
    for u in keys:
        if t == u:
            return True
    return False


class objet:
    def __init__(self, img, x=0, y=0, tag=None):
        self.defaultimage = image.load(img)
        self.image = image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.tag = tag
        self.zoom = [100, 100]

    def checkappui(self):
        if clic and not clicavant:
            if self.rect.collidepoint(cliclog[1]):
                self.image = pygame.transform.scale(self.defaultimage, (
                    self.defaultimage.get_size()[0] / 100 * 90, self.defaultimage.get_size()[1] / 100 * 90))
                self.rect = self.image.get_rect(center=self.rect.center)
                return True
            else:
                return False
        else:
            if not clic and clicavant:
                self.image = self.defaultimage
                self.rect = self.image.get_rect(center=self.rect.center)
        return False


    def setzoom(self, zoom):
        self.zoom = zoom
        self.image = pygame.transform.scale(self.defaultimage, (self.defaultimage.get_size()[0] / 100 * zoom[0],
                                                                self.defaultimage.get_size()[1] / 100 * zoom[1]))
        self.rect = self.image.get_rect(center=self.rect.center)


b = []

bol = objet("bol.svg", screen.get_size()[0] // 2 - 30, 600)

b.append(objet("balle.svg", random.randint(bol.rect.x - 150, bol.rect.x + 150), -100, {"Visible": True}))
b.append(objet("balle.svg", random.randint(bol.rect.x - 150, bol.rect.x + 150), 50, {"Visible": False}))
b.append(objet("balle.svg", random.randint(bol.rect.x - 150, bol.rect.x + 150), 50, {"Visible": False}))
b.append(objet("balle.svg", random.randint(bol.rect.x - 150, bol.rect.x + 150), 50, {"Visible": False}))
b.append(objet("balle.svg", random.randint(bol.rect.x - 150, bol.rect.x + 150), 50, {"Visible": False}))

FPSred = objet("FPS red.png", 10, 10)

bolspeedaug = objet("bolspeed aug.png", 167, 10)

bolsizeaug = objet("bolsize aug.png", 177 + 170, 10)

mixer.init()

popsound = mixer.Sound("pop.mp3")

while on:
    clicavant = clic
    screen.fill((80, 80, 80))
    for event in pygame.event.get():
        if event.type == QUIT:
            on = False
            quit()
        if event.type == KEYDOWN:
            keys.append(event.key)
        if event.type == KEYUP:
            keys.remove(event.key)
        if event.type == MOUSEBUTTONDOWN:
            clic = True
            clicpos = event.pos
        if event.type == MOUSEBUTTONUP:
            clic = False
    cliclog = [clic, clicpos]

    if t(K_a) or t(K_LEFT):
        if bol.rect.x > 80:
            bol.rect.x -= bolspeed
    if t(K_d) or t(K_RIGHT):
        if bol.rect.x < 1024 - 80:
            bol.rect.x += bolspeed
    if FPSred.checkappui():
        if p > 15 and fps > 20:
            fps -= 10
            p -= 15
    if bolspeedaug.checkappui():
        if p > 20 and bolspeed < 40:
            bolspeed += 5
            p -= 20
    if bolsizeaug.checkappui():
        if p > 10 and bolsize < 200:
            bolsize += 2
            bol.setzoom([bolsize, 100])
            p -= 10
    if on:
        screen.blit(bol.image, bol.rect)
        screen.blit(FPSred.image, FPSred.rect)
        screen.blit(bolspeedaug.image, bolspeedaug.rect)
        screen.blit(bolsizeaug.image, bolsizeaug.rect)
        affiche_score(p, 10, 60)
        if p > 15 and fps > 20:
            draw.line(screen, (0, 255, 0), (10, 55), (157, 55))
        else:
            draw.line(screen, (255, 0, 0), (10, 55), (157, 55))

        if p > 20 and bolspeed < 40:
            draw.line(screen, (0, 255, 0), (167, 55), (167 + 170, 55))
        else:
            draw.line(screen, (255, 0, 0), (167, 55), (167 + 170, 55))

        if p > 10 and bolsize < 200:
            draw.line(screen, (0, 255, 0), (167 + 170 + 10, 55), (167 + 170 + 10 + 150, 55))
        else:
            draw.line(screen, (255, 0, 0), (167 + 170 + 10, 55), (167 + 170 + 10 + 150, 55))
    for i in b:
        if i.tag["Visible"]:
            i.rect.y += 8
            if on:
                screen.blit(i.image, i.rect)
            if i.rect.colliderect(bol.rect):
                i.rect.y = 50
                ok = False
                while not ok:
                    a = random.randint(bol.rect.x - 200, bol.rect.x + 200)
                    if 950 > a > 80:
                        ok = True
                        i.rect.x = a
                p += 1
                start = False
                pa10 += 1
                popsound.play()
            if i.rect.y > 700:
                i.rect.y = 50
                ok = False
                while not ok:
                    a = random.randint(bol.rect.x - 150, bol.rect.x + 150)
                    if 950 > a > 80:
                        ok = True
                        i.rect.x = a
                if not start:
                    p -= 1
                    fps += 1
                    pa10 -= 1
    print(p)
    if pa10 == 10:
        pa10 = 0
        fps += 2
        if bp < len(b):
            b[bp].tag["Visible"] = True
            b[bp].rect.y = -100
            ok = False
            while not ok:
                a = random.randint(bol.rect.x - 150, bol.rect.x + 150)
                if 950 > a > 80:
                    ok = True
                    b[bp].rect.x = a
            bp += 1
    if p <= 0 and not start:
        on = False
        print("GAME OVER")
    if on:
        display.flip()
    if fps > 20:
        time.sleep(1 / fps)
    else:
        time.sleep(1 / 20)
