# pygame ვერსია.
# Importing pygame, engine of the TicTacToe and exit function from sys module.
import pygame
import tictaxtoeEngine
from sys import exit

pygame.init()

# Width and height of screen.
WIDTH, HEIGHT = 600, 600

# Positions of 'X' 'and 'O' on the screen.
DRAW_BY_INDEXES = {
    '(0,0)': (WIDTH / 3 - 170, 10),
    '(0,1)': (WIDTH / 3 + 20, 10),
    '(0,2)': (WIDTH - WIDTH / 3 + 20, 10),
    '(1,0)': (WIDTH / 3 - 170, HEIGHT / 3 + 10),
    '(1,1)': (WIDTH / 3 + 20, HEIGHT / 3 + 10),
    '(1,2)': (WIDTH - WIDTH / 3 + 20, HEIGHT / 3 + 10),
    '(2,0)': (WIDTH / 3 - 170, HEIGHT - HEIGHT / 3 + 10),
    '(2,1)': (WIDTH / 3 + 20, HEIGHT - HEIGHT / 3 + 10),
    '(2,2)': (WIDTH - WIDTH / 3 + 20, HEIGHT - HEIGHT / 3 + 10)
}

# Importing list of tictactoe board.
BOARD = tictaxtoeEngine.rows

# Drawing screen and making clock variable.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

# Drawing board of the tictactoe on the screen.
background = pygame.surface.Surface((WIDTH, HEIGHT))
background.fill('Purple')
line_rigi = pygame.surface.Surface((WIDTH, 2))
line_rigi.fill('Black')
line_sveti = pygame.surface.Surface((2, HEIGHT))
line_sveti.fill('Black')
text_X = pygame.font.Font(None, 300)
text_X_surf = text_X.render('X', False, 'White')
text_O = pygame.font.Font(None, 300)
text_O_surf = text_X.render('O', False, 'Black')

# Writing winners name or draw at the end of the game.
draw = pygame.font.Font(None, 100)
draw_surf = draw.render('Draw', False, 'Grey')
win_x = pygame.font.Font(None, 100)
win_surf = win_x.render('Winner is X', False, "White")
win_o = pygame.font.Font(None, 100)
wino_surf = win_o.render('Winner is O', False, "Black")


# Drawing "X" and "O" on the board.
def draw_surface(new, num):
    if new == 1:
        if num % 2 == 0:
            screen.blit(text_X_surf, (DRAW_BY_INDEXES['(0,0)']))
            BOARD[0][0] = 'X'
        else:
            screen.blit(text_O_surf, (DRAW_BY_INDEXES['(0,0)']))
            BOARD[0][0] = 'O'
    if new == 2:
        if num % 2 == 0:
            screen.blit(text_X_surf, (DRAW_BY_INDEXES['(0,1)']))
            BOARD[0][1] = 'X'
        else:
            screen.blit(text_O_surf, (DRAW_BY_INDEXES['(0,1)']))
            BOARD[0][1] = 'O'
    if new == 3:
        if num % 2 == 0:
            screen.blit(text_X_surf, (DRAW_BY_INDEXES['(0,2)']))
            BOARD[0][2] = 'X'
        else:
            screen.blit(text_O_surf, (DRAW_BY_INDEXES['(0,2)']))
            BOARD[0][2] = 'O'
    if new == 4:
        if num % 2 == 0:
            screen.blit(text_X_surf, (DRAW_BY_INDEXES['(1,0)']))
            BOARD[1][0] = 'X'
        else:
            screen.blit(text_O_surf, (DRAW_BY_INDEXES['(1,0)']))
            BOARD[1][0] = 'O'
    if new == 5:
        if num % 2 == 0:
            screen.blit(text_X_surf, (DRAW_BY_INDEXES['(1,1)']))
            BOARD[1][1] = 'X'
        else:
            screen.blit(text_O_surf, (DRAW_BY_INDEXES['(1,1)']))
            BOARD[1][1] = 'O'
    if new == 6:
        if num % 2 == 0:
            screen.blit(text_X_surf, (DRAW_BY_INDEXES['(1,2)']))
            BOARD[1][2] = 'X'
        else:
            screen.blit(text_O_surf, (DRAW_BY_INDEXES['(1,2)']))
            BOARD[1][2] = 'O'
    if new == 7:
        if num % 2 == 0:
            screen.blit(text_X_surf, (DRAW_BY_INDEXES['(2,0)']))
            BOARD[2][0] = 'X'
        else:
            screen.blit(text_O_surf, (DRAW_BY_INDEXES['(2,0)']))
            BOARD[2][0] = 'O'
    if new == 8:
        if num % 2 == 0:
            screen.blit(text_X_surf, (DRAW_BY_INDEXES['(2,1)']))
            BOARD[2][1] = 'X'
        else:
            screen.blit(text_O_surf, (DRAW_BY_INDEXES['(2,1)']))
            BOARD[2][1] = 'O'
    if new == 9:
        if num % 2 == 0:
            screen.blit(text_X_surf, (DRAW_BY_INDEXES['(2,2)']))
            BOARD[2][2] = 'X'
        else:
            screen.blit(text_O_surf, (DRAW_BY_INDEXES['(2,2)']))
            BOARD[2][2] = 'O'


