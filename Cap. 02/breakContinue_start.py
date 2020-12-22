#
# Exemplo de como usar os comando Break e Continue
# Break interrompe a execução do Loop
# Continue interrompe UMA execução e passa para o próximo item
def loopBreak():
  for x in range(5,10):
    if(x == 7):
      break
    print("O valor de X é: ", x)

#loopBreak()

def loopContinue():
  for x in range(5,10):
    if(x == 7):
      continue
    print("O valor de X é: ", x)

loopContinue()