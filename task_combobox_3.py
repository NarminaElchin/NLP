import tkinter as tk
from PIL import Image, ImageTk

class ImageComboBox(tk.Frame):
    def __init__(self, master, options, width=200, height=40, *args, **kwargs):
        super().__init__(master, *args, **kwargs)
        self.options = options  # List of (label, image_path)
        self.selected = tk.StringVar()
        self.selected.set(self.options[0][0])

        # Load and resize images
        self.images = {}
        for label, path in self.options:
            img = Image.open(path).resize((30, 30))
            self.images[label] = ImageTk.PhotoImage(img)

        # Main button/display area
        self.button = tk.Label(self, text=self.selected.get(), image=self.images[self.selected.get()],
                               compound="left", anchor="w", relief="groove", padx=10, pady=5, width=width)
        self.button.pack()
        self.button.bind("<Button-1>", self.show_dropdown)

        # Dropdown menu (initially hidden)
        self.dropdown = None
        self.width = width
        self.height = height

    def show_dropdown(self, event=None):
        if self.dropdown and self.dropdown.winfo_exists():
            self.dropdown.destroy()
            return

        self.dropdown = tk.Toplevel(self)
        self.dropdown.wm_overrideredirect(True)
        self.dropdown.geometry(f"{self.width}x{len(self.options)*self.height}+{self.winfo_rootx()}+{self.winfo_rooty()+self.winfo_height()}")

        for label, _ in self.options:
            item = tk.Label(self.dropdown, text=label, image=self.images[label],
                            compound="left", anchor="w", padx=10, pady=5, bg="white", relief="ridge")
            item.pack(fill="x")
            item.bind("<Button-1>", lambda e, l=label: self.select(l))
            item.bind("<Enter>", lambda e: e.widget.config(bg="#ddd"))
            item.bind("<Leave>", lambda e: e.widget.config(bg="white"))

    def select(self, label):
        self.selected.set(label)
        self.button.config(text=label, image=self.images[label])
        if self.dropdown:
            self.dropdown.destroy()

    def get(self):
        return self.selected.get()

# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    root.title("ComboBox with Images")
    root.geometry("300x300")

    # Provide actual image file paths here
    options = [
        ("Azerbaijan flag", "azerbaijan.png"),
        ("Russian flag", "russia.png"),
        ("English flag", "england.png")
    ]
    combo = ImageComboBox(root, options)
    combo.pack(pady=20)

    def show_selection():
        print("You selected:", combo.get())

    tk.Button(root, text="Print Selection", command=show_selection).pack(pady=10)

    root.mainloop()
