import datetime
import customtkinter as ctk
import tkinter as tk
import random

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("green")

appWidth, appHeight = 700, 550

class App(ctk.CTk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title("GUI Application")
        self.geometry(f"{appWidth}x{appHeight}")

        # Mission Label
        self.missionLabel = ctk.CTkLabel(self, text="Mission")
        self.missionLabel.grid(row=0, column=0, padx=20, pady=20, sticky="ew")

        # Mission combo box
        self.missionOptionMenu = ctk.CTkOptionMenu(self, values=["mission10000000000000000000000000000000000000000", "mission2", "mission3"])
        self.missionOptionMenu.grid(row=0, column=1, padx=20, pady=20, columnspan=2, sticky="ew")

        # Run Option Label
        self.runOptionLabel = ctk.CTkLabel(self, text="Choose run or merge (default: run)")
        self.runOptionLabel.grid(row=1, column=0, padx=20, pady=20, sticky="ew")

        # Run Option Radio Buttons
        self.runOptionVar = tk.StringVar(value="run")

        self.runRadioButton = ctk.CTkRadioButton(self, text="Run", variable=self.runOptionVar, value="run")
        self.runRadioButton.grid(row=1, column=1, padx=20, pady=20, sticky="ew")

        self.mergeRadioButton = ctk.CTkRadioButton(self, text="Merge", variable=self.runOptionVar, value="merge")
        self.mergeRadioButton.grid(row=1, column=2, padx=20, pady=20, sticky="ew")

        # Choice Label
        self.choiceLabel = ctk.CTkLabel(self, text="Choice (Select either P or F)")
        self.choiceLabel.grid(row=2, column=0, padx=20, pady=20, sticky="ew")

        # Choice Check boxes
        self.checkboxVar = tk.StringVar(value="P")

        self.choice1 = ctk.CTkRadioButton(self, text="P- with figures", variable=self.checkboxVar, value="P")
        self.choice1.grid(row=2, column=1, padx=20, pady=20, sticky="ew")

        self.choice2 = ctk.CTkRadioButton(self, text="F - just split csv", variable=self.checkboxVar, value="F")
        self.choice2.grid(row=2, column=2, padx=20, pady=20, sticky="ew")

        # Batch Size Label
        self.batchSizeLabel = ctk.CTkLabel(self, text="Batch Size (default: 10)")
        self.batchSizeLabel.grid(row=3, column=0, padx=20, pady=20, sticky="ew")

        # Batch Size Entry Field
        self.batchSizeEntry = ctk.CTkEntry(self, placeholder_text="10")
        self.batchSizeEntry.grid(row=3, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        # Set default value for Batch Size Entry Field
        self.batchSizeEntry.insert(0, "10")

        # Generate Button
        self.generateResultsButton = ctk.CTkButton(self, text="Generate Results", command=self.generateResults)
        self.generateResultsButton.grid(row=4, column=1, columnspan=2, padx=20, pady=20, sticky="ew")

        # Text Box
        self.displayBox = ctk.CTkTextbox(self, width=200, height=100)
        self.displayBox.grid(row=5, column=0, columnspan=3, padx=20, pady=20, sticky="nsew")

    def generateResults(self):
        self.displayBox.delete("0.0", "200.0")
        text = self.createText()
        self.displayBox.insert("0.0", text)

        # Generating three random numbers
        random_number_1 = random.randint(1, 100)
        random_number_2 = random.randint(1, 100)
        random_number_3 = random.randint(1, 100)

        # Displaying random numbers
        random_numbers_text = f"\nRandom Numbers: number_1 = {random_number_1}, number_2 = {random_number_2}, number_3 = {random_number_3}"
        self.displayBox.insert(tk.END, random_numbers_text)

    def createText(self):
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S")
        text = f"Current Time: {formatted_time}\n"

        mission = self.missionOptionMenu.get()
        run_option = self.runOptionVar.get()
        text = text + f"{run_option} {mission}"
        if run_option == "run":
            checkbox_value = self.checkboxVar.get()
            batch_size = self.batchSizeEntry.get()
            text = text + f" with {checkbox_value} and batch size {batch_size}\n"
        elif run_option == "merge":
            text = text + "."


        return text


if __name__ == "__main__":
    app = App()
    app.mainloop()
