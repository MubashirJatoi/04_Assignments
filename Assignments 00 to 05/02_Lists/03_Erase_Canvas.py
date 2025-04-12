import tkinter as tk

CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase_objects(canvas, eraser):
    mouse_x = canvas.winfo_pointerx() - canvas.winfo_rootx()
    mouse_y = canvas.winfo_pointery() - canvas.winfo_rooty()

    overlapping_objects = canvas.find_overlapping(
        mouse_x, mouse_y, mouse_x + ERASER_SIZE, mouse_y + ERASER_SIZE
    )

    for overlapping_object in overlapping_objects:
        canvas.itemconfig(overlapping_object, fill="white")

def main():
    root = tk.Tk()
    canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT)
    canvas.pack()

    # Draw grid
    for row in range(CANVAS_HEIGHT // CELL_SIZE):
        for col in range(CANVAS_WIDTH // CELL_SIZE):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            canvas.create_rectangle(left_x, top_y, right_x, bottom_y, fill='blue')

    # Eraser
    eraser = canvas.create_rectangle(0, 0, ERASER_SIZE, ERASER_SIZE, fill='pink')

    def move_eraser(event):
        mouse_x = event.x
        mouse_y = event.y
        canvas.moveto(eraser, mouse_x, mouse_y)
        erase_objects(canvas, eraser)

    canvas.bind("<Motion>", move_eraser)

    root.mainloop()

if __name__ == '__main__':
    main()
