import GUI
import wx
import wx.grid

class Daftar (GUI.Daftar):
    def __init__(self, parent):
        GUI.Daftar.__init__(self,parent)
        user = []
        password = []
        nama_toko = []
    def simpan_btn( self, event ):
        msgdlg = wx.MessageDialog(None,"Apakah Anda Yakin?", "konfirmasi", wx.YES_NO | wx.ICON_EXCLAMATION)
        kodedlg = msgdlg.ShowModal()
        if kodedlg == wx.ID_YES:
            self.user.append(self.input_username.GetValue())
            self.password.append(self.input_password.GetValue())
            self.nama_toko.append(self.input_toko.GetValue())
            print('username : ', self.user)
            print('password : ', self.password)
            print('nama_toko: ', self.nama_toko)
        else:
            cancel = wx.MessageDialog(None,"Data Tidak Disimpan", "Data Tidak Disimpan", wx.YES_NO | wx.ICON_INFORMATION)
            canceldlg = cancel.ShowModal()
    
    def masuk_btn( self, event ):
        framemasuk.Show()
        framedaftar.Hide()

class Masuk (GUI.Masuk):
    def __init__(self, parent):
        GUI.Masuk.__init__(self,parent)
        self.user = []
        self.password = []
    def simpan_btn_onbuttonclick( self, event ):
        msgdlg = wx.MessageDialog(None,"Apakah Anda Yakin?", "konfirmasi", wx.YES_NO | wx.ICON_EXCLAMATION)
        kodedlg = msgdlg.ShowModal()
        if kodedlg == wx.ID_YES:
            self.user.append(self.input_username.GetValue())
            self.password.append(self.input_password.GetValue())
            print('username : ', self.user)
            print('password : ', self.password)
        else:
            cancel = wx.MessageDialog(None,"Data Tidak Disimpan", "Data Tidak Disimpan", wx.YES_NO | wx.ICON_INFORMATION)
            canceldlg = cancel.ShowModal()    

    def daftar_btn( self, event ):
        framedaftar.Show()
        framemasuk.Hide()
    
    def login_btn(self, event):
        for i in range(len(self.user)):
            if self.input_username.GetValue() == self.user[i] and self.input_password.GetValue() == self.password[i]:
                framemasuk.Hide()
                framedashboard.Show()
    

        
    

        


app = wx.App()
framedaftar = Daftar(parent=None)
framedaftar.Show()
framemasuk = Masuk(parent=None)
framedashboard = GUI.Dashboard(parent=None)

app.MainLoop()