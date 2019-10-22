import tkinter
from tkinter import filedialog

filename=''

def save():
	global filename
	if not filename:
		filename=filedialog.asksaveasfilename()
		file=open(filename, 'w')
		txt=text.get('1.0', tkinter.END)
		file.write(txt)
		file.close()
	else:
		file=open(filename, 'w')
		txt=text.get('1.0', tkinter.END)
		file.write(txt)
		file.close()
		
def saveas():
	global filename
	filename=filedialog.asksaveasfilename()
	file=open(filename, 'w')
	txt=text.get('1.0', tkinter.END)
	file.write(txt)
	file.close()

def openfile():
	global filename
	filename=filedialog.askopenfilename()
	file=open(filename)
	txt=file.read()
	text.delete('1.0', tkinter.END)
	text.insert('1.0', txt)

root=tkinter.Tk()
root.title('TSARSOFT Text Editor')

menubar=tkinter.Menu()
filemen=tkinter.Menu()

menubar.add_cascade(menu=filemen, label='File')

filemen.add_command(label='Close', command=lambda:root.destroy())
filemen.add_separator()
filemen.add_command(label='Save', command=lambda:save())
filemen.add_command(label='Save as', command=lambda:saveas())
filemen.add_command(label='Open', command=lambda:openfile())

root.config(menu=menubar)

text=tkinter.Text(root)
text.pack(fill='both')

root.mainloop()