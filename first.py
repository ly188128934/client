#!/usr/bin/python
#coding:utf-8
import wx

app = wx.App()
window = wx.Frame(None, title = "first test", size = (300,300))
panel = wx.Panel(window)
label = wx.StaticText(panel, label = "hello world", pos = (100,50))
window.Show(True)
app.mainLoop()
