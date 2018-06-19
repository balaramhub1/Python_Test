from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror
import os
import filecmp
import smtplib


class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("BIN Compare...!!!")
        #self.master.rowconfigure(50, weight=50)
        #self.master.columnconfigure(50, weight=50)
        #self.grid(sticky=W+E+N+S)
        self.L1 = Label(text="First file name:",width=10)
        self.L1.grid(row=0,column=0,sticky=N)
        self.button = Button(text="Browse file 1", command=self.load_file, width=10)
        self.button.grid(row=0, column=1,sticky=N)
        self.L1 = Label(text="Second file name:",width=15)
        self.L1.grid(row=1,column=0,sticky=N)
        self.button = Button(text="Browse file 2", command=self.load_file1, width=10)
        self.button.grid(row=1, column=1,sticky=N)
        self.button = Button( text="compare", command=self.cmpp, width=10)
        self.button.grid(row=3, column=1, sticky=N)
        self.button=Button(text="Compose mail",command=self.send,width=10)
        self.button.grid(row=5,column=3,sticky=N)
     
       
    def load_file(self):
        
        self.fname = askopenfilename(filetypes = (("All files", "*.*")
                                                             ,("HTML files", "*.html;*.htm")
                                                             ,("Template files", "*.tplate") ))
        self.l=Label(text="",width=10)
        self.l.grid(row=5,column=1,sticky=N)
        self.s1= os.path.basename(self.fname)
        return self.s1
        
    def load_file1(self):
        
        self.fname1 = askopenfilename(filetypes = (("All files", "*.*")
                                                             ,("HTML files", "*.html;*.htm")
                                                             ,("Template files", "*.tplate") ))
        self.s2= os.path.basename(self.fname1)
        return self.s2
       # if fname:
        #    try:
         #       print("""here it comes: self.settings["template"].set(fname)""")
          #  except:                     # <- naked except is a bad idea
           #     showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            #return

    def cmpp(self):

        a=filecmp.cmp(self.fname,self.fname1)
       
        if a==1:
            part4 = str(a);
            self.l=Label(text=part4,width=10,bg="green")
            self.l.grid(row=5,column=1,sticky=N)
            return part4
        else:
            part4 = str(a);
            self.l=Label(text=part4,width=10,bg="red")
            self.l.grid(row=5,column=1,sticky=N)
            return part4


    def send(self):
        
        self.part10=self.cmpp()
        self.part11="Bin comparsion result:"
        self.part12=self.part11+self.part10
        self.l1=Label(text="To:",width=10)
        self.l1.grid(row=6,column=0,sticky=N)
        self.t1=Text(height=1,width=35)
        self.t1.grid(row=6,column=1,sticky=N)
        self.l2=Label(text="Subject:",width=10)
        self.l2.grid(row=7,column=0,sticky=N)
        self.t2=Text(height=1,width=35)
        self.t2.grid(row=7,column=1,sticky=N)
        self.l3=Label(text="Body",width=10)
        self.l3.grid(row=8,column=0,sticky=N)
        self.t3=Text(height=10,width=35)
        self.t3.grid(row=8,column=1,sticky=N)
        self.t2.insert(END,self.part12)
        self.part13="Dear Sir/Ma'am, \n Please find the comparsion test result for below files.\n\n First file name: %s \n Second file name:%s \n comparsion result: %s \n\n Regards \n" %(self.s1,self.s2,self.part10)
        self.t3.insert(END,self.part13)
        self.button=Button(text="Send mail",command=self.send1,width=10)
        self.button.grid(row=9,column=2,sticky=N)
        self.g2=self.t2.get(1.0,END)
        self.g3=self.t3.get(1.0,END)
        
        

        
    def send1(self):

        self.g1=self.t1.get(1.0,END)
        sender = self.g1
        receivers = self.g1
        #print(self.g1);
        #print(self.g2);
        #print(self.g3);
        #part1= "Bin comparesion result:%s" %(part4)
        #part2 = self.fname;
        #part3 = self.fname1;
        


        msg = """From: %s
To: %s
MIME-Version: 1.0
Content-type: text/html
Subject: %s
%s
""" % ( self.g1, self.g1, self.g2, self.g3 )
        


        
        
       # message= part1 +part2+part3+part4;
       
        try:
           username = 'legendrock999@gmail.com';
           password = '999legend';
           server = smtplib.SMTP('smtp.gmail.com:587');
           server.starttls();
           server.login(username,password);
           server.sendmail(sender, receivers, msg);
           print("Mail send sucessfully...!");
           server.quit();
    
        except SMTPException:
           print ("Error: unable to send email");



if __name__ == "__main__":
    MyFrame().mainloop()
