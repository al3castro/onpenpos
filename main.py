from windows import MainWindow
import sqlite3

class Aplication():
    def __init__(self):
        self.main_window = MainWindow()
    
    def run(self):
        self.main_window.mainloop()

if __name__ == "__main__":
    app = Aplication()
    app.run()
