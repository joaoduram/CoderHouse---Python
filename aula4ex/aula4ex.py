from plyer import notification
from datetime import datetime

def alerta(nivel, base, etapa):
    if nivel == 1:
        title = "Alerta Baixo"
    elif nivel == 2:
        title = "Alerta Médio"
    elif nivel == 3:
        title = "Alerta Alto"


    message = f"Falha no carregamento da base {base} na etapa {etapa}\nData: {current_date}"
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    notification.notify(
        title=title,
        message=message,
        app_name="Alerta"
    )


#Exemplos de uso
alerta(1, "CLIENTES", "EXTRACAO")
alerta(2, "CLIENTES", "EXTRACAO")
alerta(3, "CLIENTES", "EXTRACAO")
