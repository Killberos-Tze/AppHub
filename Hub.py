#!/usr/bin/env python3

from tkinter import Frame, Tk, Button
import sys


class MultipleApps():
    def init_start(self):
        self.root.mainloop()
    
    def __init__(self,**kwargs):
        self.root = Tk()
        self.root.title('Application hub')
        self.root.geometry('%dx%d+%d+%d' % (350, 400, 50, 50))
        self.rootframe = Frame(self.root)
        self.rootframe.pack(pady = (25,25), padx = (25,25))
        self.landingframe=Frame(self.rootframe)
        self.landingframe.grid(row=0,column=0)
        kwargs=self.process_kwargs(**kwargs)
        self.apps_landing(self.landingframe,kwargs['app_list'])
        
    def my_exit(self,*args,**kwargs):
        sys.exit()
        
    def process_kwargs(self,**kwargs):
        if 'app_list' not in kwargs:
            kwargs['app_list']=[self.my_exit]
        return kwargs
    
    def apps_landing(self,parent,app_list):
        row=0
        for key, item in app_list.items():
            Button(self.landingframe, text=f"{key}", command=lambda app=item,apps=app_list: self.start_app(app,apps),width=12,bg='lightgray').grid(row=row,column=1)
            row+=1
        
    def single_app_landing(self,apps):
        self.sideframe=Frame(self.landingframe)
        self.sideframe.grid(row=0,column=0,sticky='NW')
        self.mainframe=Frame(self.landingframe)
        self.mainframe.grid(row=0,column=1,columnspan=10)
        Button(self.sideframe, text="Go back", command= lambda apps=apps: self.stop_app(apps),width=4,bg='lightgray').grid(row=0,column=0)
        
    def placeholder(self):
        pass
#
    def start_app(self,app,apps):
        self.landingframe.destroy()
        self.landingframe=Frame(self.rootframe)
        self.landingframe.grid(row=0,column=0)
        self.single_app_landing(apps)
        #AppWindow(parent=parent).grid(row=0,column=0)
        tmp=app(parent=self.mainframe)
        tmp.grid(row=0,column=0)
        self.root.title(str(tmp))
        self.root.geometry('%dx%d+%d+%d' % tmp.appgeometry)
        #Button(parent, text="Go back", command=lambda frame=parent: self.stop_app(parent),width=12,bg='lightgray').grid(row=rowcount,column=1)
#
        
    def stop_app(self,apps):
        self.landingframe.destroy()
        self.landingframe=Frame(self.rootframe)
        self.landingframe.grid(row=0,column=0)
        self.apps_landing(self.landingframe,app_list=apps)
        self.root.title('Application hub')
        self.root.geometry('%dx%d+%d+%d' % (350, 400, 50, 50))
        
        
class SingleApp(MultipleApps):
    def init_start(self):
        self.root.mainloop()
    
    def __init__(self,**kwargs):
        self.root = Tk()
        self.root.title('Application hub')
        self.root.geometry('%dx%d+%d+%d' % (350, 400, 50, 50))
        self.rootframe = Frame(self.root)
        self.rootframe.pack(pady = (25,25), padx = (25,25))
        self.process_kwargs(kwargs)
        app=kwargs['app']
        tmp=app(parent=self.rootframe)
        tmp.grid(row=0,column=0)
        self.root.title(str(tmp))
        try:
            self.root.geometry('%dx%d+%d+%d' % tmp.appgeometry)
        except:
            pass

     
    def process_kwargs(self,kwargs):
        if 'app' not in kwargs:
            sys.exit()
        return kwargs
        
#if __name__=='__main__':
#    MultipleApps.init_start(MultipleApps())
    
