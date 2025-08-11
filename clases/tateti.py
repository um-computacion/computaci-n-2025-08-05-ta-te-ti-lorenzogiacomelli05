from clases.tablero import Tablero
import clases.tablero as tablero

class Tateti:
    def __init__(self): 
        self.turno = "X"
        self.tablero = Tablero()

    def ocupar_una_de_las_casillas(self, fil, col):
        self.tablero.poner_la_ficha(fil, col, self.turno)
        if self.hay_ganador():
            self.tablero.mostrar()
            print(f"Jugador {self.turno} gano")
            return "GANADOR"

        if self.hay_empate():
            self.tablero.mostrar()
            print("Empate")
            return "EMPATE"
    
        if self.turno == "X":
            self.turno = "0"
        else:
            self.turno = "X"

    def hay_ganador(self):
        casillas= self.tablero.contenedor
        for fila in casillas:
            if fila[0] != "" and fila[0] == fila[1] == fila[2]:
                return True

        for col in range(3):
            if casillas[0][col] != "" and casillas[0][col] == casillas[1][col] == casillas[2][col]:
                return True

        if casillas[0][0] != "" and casillas[0][0] == casillas[1][1] == casillas[2][2]:
            return True
        if casillas[0][2] != "" and casillas[0][2] == casillas[1][1] == casillas[2][0]:
            return True

        return False

    def hay_empate(self):
        for fila in self.tablero.contenedor:
            if "" in fila:
                return False
        return True