# importamos o frame principal
import frame_principal

#importe da biblioteca wxpython
import wx

# Aqui criamos uma classe que é herdada frame principal
class FramePrincipal(frame_principal.MyFrame1):    
    def __init__(self, parent):
        frame_principal.MyFrame1.__init__(self,parent)
    def func_calcular(self, event):
        
        imc = float(self.peso.GetValue()) / (float(self.altura.GetValue())*float(self.altura.GetValue()))
       
        
        
        if imc < 17:
            print("Nome: " , self.nome.GetValue())
            print("Endereço Completo:" , self.endereco.GetValue())
            print("IMC:",round(imc,2), " - Muito abaixo do peso!")
        elif imc >= 17 and imc <= 18.49:
            print("Nome: " , self.nome.GetValue())
            print("Endereço Completo:" , self.endereco.GetValue())            
            print("IMC:",round(imc,2)," - Abaixo do peso")  
        elif imc >= 18.50 and imc <= 24.99:
            print("Nome: " , self.nome.GetValue())
            print("Endereço Completo:" , self.endereco.GetValue())            
            print("IMC:",round(imc,2)," - Peso normal")
        elif imc >= 25 and imc <= 29.99:
            print("Nome: " , self.nome.GetValue())
            print("Endereço Completo:" , self.endereco.GetValue())            
            print("IMC:",round(imc,2)," - Acima do peso")
        elif imc >= 30 and imc <= 34.99:
            print("Nome: " , self.nome.GetValue())
            print("Endereço Completo:" , self.endereco.GetValue())            
            print("IMC:",round(imc,2)," - Obesidade I")
        elif imc >= 35 and imc <= 39.99:
            print("Nome: " , self.nome.GetValue())
            print("Endereço Completo:" , self.endereco.GetValue())            
            print("IMC:",round(imc,2)," - Obesidade II (severa)")
        elif imc > 40:
            print("Nome: " , self.nome.GetValue())
            print("Endereço Completo:" , self.endereco.GetValue())            
            print("IMC:",round(imc,2)," - Obesidade III (mórbida)")  
                  
       
        return super().func_calcular(event)
    
    def func_reiniciar( self, event ):
        self.nome.SetValue("")
        self.endereco.SetValue("")
        self.altura.SetValue("")
        self.peso.SetValue("")
        event.Skip()
        
    def func_sair( self, event ):
        self.Close()
        event.Skip()
    def txt_total( self, event ): 
        print('teste')
        event.Skip()


  
app = wx.App()
frame = FramePrincipal(None)
frame.Show()
txt_total()
app.MainLoop()