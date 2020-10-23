class FinanzasPersonales:
    def __init__(self):
        pass

    def NewFinance(self):
        nombreFinan = input("Ingresa tu nombre para abrir tu cuenta financiera: ")
        print(f"esta cuenta pertenecera a: ", nombreFinan, "\n")


class Ingresos:
    def __init__(self):
        self.ingresos = []

    def NewIngreso(self):
        newIngreso = int(input("Registra tus ingresos: $"))
        self.ingresos.append(newIngreso)
        self.sumaIngreso = 0
        self.sumaIngreso += newIngreso

    def ReportIngreso(self):
        for x in self.ingresos:
            print(f"$",x,"dolares")

    def sumIngresos(self):
        print(self.sumaIngreso)


class Egresos:
    def __init__(self):
        self.egresos = []

    def NewEgreso(self):
        newEgreso = int(input("Registra tus Egresos: $"))
        self.egresos.append(newEgreso)
        self.sumaEgreso = 0
        self.sumaEgreso += newEgreso

    def ReportEgreso(self):
        for x in self.egresos:
            print(f"$",x,"dolares")

    def sumEgresos(self):
        print(self.sumaEgreso)
