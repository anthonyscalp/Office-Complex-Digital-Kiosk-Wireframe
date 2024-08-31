import tkinter as tk
from tkinter import ttk, messagebox

# Create the main window
root = tk.Tk()
root.title("Digital Kiosk Interface")
root.geometry("1000x700")
root.configure(bg='#4B0082')

# Function to simulate search action
def search_action():
    query = search_entry.get()
    if query:
        messagebox.showinfo("Search", f"Searching for '{query}'...")
    else:
        messagebox.showwarning("Input Error", "Please enter a search term.")

# Function to switch levels
def switch_level(level):
    map_label.config(text=f"Current Level: {level}")
    map_canvas.delete("all")
    map_canvas.create_rectangle(50, 50, 400, 250, fill="lightblue", outline="black", width=2)
    map_canvas.create_rectangle(150, 100, 350, 200, fill="lightgray", outline="black")
    map_canvas.create_text(225, 150, text=f"Level {level} Map", font=("Arial", 14, "bold"))
    map_canvas.create_oval(60, 60, 100, 100, fill="red")

# Header Frame
header_frame = tk.Frame(root, bg='#4B0082')
header_frame.pack(fill=tk.X, pady=10)

# Digital Kiosk Header Label
header_label = tk.Label(header_frame, text="DIGITAL KIOSK INTERFACE", font=("Arial", 24, "bold"), fg="white", bg='#4B0082')
header_label.pack(pady=10)

# Main Content Frame
content_frame = tk.Frame(root, bg='white')
content_frame.pack(fill=tk.BOTH, expand=True)

# Map Frame (Central Area)
map_frame = tk.Frame(content_frame, bg='lightgray', bd=2, relief="sunken")
map_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

# Map Label (for "You Are Here")
map_label = tk.Label(map_frame, text="Current Level: 1", font=("Arial", 16, "bold"), bg='lightgray')
map_label.pack(anchor='nw', padx=10, pady=5)

# Display a placeholder map with dynamic "You Are Here" marker
map_canvas = tk.Canvas(map_frame, bg='white', width=500, height=400)
map_canvas.pack(padx=10, pady=10)

# Draw a simple room layout on the canvas
map_canvas.create_rectangle(50, 50, 400, 250, fill="lightblue", outline="black", width=2)
map_canvas.create_rectangle(150, 100, 350, 200, fill="lightgray", outline="black")
map_canvas.create_text(225, 150, text="Office", font=("Arial", 14, "bold"))
map_canvas.create_oval(60, 60, 100, 100, fill="red")

# Side Panel Frames
side_panel_frame = tk.Frame(content_frame, bg='#4B0082', width=200)
side_panel_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

# Search Frame
search_frame = tk.Frame(side_panel_frame, bg='#4B0082')
search_frame.pack(pady=20)

# Enhanced Search Options Label
search_label = tk.Label(search_frame, text="Search Options", font=("Arial", 18, "bold"), fg="white", bg='#4B0082')
search_label.pack(pady=10)

# Search Entry Box
search_entry = ttk.Entry(search_frame, width=20)
search_entry.pack(pady=10)

# Search Button
search_button = ttk.Button(search_frame, text="Search", command=search_action)
search_button.pack(pady=5)

# Level Selection Frame
level_frame = tk.Frame(search_frame, bg='#4B0082')
level_frame.pack(pady=20)

# Level 1 and Level 2 Buttons with functionality
level1_button = ttk.Button(level_frame, text="Level 1", width=15, command=lambda: switch_level(1))
level1_button.pack(pady=5)

level2_button = ttk.Button(level_frame, text="Level 2", width=15, command=lambda: switch_level(2))
level2_button.pack(pady=5)

# Quick Search Feature Frame
quick_search_frame = tk.Frame(side_panel_frame, bg='#4B0082')
quick_search_frame.pack(pady=20)

# Quick Search Feature Label
quick_search_label = tk.Label(quick_search_frame, text="Quick Search", font=("Arial", 18, "bold"), fg="white", bg='#4B0082')
quick_search_label.pack(pady=10)

# Placeholder buttons for quick search icons (text replaced by actual icon images if available)
icon_texts = ["Restrooms", "Workstations", "Kitchens", "Meeting Rooms"]

for text in icon_texts:
    icon_button = ttk.Button(quick_search_frame, text=text, width=20)
    icon_button.pack(pady=5)

# Run the application
root.mainloop()
