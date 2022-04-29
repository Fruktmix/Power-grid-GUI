import tkinter as tk
from turtle import width
import GUI_prerequisite
from tkinter import filedialog


class FileBrowser(GUI_prerequisite.Prerequisite):
    """
    ipb1/2 Input browser button
    opb output browse button
    """
    def __init__(self):
        GUI_prerequisite.Prerequisite.__init__(self)

        self.master = tk.Tk(width=300)
        self.master.title("File Browser")
        #sell.mainFrame = tk.Frame(self.master, width=300, height=200)
        self.topFrame = tk.Frame(self.master)

        self.topFrame.grid()

        self.input1_var = tk.StringVar()

        self.input1_entry = tk.Entry(self.topFrame, font=self.text_font,
                                     textvariable=self.input1_var,
                                     width=self.entry_box_width)
        self.input1_entry.grid(row=1, column=0, padx=self.spacingX,
                               pady=self.spacingY)

        self.ipb1 = tk.Button(self.topFrame, text="File 1", command=lambda:
                              self.browse_file(self.input1_var, "File 1"),
                              font=self.text_font, height=self.button_height,
                              width=self.button_width)

        self.ipb1.grid(row=1, column=1, padx=self.spacingX, pady=self.spacingY)

        self.input2_var = tk.StringVar()
        self.input2_entry = tk.Entry(self.topFrame, font=self.text_font,
                                     textvariable=self.input2_var,
                                     width=self.entry_box_width)

        self.input2_entry.grid(row=2, column=0, padx=self.spacingX,
                               pady=self.spacingY)

        self.ipb2 = tk.Button(self.topFrame, text="File 2",
                              command=lambda: self.browse_file(self.input2_var,
                                                               "File 2"),
                              font=self.text_font, height=self.button_height,
                              width=self.button_width)

        self.ipb2.grid(row=2, column=1, padx=self.spacingX, pady=self.spacingY)

        self.bottom_frame = tk.Frame(self.master)
        self.bottom_frame.grid(row=2, sticky="w")

        self.output_var = tk.StringVar()

        self.output_entry = tk.Entry(self.bottom_frame, font=self.text_font,
                                     textvariable=self.output_var,
                                     width=self.entry_box_width)
        self.output_entry.grid(row=1, column=0, padx=self.spacingX,
                               pady=self.spacingY)

        self.opb = tk.Button(self.bottom_frame, text="Save", command=lambda:
                             self.save_output(self.output_var,
                                              "Output destination"),
                             font=self.text_font, height=self.button_height,
                             width=self.button_width)
        self.opb.grid(row=1, column=1, padx=self.spacingX, pady=self.spacingY)

        self.go_button = tk.Button(self.bottom_frame, text="Kör",
                                   font=self.text_font,
                                   width=self.button_width,
                                   height=self.button_height,
                                   command=lambda: self.compute_files())
        self.go_button.grid(row=2, column=1, pady=self.spacingY,
                            padx=self.spacingX)

        self.master.mainloop()

    def save_output(self, output, text):
        output.set(filedialog.asksaveasfilename(initialdir=".",
                   title=text, filetypes=(("txt files", "*.txt"),
                                          ("all files", "*.*"))))

    def browse_file(self, var, text):
        var.set(filedialog.askopenfilename(initialdir=".", title=text,
                filetypes=(("txt files", "*.txt"), ("all files", "*.*"))))

    def compute_files(self):
        # Call on main function
        # Use return value as input for text box
        pass


if __name__ == "__main__":
    FC = FileBrowser()
