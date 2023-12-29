import tkinter as tk
root = tk.Tk()
root.title("BMI Calculator")
root.geometry("300x200")

root.rowconfigure(0,weight=1)
root.rowconfigure(1,weight=1)
root.rowconfigure(2,weight=1)
root.rowconfigure(3,weight=1)
root.columnconfigure(0,weight=1)
root.columnconfigure(1,weight=1)

def onclick():
    global l4
    global e1
    global e2
    height=float(e1.get())
    weight=float(e2.get())
    try:
        calc=weight/(height*height)
        result=round(calc,2)
    except:
        result="Error"
    finally:
        l4.config(text=f"{result}")

#    bmi= weight/height*height

l1=tk.Label(root,text="Height(in Meter)",font=("Arial", 15))
l1.grid(row=1,column=0,ipadx=4,ipady=1,padx=1,pady=1)
l2=tk.Label(root,text="Weight(in Kg)",font=("Arial", 15))
l2.grid(row=2,column=0,ipadx=4,ipady=1,padx=1,pady=1)
l3=tk.Label(root,text="Your BMI ",font=("Arial", 15))
l3.grid(row=3,column=0,ipadx=4,ipady=1,padx=1,pady=1)
e1=tk.Entry(root,width=10,bg="white",font=("Arial", 15))
e1.grid(row=1,column=1,sticky="NEWS",ipadx=2,ipady=1,padx=20,pady=5)
e2=tk.Entry(root,width=10,bg="white",font=("Arial", 15))
e2.grid(row=2,column=1,sticky="NEWS",ipadx=2,ipady=1,padx=20,pady=5)
l4=tk.Label(root,bg="white",font=("Arial", 15))
l4.grid(row=3,column=1,sticky="NEWS",ipadx=4,ipady=1,padx=20,pady=5)
btn=tk.Button(root,text="Calculate",bg="yellow",command=onclick,font=("Arial", 15))
btn.grid(row=4,column=1,rowspan=1,columnspan=1)
root.mainloop()
