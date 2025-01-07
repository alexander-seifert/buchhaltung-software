import tkinter as tk
from Views.view import SalesView


def main():
    root = tk.Tk()
    root.title("Umsatzanalyse")
    root.geometry("700x300")
    root.resizable(True, False)  # Breite anpassbar, Hoehe nicht

    app = SalesView(root)
    root.mainloop()


if __name__ == "__main__":
    main()