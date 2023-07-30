import pygame
import math
import random

# Opening game module and defining length portion of game
pygame.init()
LENGTH, BREADTH = 950, 750
win = pygame.display.set_mode((LENGTH, BREADTH))
pygame.display.set_caption("Hangman")

# Buttons
RADIUS = 20
GAP = 25
letters = []
start_x = round((LENGTH-(RADIUS * 2 + GAP) *13) / 2)
start_y = 550
A = 65
for i in range(26):
    x = start_x + GAP *2 + ((RADIUS * 2 + GAP) * (i % 13))
    y = start_y + ((i//13)* (GAP + RADIUS * 2))
    letters.append([x, y, chr(A+i), True])


# Fonts
LETTER_FONT = pygame.font.SysFont("comicsans", 35)
WORD_FONT = pygame.font.SysFont("comicsans", 55)
TITLE_FONT = pygame.font.SysFont("comicsans", 75)
SUB_TITLE_FONT = pygame.font.SysFont("comicsans", 25)



# Load images
images = []
for i in range(7):
    image = pygame.image.load("hangman" + str(i) + ".png")
    images.append(image)

# Game variables
hangman_status = 0
words = ["GRAPHICS", "COMPUTER", "RECURSION", "CLASS", "CATCH", "THROW",
         "ARRAY", "LIST", "FUNCTION", "VARIABLE", "DATA", "LOOP", "CONDITIONAL",
           "ERROR", "BUG", "DEBUG", "OBJECT", "CHILD", "HACK", "CODE"] 
word = random.choice(words)
guessed = []


# Colors
#RGB code in the format (R,G,B)
BACKGROUND = (15,255,80) 
WRITINGS = (255,255,255)
L_BACKGROUND = (255,0,0)
W_BACKGROUND = (0,0,255)


# Setup game loop
FPS = 60
clock = pygame.time.Clock()
run = True

# display message
def display_message(message,colour):
    pygame.time.delay(1000)
    win.fill(colour)
    text = WORD_FONT.render(message, 1, WRITINGS)
    win.blit(text, (LENGTH/2 - text.get_width()/2, BREADTH/2 - text.get_height()/2))
    pygame.display.update()
    pygame.time.delay(2500)


def draw():
    win.fill(BACKGROUND)
    text = TITLE_FONT.render("Hangman Game", 1, WRITINGS)
    win.blit(text, (LENGTH/2 - text.get_width()/2, 20))
    text= SUB_TITLE_FONT.render("Guess the word", 1, WRITINGS)
    win.blit(text, (LENGTH/2 - text.get_width()/2, 110))

    # draw word
    display_word = ""
    for letter in word:
        if letter in guessed:
            display_word += letter + " "
        else:
            display_word += "_ "
    text = WORD_FONT.render(display_word, 1, WRITINGS)
    win.blit(text, (400,350))


    # drawing buttons
    for letter in letters:
        x, y, ltr, visible= letter
        if visible:
            pygame.draw.circle(win, WRITINGS, (x, y), RADIUS, 3)
            text = LETTER_FONT.render(ltr, 1, WRITINGS)
            win.blit(text, (x - text.get_width()/2, y - text.get_height()/2))

    win.blit(images[hangman_status], (100, 200))
    pygame.display.update()

# Game running loop
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT: #Checks for quiting
            run = False

        if event.type== pygame.MOUSEBUTTONDOWN: #Gets the coordinates of pixel the mouse clicked
            m_x, m_y = pygame.mouse.get_pos()
            for letter in letters:
                x, y, ltr, visible= letter
                if visible:
                    dis = math.sqrt((x - m_x)**2 + (y - m_y)**2)
                    if dis < RADIUS:
                        letter[3] = False
                        guessed.append(ltr)
                        if ltr not in word:
                            hangman_status += 1
    
    draw()

    won = True
    for letter in word:
        if letter not in guessed:
            won = False
            break
    
    if won:
        display_message("You WON",W_BACKGROUND)
        break

    if hangman_status == 6:
        display_message("You LOST",L_BACKGROUND)
        break
        
pygame.quit()