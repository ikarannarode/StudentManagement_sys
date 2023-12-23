from tkinter import *
from tkinter import ttk
import pymysql as msql
from tkinter import messagebox


class StudentManagement:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry('1440x880')

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE, height=2,
                      font=('arial', 20, "bold"), bg="slategrey", fg="lightgrey")
        title.pack(side=TOP, fill='x')

        Manage_frame = Frame(self.root, bd=4, relief=RIDGE, bg='slategrey')
        Manage_frame.place(x=10, y=80, width=510, height=760)

        m_title = Label(Manage_frame, text="Manage Students",
                        fg='white', bg='slategrey', font=('arial', 30, 'bold'))
        m_title.grid(row=0, columnspan=5, pady=20, padx=100)

        # ===================All Variables=====================
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()
        self.address_var = StringVar()
        self.Search_by = StringVar()
        self.Search_txt = StringVar()

        # =====================Manage Frame====================

        lbl_roll = Label(Manage_frame, text="Roll No: ", fg='white',
                         bg='slategrey', font=('arial', 18, 'bold'))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        txt_Roll = Entry(Manage_frame, textvariable=self.Roll_No_var, font=(
            'arial', 18, 'bold'), bd=5, relief=GROOVE)
        txt_Roll.grid(row=1, column=2, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_frame, text="Name : ", fg='white',
                         bg='slategrey', font=('arial', 18, 'bold'))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        txt_name = Entry(Manage_frame, textvariable=self.name_var, font=(
            'arial', 18, 'bold'), bd=5, relief=GROOVE)
        txt_name.grid(row=2, column=2, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_frame, text="Email: ", fg='white',
                          bg='slategrey', font=('arial', 18, 'bold'))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        txt_email = Entry(Manage_frame, textvariable=self.email_var, font=(
            'arial', 18, 'bold'), bd=5, relief=GROOVE)
        txt_email.grid(row=3, column=2, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_frame, text="Gender: ",
                           fg='white', bg='slategrey', font=('arial', 18, 'bold'))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_frame, textvariable=self.gender_var, font=('arial', 18, 'bold'),
                                    state='readonly')
        combo_gender['values'] = ("Male", "Female", "Others")
        combo_gender.grid(row=4, column=2, pady=10, padx=20, sticky="w")

        lbl_contact = Label(Manage_frame, text="Contact: ",
                            fg='white', bg='slategrey', font=('arial', 18, 'bold'))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        txt_contact = Entry(Manage_frame, textvariable=self.contact_var, font=('arial', 18, 'bold'), bd=5,
                            relief=GROOVE)
        txt_contact.grid(row=5, column=2, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_frame, text="Date Of Birth : ",
                        fg='white', bg='slategrey', font=('arial', 18, 'bold'))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        txt_dob = Entry(Manage_frame, textvariable=self.dob_var,
                        font=('arial', 18, 'bold'), bd=5, relief=GROOVE)
        txt_dob.grid(row=6, column=2, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_frame, text="Address: ",
                            fg='white', bg='slategrey', font=('arial', 18, 'bold'))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        txt_address = Entry(Manage_frame, font=('arial', 18, 'bold'), textvariable=self.address_var, bd=5,
                            relief=GROOVE)
        txt_address.grid(row=7, column=2, pady=10, padx=20, sticky="w")

        # ================Button Frame==============

        btn_Frame = Frame(Manage_frame, bd=4, relief=RAISED, bg='slategrey')
        btn_Frame.place(x=1, y=600, width=500, height=150)

        addbtn = Button(btn_Frame, text="Add", width=8,
                        height=2, command=self.add_students)
        addbtn.grid(row=1, column=1, padx=5, pady=10)

        updatebtn = Button(btn_Frame, text="Update", width=8,
                           height=2, command=self.update_data)
        updatebtn.grid(row=1, column=2, padx=5, pady=10)

        deletebtn = Button(btn_Frame, text="Delete", width=8,
                           height=2, command=self.delete_data)
        deletebtn.grid(row=1, column=3, padx=5, pady=10)

        clearbtn = Button(btn_Frame, text="Clear", width=8,
                          height=2, command=self.clear)
        clearbtn.grid(row=1, column=4, padx=5, pady=10)

        # ===============Detail Frame=================

        Detail_frame = Frame(self.root, bd=4, relief=RIDGE, bg='slategrey')
        Detail_frame.place(x=528, y=80, width=890, height=760)

        lblSearch = Label(Detail_frame, text="Search By",
                          fg='white', bg='slategrey', font=('arial', 15, 'bold'))
        lblSearch.grid(row=0, column=0, pady=20, padx=30)

        combo_search = ttk.Combobox(Detail_frame, font=('arial', 12, 'bold'), state='readonly', width=20,
                                    textvariable=self.Search_txt)
        combo_search['values'] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=10)

        txt_search = Entry(Detail_frame, font=(
            'arial', 13, 'bold'), bd=5, relief=GROOVE, textvariable=self.Search_by)
        txt_search.grid(row=0, column=2, pady=10, padx=10, sticky="w")

        searchbtn = Button(Detail_frame, bd=4, text="Search",
                           width=8, height=1, command=self.Search_data)
        searchbtn.grid(row=0, column=4, padx=10, pady=10)

        showallbtn = Button(Detail_frame, bd=4, text="Show All",
                            width=8, height=1, command=self.fetch_data)
        showallbtn.grid(row=0, column=5, padx=10, pady=10)

        # ===================Table Frame===================

        Table_frame = Frame(Detail_frame, bd=4, relief=RIDGE, bg='slategrey')
        Table_frame.place(x=20, y=80, width=850, height=670)

        scroll_x = Scrollbar(Table_frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_frame, orient=VERTICAL)
        self.Student_table = ttk.Treeview(Table_frame,
                                          columns=(
                                              "roll", "name", "email", "gender", "contact", "dob", "address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)
        self.Student_table.heading("roll", text="Roll No")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("address", text="Address")
        self.Student_table['show'] = "headings"
        self.Student_table.column('roll', width=10)
        self.Student_table.column('name', width=150)
        self.Student_table.column('email', width=180)
        self.Student_table.column('gender', width=60)
        self.Student_table.column('contact', width=60)
        self.Student_table.column('dob', width=50)
        self.Student_table.column('address', width=100)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>",
                                lambda event: self.get_cursor())
        self.fetch_data()

    def add_students(self):
        if self.Roll_No_var.get() == "" or self.name_var.get() == "":
            messagebox.showerror("Error", "All Fields Are Required!!!")
        else:
            con = msql.connect(host="localhost", user="root",
                               password="Apple012@2002$", db="StudentManagement")
            cursor = con.cursor()
            cursor.execute("INSERT INTO Students VALUES (%s,%s,%s, %s,%s, %s,%s)", (self.Roll_No_var.get(),
                                                                                    self.name_var.get(),
                                                                                    self.email_var.get(),
                                                                                    self.gender_var.get(),
                                                                                    self.contact_var.get(),
                                                                                    self.dob_var.get(),
                                                                                    self.address_var.get()
                                                                                    ))
            con.commit()
            self.fetch_data()
            self.clear()
            con.close()
            messagebox.showinfo("Success", "Record has been submitted..")

    def fetch_data(self):
        con = msql.connect(host="localhost", user="root",
                           password="Apple012@2002$", db="StudentManagement")
        cursor = con.cursor()
        cursor.execute('SELECT * FROM Students')
        rows = cursor.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)

        con.commit()
        con.close()

    def clear(self):
        self.Roll_No_var.set("")
        self.name_var.set("")
        self.email_var.set("")
        self.gender_var.set("")
        self.contact_var.set("")
        self.dob_var.set("")
        self.address_var.set("")

    def get_cursor(self):
        cursor_row = self.Student_table.focus()
        if cursor_row:
            contents = self.Student_table.item(cursor_row)
            row = contents['values']
            self.Roll_No_var.set(row[0])
            self.name_var.set(row[1])
            self.email_var.set(row[2])
            self.gender_var.set(row[3])
            self.contact_var.set(row[4])
            self.dob_var.set(row[5])
            self.address_var.set(row[6])

    def update_data(self):
        con = msql.connect(host="localhost", user="root",
                           password="Apple012@2002$", db="StudentManagement")
        cursor = con.cursor()
        cursor.execute("UPDATE Students SET name=%s, email=%s, gender=%s, contact=%s, dob=%s, address=%s WHERE roll_no=%s", (
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.address_var.get(),
            self.Roll_No_var.get()
        ))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def delete_data(self):
        messagebox.askyesnocancel("Warning","Are sure want to delete")
        con = msql.connect(host="localhost", user="root",
                           password="Apple012@2002$", db="StudentManagement")
        cursor = con.cursor()
        cursor.execute('DELETE FROM Students WHERE roll_no=%s',
                       (self.Roll_No_var.get(),))
        con.commit()
        self.fetch_data()
        self.clear()
        con.close()

    def Search_data(self):
        con = msql.connect(host="localhost", user="root",
                           password="Apple012@2002$", db="StudentManagement")
        cursor = con.cursor()

        column_name = self.Search_by.get()
        search_value = self.Search_txt.get()

        # Clear the table
        self.Student_table.delete(*self.Student_table.get_children())

        # Check if search_value is not empty
        if search_value.strip():
            # Execute the SQL query based on the selected column and search value
            cursor.execute(
                f"SELECT * FROM Students WHERE {column_name} LIKE %s", ('%' + search_value + '%',))
            rows = cursor.fetchall()

            for row in rows:
                self.Student_table.insert('', END, values=row)

        con.commit()
        con.close()


root = Tk()
obj = StudentManagement(root)
root.mainloop()
