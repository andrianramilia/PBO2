import wx
from wx.core import FULLSCREEN_ALL, FULL_REPAINT_ON_RESIZE
import GUI
import sqlite3

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
                event = dashboard(parent=None)
                event.ShowFullScreen(show=True, style=FULL_REPAINT_ON_RESIZE)
                self.Destroy()
                self.data.con.close()

    def daftar_btn(self, event):
        event = daftar(parent=None)
        event.Show()
        self.Destroy()

class dashboard(data, GUI.Dashboard):
    def __init__(self, parent):
        GUI.Dashboard.__init__(self, parent)
        self.data = data()
        self.showTransaksi()
        self.addEditDeleteTransaksi()

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
        self.m_panel33.Layout()

    # def editDeleteTransaksi(self, event):
    #     baris = event.GetRow()
    #     kolom = event.GetCol()

    #     print('baris: ', baris)
    #     print('kolom: ', kolom)

    #     self.query = 'SELECT id_transaksi FROM transaksi'
    #     result = self.data.executeQuery(self.query, retVal=True)
        
    #     if kolom == 6:
    #         id_person = self.lstIdPerson[baris]
    #         dlg = dlgInsert(self, id_person)
    #         nama = self.tabelSiswa.GetCellValue(baris, 0)
    #         email = self.tabelSiswa.GetCellValue(baris, 1)
    #         nim = self.tabelSiswa.GetCellValue(baris, 2)
    #         tahunMasuk = self.tabelSiswa.GetCellValue(baris, 3)
    #         dlg.isiDataMhs(nama, email, nim, tahunMasuk)
    #         dlg.ShowModal()
    #     elif kolom == 7:
    #         dlg = wx.MessageDialog(
    #             self, 'Hapus data', 'Informasi', style=wx.YES_NO)
    #         retval = dlg.ShowModal()
    #         if retval == wx.ID_YES:
    #             print('hapus')
    #             self.mhs.deleteMahasiswa(self.lstIdPerson[baris])
    #             self.initData()
    #             self.AddButtonEditDelete()

    def tambahTransaksi(self, event):
        event = tambahTransaksi(parent=None)
        event.Show()

class tambahTransaksi(data, GUI.Tambah_Transaksi):
    def __init__(self, parent):
        GUI.Tambah_Transaksi.__init__(self, parent)

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
            else:
                wx.MessageBox('Data tidak boleh kosong !', 'Terjadi kesalahan')
        else:
            cancel = wx.MessageDialog(None,"Data Tidak Disimpan", "Data Tidak Disimpan", wx.YES_DEFAULT | wx.ICON_INFORMATION)
            canceldlg = cancel.ShowModal()

class tambahBarang(data, GUI.Tambah_Barang):
    def __init__(self, parent):
        GUI.Tambah_Barang.__init__(self, parent)

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
            else:
                wx.MessageBox('Data tidak boleh kosong !', 'Terjadi kesalahan')
        else:
            cancel = wx.MessageDialog(None,"Data Tidak Disimpan", "Data Tidak Disimpan", wx.YES_DEFAULT | wx.ICON_INFORMATION)
            canceldlg = cancel.ShowModal()
    

app = wx.App()
frame = daftar(parent=None)
frame.Show()
app.MainLoop()    