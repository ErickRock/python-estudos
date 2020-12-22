#
# Exemplo de como criar classes
#
# __init__ é um construtor e todos os métodos recebem self como paramêtro, 
# mas não precisa ser usando

class minhaClasse():
  def __init__(self):
      self.meuAtributo = "Passou pelo meu construtor!"

  def meuMetodo(self):
      print("Passou pelo meu método")

  def meuMetodo2(self, valor):
      self.outroAtributo = valor
      print(self.outroAtributo)

def criarObjeto():
  meuObj = minhaClasse()
  var1 = meuObj.meuAtributo
  print(var1)
  
  meuObj.meuMetodo()
  meuObj.meuMetodo2("Executando um método")

criarObjeto()