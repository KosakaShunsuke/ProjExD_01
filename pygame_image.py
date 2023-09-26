import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img2 = pg.transform.flip(bg_img,True,False)
    img3 = pg.image.load("ex01/fig/3.png")
    img3 = pg.transform.flip(img3,True,False)
    img5 = pg.transform.rotozoom(img3,5,1.0)
    img6 = pg.transform.rotozoom(img3,10,1.0)
    

    imgs = [img3,img5,img6,img5]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x=tmr%3200

        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img2,[1600-x, 0])
        screen.blit(bg_img,[3200-x,0])
       
        screen.blit(imgs[tmr%4],[300,200])
        pg.display.update()
        tmr += 1    
        clock.tick(160)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()