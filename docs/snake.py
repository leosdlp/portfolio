from tkinter import *
import random
import time

GAME_WIDTH = 800
GAME_HEIGHT = 800
SPEED = 100
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOR = "#00FF00"
FOOD_COLOR = "#FF0000"
GRID_SIZE = 50
diff_verif = 1
colorTemp1 = "#F5B041"
colorTemp2 ="#F39C12"

window = Tk()
window.title("Snake")
window.resizable(False, False)

# Créer le canvas
canvas = Canvas(window, bg=colorTemp1, height=GAME_HEIGHT, width=GAME_WIDTH)

# Ajouter la grille
for i in range(0, GAME_WIDTH, GRID_SIZE):
    for j in range(0, GAME_HEIGHT, GRID_SIZE):
        if (i//GRID_SIZE + j//GRID_SIZE) % 2 == 0:
            color = colorTemp1
        else:
            color = colorTemp2
        canvas.create_rectangle(i, j, i+GRID_SIZE, j+GRID_SIZE, fill=color, outline="")

# Afficher le canvas dans la fenêtre principale
canvas.pack()
class Snake:
    
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = []
        self.squares = []

        for i in range(0, BODY_PARTS):
            self.coordinates.append([0, 0])

        for x, y in self.coordinates:
            square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR, tag="snake")
            self.squares.append(square)

class Food:
    
    def __init__(self):
        
        x = random.randint(0, (GAME_WIDTH/SPACE_SIZE)-1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT/SPACE_SIZE)-1) * SPACE_SIZE

        self.coordinates = [x, y]

        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOR, tag="food")


def next_turn(snake, food):

    global score_time2
    if diff_verif == 2:
        time.sleep(0.05)
        score_time2 += 0.08
        score_temp = int(score_time2)
        label2.config(text="Time:{}".format(score_temp))
    elif diff_verif == 1:
        time.sleep(0.05)
        score_time2 += 0.12
        score_temp = int(score_time2)
        label2.config(text="Time:{}".format(score_temp))
    elif diff_verif == 3:
        time.sleep(0.05)
        score_time2 += 0.06
        score_temp = int(score_time2)
        label2.config(text="Time:{}".format(score_temp))
    
    x, y = snake.coordinates[0]

    if direction == "up":
        y -= SPACE_SIZE
    elif direction == "down":
        y += SPACE_SIZE
    elif direction == "left":
        x -= SPACE_SIZE
    elif direction == "right":
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))

    square= canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOR)

    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:

        global score

        score += 1

        label.config(text="Score:{}".format(score))

        canvas.delete("food")

        food = Food()
    
    else:

        del snake.coordinates[-1]

        canvas.delete(snake.squares[-1])

        del snake.squares[-1]

    if check_colliisons(snake):
        game_over()

    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    
    global direction

    if new_direction == 'left':
        if direction != 'right':
            direction = new_direction
    elif new_direction == 'right':
        if direction != 'left':
            direction = new_direction
    elif new_direction == 'up':
        if direction != 'down':
            direction = new_direction
    elif new_direction == 'down':
        if direction != 'up':
            direction = new_direction

def check_colliisons(snake):
    
    x, y = snake.coordinates[0]

    if x < 0 or x >= GAME_WIDTH:
        print("GAME OVER")
        return True
    if y < 0 or y >= GAME_HEIGHT:
        print("GAME OVER")
        return True
    
    for body_part in snake.coordinates[1:]:
        if x == body_part[0] and y == body_part[1]:
            print("GAME OVER")
            return True
        
    return False


def game_over():
    global colorTemp1
    canvas.delete(ALL)
# Affichage du texte "GAME OVER"
    canvas.create_text(canvas.winfo_width()/2, canvas.winfo_height()/2, font=('consolas',70), text="GAME OVER", fill="red", tag="gameover")

    

# Création du bouton
    restart_btn = Button(window, text="Restart Facile", font=('consolas', 20), command=restart_game)
    canvas.create_window(canvas.winfo_width()/2, canvas.winfo_height()/2+100, window=restart_btn, tag="restart_btn")
    diff2 = Button(window, text="Difficulté Medium", font=('consolas', 20), command=restart_game2)
    canvas.create_window(canvas.winfo_width()/2, canvas.winfo_height()/2+200, window=diff2, tag="DiffMed")
    diff3 = Button(window, text="Difficulté Max", font=('consolas', 20), command=restart_game3)
    canvas.create_window(canvas.winfo_width()/2, canvas.winfo_height()/2+300, window=diff3, tag="DiffMax")
    if colorTemp1 == "#F5B041":
        green = Button(window, text="Color green", font=('consolas', 20), command=Green)
        canvas.create_window(canvas.winfo_width()/3, canvas.winfo_height()/2-100, window=green, tag="green")
        canvas.delete("orange")
    else:
        orange = Button(window, text="Color orange", font=('consolas', 20), command=Orange)
        canvas.create_window(canvas.winfo_width()/1.5, canvas.winfo_height()/2-100, window=orange, tag="orange")
        canvas.delete("green")
    
    

