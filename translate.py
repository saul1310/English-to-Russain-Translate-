import tkinter as tk
from tkinter import messagebox
from googletrans import Translator

def translate_text():
    text_to_translate = entry.get("1.0", tk.END).strip()
    if not text_to_translate:
        messagebox.showwarning("Input Error", "Please enter text to translate.")
        return
    translator = Translator()
    try:
        translation = translator.translate(text_to_translate, src='en', dest='ru')
        result_text.delete("1.0", tk.END)
        result_text.insert(tk.END, translation.text)
    except Exception as e:
        messagebox.showerror("Translation Error", f"An error occurred: {e}")


root = tk.Tk()
root.title("English to Russian Translator")


label = tk.Label(root, text="Enter English text:")
label.pack(pady=10)

entry = tk.Text(root, height=10, width=50)
entry.pack(pady=10)

translate_button = tk.Button(root, text="Translate", command=translate_text)
translate_button.pack(pady=10)

result_label = tk.Label(root, text="Translated text in Russian:")
result_label.pack(pady=10)

result_text = tk.Text(root, height=10, width=50)
result_text.pack(pady=10)

root.mainloop()
