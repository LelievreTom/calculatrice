import tkinter as tk


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculatrice")
        self.window.geometry("320x480")
        self.window.resizable(False, False)

        self.expression = ""
        self.display_text = tk.StringVar()

        self._build_display()
        self._build_buttons()

    def _build_display(self):
        display_frame = tk.Frame(self.window, bg="#1e1e1e")
        display_frame.pack(expand=True, fill="both")

        self.expression_label = tk.Label(
            display_frame,
            text="",
            font=("Segoe UI", 16),
            fg="#aaaaaa",
            bg="#1e1e1e",
            anchor="e",
        )
        self.expression_label.pack(expand=True, fill="both", padx=10)

        display = tk.Entry(
            display_frame,
            textvariable=self.display_text,
            font=("Segoe UI", 36),
            fg="white",
            bg="#1e1e1e",
            bd=0,
            justify="right",
            state="readonly",
        )
        display.pack(expand=True, fill="both", padx=10)

    def _build_buttons(self):
        buttons_frame = tk.Frame(self.window, bg="#2d2d2d")
        buttons_frame.pack(expand=True, fill="both")

        buttons = [
            ("C", "±", "%", "÷"),
            ("7", "8", "9", "×"),
            ("4", "5", "6", "-"),
            ("1", "2", "3", "+"),
            ("0", ".", "⌫", "="),
        ]

        for r, row in enumerate(buttons):
            buttons_frame.rowconfigure(r, weight=1)
            for c, label in enumerate(row):
                buttons_frame.columnconfigure(c, weight=1)
                btn = tk.Button(
                    buttons_frame,
                    text=label,
                    font=("Segoe UI", 22),
                    bd=0,
                    cursor="hand2",
                    command=lambda lbl=label: self._on_click(lbl),
                )
                self._style_button(btn, label)
                btn.grid(row=r, column=c, sticky="nsew", padx=2, pady=2)

    def _style_button(self, btn, label):
        if label in ("C", "⌫"):
            bg, fg = "#505050", "white"
        elif label in ("÷", "×", "-", "+", "%", "="):
            bg, fg = "#ff9f0a", "white"
        elif label == "±":
            bg, fg = "#505050", "white"
        else:
            bg, fg = "#3a3a3a", "white"
        btn.config(bg=bg, fg=fg, activebackground="#5a5a5a")

    def _on_click(self, label):
        if label == "C":
            self.expression = ""
            self.display_text.set("0")
            self.expression_label.config(text="")
        elif label == "⌫":
            self.expression = self.expression[:-1]
            self.display_text.set(self.expression if self.expression else "0")
        elif label == "=":
            self._evaluate()
        elif label == "±":
            self._toggle_sign()
        elif label == "%":
            self._apply_percent()
        elif label == "÷":
            self._append_operator("/")
        elif label == "×":
            self._append_operator("*")
        else:
            self.expression += label
            self.display_text.set(self.expression)

    def _append_operator(self, op):
        if self.expression and self.expression[-1] in "+-*/":
            self.expression = self.expression[:-1]
        self.expression += op
        self.display_text.set(self.expression)

    def _toggle_sign(self):
        if self.expression:
            try:
                value = eval(self.expression)
                self.expression = str(-value)
                self.display_text.set(self.expression)
            except Exception:
                pass

    def _apply_percent(self):
        if self.expression:
            try:
                value = eval(self.expression)
                self.expression = str(value / 100)
                self.display_text.set(self.expression)
            except Exception:
                pass

    def _evaluate(self):
        try:
            display_expr = (
                self.expression.replace("*", "×").replace("/", "÷")
            )
            result = eval(self.expression)
            if isinstance(result, float) and result == int(result):
                result = int(result)
            self.expression_label.config(text=display_expr + " =")
            self.expression = str(result)
            self.display_text.set(self.expression)
        except (ZeroDivisionError, SyntaxError, Exception):
            self.display_text.set("Erreur")
            self.expression = ""

    def run(self):
        self.display_text.set("0")
        self.window.mainloop()


if __name__ == "__main__":
    Calculator().run()
