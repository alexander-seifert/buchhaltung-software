# main.py
import tkinter as tk
from Views.view import SalesView

def main():
    root = tk.Tk()
    root.title("Umsatzanalyse")
    app = SalesView(root)
    root.mainloop()

if __name__ == "__main__":
    main()