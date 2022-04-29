import tkinter as tk
import GUI_prerequisite
from tkinter import filedialog


class FileBrowser(GUI_prerequisite.Prerequisite):
    """
    ipb1/2 Input browser button
    opb output browse button
    """
    def __init__(self):
        GUI_prerequisite.Prerequisite.__init__(self)

        self.master = tk.Tk()
        self.master.title("File Browser")

        self.topFrame = tk.Frame(self.master)
        self.topFrame.grid()
        self.input1_var = tk.StringVar()
        self.input1_entry = tk.Entry(self.topFrame, font=self.text_font,
                                     textvariable=self.input1_var,
                                     width=self.entry_box_width)
        self.input1_entry.grid(row=1, column=0, padx=self.spacingX,
                               pady=self.spacingY)

        self.ipb1 = tk.Button(self.topFrame, text="File 1", command=lambda:
                              self.browse_file(self.input1_var, "Shose file 1"),
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
                                                               "Välj fil 2"),
                              font=self.text_font, height=self.button_height,
                              width=self.button_width)
        self.ipb2.grid(row=2, column=1, padx=self.spacingX, pady=self.spacingY)

        self.second_frame = tk.Frame(self.master)
        self.second_frame.grid(row=1, sticky="w")
        self.button_dict = {}
        self.button_list = ["Union", "Kompliment", "Snitt"]
        self.rb_var = tk.IntVar()

        self.column = 0
        for i in self.button_list:
            self.button_dict[i] = tk.Radiobutton(self.second_frame, text=i,
                                                 variable=self.rb_var,
                                                 font=self.text_font,
                                                 value=self.column)
            self.button_dict[i].grid(row=0, column=self.column,
                                     pady=self.spacingY, sticky="w")
            self.column += 1

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
                                              "Välj output destination"),
                             font=self.text_font, height=self.button_height,
                             width=self.button_width)
        self.opb.grid(row=1, column=1, padx=self.spacingX, pady=self.spacingY)

        self.go_button = tk.Button(self.bottom_frame, text="Kör",
                                   font=self.text_font,
                                   width=self.button_width,
                                   height=self.button_height,
                                   command=lambda: self.compare_files())
        self.go_button.grid(row=2, column=1, pady=self.spacingY,
                            padx=self.spacingX)

        self.master.mainloop()

    def save_output(self, output, text):
        output.set(filedialog.asksaveasfilename(initialdir=".", title=text,
                                                filetypes=(("txt files",
                                                            "*.txt"),
                                                           ("all files",
                                                            "*.*"))))

    def browse_file(self, var, text):
        var.set(filedialog.askopenfilename(initialdir=".", title=text,
                                           filetypes=(("txt files", "*.txt"),
                                                      ("all files", "*.*"))))

    def compare_files(self):
        file_sets = file_analysis.set_files(self.input1_var.get(),
                                            self.input2_var.get())
        action = self.rb_var.get()
        if action == 0:
           done = file_analysis.union_files(file_sets[0], file_sets[1])
        elif action == 1:
            done = file_analysis.unique_file(file_sets[0], file_sets[1])
        elif action == 2:
            done = file_analysis.intersec_files(file_sets[0], file_sets[1])
        with open(self.output_var.get(), "w") as f:
            for element in done[0]:
                f.write(element+ "\n")
        file_analysis.formate_output(done[0], done[1])

    def return_to_main(self):
        self.master.destroy()
        self.main = GUI_main.StartWindow()


if __name__ == "__main__":
    FC = FileBrowser()


