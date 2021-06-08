# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class Daftar
###########################################################################

class Daftar ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText191 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Daftar", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText191.Wrap( -1 )

		self.m_staticText191.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer161.Add( self.m_staticText191, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer161 )
		self.m_panel1.Layout()
		bSizer161.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self.m_panel2, wx.ID_ANY, u"DAFTAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panel2, wx.ID_ANY, u"MASUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.input_username = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.input_username, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.input_password = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.input_password, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Nama Bisnis/Toko", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.input_toko = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.input_toko, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( fgSizer2 )
		self.m_panel3.Layout()
		fgSizer2.Fit( self.m_panel3 )
		bSizer1.Add( self.m_panel3, 3, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )

		self.m_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_button3 = wx.Button( self.m_panel21, wx.ID_ANY, u"SIMPAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel21.SetSizer( bSizer18 )
		self.m_panel21.Layout()
		bSizer18.Fit( self.m_panel21 )
		bSizer1.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.daftar_btn )
		self.m_button2.Bind( wx.EVT_BUTTON, self.masuk_btn )
		self.m_button3.Bind( wx.EVT_BUTTON, self.simpan_btn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def daftar_btn( self, event ):
		event.Skip()

	def masuk_btn( self, event ):
		event.Skip()

	def simpan_btn( self, event ):
		event.Skip()


###########################################################################
## Class Masuk
###########################################################################

class Masuk ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText191 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Masuk", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText191.Wrap( -1 )

		self.m_staticText191.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer161.Add( self.m_staticText191, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer161 )
		self.m_panel1.Layout()
		bSizer161.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button1 = wx.Button( self.m_panel2, wx.ID_ANY, u"DAFTAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button1, 0, wx.ALL, 5 )

		self.m_button2 = wx.Button( self.m_panel2, wx.ID_ANY, u"MASUK", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.static_text1 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.static_text1.Wrap( -1 )

		fgSizer2.Add( self.static_text1, 0, wx.ALL, 5 )

		self.input_username = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.input_username, 0, wx.ALL, 5 )

		self.wx_statictext_2 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.wx_statictext_2.Wrap( -1 )

		fgSizer2.Add( self.wx_statictext_2, 0, wx.ALL, 5 )

		self.input_password = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.input_password, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( fgSizer2 )
		self.m_panel3.Layout()
		fgSizer2.Fit( self.m_panel3 )
		bSizer1.Add( self.m_panel3, 3, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )

		self.m_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_button23 = wx.Button( self.m_panel21, wx.ID_ANY, u"LOGIN", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel21.SetSizer( bSizer18 )
		self.m_panel21.Layout()
		bSizer18.Fit( self.m_panel21 )
		bSizer1.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.daftar_btn )
		self.m_button23.Bind( wx.EVT_BUTTON, self.login_btn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def daftar_btn( self, event ):
		event.Skip()

	def login_btn( self, event ):
		event.Skip()


###########################################################################
## Class Dashboard
###########################################################################

class Dashboard ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 677,383 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_notebook1 = wx.Notebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_panel33 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.tabelTansaksi = wx.grid.Grid( self.m_panel33, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabelTansaksi.CreateGrid( 0, 5 )
		self.tabelTansaksi.EnableEditing( True )
		self.tabelTansaksi.EnableGridLines( True )
		self.tabelTansaksi.EnableDragGridSize( False )
		self.tabelTansaksi.SetMargins( 0, 0 )

		# Columns
		self.tabelTansaksi.SetColSize( 0, 100 )
		self.tabelTansaksi.SetColSize( 1, 150 )
		self.tabelTansaksi.SetColSize( 2, 100 )
		self.tabelTansaksi.SetColSize( 3, 100 )
		self.tabelTansaksi.SetColSize( 4, 100 )
		self.tabelTansaksi.EnableDragColMove( False )
		self.tabelTansaksi.EnableDragColSize( True )
		self.tabelTansaksi.SetColLabelSize( 30 )
		self.tabelTansaksi.SetColLabelValue( 0, u"ID Transaksi" )
		self.tabelTansaksi.SetColLabelValue( 1, u"Tanggal Transaksi" )
		self.tabelTansaksi.SetColLabelValue( 2, u"ID Barang" )
		self.tabelTansaksi.SetColLabelValue( 3, u"Jumlah" )
		self.tabelTansaksi.SetColLabelValue( 4, u"Total" )
		self.tabelTansaksi.SetColLabelValue( 5, u"Edit" )
		self.tabelTansaksi.SetColLabelValue( 6, u"Hapus" )
		self.tabelTansaksi.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelTansaksi.EnableDragRowSize( True )
		self.tabelTansaksi.SetRowLabelSize( 80 )
		self.tabelTansaksi.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelTansaksi.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer33.Add( self.tabelTansaksi, 1, wx.ALL, 5 )

		self.m_button29 = wx.Button( self.m_panel33, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer33.Add( self.m_button29, 0, wx.ALL, 5 )


		self.m_panel33.SetSizer( bSizer33 )
		self.m_panel33.Layout()
		bSizer33.Fit( self.m_panel33 )
		self.m_notebook1.AddPage( self.m_panel33, u"Transaksi", True )
		self.m_panel34 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer281 = wx.BoxSizer( wx.VERTICAL )

		self.tabelBarang = wx.grid.Grid( self.m_panel34, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.tabelBarang.CreateGrid( 0, 8 )
		self.tabelBarang.EnableEditing( True )
		self.tabelBarang.EnableGridLines( True )
		self.tabelBarang.EnableDragGridSize( False )
		self.tabelBarang.SetMargins( 0, 0 )

		# Columns
		self.tabelBarang.SetColSize( 0, 100 )
		self.tabelBarang.SetColSize( 1, 150 )
		self.tabelBarang.SetColSize( 2, 100 )
		self.tabelBarang.SetColSize( 3, 100 )
		self.tabelBarang.EnableDragColMove( False )
		self.tabelBarang.EnableDragColSize( True )
		self.tabelBarang.SetColLabelSize( 30 )
		self.tabelBarang.SetColLabelValue( 0, u"ID" )
		self.tabelBarang.SetColLabelValue( 1, u"Nama" )
		self.tabelBarang.SetColLabelValue( 2, u"Jumlah" )
		self.tabelBarang.SetColLabelValue( 3, u"Harga" )
		self.tabelBarang.SetColLabelValue( 4, u"Jenis" )
		self.tabelBarang.SetColLabelValue( 5, u"Berat" )
		self.tabelBarang.SetColLabelValue( 6, u"Edit" )
		self.tabelBarang.SetColLabelValue( 7, u"Hapus" )
		self.tabelBarang.SetColLabelValue( 8, wx.EmptyString )
		self.tabelBarang.SetColLabelValue( 9, wx.EmptyString )
		self.tabelBarang.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.tabelBarang.EnableDragRowSize( True )
		self.tabelBarang.SetRowLabelSize( 80 )
		self.tabelBarang.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.tabelBarang.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer281.Add( self.tabelBarang, 1, wx.ALL, 5 )

		self.m_button201 = wx.Button( self.m_panel34, wx.ID_ANY, u"Tambah", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer281.Add( self.m_button201, 0, wx.ALL, 5 )

		self.m_staticText30 = wx.StaticText( self.m_panel34, wx.ID_ANY, u"Peringatan : Jumlah minimum stok barang adalah 5 !", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText30.Wrap( -1 )

		bSizer281.Add( self.m_staticText30, 0, wx.ALL, 5 )


		self.m_panel34.SetSizer( bSizer281 )
		self.m_panel34.Layout()
		bSizer281.Fit( self.m_panel34 )
		self.m_notebook1.AddPage( self.m_panel34, u"Data Barang", False )
		self.m_panel35 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.m_panel35, u"Grafik Transaksi", False )
		self.m_panel30 = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_notebook1.AddPage( self.m_panel30, u"Grafik Stok", False )
		self.Akun = wx.Panel( self.m_notebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.Akun.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self.Akun, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText191 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Akun Profil", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText191.Wrap( -1 )

		self.m_staticText191.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer161.Add( self.m_staticText191, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer161 )
		self.m_panel1.Layout()
		bSizer161.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel2 = wx.Panel( self.Akun, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer2 = wx.BoxSizer( wx.HORIZONTAL )


		bSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.m_button2 = wx.Button( self.m_panel2, wx.ID_ANY, u"KELUAR", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer2.Add( self.m_button2, 0, wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel3 = wx.Panel( self.Akun, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.input_username = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.input_username, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.input_password = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.input_password, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Nama Bisnis/Toko", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.input_toko = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.input_toko, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( fgSizer2 )
		self.m_panel3.Layout()
		fgSizer2.Fit( self.m_panel3 )
		bSizer1.Add( self.m_panel3, 3, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )

		self.m_panel21 = wx.Panel( self.Akun, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_button3 = wx.Button( self.m_panel21, wx.ID_ANY, u"EDIT", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel21.SetSizer( bSizer18 )
		self.m_panel21.Layout()
		bSizer18.Fit( self.m_panel21 )
		bSizer1.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel22 = wx.Panel( self.Akun, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 0 )


		self.Akun.SetSizer( bSizer1 )
		self.Akun.Layout()
		bSizer1.Fit( self.Akun )
		self.m_notebook1.AddPage( self.Akun, u"Akun", False )

		bSizer20.Add( self.m_notebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer20 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button29.Bind( wx.EVT_BUTTON, self.tambahTransaksi )
		self.m_button201.Bind( wx.EVT_BUTTON, self.tambahBarang )
		self.m_button2.Bind( wx.EVT_BUTTON, self.masuk_btn )
		self.m_button3.Bind( wx.EVT_BUTTON, self.simpan_btn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def tambahTransaksi( self, event ):
		event.Skip()

	def tambahBarang( self, event ):
		event.Skip()

	def masuk_btn( self, event ):
		event.Skip()

	def simpan_btn( self, event ):
		event.Skip()


###########################################################################
## Class Tambah_Transaksi
###########################################################################

class Tambah_Transaksi ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText191 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Tambah Data Transaksi", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText191.Wrap( -1 )

		self.m_staticText191.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer161.Add( self.m_staticText191, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer161 )
		self.m_panel1.Layout()
		bSizer161.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"ID Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.inp_id_transaksi = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inp_id_transaksi, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Tanggal Transaksi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.inp_tgl_transaksi = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inp_tgl_transaksi, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"ID Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.inp_id_barang = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inp_id_barang, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Jumlah Pembelian", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		fgSizer2.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.inp_jml_pembelian = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inp_jml_pembelian, 0, wx.ALL, 5 )

		self.m_staticText16 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Total Pembayaran", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText16.Wrap( -1 )

		fgSizer2.Add( self.m_staticText16, 0, wx.ALL, 5 )

		self.inp_total = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inp_total, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( fgSizer2 )
		self.m_panel3.Layout()
		fgSizer2.Fit( self.m_panel3 )
		bSizer1.Add( self.m_panel3, 3, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )

		self.m_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_button23 = wx.Button( self.m_panel21, wx.ID_ANY, u"SIMPAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel21.SetSizer( bSizer18 )
		self.m_panel21.Layout()
		bSizer18.Fit( self.m_panel21 )
		bSizer1.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button23.Bind( wx.EVT_BUTTON, self.simpan_btn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def simpan_btn( self, event ):
		event.Skip()


###########################################################################
## Class Tambah_Barang
###########################################################################

class Tambah_Barang ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer161 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText191 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Tambah Data Barang", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText191.Wrap( -1 )

		self.m_staticText191.SetFont( wx.Font( 14, wx.FONTFAMILY_SWISS, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, "Arial" ) )

		bSizer161.Add( self.m_staticText191, 0, wx.ALL, 5 )


		self.m_panel1.SetSizer( bSizer161 )
		self.m_panel1.Layout()
		bSizer161.Fit( self.m_panel1 )
		bSizer1.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel2 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel2.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer1.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel3 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText7 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"ID Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText7.Wrap( -1 )

		fgSizer2.Add( self.m_staticText7, 0, wx.ALL, 5 )

		self.inp_id_barang = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inp_id_barang, 0, wx.ALL, 5 )

		self.m_staticText8 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Nama Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText8.Wrap( -1 )

		fgSizer2.Add( self.m_staticText8, 0, wx.ALL, 5 )

		self.inp_nama_barang = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inp_nama_barang, 0, wx.ALL, 5 )

		self.m_staticText9 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Jumlah Stok", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText9.Wrap( -1 )

		fgSizer2.Add( self.m_staticText9, 0, wx.ALL, 5 )

		self.inp_jml_stok = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inp_jml_stok, 0, wx.ALL, 5 )

		self.m_staticText15 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Harga Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText15.Wrap( -1 )

		fgSizer2.Add( self.m_staticText15, 0, wx.ALL, 5 )

		self.inp_harga_barang = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inp_harga_barang, 0, wx.ALL, 5 )

		self.m_staticText24 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Jenis Barang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText24.Wrap( -1 )

		fgSizer2.Add( self.m_staticText24, 0, wx.ALL, 5 )

		self.inp_jenis_barang = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inp_jenis_barang, 0, wx.ALL, 5 )

		self.m_staticText25 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Berat Bersih", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText25.Wrap( -1 )

		fgSizer2.Add( self.m_staticText25, 0, wx.ALL, 5 )

		self.inp_berat = wx.TextCtrl( self.m_panel3, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.inp_berat, 0, wx.ALL, 5 )


		self.m_panel3.SetSizer( fgSizer2 )
		self.m_panel3.Layout()
		fgSizer2.Fit( self.m_panel3 )
		bSizer1.Add( self.m_panel3, 3, wx.ALIGN_CENTER_HORIZONTAL|wx.ALL, 0 )

		self.m_panel21 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel21.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_MENU ) )

		bSizer18 = wx.BoxSizer( wx.VERTICAL )

		self.m_button23 = wx.Button( self.m_panel21, wx.ID_ANY, u"SIMPAN", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer18.Add( self.m_button23, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel21.SetSizer( bSizer18 )
		self.m_panel21.Layout()
		bSizer18.Fit( self.m_panel21 )
		bSizer1.Add( self.m_panel21, 1, wx.EXPAND |wx.ALL, 0 )

		self.m_panel22 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer1.Add( self.m_panel22, 1, wx.EXPAND |wx.ALL, 0 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.m_button23.Bind( wx.EVT_BUTTON, self.simpan_btn )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def simpan_btn( self, event ):
		event.Skip()


