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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Calculo do IMC - Indice de Massa Corporal", pos = wx.DefaultPosition, size = wx.Size( 593,452 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )
		self.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel5 = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel5.SetFont( wx.Font( wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )
		self.m_panel5.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		gSizer4 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText4 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Nome do Paciente:", wx.DefaultPosition, wx.Size( 120,20 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText4.Wrap( -1 )

		self.m_staticText4.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer4.Add( self.m_staticText4, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl19 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,25 ), 0 )
		gSizer4.Add( self.m_textCtrl19, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer6.Add( gSizer4, 0, wx.EXPAND, 5 )

		gSizer41 = wx.GridSizer( 0, 2, 0, 0 )

		self.m_staticText41 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Endereço Completo:", wx.DefaultPosition, wx.Size( 120,20 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText41.Wrap( -1 )

		self.m_staticText41.SetFont( wx.Font( 11, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer41.Add( self.m_staticText41, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl191 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 450,25 ), 0 )
		gSizer41.Add( self.m_textCtrl191, 0, wx.ALL|wx.ALIGN_RIGHT, 5 )


		bSizer6.Add( gSizer41, 0, wx.EXPAND, 5 )

		bSizer9 = wx.BoxSizer( wx.VERTICAL )

		gSizer10 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer10 = wx.BoxSizer( wx.VERTICAL )

		gSizer42 = wx.GridSizer( 0, 2, 1, 1 )

		self.m_staticText42 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Altura (cm)", wx.DefaultPosition, wx.Size( 80,25 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText42.Wrap( -1 )

		self.m_staticText42.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer42.Add( self.m_staticText42, 1, wx.ALL|wx.LEFT, 5 )

		self.m_textCtrl192 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 155,25 ), 0 )
		gSizer42.Add( self.m_textCtrl192, 0, wx.ALL|wx.BOTTOM|wx.LEFT|wx.RESERVE_SPACE_EVEN_IF_HIDDEN|wx.RIGHT|wx.ALIGN_RIGHT, 5 )

		self.m_staticText421 = wx.StaticText( self.m_panel5, wx.ID_ANY, u"Peso (kg)", wx.DefaultPosition, wx.Size( 80,25 ), wx.ALIGN_CENTER_HORIZONTAL )
		self.m_staticText421.Wrap( -1 )

		self.m_staticText421.SetFont( wx.Font( 12, wx.FONTFAMILY_ROMAN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, False, wx.EmptyString ) )

		gSizer42.Add( self.m_staticText421, 0, wx.ALL, 5 )

		self.m_textCtrl1921 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 155,25 ), 0 )
		gSizer42.Add( self.m_textCtrl1921, 0, wx.ALL|wx.RIGHT|wx.ALIGN_RIGHT, 5 )


		bSizer10.Add( gSizer42, 0, 0, 1 )


		gSizer10.Add( bSizer10, 1, wx.EXPAND|wx.ALIGN_RIGHT, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self.m_panel5, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_textCtrl18.SetMinSize( wx.Size( 100,150 ) )

		gSizer10.Add( self.m_textCtrl18, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.EXPAND, 5 )


		bSizer9.Add( gSizer10, 0, wx.EXPAND, 5 )


		bSizer6.Add( bSizer9, 0, wx.EXPAND, 5 )

		gSizer14 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer16 = wx.GridSizer( 0, 2, 0, 0 )

		bSizer161 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer161.SetMinSize( wx.Size( 100,25 ) )
		self.m_button21 = wx.Button( self.m_panel5, wx.ID_ANY, u"Calcular", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer161.Add( self.m_button21, 1, wx.ALIGN_CENTER_VERTICAL|wx.RIGHT, 5 )


		gSizer16.Add( bSizer161, 0, wx.ALIGN_RIGHT, 5 )

		bSizer30 = wx.BoxSizer( wx.VERTICAL )

		self.m_button27 = wx.Button( self.m_panel5, wx.ID_ANY, u"Reiniciar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer30.Add( self.m_button27, 0, wx.EXPAND|wx.ALIGN_RIGHT, 5 )


		gSizer16.Add( bSizer30, 0, wx.EXPAND, 5 )


		gSizer14.Add( gSizer16, 1, wx.ALIGN_RIGHT, 5 )

		gSizer17 = wx.GridSizer( 0, 2, 0, 0 )

		gSizer19 = wx.GridSizer( 0, 2, 0, 0 )


		gSizer17.Add( gSizer19, 1, wx.EXPAND, 5 )

		self.m_button24 = wx.Button( self.m_panel5, wx.ID_ANY, u"Sair", wx.DefaultPosition, wx.DefaultSize, 0 )

		self.m_button24.SetBitmapMargins( wx.Size( 100,25 ) )
		gSizer17.Add( self.m_button24, 0, wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL|wx.RIGHT, 5 )


		gSizer14.Add( gSizer17, 1, wx.EXPAND, 5 )


		bSizer6.Add( gSizer14, 0, wx.EXPAND, 5 )


		self.m_panel5.SetSizer( bSizer6 )
		self.m_panel5.Layout()
		bSizer6.Fit( self.m_panel5 )
		bSizer1.Add( self.m_panel5, 1, wx.EXPAND, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


