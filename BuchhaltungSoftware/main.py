import tkinter as tk
from Views.view import SalesView

def main():
    root = tk.Tk()
    root.title("Umsatzanalyse")
    root.geometry("800x600")

    app = SalesView(root)
    root.mainloop()

if __name__ == "__main__":
    main()