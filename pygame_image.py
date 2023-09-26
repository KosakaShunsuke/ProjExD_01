import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    img3 = pg.image.load("ex01/fig/3.png")
    img3 = pg.transform.flip(img3,True,False)
    img4 = pg.transform.rotozoom(img3,10,1.0)
    imgs = [img3,img4]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        screen.blit(bg_img, [0, 0])
       
        screen.blit(imgs[tmr%2],[300,200])
        pg.display.update()
        tmr += 1
                
        clock.tick(50)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()