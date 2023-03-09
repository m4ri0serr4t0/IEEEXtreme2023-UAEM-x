class Menu:

    def __init__(self):
        self.opciones = []

    def addOpcion(self,op):
        self.opciones.append(op)

    def pintaMenu(self):
        i=1
        for op in self.opciones:
            print("{}) {}".format(i,op))
            i = i + 1

    def leeOpcion(self):
        sigue = True
        talla = len(self.opciones)
        while sigue:
            try:
                op = int(input("Selcciona una opcion: "))

                if op > 0 and op <= talla:
                    sigue = False
                else:
                    print("Debe ser un numero entre 1 y "+ str(talla))
            except Exception as e:
                print("Debes seleccionar un numero "+repr(e))
        return op

