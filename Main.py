import tkinter as tk
import customtkinter as ctk
from tkinter import ttk
import Summarization_model as sm
import Question_Answering_Model as qa
import threading


def summarize_thread(text, min_sequence_length, max_sequence_length):
    summary = sm.summarization_fn(text, min_sequence_length, max_sequence_length)
    summary_notepad.delete("1.0", "end")
    summary_notepad.insert(tk.END, summary)
    progress_bar.stop()
    progress_window.destroy()


def open_progress_window():
    progress_bar.start(10)
    progress_window.mainloop()


def summarize():
    global progress_window, progress_bar, progress_bar_label

    text = question_notepad.get("1.0", tk.END)

    min_sequence_length = min_sequence_length_entry.get()
    if min_sequence_length:
        min_sequence_length = int(min_sequence_length)
    else:
        min_sequence_length = 20

    max_sequence_length = max_sequence_length_entry.get()
    if max_sequence_length:
        max_sequence_length = int(max_sequence_length)
    else:
        max_sequence_length = 50

    progress_window = tk.Toplevel(window)
    progress_window.overrideredirect(True)
    progress_window.geometry("250x85")

    progress_window.configure(bg='#282e2c')

    # Calculate the position to center the new window
    window_width = window_summarize.winfo_width()
    window_height = window_summarize.winfo_height()
    window_x = window_summarize.winfo_x()
    window_y = window_summarize.winfo_y()

    progress_window_x = window_x + window_width // 2 - 200 // 2
    progress_window_y = window_y + window_height // 2 - 50 // 2

    progress_window.geometry(f"+{progress_window_x}+{progress_window_y}")

    progress_bar = ttk.Progressbar(progress_window, length=200, mode='indeterminate')
    progress_bar.place(relx=0.5, rely=0.7, anchor='center')

    progress_bar_label = ctk.CTkLabel(progress_window, text="Processing...", font=("Helvetica", 16))
    progress_bar_label.place(x=5, y=5)

    threading.Thread(target=open_progress_window).start()
    threading.Thread(target=summarize_thread, args=(text, min_sequence_length, max_sequence_length)).start()

def summarization_clear_All():
    summary_notepad.delete("1.0", "end")
    question_notepad.delete("1.0", "end")


def open_summarization_window():
    global question_notepad, max_sequence_length_entry, min_sequence_length_entry, summary_notepad, window_summarize

    window_summarize = ctk.CTkToplevel()
    window_summarize.geometry("800x620")

    sm_Label_1 = ctk.CTkLabel(window_summarize, text="Add Your Text into Following Entry:", font=("Helvetica", 16))
    sm_Label_1.place(x=20, y=10)

    question_notepad = tk.Text(window_summarize, wrap=tk.WORD, font=("Helvetica", 12))
    question_notepad.place(x=20, y=50, width=950, height=350)

    min_label = ctk.CTkLabel(window_summarize, text="Set Min Words:", font=("Helvetica", 16))
    min_label.place(x=130, y=330)

    min_sequence_length_entry = ctk.CTkEntry(window_summarize, placeholder_text="20", width=60, height=30)
    min_sequence_length_entry.place(x=260, y=330)

    max_label = ctk.CTkLabel(window_summarize, text="Set Max Words:", font=("Helvetica", 16))
    max_label.place(x=480, y=330)

    max_sequence_length_entry = ctk.CTkEntry(window_summarize, placeholder_text="50", width=60, height=30)
    max_sequence_length_entry.place(x=610, y=330)

    button_summarize = ctk.CTkButton(window_summarize, text="Summarize", width=50, height=35, font=("Helvetica", 15, "bold"), command=summarize)
    button_summarize.place(x=280, y=380)

    button_clear_all_sum = ctk.CTkButton(window_summarize, text="  Clear All  ", width=50, height=35,
                                     font=("Helvetica", 15, "bold"), command=summarization_clear_All)
    button_clear_all_sum.place(x=430, y=380)

    sm_Label_2 = ctk.CTkLabel(window_summarize, text="Summary:", font=("Helvetica", 16))
    sm_Label_2.place(x=20, y=420)

    summary_notepad = tk.Text(window_summarize, wrap=tk.WORD, font=("Helvetica", 12))
    summary_notepad.place(x=20, y=560, width=950, height=200)


