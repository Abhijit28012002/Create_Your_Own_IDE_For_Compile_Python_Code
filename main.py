from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess
compiler = Tk()
compiler.title("My IDE")
file_path=''


def set_file_path(path):
    global file_path
    file_path = path




### Run Funtion ####
def run():
    if file_path =='':
        save_prompt = Toplevel()
        text=Label(save_prompt,text="Please save your code")
        text.pack()
    command = f'python {file_path}'
    process = subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output,error = process.communicate()
    code_output.insert('1.0',output)
    code_output.insert('1.0',error)


#### Open File Funtion ############

def open_file():
    path = askopenfilename(filetypes=[('Python Files','*.py')])
    with open(path,'r') as file:
        code = file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_file_path(path)

####### Close Project Function ########

def closeProject():
    editor.delete('1.0', END)


### Save_as Funtion ######
def save_as():
    if file_path =='':
        path = asksaveasfilename(filetypes=[('Python Files','*.py')])
    else:
        path = file_path
    with open(path,'w') as file:
        code = editor.get('1.0', END)
        file.write(code)
        set_file_path(path)


###################################################

menu_bar= Menu(compiler)

#################### File Menu #######################

file_bar = Menu(menu_bar,tearoff=0)
file_bar.add_command(label='Open file',command=open_file)
file_bar.add_command(label='Save',command=save_as)
file_bar.add_command(label='Save as',command=save_as)
file_bar.add_command(label='Close Project',command=closeProject)
file_bar.add_command(label='Exit',command=exit)
menu_bar.add_cascade(label='File', menu=file_bar)

######################################################


##################### Run Menu #######################

run_bar = Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Run',command=run)
run_bar.add_command(label='Compile',command=run)
menu_bar.add_cascade(label='Run', menu=run_bar)

######################################################

compiler.config(menu=menu_bar)

editor = Text()
editor.pack()

code_output =Text(height=10)
code_output.pack()

compiler.mainloop()