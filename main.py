import wx
from wx.core import BORDER_NONE, Event, FULL_REPAINT_ON_RESIZE, GetTextFromUser, ShowEvent
import GUI
import sqlite3
import numpy as np
import matplotlib

from matplotlib.figure import Figure
from matplotlib.backends.backend_wxagg import FigureCanvasWxAgg as FigureCanvas

class data:
    def __init__(self):
        self.con = sqlite3.connect("toko.db")
        self.cursor = self.con.cursor()

    def executeQuery(self, query, retVal = False):
        self.cursor.execute(query)
        all_result = self.cursor.fetchall()
        self.con.commit()
        if retVal:
            return all_result

class daftar(data, GUI.Daftar):
    def __init__(self, parent):
        GUI.Daftar.__init__(self, parent)
        self.data = data()

    def simpan_btn(self, event):
        msgdlg = wx.MessageDialog(None,"Apakah Anda Yakin?", "konfirmasi", wx.YES_NO | wx.ICON_EXCLAMATION)
        kodedlg = msgdlg.ShowModal()
        if kodedlg == wx.ID_YES:
            username = self.input_username.GetValue()
            password = self.input_password.GetValue()
            toko = self.input_toko.GetValue()
            if username != "" and password != "" and toko != "":
                self.query = f"INSERT INTO akun (username, password, nama_toko) VALUES (\'%s\', \'%s\', \'%s\')"
                self.query = self.query % (username, password, toko)
                self.data.executeQuery(self.query, retVal=True)
                wx.MessageBox('Data telah berhasil disimpan !', 'Berhasil')
                event = login(parent=None)
                event.Show()
                self.Destroy()
            else:
                wx.MessageBox('Data tidak boleh kosong !', 'Terjadi kesalahan')
        else:
            cancel = wx.MessageDialog(None,"Data Tidak Disimpan", "Data Tidak Disimpan", wx.YES_DEFAULT | wx.ICON_INFORMATION)
            canceldlg = cancel.ShowModal()

    def masuk_btn( self, event ):
        event = login(parent=None)
        event.Show()
        self.Destroy()

class login(data, GUI.Masuk):
    def __init__(self, parent):
        GUI.Masuk.__init__(self, parent)
        self.data = data()

    def login_btn(self, event):
        username = self.input_username.GetValue()
        password = self.input_password.GetValue()
        self.query = f"SELECT * FROM akun where username = '{username}' and password = '{password}'"
        result = self.data.executeQuery(self.query, retVal=True)
        print (result)
        
        if len(result) <= 0:
            wx.MessageBox('Username dan Password salah !', 'Terjadi kesalahan')
        for row in result:
            if row[0] == username and row[1] == password:
                event = dashboard(parent=None, user=self.input_username.GetValue())
                event.ShowFullScreen(show=True, style=FULL_REPAINT_ON_RESIZE)
                self.Destroy()
                self.data.con.close()

    def daftar_btn(self, event):
        event = daftar(parent=None)
        event.Show()
        self.Destroy()

