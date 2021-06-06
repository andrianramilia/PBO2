import mysql.connector
import sqlite3

class data:
    def __init__(self):
        self.con = sqlite3.connect("db_toko")
        self.cursor = self.con.cursor()

    def executeQuery(self, query, retVal = False):
        self.cursor.execute(query)
        all_result = self.cursor.fetchall()
        self.con.commit()
        if retVal:
            return all_result

class transaksi(data):

    def UpdateDataTransaksi(self, id_transaksi, tanggal , id_barang, jumlah_pembelian, total_pembayaran):
        self.query = "UPDATE transaksi SET id_transaksi= ?, tanggal = ?, id_barang = ?, jumlah_pembelian = ?, total_pembayaran = ? where id = id_transaksi"
        self.query = self.query % (id_transaksi, tanggal , id_barang, jumlah_pembelian, total_pembayaran)
        print('self.query : ', self.query)
        self.executeQuery(self.query)

    def getDataTransaksi(self):
        self.query = "SELECT id_transaksi, tanggal , id_barang, jumlah_pembelian, total_pembayaran FROM transaksi ORDER BY id_transaksi"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result

class stok(data):
    
    def UpdateDataStok(self, id_barang, nama_barang, jumlah_stok, harga):
        self.query = "UPDATE barang SET id_barang= ?, nama_barang = ?, jumlah_stok = ?, harga = ?, where id = id_barang"
        self.query = self.query % (id_barang, nama_barang , jumlah_stok, harga)
        self.executeQuery(self.query)

    def getDataBarang(self):
        self.query = "SELECT id_barang, nama_barang, jumlah_stok, harga"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result

class akun(data):
    def UpdateDataAkun(self, username, password, nama_toko):
        self.query = "UPDATE akun SET username= ?, password = ?, nama_toko = ? where id = username"
        self.query = self.query % (username, password, nama_toko)
        self.executeQuery(self.query)

    def getDataBarang(self):
        self.query = "SELECT  username, password, nama_toko"
        print('self.query : ', self.query)
        result = self.executeQuery(self.query, True)
        return result
