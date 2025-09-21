import tkinter as tk


def on_key_press(event):
    """Function to handle key presses."""
    print(f"Key pressed: {event.keysym}")
    if event.keysym == "a":
        print("Moving up!")
        # Add your action here, e.g., move a canvas object
    elif event.keysym == "d":
        print("Moving down!")
        # Add your action here
    # ... and so on for other keys


root = tk.Tk()
root.title("Canvas Key Press Example")

canvas = tk.Canvas(root, width=400, height=300, bg="lightgray")
canvas.pack()

# Give the canvas focus so it can receive key events
canvas.focus_set()

# Bind the <Key> event to the on_key_press function for all keys
canvas.bind("<Key>", on_key_press)

# Alternatively, bind specific keys:
# canvas.bind("<Up>", on_key_press)
# canvas.bind("<Down>", on_key_press)
# canvas.bind("<a>", on_key_press) # For the 'a' key

root.mainloop()