from datetime import datetime, timedelta

from rental.models import Rental

class Atraso:
    def __init__(self, rental: Rental) -> None:
        self.rental = rental

    @property
    def dias_atraso(self):
        agora = (datetime.now() - timedelta(hours=3)).date()
        previsao = (self.rental.return_period - timedelta(hours=3)).date()
        
        return (agora - previsao).days
    
    @property
    def multa(self):
        calculo = self.dias_atraso * 1.5 + 3.5

        return "R$ {:.2f}".format(calculo)