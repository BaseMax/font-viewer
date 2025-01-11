import tkinter as tk
from tkinter import ttk, font

class FontViewer:
    BG_COLOR = "#eef2f7"
    TEXT_FONT = ("Arial", 12)
    LABEL_FONT = ("Arial", 10)
    BUTTON_FONT = ("Arial", 10, "bold")
    SEARCH_LABEL_FONT = ("Arial", 12, "bold")
    RTL_TAG = "rtl"
    LTR_TAG = "ltr"
    BUTTON_COLOR = "#007acc"
    BUTTON_TEXT_COLOR = "white"
    BUTTON_PADDING = {"padx": 10, "pady": 5}

    def __init__(self, root):
        self.root = root
        self.root.title("GUI Font Viewer")
        self.root.geometry("800x600")
        self.root.configure(bg=self.BG_COLOR)

        self.font_families = sorted(font.families())

        self.style = ttk.Style()
        self.style.configure("TLabel", background=self.BG_COLOR, font=self.LABEL_FONT)
        self.style.configure("TEntry", font=self.LABEL_FONT)
        self.style.configure("TButton", font=self.BUTTON_FONT)
        self.style.configure("TCheckbutton", background=self.BG_COLOR, font=self.LABEL_FONT)
        self.style.configure("TCombobox", font=self.LABEL_FONT)

        self._create_widgets()
        self.update_font()
        self.update_direction()

    def _create_widgets(self):
        search_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        tk.Label(search_frame, text="Search Font:", bg=self.BG_COLOR, font=self.SEARCH_LABEL_FONT).pack(side=tk.LEFT, padx=5)
        self.search_var = tk.StringVar()
        search_entry = ttk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=5)
        search_entry.bind("<KeyRelease>", self.filter_fonts)
        search_frame.pack(fill=tk.X, pady=(10, 5), padx=10)

        font_label = ttk.Label(self.root, text="Select Font:")
        font_label.pack(pady=(5, 0))
        self.selected_font = tk.StringVar(value=self.font_families[0])
        self.font_dropdown = ttk.Combobox(self.root, textvariable=self.selected_font, values=self.font_families, state="readonly")
        self.font_dropdown.bind("<<ComboboxSelected>>", self.update_font)
        self.font_dropdown.pack(fill=tk.X, pady=5, padx=10)

        size_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        ttk.Label(size_frame, text="Font Size:").pack(side=tk.LEFT, padx=5)
        self.font_size = tk.IntVar(value=20)
        size_spinbox = ttk.Spinbox(size_frame, from_=8, to=200, textvariable=self.font_size, width=5, command=self.update_font)
        size_spinbox.pack(side=tk.LEFT)
        size_frame.pack(pady=(5, 10), padx=10)

        style_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        self.bold_var = tk.BooleanVar(value=False)
        self.italic_var = tk.BooleanVar(value=False)
        ttk.Checkbutton(style_frame, text="Bold", variable=self.bold_var, command=self.update_font).pack(side=tk.LEFT, padx=5)
        ttk.Checkbutton(style_frame, text="Italic", variable=self.italic_var, command=self.update_font).pack(side=tk.LEFT, padx=5)
        style_frame.pack(pady=10)

        direction_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        ttk.Label(direction_frame, text="Text Direction:").pack(side=tk.LEFT, padx=5)
        self.direction_var = tk.StringVar(value="LTR")
        rtl_button = ttk.Radiobutton(direction_frame, text="RTL", variable=self.direction_var, value="RTL", command=self.update_direction)
        rtl_button.pack(side=tk.LEFT, padx=5)
        ltr_button = ttk.Radiobutton(direction_frame, text="LTR", variable=self.direction_var, value="LTR", command=self.update_direction)
        ltr_button.pack(side=tk.LEFT, padx=5)
        direction_frame.pack(pady=10)

        text_box_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        self.text_box = tk.Text(text_box_frame, height=10, wrap="word", font=self.TEXT_FONT, relief=tk.GROOVE, bd=2)
        self.text_box.insert("1.0", "Sample text to view fonts")
        self.text_box.pack(fill="both", expand=True, padx=10, pady=10)
        text_box_frame.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        button_frame = tk.Frame(self.root, bg=self.BG_COLOR)
        copy_button = tk.Button(button_frame, text="Copy Text", command=self.copy_text, bg=self.BUTTON_COLOR, fg=self.BUTTON_TEXT_COLOR, font=self.BUTTON_FONT, relief=tk.FLAT, **self.BUTTON_PADDING)
        copy_button.pack()
        button_frame.pack(pady=10)

        self.text_box.tag_configure(self.LTR_TAG, justify="left")
        self.text_box.tag_configure(self.RTL_TAG, justify="right")

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

    def update_direction(self):
        direction = self.direction_var.get()
        tag = self.RTL_TAG if direction == "RTL" else self.LTR_TAG
        self.text_box.tag_remove(self.LTR_TAG, "1.0", "end")
        self.text_box.tag_remove(self.RTL_TAG, "1.0", "end")
        self.text_box.tag_add(tag, "1.0", "end")

    def copy_text(self):
        self.root.clipboard_clear()
        self.root.clipboard_append(self.text_box.get("1.0", "end-1c"))
        self.root.update()

if __name__ == "__main__":
    root = tk.Tk()
    app = FontViewer(root)
    root.mainloop()
