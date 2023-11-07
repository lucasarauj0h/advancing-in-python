import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title('Cadastro de Alunos')

def add_employee():
    name = entry_name.get()
    email = entry_email.get()
    
    # Add code here to store the employee data somewhere (e.g., database, file, list, etc.)
    # For now, we're just displaying the data in the table
    
    tree.insert("", tk.END, values=(name, email))
    
    # Clear the entry fields after adding an employee
    entry_name.delete(0, tk.END)
    entry_email.delete(0, tk.END)


# 2 - Criando Tabela TreeView
tree = ttk.Treeview(root,columns=('Name', 'E-mail'))
tree.heading('Name', text='Name')
tree.heading('E-mail', text='E-mail')
tree.pack()

# 3 - Criando campos de nome e email
label_name = tk.Label(root, text='Name')
label_name.pack()
entry_name = tk.Entry(root)
entry_name.pack()

label_email = tk.Label(root, text='E-mail')
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

# 4 - botão para adicionalo
button_add = tk.Button(root,text='ADD', command=add_employee)
button_add.pack()


root.mainloop()