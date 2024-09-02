from tkinter import*
import random
from tkinter import messagebox


class Bill_App:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1350x700+0+0")
        self.root.title("Billing Software")
        bg_color="#FF0000"
        title=Label(self.root, text="Billing Software",bd=12, relief=GROOVE, bg=bg_color,fg="white",  font=("times new roman",30,"bold"),pady=2).pack(fill=X)
        #============================================VARIABLES==================================================

        #===========================================Food Delights===============================================
        self.shawarma=IntVar()
        self.burger=IntVar()
        self.pizza=IntVar()
        self.cutlet=IntVar()
        self.kebab=IntVar()
        self.momos=IntVar()
        self.wrap=IntVar()
        #==========================================Sweets========================================================
        self.rasmalai = IntVar()
        self.rasogulla = IntVar()
        self.kajuk = IntVar()
        self.laddoo = IntVar()
        self.ghevar = IntVar()
        self.kheer = IntVar()
        self.coco = IntVar()
        #============================================Drinks=======================================================
        self.tea = IntVar()
        self.cold = IntVar()
        self.breez = IntVar()
        self.vod = IntVar()
        self.wine = IntVar()
        self.teq = IntVar()
        self.mojito = IntVar()
        #===============================================Total=====================================================
        self.fp = StringVar()
        self.bp = StringVar()
        self.sp = StringVar()

        self.fta = StringVar()
        self.stx = StringVar()
        self.btx = StringVar()
        #=============================================Customer=====================================================
        self.c_name=StringVar()
        self.c_phn=StringVar()
        self.b_no=StringVar()
        x=random.randint(1000,9999)
        self.b_no.set(str(x))




        #===============================CUSTOMER DETAILS=========================================================
        F1=LabelFrame(self.root,bd=10,relief=GROOVE, text="Customer Details", font=("times new roman",15,"bold"),fg="gold",bg="black")
        F1.place(x=0,y=80, relwidth=1)

        cname_lbl=Label(F1,text="Customer Name",bg="#00ffff", font=("times new roman",15,"bold")).grid(row=0,column=0,padx=20,pady=5)
        cname_txt=Entry(F1,width=16,font="arial 15",textvariable=self.c_name, bd=7).grid(row=0, column=1, pady=5, padx=10)

        cphn_lbl = Label(F1, text="Customer Phone No.", bg="#00ffff", font=("times new roman", 15, "bold")).grid(row=0,column=6,padx=20,pady=5)
        cphn_txt = Entry(F1, width=16, font="arial 15",textvariable=self.c_phn, bd=7).grid(row=0, column=8, pady=5, padx=10)




        #=====================================FOOD ITEMS============================================================================
        F2=LabelFrame(self.root,bd=10,relief=SUNKEN, text="FOOD DELIGHTS", font=("times new roman",15,"bold"),fg="gold",bg="black")
        F2.place(x=5,y=180, width=300, height=380)

        f_lbl=Label(F2,text="SHAWARMA",bg="cyan", font=("times new roman",15,"bold"),fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        f_txt=Entry(F2,width=10,font=("times new roman",15,"bold"),textvariable=self.shawarma, bd=7, relief=SUNKEN).grid(row=0, column=1, pady=5, padx=10)

        f_lbl = Label(F2, text="BURGER", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F2, width=10, font=("times new roman", 15, "bold"), bd=7,textvariable=self.burger, relief=SUNKEN).grid(row=1, column=1,pady=5, padx=10)

        f_lbl = Label(F2, text="PIZZA", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F2, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.pizza).grid(row=2, column=1,pady=5, padx=10)

        f_lbl = Label(F2, text="MOMOS", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F2, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.momos).grid(row=3, column=1,pady=5, padx=10)

        f_lbl = Label(F2, text="KEBAB", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F2, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.kebab).grid(row=4, column=1,pady=5, padx=10)

        f_lbl = Label(F2, text="WRAP", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F2, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.wrap).grid(row=5, column=1,pady=5, padx=10)

        f_lbl = Label(F2, text="CUTLET", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F2, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.cutlet).grid(row=6, column=1,pady=5, padx=10)

        # =====================================DESSERT============================================================================
        F3 = LabelFrame(self.root, bd=10, relief=SUNKEN, text="DESSERT", font=("times new roman", 15, "bold"),fg="gold", bg="black")
        F3.place(x=310, y=180, width=300, height=380)

        d_lbl = Label(F3, text="Rasmalai", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        d_txt = Entry(F3, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.rasmalai).grid(row=0, column=1,pady=5, padx=10)

        d_lbl = Label(F3, text="Rasogulla", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=1,column=0,padx=10,pady=1,sticky="w")
        d_txt = Entry(F3, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.rasogulla).grid(row=1, column=1,pady=5, padx=10)

        d_lbl = Label(F3, text="Kaju Katli", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        d_txt = Entry(F3, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.kajuk).grid(row=2, column=1,pady=5, padx=10)

        d_lbl = Label(F3, text="Ghevar", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        d_txt = Entry(F3, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.ghevar).grid(row=3, column=1,pady=5, padx=10)

        d_lbl = Label(F3, text="Coconut Burfi", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        d_txt = Entry(F3, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.coco).grid(row=4, column=1,pady=5, padx=10)

        d_lbl = Label(F3, text="Laddoo", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        d_txt = Entry(F3, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.laddoo).grid(row=5, column=1,pady=5, padx=10)

        d_lbl = Label(F3, text="Kheer", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        d_txt = Entry(F3, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.kheer).grid(row=6, column=1,pady=5, padx=10)

        #=====================================================Beverages/Drinks==================================================================================
        F4 = LabelFrame(self.root, bd=10, relief=SUNKEN, text="Beverages/Drinks", font=("times new roman", 15, "bold"),fg="gold", bg="black")
        F4.place(x=615, y=180, width=300, height=380)

        f_lbl = Label(F4, text="Tea/Coffee", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=0,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F4, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.tea).grid(row=0, column=1,pady=5, padx=10)

        f_lbl = Label(F4, text="Cold Drink", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=1,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F4, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.cold).grid(row=1, column=1,pady=5, padx=10)

        f_lbl = Label(F4, text="Mojito", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=2,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F4, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.mojito).grid(row=2, column=1,pady=5, padx=10)

        f_lbl = Label(F4, text="Breezer", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=3,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F4, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.breez).grid(row=3, column=1,pady=5, padx=10)

        f_lbl = Label(F4, text="Vodka", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=4,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F4, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.vod).grid(row=4, column=1,pady=5, padx=10)

        f_lbl = Label(F4, text="Whiskey/Wine", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=5,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F4, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.wine).grid(row=5, column=1,pady=5, padx=10)

        f_lbl = Label(F4, text="Tequilla", bg="cyan", font=("times new roman", 15, "bold"), fg="black").grid(row=6,column=0,padx=10,pady=10,sticky="w")
        f_txt = Entry(F4, width=10, font=("times new roman", 15, "bold"), bd=7, relief=SUNKEN,textvariable=self.teq).grid(row=6, column=1,pady=5, padx=10)

        #=====================================================Billing Area======================================================================================
        F5 = LabelFrame(self.root, bd=10, relief=SUNKEN)
        F5.place(x=930, y=180, width=590, height=380)
        bill_title=Label(F5,text="Bill Area",font="arial 15 bold",bd=7,relief=GROOVE,bg="black",fg="gold").pack(fill=X)
        scrol_y=Scrollbar(F5,orient=VERTICAL)
        self.txtarea=Text(F5,yscrollcommand=scrol_y.set)
        scrol_y.pack(side=RIGHT,fill=Y)
        scrol_y.config(command=self.txtarea.yview)
        self.txtarea.pack(fill=BOTH,expand=1)

        #=============================================BUTTON FRAME======================================================================================
        F6 = LabelFrame(self.root, bd=10, relief=SUNKEN, text="Bill Menu", font=("times new roman", 15, "bold"),fg="cyan", bg="dark blue")
        F6.place(x=0, y=560, relwidth=1, height=240)

        m1_lbl=Label(F6,text="Total Food Cost",font=("times new roman",15,"bold"),fg="cyan",bg="dark blue").grid(row=0,column=0,padx=20,pady=2,sticky="w")
        m1_txt=Entry(F6,width=18,font="arial 10 bold",bd=7,relief=SUNKEN,textvariable=self.fp).grid(row=0,column=1,padx=10,pady=2)

        m2_lbl = Label(F6, text="Total Dessert Cost", font=("times new roman", 15, "bold"), fg="cyan",bg="dark blue").grid(row=1, column=0, padx=20, pady=2, sticky="w")
        m2_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN,textvariable=self.sp).grid(row=1, column=1, padx=10, pady=2)

        m3_lbl = Label(F6, text="Total Beverage/Drink Cost", font=("times new roman", 15, "bold"), fg="cyan",bg="dark blue").grid(row=2, column=0, padx=20, pady=2, sticky="w")
        m3_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN,textvariable=self.bp).grid(row=2, column=1, padx=10, pady=2)

        c1_lbl = Label(F6, text="Food Tax", font=("times new roman", 15, "bold"), fg="cyan",bg="dark blue").grid(row=0, column=2, padx=20, pady=2, sticky="w")
        c1_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN,textvariable=self.fta).grid(row=0, column=3, padx=10, pady=2)

        c2_lbl = Label(F6, text="Dessert Tax", font=("times new roman", 15, "bold"), fg="cyan",bg="dark blue").grid(row=1, column=2, padx=20, pady=2, sticky="w")
        c2_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN,textvariable=self.stx).grid(row=1, column=3, padx=10, pady=2)

        c3_lbl = Label(F6, text="Beverage/Drink Tax", font=("times new roman", 15, "bold"), fg="cyan",bg="dark blue").grid(row=2, column=2, padx=20, pady=2, sticky="w")
        c3_txt = Entry(F6, width=18, font="arial 10 bold", bd=7, relief=SUNKEN,textvariable=self.btx).grid(row=2, column=3, padx=10, pady=2)

        btn_f=Frame(F6,bd=7, relief=GROOVE)
        btn_f.place(x=920,width=590,height=105)

        total_btn=Button(btn_f,text="TOTAL",command=self.total,font="arial 15 bold",bd=5,width=10,bg="cadetblue",fg="white",pady=15).grid(row=0,column=0,padx=5,pady=5)
        GBill_btn = Button(btn_f, text="GENERATE",command=self.bill_area, font="arial 15 bold", bd=5, width=10, bg="cadetblue", fg="white",pady=15).grid(row=0, column=1, padx=5, pady=5)
        Clear_btn = Button(btn_f, text="CLEAR",command=self.clear, font="arial 15 bold", bd=5, width=10, bg="cadetblue", fg="white",pady=15).grid(row=0, column=2, padx=5, pady=5)
        Exit_btn = Button(btn_f, text="EXIT",command=self.Exit, font="arial 15 bold", bd=5, width=9, bg="cadetblue", fg="white",pady=15).grid(row=0, column=3, padx=5, pady=5)
        self.welcome_bill()

    def total(self):
        self.fsp=self.shawarma.get()*60
        self.fbp=self.burger.get() *120
        self.fpp=self.pizza.get() *350
        self.fmp=self.momos.get() *100
        self.fkp= self.kebab.get() *260
        self.fcp=self.cutlet.get() *60
        self.fwp=self.wrap.get() *100



        self.total_fp= float(
                         self.fsp +
                         self.fbp +
                         self.fpp +
                         self.fmp +
                         self.fkp +
                         self.fcp +
                         self.fwp)
        self.fp.set("Rs. "+str(self.total_fp))
        self.f_tax = round((self.total_fp) * 0.18, 2)
        self.fta.set("Rs. "+ str(self.f_tax))

        self.srp=self.rasogulla.get() * 30
        self.srm=self.rasmalai.get() * 30
        self.skp=self.kheer.get() * 50
        self.slp=self.laddoo.get() * 10
        self.snp=self.coco.get() * 26
        self.skj=self.kajuk.get() * 60
        self.sgp=self.ghevar.get() * 100



        self.total_sp = float(
                               self.srp +
                               self.srm +
                               self.skp +
                               self.slp +
                               self.snp +
                               self.skj +
                               self.sgp
                              )
        self.sp.set("Rs. "+str(self.total_sp))
        self.s_tax = round((self.total_sp) * 0.18, 2)
        self.stx.set("Rs. " + str(self.s_tax))

        self.btp=self.tea.get() * 10
        self.bcp=self.cold.get() * 40
        self.bmp=self.mojito.get() * 150
        self.bwp=self.wine.get() * 1200
        self.btq=self.teq.get() * 1540
        self.bvp=self.vod.get() * 6000
        self.bbp=self.breez.get() * 100



        self.total_bp = float(
                              self.btp +
                              self.bcp +
                              self.bmp +
                              self.bwp +
                              self.btq +
                              self.bvp +
                              self.bbp)
        self.bp.set("Rs. "+str(self.total_bp))
        self.b_tax = round((self.total_bp) * 0.18, 2)
        self.btx.set("Rs. " + str(self.b_tax))

        self.Total_bill=float(self.total_fp+self.total_bp+self.total_sp+self.f_tax+self.s_tax+self.b_tax)
        self.tb=round(self.Total_bill,2)

    def welcome_bill(self):
        self.txtarea.delete('1.0',END)
        self.txtarea.insert(END,"\t\t\t   Welcome to RB Plaza \n")
        self.txtarea.insert(END, f"\n Bill Number : {self.b_no.get()}")
        self.txtarea.insert(END, f"\n Customer Name : {self.c_name.get()}")
        self.txtarea.insert(END, f"\n Phone Number : {self.c_phn.get()}")
        self.txtarea.insert(END, f"\n====================================================================")
        self.txtarea.insert(END, f"\nProducts \t\t\t\t QTY \t\t\t  Price")
        self.txtarea.insert(END, f"\n====================================================================")
    def bill_area(self):
        if self.c_name.get()=="" or self.c_phn.get()=="":
            messagebox.showerror("Error","Customer Details Not Found")
        elif self.fp.get()=="Rs. 0.0" and  self.sp.get()=="Rs. 0.0" and self.bp.get()=="Rs. 0.0":
            messagebox.showerror("Error", "No Product Selected")
        else:
            self.welcome_bill()
            #====================================Food===================================================
            if self.shawarma.get()!=0:
                self.txtarea.insert(END, f"\nShawarma \t\t\t\t {self.shawarma.get()} \t\t\t  {self.fsp}")
            if self.burger.get() != 0:
                    self.txtarea.insert(END, f"\nBurger \t\t\t\t {self.burger.get()} \t\t\t  {self.fbp}")
            if self.pizza.get() != 0:
                    self.txtarea.insert(END, f"\nPizza \t\t\t\t {self.pizza.get()} \t\t\t  {self.fpp}")
            if self.momos.get() != 0:
                    self.txtarea.insert(END, f"\nMomos \t\t\t\t {self.momos.get()} \t\t\t  {self.fmp}")
            if self.kebab.get() != 0:
                    self.txtarea.insert(END, f"\nKebab \t\t\t\t {self.kebab.get()} \t\t\t  {self.fkp}")
            if self.cutlet.get() != 0:
                    self.txtarea.insert(END, f"\nCutlet \t\t\t\t {self.cutlet.get()} \t\t\t  {self.fcp}")
            if self.wrap.get() != 0:
                    self.txtarea.insert(END, f"\nWrap \t\t\t\t {self.wrap.get()} \t\t\t  {self.fwp}")

            # ====================================Sweets===================================================
            if self.rasmalai.get() != 0:
                self.txtarea.insert(END, f"\nRasmalai \t\t\t\t {self.rasmalai.get()} \t\t\t  {self.srm}")
            if self.rasogulla.get() != 0:
                self.txtarea.insert(END, f"\nRasogulla \t\t\t\t {self.rasogulla.get()} \t\t\t  {self.srp}")
            if self.kheer.get() != 0:
                self.txtarea.insert(END, f"\nKheer \t\t\t\t {self.kheer.get()} \t\t\t  {self.skp}")
            if self.kajuk.get() != 0:
                self.txtarea.insert(END, f"\nKaju Katli \t\t\t\t {self.kajuk.get()} \t\t\t  {self.skj}")
            if self.ghevar.get() != 0:
                self.txtarea.insert(END, f"\nGhevar \t\t\t\t {self.ghevar.get()} \t\t\t  {self.sgp}")
            if self.laddoo.get() != 0:
                self.txtarea.insert(END, f"\nLaddoo \t\t\t\t {self.laddoo.get()} \t\t\t  {self.slp}")
            if self.coco.get() != 0:
                self.txtarea.insert(END, f"\nCoconut Burfi \t\t\t\t {self.coco.get()} \t\t\t  {self.snp}")
            # ====================================Drinks===================================================
            if self.tea.get() != 0:
                    self.txtarea.insert(END, f"\nTea/Coffee \t\t\t\t {self.tea.get()} \t\t\t  {self.btp}")
            if self.cold.get() != 0:
                    self.txtarea.insert(END, f"\nCold Drink \t\t\t\t {self.cold.get()} \t\t\t  {self.bcp}")
            if self.mojito.get() != 0:
                    self.txtarea.insert(END, f"\nMojito \t\t\t\t {self.mojito.get()} \t\t\t  {self.bmp}")
            if self.teq.get() != 0:
                    self.txtarea.insert(END, f"\nTequila \t\t\t\t {self.teq.get()} \t\t\t  {self.btq}")
            if self.vod.get() != 0:
                    self.txtarea.insert(END, f"\nVodka \t\t\t\t {self.vod.get()} \t\t\t  {self.bvp}")
            if self.wine.get() != 0:
                    self.txtarea.insert(END, f"\nWine/Whiskey \t\t\t\t {self.wine.get()} \t\t\t  {self.bwp}")
            if self.breez.get() != 0:
                    self.txtarea.insert(END, f"\nBreezer \t\t\t\t {self.breez.get()} \t\t\t  {self.bbp}")
            self.txtarea.insert(END, f"\n-------------------------------------------------------------------")
            if self.fta.get()!="Rs. 0.0":
               self.txtarea.insert(END, f"\nFood Tax \t\t\t\t {self.fta.get()}")
            if self.stx.get() !="Rs. 0.0":
                self.txtarea.insert(END, f"\nSweet Tax \t\t\t\t {self.stx.get()}")
            if self.btx.get() != "Rs. 0.0":
                self.txtarea.insert(END, f"\nDrink Tax \t\t\t\t {self.btx.get()}")
            self.txtarea.insert(END, f"\nPayable Amount \t\t\t\t Rs. {self.tb}")
            self.txtarea.insert(END, f"\n--------------------------------------------------------------------")
            self.save_bill()

    def save_bill(self):
             op=messagebox.askyesno("Save File","Do you want to save this bill?")
             if op>0:
                self.bill_data= self.txtarea.get('1.0',END)
                F1=open("bills/"+str(self.b_no.get())+".txt","w")
                F1.write(self.bill_data)
                F1.close()
                messagebox.showinfo("Successfully Saved",f"The Bill {self.b_no.get()} has been saved")
             else:
                return

    def clear(self):
        op = messagebox.askyesno("Clear Data", "Do you want to clear data?")
        if op > 0:

            # ===========================================Food Delights===============================================
            self.shawarma.set(0)
            self.burger.set(0)
            self.pizza.set(0)
            self.cutlet.set(0)
            self.kebab.set(0)
            self.momos.set(0)
            self.wrap.set(0)
            # ==========================================Sweets========================================================
            self.rasmalai.set(0)
            self.rasogulla.set(0)
            self.kajuk.set(0)
            self.laddoo.set(0)
            self.ghevar.set(0)
            self.kheer.set(0)
            self.coco.set(0)
            # ============================================Drinks=======================================================
            self.tea.set(0)
            self.cold.set(0)
            self.breez.set(0)
            self.vod.set(0)
            self.wine.set(0)
            self.teq.set(0)
            self.mojito.set(0)
            # ===============================================Total=====================================================
            self.fp.set("")
            self.bp.set("")
            self.sp.set("")

            self.fta.set("")
            self.stx.set("")
            self.btx.set("")
            # =============================================Customer=====================================================
            self.c_name.set("")
            self.c_phn.set("")
            self.b_no.set("")
            x = random.randint(1000, 9999)
            self.b_no.set(str(x))

            self.welcome_bill()
    def Exit(self):
        op=messagebox.askyesno("Exit","Do you want to exit?")
        if op > 0:
            self.root.destroy()




root=Tk()
obj = Bill_App(root)
root.mainloop()



