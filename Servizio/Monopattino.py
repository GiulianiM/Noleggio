from Servizio.Mezzo import Mezzo


class Monopattino(Mezzo):

    def __init__(self):
        super(Monopattino, self).__init__()
        self.costo_minuto = 0.20