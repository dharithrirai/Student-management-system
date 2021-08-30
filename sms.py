from tkinter import*
from tkinter import ttk, messagebox
import pymysql
from pymysql.connections import Connection


class Students():
    def __init__(self,root):
        self.root=root
        self.root.title("Student Management System")
        self.root.geometry("1370x700+0+0")
        title= Label(self.root, text="Student Management System",bd=9,relief=GROOVE,font=("times new roman",50,"bold"),bg="Black",fg="Light blue")
        title.pack(side=TOP,fill=X)
 # ==============All variables=========
        self.Roll_No_var= StringVar()
        self.name_var= StringVar()
        self.email_var= StringVar()
        self.gender_var= StringVar()
        self.contact_var= StringVar()
        self.dob_var= StringVar()
        self.search_by= StringVar()
        self.search_txt= StringVar()
#==============Manage frame============
        Manage_Frame=Frame(self.root, bd=4,relief=RIDGE,bg="light blue")
        Manage_Frame.place(x=20,y=100,height=585, width=470)

        m_title=Label(Manage_Frame, text="Manage student", bg="black", fg="white",font=("times new roman",40,"bold"))
        m_title.grid(row=0,columnspan=2,pady=20)

        lbl_roll=Label(Manage_Frame, text="Roll Number", bg="light blue", fg="black",font=("times new roman",20,"bold"))
        lbl_roll.grid(row=1,column=0,pady=10,padx=20,sticky="w")
        txt_roll=Entry(Manage_Frame,textvariable=self.Roll_No_var,font=("times new roman",15,"bold"), bd=5, relief=GROOVE)
        txt_roll.grid(row=1,column=1,pady=10,padx=20,sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="light blue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")
        txt_name = Entry(Manage_Frame,textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email", bg="light blue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")
        txt_email = Entry(Manage_Frame,textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="light blue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender=ttk.Combobox(Manage_Frame,textvariable=self.gender_var,font=("times new roman", 13, "bold"),state='readonly')
        combo_gender['values']=("male","female","other")
        combo_gender.grid(row=4, column=1,padx=20,pady=10)

        lbl_contact = Label(Manage_Frame,text="contact Number",  bg="light blue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")
        txt_contact = Entry(Manage_Frame,textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame,text="Date of birth", bg="light blue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")
        txt_dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", bg="light blue", fg="black",
                         font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")
        self.txt_address = Text(Manage_Frame,width=30, height=3 ,font=("times new roman", 10, "bold"))
        self.txt_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")
#==========btn frame==========
        btn_frame=Frame(Manage_Frame,bd=4,relief=RIDGE,bg="black")
        btn_frame.place(x=15,y=525,width=420)

        addbtn=Button(btn_frame, text="Add", width=10, command=self.add_students).grid(row=0,column=0,padx=10,pady=10)
        updatebtn=Button(btn_frame, text="Update", width=10, command=self.update_data).grid(row=0,column=1,padx=10,pady=10)
        delbtn=Button(btn_frame, text="Delete", width=10,command=self.delete_data).grid(row=0,column=2,padx=10,pady=10)
        clrbtn=Button(btn_frame, text="Clear", width=10, command=self.clear).grid(row=0,column=3,padx=10,pady=10)

#==============Detail frame============
        Detail_Frame=Frame(self.root, bd=4,relief=RIDGE,bg="light blue")
        Detail_Frame.place(x=500,y=100,height=585, width=880)

        lbl_search = Label(Detail_Frame, text="Search By", bg="light blue", fg="black",
                        font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame,textvariable=self.search_by, font=("times new roman", 13, "bold"),width=10,  state='readonly')
        combo_search['values'] = ("roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, padx=20, pady=10)

        txt_search = Entry(Detail_Frame,textvariable=self.search_txt, font=("times new roman", 10, "bold"),width=20, bd=5, relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        searchbtn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        showbtn = Button(Detail_Frame, text="Show all", width=10, pady=5, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)
# ==============tableframe============
        table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="black")
        table_Frame.place(x=10, y=70, height=500, width=760)

        scroll_x=Scrollbar(table_Frame,orient=HORIZONTAL)
        scroll_y=Scrollbar(table_Frame,orient=VERTICAL)

        self.Student_table= ttk.Treeview(table_Frame,column=("roll","name","email","gender","contact","dob","address"),xscrollcommand=scroll_y,yscrollcommand=scroll_x)
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)

        scroll_x.config()
        scroll_y.config()

        self.Student_table.heading("roll", text="Roll No")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("address", text="Address")

        self.Student_table['show']='headings'
        self.Student_table.column("roll", width=100)
        self.Student_table.column("name", width=100)
        self.Student_table.column("email", width=100)
        self.Student_table.column("gender", width=100)
        self.Student_table.column("contact", width=100)
        self.Student_table.column("dob", width=100)
        self.Student_table.column("address", width=100)

        self.Student_table.pack(fill=BOTH,expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get()==""or self.name_var.get()=="":
            messagebox.showerror("Error", "all fields are required to fill")
        else:
            con: Connection= pymysql.connect(host="localhost",user="root",password="",database="sms")
            cur=con.cursor()
            cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)",(self.Roll_No_var.get(),
                                                                             self.name_var.get(),
                                                                              self.email_var.get(),
                                                                              self.gender_var.get(),
                                                                              self.contact_var.get(),
                                                                              self.dob_var.get(),
                                                                              self.txt_address.get('1.0',END)))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("success","record has been inserted")
    def fetch_data(self ):
        con: Connection = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from students")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
            con.commit()
        con.close()

    def get_cursor(self,ev ):
        cursor_row=self.Student_table.focus()
        contents=self.Student_table.item(cursor_row)
        row=contents['values']
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END,row[6])



    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.txt_address.delete("1.0", END)

    def update_data(self):
        con: Connection = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("update students set name=%s, email=%s, gender=%s, contact=%s, dob=%s,address=%s where roll_no=%s", (
                                                                          self.name_var.get(),
                                                                          self.email_var.get(),
                                                                          self.gender_var.get(),
                                                                          self.contact_var.get(),
                                                                          self.dob_var.get(),
                                                                          self.txt_address.get('1.0', END),
                                                                          self.Roll_No_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()
        messagebox.showinfo("success", "record has been inserted")

    def delete_data(self):
        con:Connection = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("delete from students where roll_no=%s", self.Roll_No_var.get())
        con.commit()
        con.close()
        self.fetch_data()
        self.clear()

    def search_data(self):
        con:Connection = pymysql.connect(host="localhost", user="root", password="", database="sms")
        cur = con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" like'%"+str(self.search_txt.get())+"%'")
        rows=cur.fetchall()
        if len(rows)!=0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert("", END, values=row)
            con.commit()
        con.close()






class Students():
    root=Tk()
    obj=Students(root)
    root.mainloop()
