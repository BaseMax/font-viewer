import tkinter as tk
from tkinter import font

class FontViewer:
    def __init__(self, root):
        self.root = root
        self.root.title("GUI Font Viewer")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        self.font_families = sorted(font.families())

        self.selected_font = tk.StringVar(value=self.font_families[0])
        font_label = tk.Label(root, text="Select Font:", bg="#f0f0f0", font=("Arial", 10))
        font_label.pack(pady=(10, 0))
        self.font_dropdown = tk.OptionMenu(root, self.selected_font, *self.font_families, command=self.update_font)
        self.font_dropdown.pack(pady=(0, 10))

        self.font_size = tk.IntVar(value=20)
        size_frame = tk.Frame(root, bg="#f0f0f0")
        tk.Label(size_frame, text="Font Size:", bg="#f0f0f0", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Spinbox(size_frame, from_=8, to=200, textvariable=self.font_size, width=5, command=self.update_font).pack(side=tk.LEFT)
        size_frame.pack(pady=(0, 10))

        self.bold_var = tk.BooleanVar(value=False)
        self.italic_var = tk.BooleanVar(value=False)
        style_frame = tk.Frame(root, bg="#f0f0f0")
        tk.Checkbutton(style_frame, text="Bold", variable=self.bold_var, command=self.update_font, bg="#f0f0f0", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        tk.Checkbutton(style_frame, text="Italic", variable=self.italic_var, command=self.update_font, bg="#f0f0f0", font=("Arial", 10)).pack(side=tk.LEFT, padx=5)
        style_frame.pack(pady=(0, 10))

        text_box_frame = tk.Frame(root, bg="#f0f0f0")
        self.text_box = tk.Text(text_box_frame, height=10, wrap="word", font=("Arial", 12))
        self.text_box.insert("1.0", "Sample text to view fonts")
        self.text_box.pack(fill="both", expand=True, padx=10, pady=10)
        text_box_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        button_frame = tk.Frame(root, bg="#f0f0f0")
        copy_button = tk.Button(button_frame, text="Copy Text", command=self.copy_text, bg="#0078D7", fg="white", font=("Arial", 10), relief="flat")
        copy_button.pack()
        button_frame.pack(pady=10)

        self.update_font()

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
