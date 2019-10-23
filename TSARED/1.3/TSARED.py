import tkinter
from tkinter import filedialog

filename=''
fullscreen=False

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

def ftoggle():
        global fullscreen
        print(fullscreen)
        if fullscreen:
                root.attributes('-fullscreen', False)
                fullscreen=False
        else:
                root.attributes('-fullscreen', True)
                fullscreen=True

def blueselected():
        text.tag_add('blue', tkinter.SEL_FIRST, tkinter.SEL_LAST)
        text.tag_config('blue', foreground='blue')

def blackselected():
        text.tag_add('black', tkinter.SEL_FIRST, tkinter.SEL_LAST)
        text.tag_config('black', foreground='black')

def greenselected():
        text.tag_add('green', tkinter.SEL_FIRST, tkinter.SEL_LAST)
        text.tag_config('green', foreground='green')

def redselected():
        text.tag_add('red', tkinter.SEL_FIRST, tkinter.SEL_LAST)
        text.tag_config('red', foreground='red')

def hackselected():
        text.tag_add('hack', tkinter.SEL_FIRST, tkinter.SEL_LAST)
        text.tag_config('hack', foreground='green', background='black')

def clearallcoloures():
        for tag in text.tag_names():
                text.tag_delete(tag)

def runpy():
        txt=text.get('1.0', tkinter.END)
        exec(txt)

root=tkinter.Tk()
root.title('TSARSOFT Text Editor')

menubar=tkinter.Menu()
filemen=tkinter.Menu()
viewmen=tkinter.Menu()
editmen=tkinter.Menu()
colourmen=tkinter.Menu()

menubar.add_cascade(menu=filemen, label='File')
menubar.add_cascade(menu=viewmen, label='View')
menubar.add_cascade(menu=editmen, label='Edit')
editmen.add_cascade(menu=colourmen, label='Colour selected')

filemen.add_command(label='Close', command=lambda:root.destroy())
filemen.add_separator()
filemen.add_command(label='Save', command=lambda:save())
filemen.add_command(label='Save as', command=lambda:saveas())
filemen.add_command(label='Open', command=lambda:openfile())

viewmen.add_command(label='toggle fullscreen', command=lambda:ftoggle())

colourmen.add_command(label='Black', command=lambda:blackselected())
colourmen.add_command(label='red', command=lambda:redselected())
colourmen.add_command(label='green', command=lambda:greenselected())
colourmen.add_command(label='Blue', command=lambda:blueselected())
colourmen.add_command(label='hacking style', command=lambda:hackselected())

editmen.add_command(label='clear all colours', command=lambda:clearallcoloures())

root.config(menu=menubar)

scroller=tkinter.Scrollbar(root)
scroller.pack(side=tkinter.RIGHT, fill='y')
scrollerx=tkinter.Scrollbar(root, orient=tkinter.HORIZONTAL)
scrollerx.pack(side=tkinter.BOTTOM, fill='x')

text=tkinter.Text(root, yscrollcommand=scroller.set, xscrollcommand=scrollerx.set, wrap='none')
text.pack(fill='both')

tkinter.Button(root, text = 'Run python', height=2, compound=tkinter.LEFT, command=lambda:runpy()).pack(side=tkinter.BOTTOM, fill='x') 
scroller.config(command=text.yview)
scrollerx.config(command=text.xview)


root.mainloop()