def QA_thread(question, context):
    answer = qa.question_answering_fn(question, context)
    answer_notepad.delete("1.0", "end")
    answer_notepad.insert(tk.END, answer)
    progress_bar_1.stop()
    progress_window_1.destroy()


def open_progress_window_QA():
    progress_bar_1.start(10)
    progress_window_1.mainloop()


def submit():
    global progress_window_1, progress_bar_1, progress_bar_label_1

    question = paragraph_notepad.get("1.0", tk.END)
    context = question_notepad.get("1.0", tk.END)


    progress_window_1 = tk.Toplevel(window)
    progress_window_1.geometry("250x85")
    progress_window_1.configure(bg='#282e2c')
    progress_window_1.overrideredirect(True)

    # Calculate the position to center the new window
    window_width = window_QA.winfo_width()
    window_height = window_QA.winfo_height()
    window_x = window_QA.winfo_x()
    window_y = window_QA.winfo_y()

    progress_window_x = window_x + window_width // 2 - 200 // 2
    progress_window_y = window_y + window_height // 2 - 50 // 2

    progress_window_1.geometry(f"+{progress_window_x}+{progress_window_y}")

    progress_bar_1 = ttk.Progressbar(progress_window_1, length=200, mode='indeterminate')
    progress_bar_1.place(relx=0.5, rely=0.7, anchor='center')
    progress_bar_label_1 = ctk.CTkLabel(progress_window_1, text="Finding Answer...", font=("Helvetica", 16))
    progress_bar_label_1.place(x=5, y=5)

    threading.Thread(target=open_progress_window_QA).start()
    threading.Thread(target=QA_thread, args=(question, context)).start()

def QA_clear_All():
    paragraph_notepad.delete("1.0", "end")
    answer_notepad.delete("1.0", "end")
    question_notepad.delete("1.0", "end")


def open_QA_window():
    global paragraph_notepad, answer_notepad, question_notepad, window_QA

    window_QA = ctk.CTkToplevel()
    window_QA.geometry("800x620")

    qa_Label_1 = ctk.CTkLabel(window_QA, text="Add Your Context into Following Entry:", font=("Helvetica", 16))
    qa_Label_1.place(x=20, y=10)

    question_notepad = tk.Text(window_QA, wrap=tk.WORD, font=("Helvetica", 12))
    question_notepad.place(x=20, y=50, width=950, height=350)

    qa_Label_2 = ctk.CTkLabel(window_QA, text="Add Your Question into Following Entry:", font=("Helvetica", 16))
    qa_Label_2.place(x=20, y=420)

    paragraph_notepad = tk.Text(window_QA, wrap=tk.WORD, font=("Helvetica", 12))
    paragraph_notepad.place(x=20, y=560, width=390, height=200)

    button_answer = ctk.CTkButton(window_QA, text="Get Answer", width=50, height=35, font=("Helvetica", 15, "bold"), command=submit)
    button_answer.place(x=350, y=475)

    button_clear_all_QA = ctk.CTkButton(window_QA, text="   Clear All   ", width=50, height=35, font=("Helvetica", 15, "bold"),
                                  command=QA_clear_All)
    button_clear_all_QA.place(x=350, y=550)

    qa_Label_3 = ctk.CTkLabel(window_QA, text="Answer:", font=("Helvetica", 16))
    qa_Label_3.place(x=475, y=420)

    answer_notepad = tk.Text(window_QA, wrap=tk.WORD, font=("Helvetica", 12))
    answer_notepad.place(x=590, y=560, width=390, height=200)


window = ctk.CTk()

window.geometry("250x180")
window.title("NLP Application")
Label_1 = ctk.CTkLabel(window, text="What do you want to do?")
Label_1.place(x=10, y=0)

button_Summarization = ctk.CTkButton(window, text="Summarization", command=open_summarization_window, width=50, height=35, font=("Helvetica", 15, "bold"))
button_Summarization.place(x=65, y=40)

Label_2 = ctk.CTkLabel(window, text="-OR-", font=("Helvetica", 16))
Label_2.place(x=110, y=85)

button_QA = ctk.CTkButton(window, text="Question-Answering", command=open_QA_window, width=50, height=35, font=("Helvetica", 15, "bold"))
button_QA.place(x=45, y=115)

window.mainloop()