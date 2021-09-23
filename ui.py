# -*- coding: utf-8 -*-
"""
Created on Thu Sep 23 12:15:36 2021

@author: s2786134
"""

try:
    import wx
except ImportError:
    raise ImportError, "The wxPython module is required to run this program"

class myGui(wx.Frame):
    def __init__(self,parent,id,title):
        wx.Frame.__init__(self,parent,id,title)
        self.parent = parent
        self.initialise()
        
    def initialise(self):
        self.Show(True)
        
if __name__ == "__main__":
    app = wx.App()
    frame = myGui(None,-1,‘My Application')
    app.MainLoop()