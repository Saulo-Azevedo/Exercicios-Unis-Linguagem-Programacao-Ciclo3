# importamos o frame principal
import frame_principal

#importe da biblioteca wxpython
import wx
import traceback,sys

# Aqui criamos uma classe que é herdada frame principal
class FramePrincipal(frame_principal.MyFrame1):    
    def __init__(self, parent):
        frame_principal.MyFrame1.__init__(self,parent)
    def func_calcular(self, event):

            
        imc = float(self.peso.GetValue()) / (float(self.altura.GetValue())*float(self.altura.GetValue()))     
        
        
        if imc < 17:           
            self.txt_total.SetLabel("Nome: " + self.nome.GetValue() + "\n" + "Endereço Completo: " + self.endereco.GetValue() + "\n"+ "Altura: " + self.altura.GetValue() + "\n" + "Peso: " + self.peso.GetValue() + " kG " + "\n" + 'IMC: {:.2f} - Muito abaixo do peso!'.format(imc)) 
                    
        elif imc >= 17 and imc <= 18.49:
            self.txt_total.SetLabel("Nome: " + self.nome.GetValue() + "\n" + "Endereço Completo: " + self.endereco.GetValue() + "\n"+ "Altura: " + self.altura.GetValue() + "\n" + "Peso: " + self.peso.GetValue() + " kG " + "\n" + 'IMC: {:.2f} - Abaixo do peso!'.format(imc)) # observar

        elif imc >= 18.50 and imc <= 24.99:
            self.txt_total.SetLabel("Nome: " + self.nome.GetValue() + "\n" + "Endereço Completo: " + self.endereco.GetValue() + "\n"+ "Altura: " + self.altura.GetValue() + "\n" + "Peso: " + self.peso.GetValue() + " kG " + "\n" + 'IMC: {:.2f} - Peso normal!'.format(imc)) # observar

        elif imc >= 25 and imc <= 29.99:
            self.txt_total.SetLabel("Nome: " + self.nome.GetValue() + "\n" + "Endereço Completo: " + self.endereco.GetValue() + "\n"+ "Altura: " + self.altura.GetValue() + "\n" + "Peso: " + self.peso.GetValue() + " kG " + "\n" + 'IMC: {:.2f} - Acima do peso!'.format(imc)) # observar            

        elif imc >= 30 and imc <= 34.99:
            self.txt_total.SetLabel("Nome: " + self.nome.GetValue() + "\n" + "Endereço Completo: " + self.endereco.GetValue() + "\n"+ "Altura: " + self.altura.GetValue() + "\n" + "Peso: " + self.peso.GetValue() + " kG " + "\n" + 'IMC: {:.2f} - Obesidade I'.format(imc)) # observar  

        elif imc >= 35 and imc <= 39.99:
            self.txt_total.SetLabel("Nome: " + self.nome.GetValue() + "\n" + "Endereço Completo: " + self.endereco.GetValue() + "\n"+ "Altura: " + self.altura.GetValue() + "\n" + "Peso: " + self.peso.GetValue() + " kG " + "\n" + 'IMC: {:.2f} - Obesidade II'.format(imc)) # observar 

        elif imc > 40:
            self.txt_total.SetLabel("Nome: " + self.nome.GetValue() + "\n" + "Endereço Completo: " + self.endereco.GetValue() + "\n"+ "Altura: " + self.altura.GetValue() + "\n" + "Peso: " + self.peso.GetValue() + " kG " + "\n" + 'IMC: {:.2f} - Obesidade III'.format(imc)) # observar 

                
    
        return super().func_calcular(event)

    
    def func_reiniciar( self, event ):
        self.nome.SetValue("")
        self.endereco.SetValue("")
        self.altura.SetValue("")
        self.peso.SetValue("")
        self.txt_total.SetLabelText("")
        event.Skip()
        
    def func_sair( self, event ):
        self.Close()
        event.Skip()
    def txt_total( self, event ): 
        
        event.Skip()



        
app = wx.App()
frame = FramePrincipal(None)
frame.Show()

app.MainLoop()
