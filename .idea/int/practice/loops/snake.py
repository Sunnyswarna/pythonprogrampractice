import random

# Game dimensions
WIDTH = 10
HEIGHT = 10

# Initialize snake and direction
snake = [(5, 5)]
direction = "RIGHT"

# Generate initial food
def place_food():
    while True:
        f = (random.randint(1, HEIGHT - 2), random.randint(1, WIDTH - 2))
        if f not in snake:
            return f

food = place_food()
score = 0

# Print game board
def print_board():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (y, x) == snake[0]:
                print("O", end="")  # Head
            elif (y, x) in snake:
                print("o", end="")  # Body
            elif (y, x) == food:
                print("*", end="")  # Food
            elif y == 0 or y == HEIGHT-1 or x == 0 or x == WIDTH-1:
                print("#", end="")  # Wall
            else:
                print(" ", end="")
        print()
    print(f"Score: {score}")

# Move snake
def move_snake():
    head_y, head_x = snake[0]
    if direction == "UP":
        head_y -= 1
    elif direction == "DOWN":
        head_y += 1
    elif direction == "LEFT":
        head_x -= 1
    elif direction == "RIGHT":
        head_x += 1

    new_head = (head_y, head_x)

    # Collision
    if (new_head in snake or
        head_y == 0 or head_y == HEIGHT-1 or
        head_x == 0 or head_x == WIDTH-1):
        return False  # Game Over

    snake.insert(0, new_head)

    global food, score
    if new_head == food:
        score += 1
        food = place_food()
    else:
        snake.pop()

    return True

# Game loop
while True:
    print_board()
    move = input("Enter direction (WASD): ").upper()
    if move == "W" and direction != "DOWN":
        direction = "UP"
    elif move == "S" and direction != "UP":
        direction = "DOWN"
    elif move == "A" and direction != "RIGHT":
        direction = "LEFT"
    elif move == "D" and direction != "LEFT":
        direction = "RIGHT"

    if not move_snake():
        print_board()
        print("Game Over!")
        break
