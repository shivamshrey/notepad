import os
import tkinter
from tkinter import *
from tkinter.messagebox import *
from tkinter.filedialog import *

class Notepad():
    
    root = Tk()

    # Set default window width and height
    width = 400
    height = 400

    text_area = Text(root)
    menu_bar = Menu(root)
    file_menu = Menu(menu_bar, tearoff=0)
    edit_menu = Menu(menu_bar, tearoff=0)
    help_menu = Menu(menu_bar, tearoff=0)

    # Create scrollbar
    scrollbar = Scrollbar(text_area)
    file = None

    def __init__(self, **kwargs):
        
        # Set icon
        try:
            self.root.wm_iconbitmap("notepad.ico")
        except:
            pass

        # Set window size
        try:
            self.width = kwargs['width']
        except KeyError:
            pass
        
        try:
            self.height = kwargs['height']
        except KeyError:
            pass

        # Set window text
        self.root.title("Untitled - Notepad")

        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Left align
        left = (screen_width / 2) - (self.width / 2)

        # Right align
        right = (screen_height / 2) - (self.height / 2) 

        # Top and bottom align
        self.root.geometry("%dx%d+%d+%d" % (self.width, self.height,
                                            left, right))

        # Pack text area and make it auto-resizable
        self.text_area.pack(expand=True, fill=BOTH)

        # Add menus
        
        # File Menu
        # To open a new file
        self.file_menu.add_command(label="New", command=self.new_file)

        # To open an existing file
        self.file_menu.add_command(label="Open...", command=self.open_file)

        # To save the current file
        self.file_menu.add_command(label="Save", command=self.save_file)

        # Add separator
        self.file_menu.add_separator()
        
        # To exit the application
        self.file_menu.add_command(label="Exit", command=self.exit_application)

        # Add File Menu to Menu Bar
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)

        # Edit Menu
        # To cut text
        self.edit_menu.add_command(label="Cut", command=self.cut)

        # To copy text
        self.edit_menu.add_command(label="Copy", command=self.copy)

        # To paste text
        self.edit_menu.add_command(label="Paste", command=self.paste)

        # Add Edit Menu to Menu Bar
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)

        # Help Menu
        # To show about
        self.help_menu.add_command(label="About Notepad", command=self.show_about)
        
        # Add Help Menu to Menu Bar
        self.menu_bar.add_cascade(label="Help", menu=self.help_menu)

        # Add Menu Bar to root
        self.root.config(menu=self.menu_bar)

        # Adjust scrollbar according to content
        self.scrollbar.config(command=self.text_area.yview)
        self.text_area.config(yscrollcommand=self.scrollbar.set)

        # Pack scrollbar
        self.scrollbar.pack(side=RIGHT, fill=Y)


    def new_file(self):
        self.root.title("Untitled - Notepad")
        self.file = None
        self.text_area.delete(1.0, END)

    def open_file(self):
        self.file = askopenfilename(defaultextension=".txt",
                                    filetypes=[("Text Documents (*.txt)", "*.txt"),
                                               ("All Files", "*.*")])
        
        if self.file == "":
            # No file to open
            self.file = None
        else:
            # Update the window title
            self.root.title(os.path.basename(self.file).split('.')[0] + " - Notepad")
            # Open the file
            self.text_area.delete(1.0, END)
            with open(self.file, "r") as file:
                self.text_area.insert(1.0, file.read())
    
    def save_file(self):
        if self.file == None:
            # Save as new file
            self.file = asksaveasfilename(initialfile="*.txt",
                                          defaultextension="*.txt",
                                          filetypes=[("Text Documents (*.txt)", "*.txt"),
                                                     ("All Files", "*.*")])

            if self.file == "":
                self.file = None
            else:
                # Save the file
                with open(self.file, "w") as file:
                    file.write(self.text_area.get(1.0, END))

                # Update window title after saving
                self.root.title(os.path.basename(self.file) + " - Notepad")
        else:
            with open(self.file, "w") as file:
                file.write(self.text_area.get(1.0, END))

    def exit_application(self):
        self.root.destroy()

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")
    
    def show_about(self):
        showinfo(title="About Notepad", message="Made by Shivam")

    def run(self):
        '''Run Notepad application.'''
        self.root.mainloop()


if __name__ == '__main__':
    notepad = Notepad(width=744, height=400)
    notepad.run()
    