# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Calculo do IMC - Indice de Massa Corporal", pos = wx.DefaultPosition, size = wx.Size( 650,340 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.Size( 650,340 ), wx.Size( 650,340 ) )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		bSizer2.SetMinSize( wx.Size( 800,600 ) )
		self.m_panel1 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel1.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		gSizer1 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText2 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Nome do paciente:", wx.DefaultPosition, wx.Size( 150,20 ), 0 )
		self.m_staticText2.Wrap( -1 )

		self.m_staticText2.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer1.Add( self.m_staticText2, 0, wx.ALIGN_CENTER_VERTICAL|wx.LEFT, 5 )

		self.nome = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 459,25 ), 0 )
		self.nome.SetMinSize( wx.Size( 459,25 ) )
		self.nome.SetMaxSize( wx.Size( 459,25 ) )

		gSizer1.Add( self.nome, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer3.Add( gSizer1, 0, wx.EXPAND, 5 )

		gSizer11 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText21 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Endereço Completo:", wx.DefaultPosition, wx.Size( 150,20 ), 0 )
		self.m_staticText21.Wrap( -1 )

		self.m_staticText21.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer11.Add( self.m_staticText21, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.endereco = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 459,25 ), 0 )
		self.endereco.SetMinSize( wx.Size( 459,25 ) )
		self.endereco.SetMaxSize( wx.Size( 459,25 ) )

		gSizer11.Add( self.endereco, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer3.Add( gSizer11, 0, wx.EXPAND, 5 )

		bSizer5 = wx.BoxSizer( wx.VERTICAL )

		gSizer6 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText3 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Altura (cm)", wx.DefaultPosition, wx.Size( 80,25 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText3.Wrap( -1 )

		self.m_staticText3.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer4.Add( self.m_staticText3, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.altura = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,25 ), 0 )
		self.altura.SetMinSize( wx.Size( 145,25 ) )
		self.altura.SetMaxSize( wx.Size( 145,25 ) )

		gSizer4.Add( self.altura, 0, wx.ALL, 5 )

		self.m_staticText4 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"Peso (kg)", wx.DefaultPosition, wx.Size( 80,25 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 12, wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer4.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.peso = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 145,25 ), 0 )
		self.peso.SetMinSize( wx.Size( 145,25 ) )
		self.peso.SetMaxSize( wx.Size( 145,25 ) )

		gSizer4.Add( self.peso, 0, wx.ALL, 5 )


		bSizer6.Add( gSizer4, 0, wx.EXPAND, 5 )


		gSizer6.Add( bSizer6, 1, wx.EXPAND, 5 )

		self.total = wx.TextCtrl( self.m_panel1, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 300,150 ), 0 )
		self.total.SetMinSize( wx.Size( 300,150 ) )
		self.total.SetMaxSize( wx.Size( 300,150 ) )

		gSizer6.Add( self.total, 0, wx.ALL|wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		bSizer5.Add( gSizer6, 0, wx.EXPAND, 5 )


		bSizer3.Add( bSizer5, 0, wx.EXPAND, 5 )

		gSizer5 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer61 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer51 = wx.BoxSizer( wx.VERTICAL )

		self.btn_calcular = wx.Button( self.m_panel1, wx.ID_ANY, u"Calcular", wx.DefaultPosition, wx.Size( 130,50 ), 0 )
		self.btn_calcular.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_SCRIPT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btn_calcular.SetMinSize( wx.Size( 130,50 ) )
		self.btn_calcular.SetMaxSize( wx.Size( 130,50 ) )

		bSizer51.Add( self.btn_calcular, 0, wx.ALL, 5 )


		gSizer61.Add( bSizer51, 0, wx.ALIGN_RIGHT, 5 )

		bSizer61 = wx.BoxSizer( wx.VERTICAL )

		self.btn_reiniciar = wx.Button( self.m_panel1, wx.ID_ANY, u"Reiniciar", wx.DefaultPosition, wx.Size( 130,50 ), 0 )
		self.btn_reiniciar.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )
		self.btn_reiniciar.SetMinSize( wx.Size( 130,50 ) )
		self.btn_reiniciar.SetMaxSize( wx.Size( 130,50 ) )

		bSizer61.Add( self.btn_reiniciar, 0, wx.ALL, 5 )


		gSizer61.Add( bSizer61, 1, wx.EXPAND, 5 )


		gSizer5.Add( gSizer61, 1, wx.ALIGN_RIGHT, 5 )

		gSizer7 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer8 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer7.Add( gSizer8, 1, wx.EXPAND, 5 )

		self.btn_sair = wx.Button( self.m_panel1, wx.ID_ANY, u"Sair", wx.DefaultPosition, wx.Size( 130,50 ), 0 )
		self.btn_sair.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		gSizer7.Add( self.btn_sair, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		gSizer5.Add( gSizer7, 1, wx.EXPAND, 5 )


		bSizer3.Add( gSizer5, 0, wx.EXPAND, 5 )


		self.m_panel1.SetSizer( bSizer3 )
		self.m_panel1.Layout()
		bSizer3.Fit( self.m_panel1 )
		bSizer2.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.total.Bind( wx.EVT_TEXT, self.txt_total )
		self.btn_calcular.Bind( wx.EVT_BUTTON, self.func_calcular )
		self.btn_reiniciar.Bind( wx.EVT_BUTTON, self.func_reiniciar )
		self.btn_sair.Bind( wx.EVT_BUTTON, self.func_sair )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def txt_total( self, event ):
		event.Skip()

	def func_calcular( self, event ):
		event.Skip()

	def func_reiniciar( self, event ):
		event.Skip()

	def func_sair( self, event ):
		event.Skip()


