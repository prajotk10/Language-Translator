import tkinter as tk
from tkinter import ttk
from googletrans import Translator

# Initialize the translator
translator = Translator()

# Function to translate text
def translate_text():
    source_text = source_entry.get()
    target_language = target_language_combobox.get()
    
    try:
        translation = translator.translate(source_text, dest=target_language)
        target_text.delete(1.0, tk.END)  # Clear previous translation
        target_text.insert(tk.END, translation.text)
    except Exception as e:
        target_text.delete(1.0, tk.END)
        target_text.insert(tk.END, "Translation error: " + str(e))

# Create the main application window
root = tk.Tk()
root.title("Translator App")

# Create a frame for the input
input_frame = ttk.LabelFrame(root, text="Input Text")
input_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

source_label = ttk.Label(input_frame, text="Source Text:")
source_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

source_entry = ttk.Entry(input_frame, width=40)
source_entry.grid(row=0, column=1, padx=5, pady=5, sticky="w")

# Create a frame for the output
output_frame = ttk.LabelFrame(root, text="Translation")
output_frame.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

target_language_label = ttk.Label(output_frame, text="Target Language:")
target_language_label.grid(row=0, column=0, padx=5, pady=5, sticky="w")

target_language_combobox = ttk.Combobox(output_frame, values=["en", "es", "fr", "de"])
target_language_combobox.grid(row=0, column=1, padx=5, pady=5, sticky="w")
target_language_combobox.set("en")

translate_button = ttk.Button(output_frame, text="Translate", command=translate_text)
translate_button.grid(row=0, column=2, padx=5, pady=5)

target_text = tk.Text(output_frame, wrap=tk.WORD, width=40, height=10)
target_text.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

# Adjust column and row weights to make widgets expand with the window
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

root.mainloop()
