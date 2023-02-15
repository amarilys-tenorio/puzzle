import pygame
import random
pygame.font.init()

WIDTH = 500
HEIGHT = 500
SIZE = (WIDTH, HEIGHT)
TITLE = "Slide Puzzle"
BG_COLOR = (50, 50, 50)
WHITE = (255, 255, 255)

screen = pygame.display.set_mode(SIZE)
pygame.display.set_caption(TITLE)

pygame.font.init()
FONT = pygame.font.SysFont("Arial", 24)

board = [[1, 2, 3], [4, 5, 6], [7, 8, None]]

def draw_board(board):
    block_size = WIDTH // 3
    for row in range(3):
        for col in range(3):
            x = col * block_size
            y = row * block_size
            value = board[row][col]
            if value:
                text = FONT.render(str(value), True, WHITE)
                text_rect = text.get_rect(center=(x+block_size//2, y+block_size//2))
                pygame.draw.rect(screen, WHITE, (x, y, block_size, block_size))
                screen.blit(text, text_rect)

def move(board, row, col):
    if row < 0 or row > 2 or col < 0 or col > 2:
        return
    if board[row][col] is not None:
        return
    empty_row, empty_col = get_empty_position(board)
    board[row][col], board[empty_row][empty_col] = board[empty_row][empty_col], board[row][col]

def shuffle(board):
    for i in range(1000):
        row, col = get_empty_position(board)
        moves = []
        if row > 0:
            moves.append((row-1, col))
        if row < 2:
            moves.append((row+1, col))
        if col > 0:
            moves.append((row, col-1))
        if col < 2:
            moves.append((row, col+1))
        move(board, *random.choice(moves))

def get_empty_position(board):
    for row in range(3):
        for col in range(3):
            if board[row][col] is None:
                return row, col

def is_solved(board):
    return board == [[1, 2, 3], [4, 5, 6], [7, 8, None]]

shuffle(board)

moves = 0
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            elif event.key == pygame.K_DOWN:
                row, col = get_empty_position(board)
                move(board, row-1, col)
                moves += 1
            elif event.key == pygame.K_LEFT:
                row, col = get_empty_position(board)
                move(board, row, col+1)
                moves += 1
            elif event.key == pygame.K_RIGHT:
                row, col = get_empty_position(board)
                move(board, row, col-1)
                moves += 1

    screen.fill(BG_COLOR)
    draw_board(board)
    pygame.display.update()