class dashboard(data, GUI.Dashboard):
    def __init__(self, parent, user):
        GUI.Dashboard.__init__(self, parent)
        self.data = data()
        self.user = user
        self.showTransaksi()
        self.addEditDeleteTransaksi()
        self.showBarang()
        self.addEditDeleteBarang()
        self.showAkun()

    def refresh(self):
        event = dashboard(parent=None, user=True)
        event.ShowFullScreen(show=True, style=FULL_REPAINT_ON_RESIZE)
        self.Destroy()

    # Dashboard Transaksi
    def showTransaksi(self):
        self.query = 'SELECT * FROM transaksi'
        result = self.data.executeQuery(self.query, retVal=True)
        for a in result:
            self.tabelTansaksi.AppendRows(1)
        for b in range(5):
            a = 0
            for row in result:
                self.tabelTansaksi.SetCellValue(a, b, str(row[b]))
                a = a+1

    def addEditDeleteTransaksi(self):
        jmlKolom = self.tabelTansaksi.GetNumberCols()
        self.tabelTansaksi.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.tabelTansaksi.SetColLabelValue(colEdit, '')
        self.tabelTansaksi.SetColLabelValue(colDelete, '')

        for row in range(self.tabelTansaksi.GetNumberRows()):
            self.tabelTansaksi.SetCellValue(row, colEdit, 'Edit')
            self.tabelTansaksi.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.tabelTansaksi.SetCellTextColour(row, colEdit, wx.WHITE)

            self.tabelTansaksi.SetCellValue(row, colDelete, 'Delete')
            self.tabelTansaksi.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.tabelTansaksi.SetCellTextColour(row, colDelete, wx.WHITE)

        self.tabelTansaksi.Fit()
        self.Layout()

    def tabelTransaksiOnGridCmdSelectCell(self, event):
        baris = event.GetRow()
        kolom = event.GetCol()
        if kolom == 5:
            event = editTransaksi(parent=None)
            idtransaksi = self.tabelTansaksi.GetCellValue(baris, 0)
            tanggaltransaksi = self.tabelTansaksi.GetCellValue(baris, 1)
            idbarang = self.tabelTansaksi.GetCellValue(baris, 2)
            jumlah = self.tabelTansaksi.GetCellValue(baris, 3)
            total = self.tabelTansaksi.GetCellValue(baris, 4)
            event.settext(idtransaksi, tanggaltransaksi, idbarang, jumlah, total)
            event.Show()

        elif kolom == 6:
            idtransaksi = self.tabelTansaksi.GetCellValue(baris, 0)
            self.query = f"DELETE From Transaksi where id_transaksi = '{idtransaksi}'"
            self.data.executeQuery(self.query)
            if idtransaksi != "":
                self.refresh()

    def tambahTransaksi(self, event):
        event = tambahTransaksi(parent=None)
        event.Show()

    def grafikTransaksi(self, event):
        event = grafiktransaksi(None)
        event.Show()

    def grafikBarang(self, event):
        event = grafikbarang(None)
        event.Show()

    # Dashboard Data Barang
    def showBarang(self):
        self.query = 'SELECT * FROM barang'
        result = self.data.executeQuery(self.query, retVal=True)
        for a in result:
            self.tabelBarang.AppendRows(1)
        for b in range(6):
            a = 0
            for row in result:
                self.tabelBarang.SetCellValue(a, b, str(row[b]))
                a = a+1

    def addEditDeleteBarang(self):
        jmlKolom = self.tabelBarang.GetNumberCols()
        self.tabelBarang.AppendCols(2)
        colEdit = jmlKolom
        colDelete = jmlKolom + 1

        self.tabelBarang.SetColLabelValue(colEdit, '')
        self.tabelBarang.SetColLabelValue(colDelete, '')

        for row in range(self.tabelBarang.GetNumberRows()):
            self.tabelBarang.SetCellValue(row, colEdit, 'Edit')
            self.tabelBarang.SetCellBackgroundColour(row, colEdit, wx.BLUE)
            self.tabelBarang.SetCellTextColour(row, colEdit, wx.WHITE)

            self.tabelBarang.SetCellValue(row, colDelete, 'Delete')
            self.tabelBarang.SetCellBackgroundColour(row, colDelete, wx.RED)
            self.tabelBarang.SetCellTextColour(row, colDelete, wx.WHITE)

        self.tabelBarang.Fit()
        self.Layout()

    def tabelBarangOnGridCmdSellectCell(self, event):
        baris = event.GetRow()
        kolom = event.GetCol()
        if kolom == 6:
            event = editBarang(parent=None)
            idbarang = self.tabelBarang.GetCellValue(baris, 0)
            namabarang = self.tabelBarang.GetCellValue(baris, 1)
            jumlahstok = self.tabelBarang.GetCellValue(baris, 2)
            harga = self.tabelBarang.GetCellValue(baris, 3)
            jenis = self.tabelBarang.GetCellValue(baris, 4)
            berat = self.tabelBarang.GetCellValue(baris, 5)
            event.settext(idbarang, namabarang, jumlahstok, harga, jenis, berat)
            event.Show()

        elif kolom == 7:
            idbarang = self.tabelBarang.GetCellValue(baris, 0)
            self.query = f"DELETE From barang where id_barang = '{idbarang}'"
            self.data.executeQuery(self.query)
            if idbarang != "":
                self.refresh()
        
    def tambahBarang(self, event):
        event = tambahBarang(parent=None)
        event.Show()

    # Dashboard Akun Profil
    def showAkun(self):
        self.query = f"SELECT * FROM akun where username = '{self.user}'"
        result = self.data.executeQuery(self.query, retVal=True)
        akun = result[0]
        self.akunUsername.SetLabel(akun[0])
        self.akunPassword.SetLabel(akun[1])
        self.akunNamaToko.SetLabel(akun[2])

    def editAkun_btn(self, event):
        event = editAkun(parent=None)
        username = self.akunUsername.GetLabel()
        password = self.akunPassword.GetLabel()
        namatoko = self.akunNamaToko.GetLabel()
        event.settext(username, password, namatoko)
        event.Show()

