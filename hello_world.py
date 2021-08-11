import pygame
import math

#setup the window
pygame.init()
Width,height=800,500
win = pygame.display.set_mode((Width,height))
pygame.display.set_caption("hangman")

#load images
images = []
for i in range(7):
    image= pygame.image.load("hangman"+str(i)+".png")
    images.append(image)

#fonts
letter_font = pygame.font.SysFont('comicsans',40)
word_font = pygame.font.SysFont('comicsans',50)
title_font = pygame.font.SysFont('comicsans',60)

#game varibles
hangman_status= 0
word ="DEVELOPER"
guessed =[]


#color
white =(255,255,255)
Black = (0,0,0)


#button variable
radius=20
gap=15
letters =[]
startx=round((Width-(radius*2 + gap)*13)/2)
starty=400
A=65
for i in range(26):
    x=startx +gap*2 +(radius*2 + gap)*(i%13)
    y= starty+ (i//13)*(gap + radius*2)
    letters.append([x,y,chr(A + i),True])

def display_msg(msg):
    pygame.time.delay(1000)
    win.fill(white)
    text = word_font.render(msg,1,Black)
    win.blit(text,(Width/2 - text.get_width()/2,height/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(3000)

def draw():
    win.fill(white)
    text =title_font.render("Developer hangman",1,Black)
    win.blit(text,(Width/2 - text.get_width()/2,20))
    #draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter +" "
        else:
            display_word+="_ "
    text =word_font.render(display_word,1,Black)
    win.blit(text,(400,200))

    for letter in letters:
        x,y,ltr,visible=letter
        if visible:
            pygame.draw.circle(win,Black,(x,y),radius,3)
            text = letter_font.render(ltr,1,Black)
            win.blit(text,(x-text.get_width()/2,y-text.get_height()/2))


    win.blit(images[hangman_status],(150,100))
    pygame.display.update()



#parameters
fps=60
clock = pygame.time.Clock()
run = True

#game logic
while run:
    clock.tick(fps)
    draw()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run =False
        if event.type==pygame.MOUSEBUTTONDOWN:
            m_x,m_y = pygame.mouse.get_pos()
            for letter in letters:
                x,y,ltr,visible=letter
                if visible:
                    dis = math.sqrt((x-m_x)**2 + (y-m_y)**2)
                    if dis<radius:
                        letter[3]=False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status+=1
    won = True
    for letter in word:
        if letter not in guessed:
            won=False
            break
    draw()        
    if won:
        display_msg("You won!")
        break
    if hangman_status==6:
        display_msg("You lost!")
        break   
pygame.quit()