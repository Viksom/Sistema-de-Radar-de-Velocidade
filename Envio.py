import smtplib
import email.message
from Radar_de_Velocidade.Teste.Senha import senha
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-


def enviar_email(nome, placa, velocidade, multa, destino):
    corpo_email = f"""
    <p>Caríssimo {nome}</p>
    <p>O seu veículo de placa {placa}</p>
    <p>Foi apanhado pelo nosso radar na Avenida Deolinda Rodrigues excedendo a velocidade recomendada (60 km/h) naquela via ({velocidade} km/h)</p>
    <p>O que resulta numa multa de {multa} kzs</p>
    <p>Aconselhamos que se dirija a area mais próxima para saldar a multa!</p>
    <p>Assinado</p>
    <p>DNVT</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Você foi MULTADO"
    msg['From'] = 'josealbertovicksom@gmail.com'
    msg['To'] = destino
    password = senha
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    # Login Credentials for sending the mail
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado')
# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