class tambahTransaksi(dashboard, GUI.Tambah_Transaksi):
    def __init__(self, parent):
        GUI.Tambah_Transaksi.__init__(self, parent)
        self.data = data()

    def simpan_btn(self, event):
        msgdlg = wx.MessageDialog(None,"Apakah Anda Yakin?", "konfirmasi", wx.YES_NO | wx.ICON_EXCLAMATION)
        kodedlg = msgdlg.ShowModal()
        if kodedlg == wx.ID_YES:
            idTransaksi = self.inp_id_transaksi.GetValue()
            tglTransaksi = self.inp_tgl_transaksi.GetValue()
            idBarang = self.inp_id_barang.GetValue()
            jmlPembelian = self.inp_jml_pembelian.GetValue()
            total = self.inp_total.GetValue()

            if idTransaksi != "" and tglTransaksi != "" and idBarang != "" and jmlPembelian != "" and total != "":
                self.query = f"INSERT INTO transaksi (id_transaksi, tanggal_transaksi, id_barang, jumlah_pembelian, total_pembayaran) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\')"
                self.query = self.query % (idTransaksi, tglTransaksi, idBarang, jmlPembelian, total)
                self.data.executeQuery(self.query, retVal=True)
                wx.MessageBox('Data telah berhasil disimpan !', 'Berhasil')
                self.Destroy()
                self.refresh()
            else:
                wx.MessageBox('Data tidak boleh kosong !', 'Terjadi kesalahan')
        else:
            cancel = wx.MessageDialog(None,"Data Tidak Disimpan", "Data Tidak Disimpan", wx.YES_DEFAULT | wx.ICON_INFORMATION)
            canceldlg = cancel.ShowModal()
            self.Destroy()

class tambahBarang(dashboard, GUI.Tambah_Barang):
    def __init__(self, parent):
        GUI.Tambah_Barang.__init__(self, parent)
        self.data = data()

    def simpan_btn(self, event):
        msgdlg = wx.MessageDialog(None,"Apakah Anda Yakin?", "konfirmasi", wx.YES_NO | wx.ICON_EXCLAMATION)
        kodedlg = msgdlg.ShowModal()
        if kodedlg == wx.ID_YES:
            idBarang = self.inp_id_barang.GetValue()
            namaBarang = self.inp_nama_barang.GetValue()
            jmlStok = self.inp_jml_stok.GetValue()
            harga = self.inp_harga_barang.GetValue()
            jenis = self.inp_jenis_barang.GetValue()
            berat = self.inp_berat.GetValue()

            if idBarang != "" and namaBarang != "" and jmlStok != "" and harga != "" and jenis != "" and berat != "":
                self.query = f"INSERT INTO barang (id_barang, nama_barang, jumlah_stok, harga, jenis, berat) VALUES (\'%s\', \'%s\', \'%s\', \'%s\', \'%s\', \'%s\')"
                self.query = self.query % (idBarang, namaBarang, jmlStok, harga, jenis, berat)
                self.data.executeQuery(self.query, retVal=True)
                wx.MessageBox('Data telah berhasil disimpan !', 'Berhasil')
                self.Destroy()
                self.refresh()
            else:
                wx.MessageBox('Data tidak boleh kosong !', 'Terjadi kesalahan')
        else:
            cancel = wx.MessageDialog(None,"Data Tidak Disimpan", "Data Tidak Disimpan", wx.YES_DEFAULT | wx.ICON_INFORMATION)
            canceldlg = cancel.ShowModal()
            self.Destroy()

