from Finanzas import FinanzasPersonales, Ingresos, Egresos

FinanzasAppObj = FinanzasPersonales()
IngresosObj = Ingresos()
EgresosObj = Egresos()


def NewFinance():
    FinanzasAppObj.NewFinance()


def Ingreso():
    IngresosObj.NewIngreso()


def Egreso():
    EgresosObj.NewEgreso()


def ReportIngreso():
    IngresosObj.ReportIngreso()


def ReportEgreso():
    EgresosObj.ReportEgreso()


def ReportTrans():
    print("Tus ingresos realizados son:")
    IngresosObj.ReportIngreso()
    print("\n")
    print("Tus egresos realizados son:")
    EgresosObj.ReportEgreso()
    print("\n")


def VerSaldo():
    EgresosObj.sumEgresos()
    IngresosObj.sumIngresos()
    TotalCuenta = IngresosObj.sumIngresos() - EgresosObj.sumEgresos()
    print(f"Tu saldo total en la cuenta es: ", TotalCuenta)


print("Bienvenido a la App Finanzas personales \n")
while True:
    print("Menu de opciones: \n")
    print("(0) Salir")
    print("(1) Inicializar un proyecto de finanzas")
    print("(2) Registrar un ingreso")
    print("(3) Registrar un egreso")
    print("(4) Generar reporte de los ingresos")
    print("(5) Generar reporte de los egresos")
    print("(6) Generar reporte de las transacciones")
    print("(7) Ver saldo disponible en la cuenta \n")
    opcion = int(input("Ingresa tu opcion: "))

    if opcion == 0:
        print("Gracias por usar la App Finanzas \n")
        break

    elif opcion == 1:
        NewFinance()

    elif opcion == 2:
        Ingreso()

    elif opcion == 3:
        Egreso()

    elif opcion == 4:
        print("Los ingresos realizados son:")
        ReportIngreso()
        print("\n")

    elif opcion == 5:
        print("Los egresos realizados son:")
        ReportEgreso()
        print("\n")

    elif opcion == 6:
        ReportTrans()

    elif opcion == 7:
        VerSaldo()