# importamos o frame principal
import frame_principal

#importe da biblioteca wxpython
import wx

# Aqui criamos uma classe que é herdada frame principal
class FramePrincipal(frame_principal.MyFrame1):
    def __init__(self, parent):
        frame_principal.MyFrame1.__init__(self,parent)

app = wx.App()
frame = FramePrincipal(None)
frame.Show()

app.MainLoop()