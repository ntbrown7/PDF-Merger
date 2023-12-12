import tkinter as tk
from tkinter import filedialog, messagebox
from PyPDF2 import PdfReader, PdfWriter
import os


def merge_pdfs(paths, output):
    pdf_writer = PdfWriter()
    for path in paths:
        pdf_reader = PdfReader(path)
        for page in pdf_reader.pages:
            pdf_writer.add_page(page)
    with open(output, 'wb') as out:
        pdf_writer.write(out)


def select_files():
    filetypes = [('PDF files', '*.pdf')]
    dlg = filedialog.askopenfilenames(title='Select two PDF files to merge', filetypes=filetypes)
    return dlg


def combine_pdfs():
    paths = select_files()
    if len(paths) != 2:
        messagebox.showerror("Error", "Please select exactly two PDF files.")
        return

    # Determine the directory of the selected files
    file_dir = os.path.dirname(paths[0])

    # Create the output file path
    output_file = os.path.join(file_dir, 'NBResume&CV.pdf')

    merge_pdfs(paths, output_file)
    messagebox.showinfo("Success", f"PDFs combined successfully into {output_file}")


# Set up the tkinter GUI
root = tk.Tk()
root.title("PDF Merger")

merge_button = tk.Button(root, text="Select and Merge PDFs", command=combine_pdfs)
merge_button.pack(pady=20)

root.mainloop()
