#! /usr/bin/evn python
import wx
import time

#import the graphical library
#import the time module

class TenButtonFrame(wx.Frame):
	def __init__(self, parent):
		
		wx.Frame.__init__(self, parent, wx.ID_ANY, "Ten Button Race")
		
		#Make a new Panel
		self.panel = wx.Panel(self)
		
		#Make the start button
		self.btnStart = wx.Button(self.panel, label = "Start", pos = (150,100))
		self.btnStart.Bind(wx.EVT_BUTTON, self.OnStart)
		
		
		#Make the other ten buttons and bind all of them to their event handlers
		
		#Button 1
		self.btnButton1 = wx.Button(self.panel, label = "Button 1", pos = (200, 50))
		self.btnButton1.Bind(wx.EVT_BUTTON, self.OnButton1)
		
		#Button 2
		self.btnButton2 = wx.Button(self.panel, label = "Button 2", pos = (20, 80))
		self.btnButton2.Bind(wx.EVT_BUTTON, self.OnButton2)
	
		#Button 3
		self.btnButton3 = wx.Button(self.panel, label = "Button 3", pos = (46, 10))
		self.btnButton3.Bind(wx.EVT_BUTTON, self.OnButton3)
	
		#Button 4
		self.btnButton4 = wx.Button(self.panel, label = "Button 4", pos = (150, 100))
		self.btnButton4.Bind(wx.EVT_BUTTON, self.OnButton4)
		
		#Button 5
		self.btnButton5 = wx.Button(self.panel, label = "Button 5", pos = (74, 90))
		self.btnButton5.Bind(wx.EVT_BUTTON, self.OnButton5)
		
		#Button 6
		self.btnButton6 = wx.Button(self.panel, label = "Button 6", pos = (132, 130))
		self.btnButton6.Bind(wx.EVT_BUTTON, self.OnButton6)
		
		#Button 7
		self.btnButton7 = wx.Button(self.panel, label = "Button 7", pos = (50, 25))
		self.btnButton7.Bind(wx.EVT_BUTTON, self.OnButton7)
		
		#Button 8
		self.btnButton8 = wx.Button(self.panel, label = "Button 8", pos = (32, 61))
		self.btnButton8.Bind(wx.EVT_BUTTON, self.OnButton8)
		
		#Button 9
		self.btnButton9 = wx.Button(self.panel, label = "Button 9", pos = (171, 140))
		self.btnButton9.Bind(wx.EVT_BUTTON, self.OnButton9)
		
		#Button 10
		self.btnButton10 = wx.Button(self.panel, label = "Button 10", pos = (67, 123))
		self.btnButton10.Bind(wx.EVT_BUTTON, self.OnButton10)
		
		#End Message (Static Text)
		self.heading = wx.StaticText(self.panel, pos = (60, 100))
		
		#Hide the other ten buttons
		self.btnButton1.Show(False)
		self.btnButton2.Show(False)
		self.btnButton3.Show(False)
		self.btnButton4.Show(False)
		self.btnButton5.Show(False)
		self.btnButton6.Show(False)
		self.btnButton7.Show(False)
		self.btnButton8.Show(False)
		self.btnButton9.Show(False)
		self.btnButton10.Show(False)
		
	# Event handler for the start button
	def OnStart(self, e):
		
		#Make the start button disappear
		self.btnStart.Show(False)
		
		self.startTime = time.time()
		
		#Make Button One appear
		self.btnButton1.Show()

	#Other event handlers here
	def OnButton1(self, e):
		self.btnButton1.Show(False)
		self.btnButton2.Show()

	def OnButton2(self, e):
		self.btnButton2.Show(False)
		self.btnButton3.Show()

	def OnButton3(self, e):
		self.btnButton3.Show(False)
		self.btnButton4.Show()

	def OnButton4(self, e):
		self.btnButton4.Show(False)
		self.btnButton5.Show()

	def OnButton5(self, e):
		self.btnButton5.Show(False)
		self.btnButton6.Show()

	def OnButton6(self, e):
		self.btnButton6.Show(False)
		self.btnButton7.Show()

	def OnButton7(self, e):
		self.btnButton7.Show(False)
		self.btnButton8.Show()

	def OnButton8(self, e):
		self.btnButton8.Show(False)
		self.btnButton9.Show()

	def OnButton9(self, e):
		self.btnButton9.Show(False)
		self.btnButton10.Show()

	def OnButton10(self, e):
		self.btnButton10.Show(False)
		self.finishTime = time.time()
		self.heading.SetLabel("You have finished the race! Your time was %s seconds." % (str(self.finishTime - self.startTime)))

	#Remember the last event handler needs to print the final time.
		#It's in lines 64 and 86.


#Check lines 64 and 77.

	
# -------- Main Program Below ------------

app = wx.App(False)
frame = TenButtonFrame(None)
frame.Show()
app.MainLoop()

