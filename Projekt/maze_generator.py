import random
import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import simpledialog, messagebox, filedialog
import pickle

WIDTH, HEIGHT = 5, 5

LEFT, RIGHT, TOP, BOTTOM = (-1, 0), (1, 0), (0, -1), (0, 1)
directions = [LEFT, RIGHT, TOP, BOTTOM]



def get_maze_size():
    """Prompt the user to enter the maze dimensions."""

    global WIDTH, HEIGHT
    root = tk.Tk()
    root.withdraw()

    WIDTH = simpledialog.askinteger("Maze size",
                                    "Enter maze width:",
                                    minvalue=5)
    HEIGHT = simpledialog.askinteger("Maze size",
                                     "Enter maze height:",
                                     minvalue=5)
    root.destroy()

def initialize_maze():
    """Initialize the maze with all walls intact."""

    grid = np.zeros((HEIGHT, WIDTH), int)
    horizontal_walls = np.ones((HEIGHT + 1, WIDTH), dtype=bool)
    vertical_walls = np.ones((HEIGHT, WIDTH + 1), dtype=bool)
    vertical_walls[0][0] = False
    vertical_walls[HEIGHT - 1][WIDTH] = False
    return grid, horizontal_walls, vertical_walls


def generate_maze(grid, horizontal_walls, vertical_walls):
    """Generate the maze using a DFS algorithm."""

    visited_cells = 1
    total_cells = HEIGHT * WIDTH
    stack = []
    currentX, currentY = 0, 0
    grid[currentY][currentX] = 1

    while visited_cells < total_cells:
        random.shuffle(directions)
        moved = False

        for direction in directions:
            nextX, nextY = currentX + direction[0], currentY + direction[1]

            if (0 <= nextX < WIDTH and
                0 <= nextY < HEIGHT and
                grid[nextY][nextX] == 0):

                stack.append((currentX, currentY))
                currentX, currentY = nextX, nextY
                visited_cells += 1

                if direction == LEFT:
                    vertical_walls[currentY][currentX + 1] = False
                elif direction == RIGHT:
                    vertical_walls[currentY][currentX] = False
                elif direction == TOP:
                    horizontal_walls[currentY + 1][currentX] = False
                elif direction == BOTTOM:
                    horizontal_walls[currentY][currentX] = False

                grid[currentY][currentX] = 1
                moved = True
                break

        if not moved:
            currentX, currentY = stack.pop()


def visualize_maze(horizontal_walls, vertical_walls):
    """Visualize the maze using matplotlib."""

    fig, ax = plt.subplots(figsize=(8, 8))

    for y in range(HEIGHT + 1):
        for x in range(WIDTH):
            if horizontal_walls[y, x]:
                ax.plot([x, x + 1], [y, y], color="black", lw=2)

    for y in range(HEIGHT):
        for x in range(WIDTH + 1):
            if vertical_walls[y, x]:
                ax.plot([x, x], [y, y + 1], color="black", lw=2)

    ax.set_xlim(-0.5, WIDTH + 0.5)
    ax.set_ylim(-0.5, HEIGHT + 0.5)
    ax.set_aspect("equal")
    ax.axis("off")
    plt.gca().invert_yaxis()
    plt.show()


def save_maze(horizontal_walls, vertical_walls):
    """Save the maze to a .maze file."""
    file_path = filedialog.asksaveasfilename(defaultextension=".maze",
        filetypes=[("Maze Files", "*.maze")])

    if file_path:
        with open(file_path, 'wb') as file:
            pickle.dump((WIDTH, HEIGHT, horizontal_walls, vertical_walls), file)
        messagebox.showinfo("Save Maze", "Maze saved successfully!")


def load_maze():
    """Load the maze from a .maze file."""

    global WIDTH, HEIGHT
    file_path = filedialog.askopenfilename(filetypes=[("Maze Files", "*.maze")])
    if file_path:
        with open(file_path, 'rb') as file:
            WIDTH, HEIGHT, horizontal_walls, vertical_walls = pickle.load(file)
        messagebox.showinfo("Load Maze", "Maze loaded successfully!")
        visualize_maze(horizontal_walls, vertical_walls)


def main_menu():
    """Display the main menu for the maze generator application."""

    root = tk.Tk()
    root.title("Maze Generator")
    root.geometry("280x200")

    def on_generate():
        """Handle the Generate Maze button click event."""

        get_maze_size()
        global grid, horizontal_walls, vertical_walls
        grid, horizontal_walls, vertical_walls = initialize_maze()
        generate_maze(grid, horizontal_walls, vertical_walls)
        visualize_maze(horizontal_walls, vertical_walls)

    def on_save():
        try:
            if ('horizontal_walls' not in globals() or
                    'vertical_walls' not in globals()):
                raise NameError("The maze has not been generated yet.")

            save_maze(horizontal_walls, vertical_walls)

        except NameError as e:
            messagebox.showerror("Error", str(e))

    def on_exit():
        plt.close('all')
        root.quit()
        root.destroy()



    tk.Button(root, text="Generate Maze",
              command=on_generate, width=20).pack(pady=10)
    tk.Button(root, text="Save Maze", command=on_save, width=20).pack(pady=10)
    tk.Button(root, text="Load Maze", command=load_maze, width=20).pack(pady=10)
    tk.Button(root, text="Exit", command=on_exit, width=20).pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    main_menu()
