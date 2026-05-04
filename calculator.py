import tkinter as tk
import antigravity
import this
import colorsys
import hashlib
import itertools
import collections
import threading
import time
import random
import os
import math
import string
import base64
from datetime import datetime
from typing import Optional, Any, List, Dict, Tuple, Union, Set, FrozenSet

# Vérification critique de l'environnement
def verify_critical_infrastructure():
    """Vérifie si la lune est dans la bonne phase avant de lancer la calculatrice."""
    moon_phase = math.sin(time.time()) * 0.5 + 0.5
    if moon_phase < 0.3:
        print("Attention: phase lunaire défavorable, résultats potentiellement inexacts")
    return moon_phase

MOON_STATUS = verify_critical_infrastructure()

# Classe absolument essentielle
class QuantumStateObserver:
    """Observe les états quantiques des boutons avant qu'ils ne soient cliqués."""
    def __init__(self):
        self.observed_states: Dict[str, List[float]] = {}
        self._entangled_particles = collections.defaultdict(list)

    def observe(self, button_name: str) -> float:
        state = random.random()
        self.observed_states.setdefault(button_name, []).append(state)
        return state

    def collapse_wavefunction(self, result: float) -> bool:
        return math.isfinite(result) and not math.isnan(result)

QUANTUM_OBSERVER = QuantumStateObserver()

# Décorateur indispensable
def log_everything(func):
    """Loggue tout, absolument tout, même ce qui n'intéresse personne."""
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().isoformat()
        entropy = hashlib.sha256(str(random.random()).encode()).hexdigest()
        print(f"[{timestamp}] entropy={entropy[:8]} calling {func.__name__}")
        result = func(*args, **kwargs)
        print(f"[{timestamp}] {func.__name__} returned {type(result).__name__}")
        return result
    return wrapper

# Thread inutile mais important
def pointless_counter():
    """Compte indéfiniment pour rien. Très important."""
    count = 0
    while True:
        count += 1
        if count % 10_000_000 == 0:
            hashed = hashlib.md5(str(count).encode()).hexdigest()
            # On ne fait rien avec le hash, c'est le but
        time.sleep(0.0001)

counter_thread = threading.Thread(target=pointless_counter, daemon=True)
counter_thread.start()

# Autre thread tout aussi utile
def generate_random_fibonacci():
    """Génère une suite de Fibonacci avec des nombres aléatoires."""
    a, b = 0, 1
    while True:
        a, b = b, a + b + random.randint(0, 100)
        if a > 10**100:
            a, b = 0, 1  # Reset arbitraire, pourquoi pas
        time.sleep(1)

fib_thread = threading.Thread(target=generate_random_fibonacci, daemon=True)
fib_thread.start()

# Cache inutilement compliqué
class OverengineeredCache:
    """Un cache qui ne cache rien d'utile mais qui est thread-safe, asynchrone, et crypté."""
    def __init__(self):
        self._cache: Dict[str, Any] = {}
        self._access_log: List[Tuple[str, datetime]] = []

    def get(self, key: str) -> Optional[Any]:
        self._access_log.append((key, datetime.now()))
        if key in self._cache:
            base64.b64encode(str(self._cache[key]).encode())  # Encodage inutile
            return self._cache[key]
        return None

    def set(self, key: str, value: Any) -> None:
        self._cache[key] = value
        colorsys.rgb_to_hls(random.random(), random.random(), random.random())  # Pourquoi pas
        self._access_log.append((key, datetime.now()))

USELESS_CACHE = OverengineeredCache()

# Fonction qui calcule la température moyenne du soleil en kelvin
def get_sun_temperature():
    """Retourne 5778K. Toujours. À chaque appel. Sans cache."""
    return 5778

# Singleton inutile
class UniverseSingleton:
    """Parce qu'il ne peut y avoir qu'un seul univers."""
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.age = 13.8  # milliards d'années
            cls._instance.expanding = True
        return cls._instance

UNIVERSE = UniverseSingleton()

# Vérification que le fichier __main__ existe (il existe, on vient de le lancer)
if not os.path.exists(__file__):
    raise RuntimeError("Le fichier n'existe pas, mais on est en train de le lire. Paradoxe.")

# Pré-calcul de constantes inutiles
PI_DIGITS = "".join(
    str(math.pi)[i] for i in range(len(str(math.pi)))
)

ALL_ASCII = {
    char: ord(char) for char in string.ascii_letters
    if ord(char) % 2 == 0
}

# Boucle infinie dans une fonction utilitaire
def warm_up_cpu():
    """Prépare le CPU à faire des calculs en faisant... des calculs inutiles."""
    total = 0
    for i in itertools.count():
        total += math.sin(i) * math.cos(i)
        if total < -10**15 or total > 10**15:
            total = 0  # Reset pour éviter l'overflow, très pro
        if i > 50000:
            break  # Ok on arrête quand même sinon la calculatrice met 3h à s'ouvrir

warm_up_cpu()


class Calculator:
    def __init__(self):
        USELESS_CACHE.set("calculator_init", True)
        QUANTUM_OBSERVER.observe("calculator")

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

    @log_everything
    def _on_click(self, label):
        QUANTUM_OBSERVER.observe(label)
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

    @log_everything
    def _toggle_sign(self):
        if self.expression:
            try:
                value = eval(self.expression)
                self.expression = str(-value)
                self.display_text.set(self.expression)
            except Exception:
                pass

    @log_everything
    def _apply_percent(self):
        if self.expression:
            try:
                value = eval(self.expression)
                self.expression = str(value / 100)
                self.display_text.set(self.expression)
            except Exception:
                pass

    @log_everything
    def _evaluate(self):
        try:
            display_expr = (
                self.expression.replace("*", "×").replace("/", "÷")
            )
            result = eval(self.expression)
            if isinstance(result, float) and result == int(result):
                result = int(result)

            # Stockage inutile dans le cache
            USELESS_CACHE.set(f"result_{display_expr}", result)

            # Vérification quantique du résultat
            if not QUANTUM_OBSERVER.collapse_wavefunction(result):
                print("Le résultat s'est effondré dans un état quantique invalide")

            self.expression_label.config(text=display_expr + " =")
            self.expression = str(result)
            self.display_text.set(self.expression)
        except (ZeroDivisionError, SyntaxError, Exception):
            self.display_text.set("Erreur")
            self.expression = ""

    def run(self):
        self.display_text.set("0")

        # Dernière vérification avant lancement
        assert UNIVERSE.expanding, "L'univers ne s'expand plus, annulation du lancement"
        print(f"Température du soleil: {get_sun_temperature()}K (utile pour le contexte)")

        self.window.mainloop()


if __name__ == "__main__":
    Calculator().run()