def Green():
    global colorTemp1,colorTemp2
    colorTemp1 = "#58D68D"
    colorTemp2 = "#82E0AA"
    canvas.config(bg=colorTemp1)
    canvas.delete("green")
    orange = Button(window, text="Color orange", font=('consolas', 20), command=Orange)
    canvas.create_window(canvas.winfo_width()/1.5, canvas.winfo_height()/2-100, window=orange, tag="orange")

def Orange():
    global colorTemp1,colorTemp2
    colorTemp1 = "#F5B041"
    colorTemp2 ="#F39C12"
    canvas.config(bg=colorTemp1)
    canvas.delete("orange")
    green = Button(window, text="Color green", font=('consolas', 20), command=Green)
    canvas.create_window(canvas.winfo_width()/3, canvas.winfo_height()/2-100, window=green, tag="green")

def restart_game():
    global diff_verif, diff_verif
    global SPEED
    global score_time2
    global snake, food, direction, score
    # Supprimer le message GAME OVER et le bouton de redémarrage
    canvas.delete("gameover")
    canvas.delete("restart_btn")
    canvas.delete("DiffMax")
    canvas.delete("DiffMed")
    canvas.delete("green")
    canvas.delete("orange")
    # Réinitialiser les variables
    snake = Snake()
    food = Food()
    direction = 'down'
    score = 0
    diff_verif = 1
    
    if SPEED == 50 or SPEED == 15:
        SPEED = 100
    score_time2 = score_time
    label.config(text="Score:{}".format(score))
    label2.config(text="Time:{}".format(score_time))

    # Ajouter la grille
    for i in range(0, GAME_WIDTH, GRID_SIZE):
        for j in range(0, GAME_HEIGHT, GRID_SIZE):
            if (i//GRID_SIZE + j//GRID_SIZE) % 2 == 0:
                color = colorTemp1
            else:
                color = colorTemp2
            canvas.create_rectangle(i, j, i+GRID_SIZE, j+GRID_SIZE, fill=color, outline="")
    # Réinitialiser la nourriture
    food.__init__()

    # restart
    next_turn(snake, food)


def restart_game2():
    global SPEED, diff_verif
    global score_time2
    global snake, food, direction, score
    # Supprimer le message GAME OVER et le bouton de redémarrage
    canvas.delete("gameover")
    canvas.delete("restart_btn")
    canvas.delete("DiffMax")
    canvas.delete("DiffMed")
    canvas.delete("green")
    canvas.delete("orange")
    # Réinitialiser les variables
    snake = Snake()
    food = Food()
    direction = 'down'
    score = 0
    diff_verif = 2
    if SPEED == 100 or SPEED == 15:
        SPEED = 50
    score_time2 = score_time
    label.config(text="Score:{}".format(score))
    label2.config(text="Time:{}".format(score_time))
    # Ajouter la grille
    for i in range(0, GAME_WIDTH, GRID_SIZE):
        for j in range(0, GAME_HEIGHT, GRID_SIZE):
            if (i//GRID_SIZE + j//GRID_SIZE) % 2 == 0:
                color = colorTemp1
            else:
                color = colorTemp2
            canvas.create_rectangle(i, j, i+GRID_SIZE, j+GRID_SIZE, fill=color, outline="")
    # Réinitialiser la nourriture
    food.__init__()

    # restart
    next_turn(snake, food)


def restart_game3():
    global SPEED, diff_verif
    global score_time2
    global snake, food, direction, score
    # Supprimer le message GAME OVER et le bouton de redémarrage
    canvas.delete("gameover")
    canvas.delete("restart_btn")
    canvas.delete("DiffMax")
    canvas.delete("DiffMed")
    canvas.delete("green")
    canvas.delete("orange")
    # Réinitialiser les variables
    snake = Snake()
    food = Food()
    direction = 'down'
    score = 0
    diff_verif = 3
    if SPEED == 100 or SPEED == 50:
        SPEED = 15
    score_time2 = score_time
    label.config(text="Score:{}".format(score))
    label2.config(text="Time:{}".format(score_time))
    # Ajouter la grille
    for i in range(0, GAME_WIDTH, GRID_SIZE):
        for j in range(0, GAME_HEIGHT, GRID_SIZE):
            if (i//GRID_SIZE + j//GRID_SIZE) % 2 == 0:
                color = colorTemp1
            else:
                color = colorTemp2
            canvas.create_rectangle(i, j, i+GRID_SIZE, j+GRID_SIZE, fill=color, outline="")
    # Réinitialiser la nourriture
    food.__init__()

    # restart
    next_turn(snake, food)


# Time
score_time = 0
score_time2 = 0
time_temp2 = 0

score = 0
direction = 'down'

label = Label(window, text="Score:{}".format(score), font=('consolas', 40))
label.pack()

label2 = Label(window, text="Time:{}".format(score_time2), font=('consolas', 40))
label2.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width/2) - (window_width/2))
y = int((screen_height/2) - (window_height/2))

window.geometry(f"{window_width}x{window_height}+{x}+{y}")

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()

next_turn (snake, food)

window.mainloop()