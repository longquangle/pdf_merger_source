import tkinter as tk
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
from PyPDF2 import PdfFileMerger
from os.path import exists

# create the root window
root = tk.Tk()
root.title('PDF Merger')
root.geometry('730x525')
selected_files = []

def add_files():
    filetypes = (
        ('pdf files', '*.pdf'),
        # ('All files', '*.*')
    )

    filenames = fd.askopenfilenames(
        title='Select Files',
        filetypes=filetypes)
    for f in filenames:
        if len(selected_files) < 10:
            selected_files.append(f)
            file_buttons[len(selected_files) - 1].configure(text = f)
    if len(selected_files) >= 10:
        max_warning.configure(text='Maximum number of documents reached.')
        add_button.configure(state='disabled')
    if len(selected_files) > 0:
        delete_button.configure(state='normal')
    if len(selected_files) > 1:
        merge_button.configure(state='normal')

def delete_files():
    intro_text.configure(text='')
    remove_file_text.configure(text='Click on file name to remove. Click Cancel Remove Files button when done.')
    delete_button.configure(state='disabled')
    add_button.configure(state='disabled')
    merge_button.configure(state='disabled')
    cancel_remove_button.configure(state='normal')
    for i in range(len(selected_files)):
        file_buttons[i].configure(state='normal')

def cancel_delete_files():
    intro_text.configure(text='Files to merge (max 10)')
    remove_file_text.configure(text='')
    delete_button.configure(state='normal')
    add_button.configure(state='normal')
    cancel_remove_button.configure(state='disabled')

    if len(selected_files) <= 1:
        merge_button.configure(state='disabled')
    else:
        merge_button.configure(state='normal')
    for i in range(len(selected_files)):
        file_buttons[i].configure(state='disabled')

def merge_files():
    entry_string = e.get() + '.pdf'
    # actually merging
    if exists(entry_string ):
        file_already_exist.configure(text='* Warning: File already exists in the folder. Please choose a different name.')
    else:
        file_already_exist.configure(text='')
        merge_pdfs(selected_files, entry_string, folder_path)
        # clearning all current files
        e.delete(0, tk.END)
        merge_button.configure(state='disabled')
        delete_button.configure(state='disabled')
        selected_files.clear()
        for b in file_buttons:
            b.configure(text='',state='disabled')

def browse_folder():
    global folder_path
    filename = fd.askdirectory()
    folder_path = filename
    location_folder.configure(text=filename)


# file buttons
def click_to_delete(position):
    # remove the file from the list then remove the file button
    selected_files.pop(position)
    file_buttons[len(selected_files)].configure(text = '', state='disabled')
    # update the remaining files
    for i in range(len(selected_files)):
        file_buttons[i].configure(text = selected_files[i])
    if len(selected_files) < 10:
        max_warning.configure(text='')
    # automatically activates cancel remove button if there is files are empty
    if len(selected_files) == 0:
        intro_text.configure(text='Files to merge (max 10)')
        remove_file_text.configure(text='')
        add_button.configure(state='normal')
        merge_button.configure(state='disabled')
        cancel_remove_button.configure(state='disabled')
        delete_button.configure(state='disabled')


# buttons
add_button = tk.Button(root, 
                text='Add Files',
                width = 40,
                height=2,
                command=add_files)
delete_button = tk.Button(root,
                text='Remove Files',
                height=2,
                width = 40,
                state='disabled',
                command=delete_files)
merge_button = tk.Button(
                root,
                text= 'Merge',
                height=2,
                width=35,
                state='disabled',
                command=merge_files)
cancel_remove_button = tk.Button(root,
                text= 'Cancel Remove Files',
                height=2,
                width = 20,
                state='disabled',
                command=cancel_delete_files)
browse_folder_button = tk.Button(root,
                text='Browse Folder',
                width = 20,
                command=browse_folder)

add_button.grid(row=0,column=0, sticky=tk.W)
delete_button.grid(row=0,column=1, sticky=tk.W)
cancel_remove_button.grid(row=0,column=2, sticky=tk.W)
browse_folder_button.grid(row=15, column = 0, sticky=tk.E)
merge_button.grid(row = 17,column=0,padx=0,pady=1,sticky=tk.W)

# text and warnings
intro_text = tk.Label(text="Files to merge (max 10)")
intro_text.grid(row = 1,columnspan =3,padx=50,pady=6,sticky=tk.W)
remove_file_text = tk.Label(text="")
remove_file_text.grid(row = 2, columnspan =3,padx=50, pady=6, sticky=tk.W)
max_warning = tk.Label(text="")
max_warning.grid(row = 13, columnspan =3,padx=50, pady=1, sticky=tk.W)
file_already_exist = tk.Label(text='', fg='#f00')
file_already_exist.grid(row=16,columnspan =3,padx=0,pady=1,sticky=tk.W)
location_folder = tk.Label(text="No destination folder selected")
location_folder.grid(row=15, columnspan=2, column = 1, pady=1, sticky=tk.W)
signature = tk.Label(text='Created by Long Le, 2021').grid(row=17,column =2)

# input result file name
tk.Label(root, text="Result pdf name :  ").grid(row=14, sticky=tk.E)
e = tk.Entry(root)
e.grid(row=14, column = 1, ipadx= 55, ipady= 3,sticky=tk.W)

file1 = tk.Button(root,relief='flat',state='disabled', command=lambda: click_to_delete(0))
file2 = tk.Button(root,relief='flat',state='disabled', command=lambda: click_to_delete(1))
file3 = tk.Button(root,relief='flat',state='disabled', command=lambda: click_to_delete(2))
file4 = tk.Button(root,relief='flat',state='disabled', command=lambda: click_to_delete(3))
file5 = tk.Button(root,relief='flat',state='disabled', command=lambda: click_to_delete(4))
file6 = tk.Button(root,relief='flat',state='disabled', command=lambda: click_to_delete(5))
file7 = tk.Button(root,relief='flat',state='disabled', command=lambda: click_to_delete(6))
file8 = tk.Button(root,relief='flat',state='disabled', command=lambda: click_to_delete(7))
file9 = tk.Button(root,relief='flat',state='disabled', command=lambda: click_to_delete(8))
file10 = tk.Button(root,relief='flat',state='disabled', command=lambda: click_to_delete(9))

file_buttons = [file1, file2, file3, file4, file5, 
                file6, file7, file8, file9, file10]

for i in range(len(file_buttons)):
    file_buttons[i].grid(row = 3 + i, columnspan =3,padx=30, pady=1, sticky=tk.W)


# back-end
def merge_pdfs(files, mergedfilename, folder_path):
    merger = PdfFileMerger()
    for pdf in files:
        merger.append(open(pdf,'rb'))
    merger.write(folder_path + '//' + mergedfilename)
    merger.close()

root.mainloop()