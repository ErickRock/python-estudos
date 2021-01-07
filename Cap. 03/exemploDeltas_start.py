#
# Arquivo de exemplo para uso da classe timedeltas
#

from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta

def QuantosDiasFaltam(ano, mes, dia):
  hoje = date.today()
  dataProcurada = date(ano, mes, dia)

  qntsDias = dataProcurada - hoje

  msgRetorno = "Faltam " + str(qntsDias).replace("days, 0:00:00", "") + " dias para a data " + dataProcurada.strftime("%d/%m/%y")

  print(msgRetorno)

QuantosDiasFaltam(2022, 1, 6)