# Main function.
def main():
    xtuo = 'X'
    num = 0
    screen.blit(background, (0, 0))
    screen.blit(line_rigi, (0, 199))
    screen.blit(line_rigi, (0, 399))
    screen.blit(line_sveti, (199, 0))
    screen.blit(line_sveti, (399, 0))
    stop = False
    

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            # Detecting position of the mouse and placing players char were it should be.
            if event.type == pygame.MOUSEBUTTONDOWN and not stop:
                px, py = pygame.mouse.get_pos()
                if px < 200 and py < 200 and BOARD[0][0] == "-":
                    draw_surface(1, num)
                    num += 1
                elif 200 < px < 400 and py < 200 and BOARD[0][1] == "-":
                    draw_surface(2, num)
                    num += 1
                elif 400 < px < 600 and py < 200 and BOARD[0][2] == "-":
                    draw_surface(3, num)
                    num += 1
                elif px < 200 and 200 < py < 400 and BOARD[1][0] == "-":
                    draw_surface(4, num)
                    num += 1
                elif 200 < px < 400 and 200 < py < 400 and BOARD[1][1] == "-":
                    draw_surface(5, num)
                    num += 1
                elif 400 < px < 600 and 200 < py < 400 and BOARD[1][2] == "-":
                    draw_surface(6, num)
                    num += 1
                elif px < 200 and 400 < py < 600 and BOARD[2][0] == "-":
                    draw_surface(7, num)
                    num += 1
                elif 200 < px < 400 and 400 < py < 600 and BOARD[2][1] == "-":
                    draw_surface(8, num)
                    num += 1
                elif 400 < px < 600 and 400 < py < 600 and BOARD[2][2] == "-":
                    draw_surface(9, num)
                    num += 1
                if num%2 == 1:
                    xtuo = 'X'
                elif num%2 == 0:
                    xtuo = 'O'
        # Winning options of columns and diagonals.
        cols = tictaxtoeEngine.svetebeis_sia(BOARD)
        diag = tictaxtoeEngine.diagonalebis_sia(BOARD)

        # Checking if there is winner or draw and if there is one ending the game.

        if num == 9:
            screen.blit(background, (0, 0))
            screen.blit(draw_surf, (210, 270))
        elif tictaxtoeEngine.mogebis_naxva(cols, diag, xtuo) == 'O':
            screen.blit(background, (0, 0))
            screen.blit(wino_surf, (100, 270))
            stop = True
        elif tictaxtoeEngine.mogebis_naxva(cols, diag, xtuo) == 'X':
            screen.blit(background, (0, 0))
            screen.blit(win_surf, (100, 270))
            stop = True

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
