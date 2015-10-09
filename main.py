# -*- coding: utf-8 -*-
from Tkinter import *
import generateName as gn
import judgeName as jn

class gynn:
    fg_color=['black','green','red']
    bg_color=['black','red','green']
    mail=['gmail','hotmail','outlook','163','126','139']
    domain=['com','info','me','net']
    mailIndex=[0,0,0,0,0,0]
    domIndex=[0,0,0,0]
    def __init__(self,master):
        self.master = master
        master.title("Generate Your Net Nickname")
        #master.geometry(800*600)
        
        f_bg=Frame(master)
        f_bg.pack(side=BOTTOM)
        
        
        f_left=Frame(f_bg)
        f_right=Frame(f_bg)
        f_left.pack(side=LEFT)
        f_right.pack(side=LEFT)
        
        #左侧frame
        f_genCh=Frame(f_left)
        f_genRes=Frame(f_left)
        f_genCh.pack(side=TOP)
        f_genRes.pack(side=TOP)
        
        #右侧frame
        f_judCh=Frame(f_right)
        f_judRes=Frame(f_right)
        f_judCh.pack(side=TOP)
        f_judRes.pack(side=TOP)
        
        f_genList=Frame(f_genRes)
        f_genResCh=Frame(f_genRes)
        f_genList.pack(side=LEFT)
        f_genResCh.pack(side=LEFT)
        
        f_judEmail=Frame(f_judRes)
        f_judDom=Frame(f_judRes)
        f_judCur=Frame(f_judRes)
        f_judCur.pack(side=TOP)
        f_judEmail.pack(side=LEFT)
        f_judDom.pack(side=LEFT)
        
        Label(master,text='This is a program to generate your net nickname').pack(side=TOP)
        
        f_combine=Frame(f_genCh)
        f_dict=Frame(f_genCh)
        f_genBut=Frame(f_genCh)
        f_combine.pack(side=TOP)
        f_dict.pack(side=TOP)
        f_genBut.pack(side=TOP)
        
        Label(f_combine,text='选用几个词来进行组合：').pack(side=TOP,anchor=W)
        
        self.genC=IntVar()
        self.genC.set(2)
        
        Radiobutton(f_combine,text='1个词',variable=self.genC,value=1).pack(side=LEFT,anchor=W)        
        Radiobutton(f_combine,text='2个词',variable=self.genC,value=2).pack(side=LEFT,anchor=W)
        Radiobutton(f_combine,text='3个词',variable=self.genC,value=3).pack(side=LEFT,anchor=W)
        
        Label(f_dict,text='选用词库：').pack(side=TOP,anchor=W)
        
        self.gendict=IntVar()
        
        Radiobutton(f_dict,text='高考3500',variable=self.gendict,value=0).pack(side=LEFT,anchor=W)        
        Radiobutton(f_dict,text='四六级',variable=self.gendict,value=1).pack(side=LEFT,anchor=W)
        Radiobutton(f_dict,text='雅思',variable=self.gendict,value=2).pack(side=LEFT,anchor=W)
        
        
        Button(f_genBut,text='生成！',command=lambda:self.generateNames()).pack(side=TOP,anchor=W)
        
        
        f_judgeC=Frame(f_judCh)
        f_judgeC.pack(side=TOP)
        
        Label(f_judgeC,text='选择验证方式').pack(side=TOP)
        
        self.judgeC=IntVar()
        
        Radiobutton(f_judgeC,text='不进行检验（速度最快）',variable=self.judgeC,value=0).pack(anchor=W)        
        Radiobutton(f_judgeC,text='只验证Email',variable=self.judgeC,value=1).pack(anchor=W)
        Radiobutton(f_judgeC,text='只验证域名（多线程验证）',variable=self.judgeC,value=2).pack(anchor=W)
        Radiobutton(f_judgeC,text='都进行验证',variable=self.judgeC,value=3).pack(anchor=W)        
        Radiobutton(f_judgeC,text='直接过滤结果（域名全绿的显示，慢！）',variable=self.judgeC,value=4).pack(anchor=W) 
        Label(f_genList,text='生成的结果').pack(side=TOP)
        
        self.nameRes=StringVar()
        self.lb=Listbox(f_genList,listvariable=self.nameRes)
        
        self.lb.bind('<ButtonRelease-1>', self.judegNames)
        self.lb.pack()
        
        Label(f_genResCh,text='显示结果选项').pack(side=TOP)
        
        self.genTimes=IntVar()
        self.genTimes.set(3)
        Radiobutton(f_genResCh,text='1',variable=self.genTimes,value=1).pack(anchor=W)        
        Radiobutton(f_genResCh,text='3',variable=self.genTimes,value=3).pack(anchor=W)
        Radiobutton(f_genResCh,text='5',variable=self.genTimes,value=5).pack(anchor=W)
        Radiobutton(f_genResCh,text='10',variable=self.genTimes,value=10).pack(anchor=W)
        
        self.curs=StringVar()
        
        Label(f_judCur,textvariable=self.curs,fg='blue').pack(side=TOP,anchor=W,fill=X,expand=YES)
        
        Label(f_judEmail,text='Email',fg='blue').pack(side=TOP)
        self.m=[]
        for i in xrange(len(self.mail)):
            self.m.append(Label(f_judEmail,text=self.mail[i],fg=self.fg_color[self.mailIndex[i]]))
            self.m[i].pack(side=TOP)
        
        Label(f_judDom,text='Domain',fg='blue').pack()
        self.d=[]
        for i in xrange(len(self.domain)):
            self.d.append(Label(f_judDom,text=self.domain[i],fg=self.fg_color[self.domIndex[i]]))
            self.d[i].pack(side=TOP)
        
        
    def generateNames(self):
        t=gn.generateName(self.gendict.get())
        self.names=[]
        cho=self.judgeC.get()
        for i in xrange(self.genTimes.get()):
            n=t.getNames(self.genC.get())
            if cho==4:
                domI=jn.judgeDomain(n)
                print domI
                if sum(domI)==len(self.domain):
                    self.names.append(n)
            else:
                self.names.append(n)
            
        self.nameRes.set(tuple(self.names))
        
    def judegNames(self,event):
        name=self.lb.get(self.lb.curselection())
        self.curs.set(name)
        j=jn.judgeName()
        
        if self.judgeC.get()==1:
            self.mailIndex = j.printEmail(name)
            for i in xrange(len(self.m)):
                self.m[i].config(fg=self.fg_color[self.mailIndex[i]])
            
        elif self.judgeC.get()==2:
            self.domIndex = jn.judgeDomain(name)
            for i in xrange(len(self.d)):
                self.d[i].config(fg=self.fg_color[self.domIndex[i]])
        
        elif self.judgeC.get()==3:
            self.mailIndex = j.printEmail(name)
            self.domIndex = jn.judgeDomain(name)
            for i in xrange(len(self.m)):
                self.m[i].config(fg=self.fg_color[self.mailIndex[i]])
            for i in xrange(len(self.d)):
                self.d[i].config(fg=self.fg_color[self.domIndex[i]])
        
root=Tk()
g=gynn(root)
root.mainloop()