class editTransaksi(dashboard, GUI.Edit_Transaksi):
    def __init__(self, parent):
        GUI.Edit_Transaksi.__init__(self, parent)
        self.data = data()

    def settext(self, idtransaksi, tanggaltransaksi, idbarang, jumlah, total):
        self.edt_id_transaksi.SetValue(idtransaksi)
        self.edt_tgl_transaksi.SetValue(tanggaltransaksi)
        self.edt_id_barang.SetValue(idbarang)
        self.edt_jml_pembelian.SetValue(jumlah)
        self.edt_total.SetValue(total)

    def simpan_btn(self, event):
        msgdlg = wx.MessageDialog(None,"Apakah Anda Yakin?", "konfirmasi", wx.YES_NO | wx.ICON_EXCLAMATION)
        kodedlg = msgdlg.ShowModal()
        if kodedlg == wx.ID_YES:
            idTransaksi = self.edt_id_transaksi.GetValue()
            tglTransaksi = self.edt_tgl_transaksi.GetValue()
            idBarang = self.edt_id_barang.GetValue()
            jmlPembelian = self.edt_jml_pembelian.GetValue()
            total = self.edt_total.GetValue()

            if idTransaksi != "" and tglTransaksi != "" and idBarang != "" and jmlPembelian != "" and total != "":
                self.query = "UPDATE transaksi SET tanggal_transaksi = \'%s\', id_barang = \'%s\', jumlah_pembelian = \'%s\', total_pembayaran = \'%s\' WHERE id_transaksi = \'%s\'"
                self.query = self.query % (tglTransaksi, idBarang, jmlPembelian, total, idTransaksi)
                self.data.executeQuery(self.query, retVal=True)
                wx.MessageBox('Data telah berhasil disimpan !', 'Berhasil')
                self.Destroy()
                if idTransaksi != "":
                    self.refresh()
            else:
                wx.MessageBox('Data tidak boleh kosong !', 'Terjadi kesalahan')
        else:
            cancel = wx.MessageDialog(None,"Data Tidak Disimpan", "Data Tidak Disimpan", wx.YES_DEFAULT | wx.ICON_INFORMATION)
            canceldlg = cancel.ShowModal()
            self.Destroy()

class editBarang(dashboard, GUI.Edit_Barang):
    def __init__(self, parent):
        GUI.Edit_Barang.__init__(self, parent)
        self.data = data()

    def settext(self, idbarang, namabarang, jumlahstok, harga, jenis, berat):
        self.inp_id_barang.SetValue(idbarang)
        self.inp_nama_barang.SetValue(namabarang)
        self.inp_jml_stok.SetValue(jumlahstok)
        self.inp_harga_barang.SetValue(harga)
        self.inp_jenis_barang.SetValue(jenis)
        self.inp_berat.SetValue(berat)

    def simpan_btn(self, event):
        msgdlg = wx.MessageDialog(None,"Apakah Anda Yakin?", "konfirmasi", wx.YES_NO | wx.ICON_EXCLAMATION)
        kodedlg = msgdlg.ShowModal()
        if kodedlg == wx.ID_YES:
            idBarang = self.inp_id_barang.GetValue()
            namaBarang = self.inp_nama_barang.GetValue()
            jmlStok = self.inp_jml_stok.GetValue()
            harga = self.inp_harga_barang.GetValue()
            jenis = self.inp_jenis_barang.GetValue()
            berat = self.inp_berat.GetValue()

            if idBarang != "" and namaBarang != "" and jmlStok != "" and harga != "" and jenis != "" and berat != "":
                self.query = "UPDATE barang SET nama_barang = \'%s\', jumlah_stok = \'%s\', harga = \'%s\', jenis = \'%s\', berat = \'%s\' WHERE id_barang = \'%s\'"
                self.query = self.query % (namaBarang, jmlStok, harga, jenis, berat, idBarang)
                self.data.executeQuery(self.query, retVal=True)
                wx.MessageBox('Data telah berhasil disimpan !', 'Berhasil')
                self.Destroy()
                if idBarang != "":
                    self.refresh()
            else:
                wx.MessageBox('Data tidak boleh kosong !', 'Terjadi kesalahan')
        else:
            cancel = wx.MessageDialog(None,"Data Tidak Disimpan", "Data Tidak Disimpan", wx.YES_DEFAULT | wx.ICON_INFORMATION)
            canceldlg = cancel.ShowModal()
            self.Destroy()


