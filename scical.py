import tkinter as tk
import math

class CalculatorApp:
   
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("SCI-CA")
        self.root.geometry("500x850")

        self.memory_value = None  # Store memory value
        self.use_degrees = True  # Default mode is degrees

        self.screen = tk.StringVar()
        self.create_widgets()
        
        self.root.mainloop()

    def create_widgets(self):
        """Creates and places the widgets in the application."""
        entry = tk.Entry(self.root, textvar=self.screen, font="lucida 20 bold",
                         bd=10, relief=tk.SUNKEN, justify="right", state="readonly")
        entry.pack(fill=tk.BOTH, padx=10, pady=10)

        self.mode_label = tk.Label(self.root, text="Mode: Degrees", font="lucida 12 bold")
        self.mode_label.pack(pady=5)

        toggle_button = tk.Button(self.root, text="Toggle Degrees/Radians",
                                  font="lucida 12", command=self.toggle_mode)
        toggle_button.pack(pady=5)

        button_frame = tk.Frame(self.root)
        button_frame.pack()

        buttons = [
            ["1", "2", "3", "/"],
            ["4", "5", "6", "*"],
            ["7", "8", "9", "-"],
            ["C", "0", ".", "+"],
            ["sin", "cos", "tan", "="],
            ["log", "ln", "sqrt", "**"],
            ["(", ")", "π", "e"],
            ["M", "MR"]  # Memory buttons
        ]
        
        for i, row in enumerate(buttons):
            for j, btn_text in enumerate(row):
                if btn_text in {"sin", "cos", "tan", "log", "ln", "sqrt"}:
                    btn = tk.Button(button_frame, text=btn_text, font="lucida 15 bold", padx=20, pady=15,
                                    command=lambda func=btn_text: self.advanced_function(func))
                elif btn_text == "M":
                    btn = tk.Button(button_frame, text=btn_text, font="lucida 15 bold", padx=20, pady=15,
                                    command=self.store_memory)
                elif btn_text == "MR":
                    btn = tk.Button(button_frame, text=btn_text, font="lucida 15 bold", padx=20, pady=15,
                                    command=self.recall_memory)
                elif btn_text in {"π", "e"}:
                    btn = tk.Button(button_frame, text=btn_text, font="lucida 15 bold", padx=20, pady=15,
                                    command=lambda const=btn_text: self.screen.set(
                                        self.screen.get() + str(math.pi if const == "π" else math.e)))
                else:
                    btn = tk.Button(button_frame, text=btn_text, font="lucida 15 bold", padx=20, pady=15)
                    btn.bind("<Button-1>", self.click)
                btn.grid(row=i, column=j, padx=5, pady=5)

        self.screen.set("")

    def click(self, event):
        """Handles button clicks for numbers and operators."""
        text = event.widget.cget("text")
        if text == "=":
            try:
                result = eval(self.screen.get())
                self.screen.set(result)
            except Exception:
                self.screen.set("Error")
        elif text == "C":
            self.screen.set("")
        else:
            self.screen.set(self.screen.get() + text)

    def advanced_function(self, func):
        """Handles advanced mathematical operations."""
        try:
            value = float(self.screen.get())
            if self.use_degrees and func in {"sin", "cos", "tan"}:
                value = math.radians(value)
            result = getattr(math, func)(value)
            self.screen.set(result)
        except Exception:
            self.screen.set("Error")

    def store_memory(self):
        """Stores the current value in memory."""
        try:
            self.memory_value = eval(self.screen.get())
            self.screen.set(f"Stored: {self.memory_value}")
        except Exception:
            self.screen.set("Error")

    def recall_memory(self):
        """Recalls the stored memory value."""
        if self.memory_value is not None:
            self.screen.set(self.memory_value)
        else:
            self.screen.set("No Value Stored")

    def toggle_mode(self):
        """Toggles between degree and radian mode."""
        self.use_degrees = not self.use_degrees
        self.mode_label.config(text="Mode: Degrees" if self.use_degrees else "Mode: Radians")

if __name__ == "__main__":
    CalculatorApp()
