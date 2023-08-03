from tkinter import *
import sqlite3 as sql

conn=sql.connect('Contacts.db')
cur=conn.cursor()

try:
    cur.execute('create table Diary(Name varchar(100), Phone bigint)')
    
except:
    print("Diary already exists")
    
finally:
        
    def save(n,p):
        stmt='insert into Diary values(?,?)'
        cur.execute(stmt,(n.get(),p.get()))
        conn.commit()
        label=Label(app,text="Saved. Refresh or Open again")
        label.pack()
    
    app=Tk()
    app.title('Contacts')
    
    label=Label(app,text="Contacts",font=('Arial',25,'bold'))
    label.pack()
    
    #Frame for Contact Search 
    search_frame=Frame(app)
    search_frame.pack()
    s_con=Entry(search_frame,font=('Calibri',13))
    s_con.pack(side='left')
    search_button=Button(search_frame,text="Search",bg='light blue',command=lambda:search(s_con))
    search_button.pack()
    
    #Frame for search result
    s_result_frame=Frame(app)
    s_result_frame.pack()
    
    #Display all Contacts
    cont_label=Label(app,text="Contacts list",fg='green',font=("bold",12))
    cont_label.pack()
    con_list=Listbox(app,bg='sky blue',borderwidth=4,    relief=GROOVE)    #list of contacts
    con_list.pack()    
    
    for i in cur.execute('select * from Diary'):
        con_list.insert(END,i)        
    
    #Function to Search a Contact
    def search(c):
        stmt='select * from Diary where Name=?'
        for i in cur.execute(stmt,(c.get(),)):
            contact=StringVar()
            contact.set(i)
            label=Label(s_result_frame,textvariable=contact)
            label.pack(side='left')
    
    label=Label(app)
    label.pack()

    #Main frame
    main_frame=Frame(app)
    main_frame.pack()
    #Frame for Saving Contacts
    save_frame=Frame(main_frame,bg='light blue',relief=GROOVE)
    save_frame.pack()
    
    #Frame for accepting the name
    name_frame=Frame(save_frame)
    name_frame.pack()
    name_label=Label(name_frame,text="Name:",bg='light blue')
    name_label.pack(side='left')
    name=Entry(name_frame,width=21)
    name.pack()
    
    #Frame for accepting phone number
    phone_frame=Frame(save_frame)
    phone_frame.pack()
    phone_label=Label(phone_frame,text="Phone No.:",bg='light blue')
    phone_label.pack(side='left')
    phone=Entry(phone_frame,width=18)
    phone.pack()
    
    save_btn=Button(main_frame,text="Save",bg='blue',fg='white',command=lambda:save(name,phone))
    save_btn.pack()
    #Function to delete a contact
    def delete(c):
        stmt='delete from Diary where Name=?'
        cur.execute(stmt,(c.get(),))
        conn.commit()
        label=Label(app,text="Deleted. Refresh or Open again")
        label.pack()
        
    label=Label(app)
    label.pack()
    
    #Frame for Deleting a Contact
    del_frame=Frame(app)
    del_frame.pack()
    d_con=Entry(del_frame,font=('Calibri',13))
    d_con.pack(side='left')
    del_btn=Button(del_frame,text="Delete",bg='red',command=lambda:delete(d_con))
    del_btn.pack()

    app.mainloop()