class grafiktransaksi(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,size=(1920,1080))
        self.sp = wx.SplitterWindow(self)
        self.p1 = wx.Panel(self.sp)
        self.p2 = PanelTransaksi(self.sp)

class PanelTransaksi(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,1,size=(1920,1080))
        self.data = data()
        self.query = 'SELECT total_pembayaran FROM transaksi'
        result = self.data.executeQuery(self.query, retVal=True)
        a = 1
        b = len(result)+1
        s = result
        print(a)
        print(s)
        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        t = np.arange(a,b,1)
        self.axes.set_title("Grafik Transaksi")
        self.axes.set_xlabel("Tanggal")
        self.axes.set_ylabel("Pemasukan")
        self.axes.plot(t,s)
        self.canvas = FigureCanvas(self,1,self.figure)

class grafikbarang(wx.Frame):
    def __init__(self,parent):
        wx.Frame.__init__(self,parent,size=(1920,1080))
        self.sp = wx.SplitterWindow(self)
        self.p1 = wx.Panel(self.sp)
        self.p2 = PanelBarang(self.sp)

class PanelBarang(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent,1,size=(1920,1080))
        self.data = data()
        self.query = 'SELECT jumlah_stok from barang'
        result = self.data.executeQuery(self.query, retVal=True)
        a = 1
        b = len(result)+1
        s = result
        print(a)
        print(s)
        self.figure = Figure()
        self.axes = self.figure.add_subplot()
        t = np.arange(a,b,1)
        self.axes.set_title("Grafik Jumlah Stok")
        self.axes.set_xlabel("Kode Barang")
        self.axes.set_ylabel("Stok")
        self.axes.plot(t,s)
        self.canvas = FigureCanvas(self,1,self.figure)

class editAkun(dashboard, GUI.Edit_Akun):
    def __init__(self, parent):
        GUI.Edit_Akun.__init__(self,parent) 
        self.data = data()

    def settext(self, username, password, namatoko):
        self.input_username.SetValue(username)
        self.input_password.SetValue(password)
        self.input_toko.SetValue(namatoko)

    def simpan_btn(self, event):
        msgdlg = wx.MessageDialog(None,"Apakah Anda Yakin?", "konfirmasi", wx.YES_NO | wx.ICON_EXCLAMATION)
        kodedlg = msgdlg.ShowModal()
        if kodedlg == wx.ID_YES:
            username = self.input_username.GetValue()
            password = self.input_password.GetValue()
            toko = self.input_toko.GetValue()
            if username != "" and password != "" and toko != "":
                self.query = f"UPDATE akun SET password = \'%s\', nama_toko = \'%s\' WHERE username = \'%s\'"
                self.query = self.query % (password, toko, username)
                self.data.executeQuery(self.query, retVal=True)
                wx.MessageBox('Data telah berhasil disimpan !', 'Berhasil')
                self.Destroy()
                self.refresh()
            else:
                wx.MessageBox('Data tidak boleh kosong !', 'Terjadi kesalahan')
        else:
            cancel = wx.MessageDialog(None,"Data Tidak Disimpan", "Data Tidak Disimpan", wx.YES_DEFAULT | wx.ICON_INFORMATION)
            canceldlg = cancel.ShowModal()

app = wx.App()
frame = daftar(parent=None)
frame.Show()
app.MainLoop()    