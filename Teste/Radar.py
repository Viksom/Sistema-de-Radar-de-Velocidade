import mysql.connector
from datetime import *
from Radar_de_Velocidade.Envio import enviar_email
import cv2
import serial
import Le_Foto

# -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
cont = 0
while True:
    try:
        porta = f'COM{cont}'
        bound = 115200
        ser = serial.Serial(porta, bound)
        print(f'Estamos utilizando a porta {cont}')
        print()
        video = cv2.VideoCapture(1)

        gui = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='base_de_dados1'
        )

        cursor = gui.cursor()

        # Lista de cores
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        normal = '\033[m'
        vermelho = '\033[31m'
        verde = '\033[32m'
        violeta = '\033[35m'
        azul = '\033[34m'
        amarelo = '\033[33m'
        cinza = '\033[37m'
        mar = '\033[36m'
        preto = '\033[30m'
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        def inserirdados():
            # p = str(input('Placa do Veículo: '))
            semana = dia_semana()
            vel = gatilho
            p = str(pl)
            verdata()
            dt = str(data)
            tempo()
            h = str(hora)
            v = str(vel)

            sql = "INSERT INTO tabela1 (placa, dia, dds, hora, velocidade, nome_foto) VALUES (%s, %s, %s,%s, %s, %s)"
            val = p, dt, semana, h, v, ft
            cursor.execute(sql, val)

            gui.commit()

            print(cursor.rowcount, "dado inserido.")
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        def enviar():
            global pl
            dados = []
            cursor.execute(f"select nome, placa, email from registo where placa = '{pl}'")
            for i in cursor:
                dados.append(i)
                #print('Não coloquei em pendentes.')
            if len(dados) > 0:
                #print('Enviando')
                enviar_email(dados[0], dados[1], gatilho, multa, dados[2])
            else:
                placa = f'Pendente({pl}'
                pl = f'{placa})'
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        def verdata():
            global data
            data = date.today()
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        def dia_semana():
            lista = [
                'Segunda-feira',
                'Terça-feira',
                'Quarta-feira',
                'Quinta-feira',
                'Sexta-feira',
                'Sábado',
                'Domingo']
            ano = datetime.now().year
            mes = datetime.now().month
            dia = datetime.now().day
            data = date(ano, mes, dia)
            indice = data.weekday()
            return lista[indice] 
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        def tempo():
            global hora
            hora = datetime.now().strftime('%H:%M:%S')
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        def verult():
            cursor.execute('select id from tabela1 order by id')
            global ct
            n = 0
            for c in cursor:
                for k in c:
                    n = k
            n = int(n)
            ct = n + 1
        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-

        def Captura():
            global ft, gatilho, multa, pl
            if video.isOpened():
                print('\033[32m Camera ligada!\033[m')
                # print('\033[32m Pressione o botão para guardar a infração >> \033[m')

                while True:
                    verult()
                    i = ct
                    c, v = video.read()
                    cv2.imshow('Gravando', v)
                    code = cv2.waitKey(2)
                    if code == 13:
                        quit()
                    # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
                    if (ser.inWaiting() > 0):
                        r = ser.readline()
                        gatilho = r.decode('utf-8')
                        ft = f'placa{i}.png'
                        cv2.imwrite(f'fotos/{ft}', v)
                        # startfile(f'placa{i}.png')
                        pl = Le_Foto.leia(ft)
                        try:
                            multa = float(gatilho) * 1000
                        except:
                            multa = int(gatilho) * 1000
                        enviar()
                        inserirdados()

        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
        try:
            print('\033[32m Arduino conectado [V]')
            if __name__ == "__main__":
                while True:
                    Captura()                    
        except Exception as fail:
            print('\033[31m Arduino desconectado [X]\033[m')
            print(fail.__class__)
            print(f'Utilizou-se a porta {cont}')
            break

        # -=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-
    except:
        cont += 1
        pass
