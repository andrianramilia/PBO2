import GUI
import wx
import wx.grid
import toko

class Daftar (GUI.Daftar):
    def __init__(self, parent):
        GUI.Daftar.__init__(self,parent)



    def simpan_btn( self, event ):
        self.akun = toko.akun()
        listAkun = self.akun.getDataAkun()

        username = self.input_username.GetValue()
        password = self.input_password.GetValue()
        namaakun = self.input_toko.GetValue()

        tempakun = []
        
        msgdlg = wx.MessageDialog(None,"Apakah Anda Yakin?", "konfirmasi", wx.YES_NO | wx.ICON_EXCLAMATION)
        kodedlg = msgdlg.ShowModal()
        if kodedlg == wx.ID_YES:
            tempakun.append(username)
            tempakun.append(password)
            tempakun.append(namaakun)
            print(listAkun)

        else:
            cancel = wx.MessageDialog(None,"Data Tidak Disimpan", "Data Tidak Disimpan", wx.YES_DEFAULT | wx.ICON_INFORMATION)
            canceldlg = cancel.ShowModal()
    
    def masuk_btn( self, event ):
        framemasuk.Show()
        framedaftar.Hide()

class Masuk (GUI.Masuk):
    def __init__(self, parent):
        GUI.Masuk.__init__(self,parent)
        self.akun = toko.akun()


    def login_btn( self, event ):
        uname = self.input_username.GetValue()
        password = self.input_password.GetValue()
        if uname == 'andrian' and password == 'Andrian123':
            framedashboard.Show()
            framemasuk.Hide()
        
        else:
            wrong = wx.MessageDialog(None,"Uername / Password Anda Salah", "Login Gagal", wx.YES_DEFAULT | wx.ICON_INFORMATION)
            wrongdlg = wrong.ShowModal()

    def daftar_btn( self, event ):
        framedaftar.Show()
        framemasuk.Hide()  

class Dashboard(GUI.Dashboard):
    def __init__(self, parent):
        GUI.Dashboard.__init__(self,parent)
        self.showTransaksi()
        self.showBarang()
    
    def showTransaksi(self):
        n_cols = self.Transaksi.GetNumberCols()
        n_rows = self.Transaksi.GetNumberRows()
        if n_cols > 0:
            self.Transaksi.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.Transaksi.DeleteRows(0, n_rows, True)

        colums = ['ID Transaksi', 'Tanggal', 'ID Barang', 'Jumlah Beli', 'Total Bayar']
        self.Transaksi.AppendCols(len(colums))

        self.transaksi = toko.transaksi()
        listtransaksi = self.transaksi.getDataTransaksi()
        row = 0

        self.lstTransaksi = []
        for col in range(len(colums)):
            self.Transaksi.SetColLabelValue(
                col, colums[col]) 
        for transaksi_row in listtransaksi:
            self.Transaksi.AppendRows(1)

            print(row, '. ', transaksi_row)
            id_transaksi, tanggal_transaksi, id_barang, jumlah_pembelian, total_pembayaran = transaksi_row
            jumlahbeli = str(jumlah_pembelian)
            jumlahbayar = str(total_pembayaran)
            self.Transaksi.SetCellValue(row, 0, id_transaksi)
            self.Transaksi.SetCellValue(row, 1, tanggal_transaksi)
            self.Transaksi.SetCellValue(row, 2, id_barang)
            self.Transaksi.SetCellValue(row, 3, jumlahbeli)
            self.Transaksi.SetCellValue(row, 4, jumlahbayar)
            self.lstTransaksi.append(id_transaksi)
            row += 1

    def showBarang(self):
        n_cols = self.Barang.GetNumberCols()
        n_rows = self.Barang.GetNumberRows()
        if n_cols > 0:
            self.Barang.DeleteCols(0, n_cols, True)
        if n_rows > 0:
            self.Barang.DeleteRows(0, n_rows, True)

        colums = ['ID Barang', 'Nama Barang', 'Jumlah Stok', 'Harga']
        self.Barang.AppendCols(len(colums))

        self.barang = toko.barang()
        listbarang = self.barang.getDataBarang()
        row = 0

        self.lstBarang = []
        for col in range(len(colums)):
            self.Barang.SetColLabelValue(
                col, colums[col]) 
        for barang_row in listbarang:
            self.Barang.AppendRows(1)

            print(row, '. ', barang_row)
            id_barang, nama_barang, jumlah_stok, harga = barang_row
            jumlahstk = str(jumlah_stok)
            hrg = str(harga)
            self.Barang.SetCellValue(row, 0, id_barang)
            self.Barang.SetCellValue(row, 1, nama_barang)
            self.Barang.SetCellValue(row, 2, jumlahstk)
            self.Barang.SetCellValue(row, 3, hrg)
            self.lstBarang.append(id_barang)
            row += 1

app = wx.App()
framedaftar = Daftar(parent=None)
framedaftar.Show()
framemasuk = Masuk(parent=None)
framedashboard = Dashboard(parent=None)

app.MainLoop()