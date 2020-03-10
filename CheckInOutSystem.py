from tkinter import *
class Student(object):
    def __init__(self, sname, sid):
        self.name = sname
        self.id = sid
        self.status = False
def checkOutPage():
    global currentNum
    currentNum = ""
    button2.destroy()
    button3.destroy()
    button1.destroy()
    global label1 
    label1 = Label(topFrame, text="Student Num:", )
    label1.pack(side=LEFT)
    global entry1 
    entry1 = Entry(topFrame)
    entry1.pack(side=LEFT)
    global button4 
    button4 = Button(bottomFrame, text = "Check Out", fg="red", command=checkOut)
    button4.pack()
def checkOut():
    i = 0
    for student in students:
        currentNum = entry1.get()
        if(int(currentNum)==(student.id)):
            student.status = True
        i += 1
    label1.destroy()
    entry1.destroy()
    button4.destroy()
    mainPage()
def mainPage():
    global button1
    button1 = Button(topFrame, text="Check Out Student", fg="red", command=checkOutPage)
    global button2 
    button2 = Button(topFrame, text="Check In Student", fg="green", command=checkInPage)
    global button3 
    button3 = Button(bottomFrame, text="View All Students", fg="gray", command=viewStudents)
    button1.pack(side=LEFT)
    button2.pack(side=RIGHT)
    button3.pack(side=BOTTOM)
def viewStudents():
    button1.destroy()
    button2.destroy()
    button3.destroy()
    global studentLabels
    studentLabels = []
    for student in students:
        currentStatus = "Out"
        if(student.status==False):
            currentStatus = "In"
        studentLabels.append(Label(topFrame, text=student.name + " " + currentStatus))
    for label in studentLabels:
        label.pack()
    global button5
    button5 = Button(bottomFrame, text = "Done", command=endViewStudents)
    button5.pack(side=BOTTOM)
def endViewStudents():
    numLabels = len(studentLabels)
    i = numLabels-1
    while(i>=0):
        studentLabels[i].destroy()
        i -=1
    button5.destroy()
    mainPage()   
def checkInPage():
    button1.destroy()
    button2.destroy()
    button3.destroy()
    global outStudentLabels
    outStudentLabels = []
    global checkboxes
    checkboxes = []
    global varis
    varis = []
    global outSutdentNames
    outSutdentNames = []
    for student in students:
        if(student.status==True):
            outStudentLabels.append(Label(topFrame, text=student.name))
            outSutdentNames.append(student.name)
    i = 0
    for label in outStudentLabels:
        varis.append(IntVar())
        checkboxes.append(Checkbutton(topFrame, variable = varis[i]))
        checkboxes[i].grid(row=i, column = 0)
        #checkboxes[i].pack(side=LEFT)
        label.grid(row=i, column = 1)
        #label.pack(side=RIGHT)
        i += 1
    global button6
    button6 = Button(bottomFrame, text = "Done", command=endCheckIn)
    button6.pack(side=BOTTOM)
def endCheckIn():
    n = 0
    for checkbox in checkboxes:
        if (varis[n].get()==1):
            for student in students:
                if(student.name==outSutdentNames[n]):
                    student.status = False
        n += 1
    numLabels = len(outStudentLabels)
    i = numLabels-1
    while(i>=0):
        outStudentLabels[i].destroy()
        checkboxes[i].destroy()
        i-=1
    button6.destroy()
    mainPage()
students = []
students.append(Student("Bryant Cassady", 555000534))
students.append(Student("Ben Burdess", 555000594))
root = Tk()
topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)
mainPage()
root.mainloop()