import tkinter as tk
from tkinter import font
from tkinter import ttk

class FontViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Font Viewer")
        self.root.geometry("800x600")  # Set larger window size
        self.root.configure(bg="#eef2f7")  # Update background color

        # Create font family list
        self.font_families = sorted(font.families())

        # Custom style
        self.style = ttk.Style()
        self.style.configure("TLabel", background="#eef2f7", font=("Arial", 10))
        self.style.configure("TEntry", font=("Arial", 10))
        self.style.configure("TButton", font=("Arial", 10, "bold"))
        self.style.configure("TCheckbutton", background="#eef2f7", font=("Arial", 10))
        self.style.configure("TCombobox", font=("Arial", 10))

        # Search bar for fonts
        search_frame = tk.Frame(root, bg="#eef2f7")
        tk.Label(search_frame, text="Search Font:", bg="#eef2f7", font=("Arial", 12, "bold")).pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        search_entry.bind("<KeyRelease>", self.filter_fonts)
        search_frame.pack(fill=tk.X, pady=(10, 5), padx=10)

        # Dropdown menu for selecting fonts
        font_label = ttk.Label(root, text="Select Font:")
        font_label.pack(pady=(5, 0))
        self.selected_font = tk.StringVar(value=self.font_families[0])
        self.font_dropdown = ttk.Combobox(root, textvariable=self.selected_font, values=self.font_families, state="readonly")
        self.font_dropdown.bind("<<ComboboxSelected>>", self.update_font)
        self.font_dropdown.pack(fill=tk.X, pady=5, padx=10)

        # Text size selection
        size_frame = tk.Frame(root, bg="#eef2f7")
        ttk.Label(size_frame, text="Font Size:").pack(side=tk.LEFT, padx=5)
        self.font_size = tk.IntVar(value=20)
        size_spinbox = ttk.Spinbox(size_frame, from_=8, to=200, textvariable=self.font_size, width=5, command=self.update_font)
        size_spinbox.pack(side=tk.LEFT)
        size_frame.pack(pady=(5, 10), padx=10)

        # Text style options (bold, italic)
        style_frame = tk.Frame(root, bg="#eef2f7")
        self.bold_var = tk.BooleanVar(value=False)
        self.italic_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(style_frame, text="Bold", variable=self.bold_var, command=self.update_font).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(style_frame, text="Italic", variable=self.italic_var, command=self.update_font).pack(side=tk.LEFT, padx=5)
        style_frame.pack(pady=10)

        # Text box to display font
        text_box_frame = tk.Frame(root, bg="#eef2f7")
        self.text_box = tk.Text(text_box_frame, height=10, wrap="word", font=("Arial", 12), relief=tk.GROOVE, bd=2)
        self.text_box.insert("1.0", "Sample text to view fonts")
        self.text_box.pack(fill="both", expand=True, padx=10, pady=10)
        text_box_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        # Copy text button
        button_frame = tk.Frame(root, bg="#eef2f7")
        copy_button = tk.Button(button_frame, text="Copy Text", command=self.copy_text, bg="#007acc", fg="white", font=("Arial", 10, "bold"), relief=tk.FLAT, padx=10, pady=5)
        copy_button.pack()
        button_frame.pack(pady=10)

        # Apply initial font
        self.update_font()

    def filter_fonts(self, event):
        search_term = self.search_var.get().lower()
        filtered_fonts = [font for font in self.font_families if search_term in font.lower()]
        self.font_dropdown["values"] = filtered_fonts
        if filtered_fonts:
            self.font_dropdown.set(filtered_fonts[0])

    def update_font(self, *args):
        font_family = self.selected_font.get()
        font_size = self.font_size.get()
        weight = "bold" if self.bold_var.get() else "normal"
        slant = "italic" if self.italic_var.get() else "roman"
        text_font = font.Font(family=font_family, size=font_size, weight=weight, slant=slant)
        self.text_box.configure(font=text_font)

    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text_box.get("1.0", "end-1c"))
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = FontViewer(root)
    root.mainloop()
