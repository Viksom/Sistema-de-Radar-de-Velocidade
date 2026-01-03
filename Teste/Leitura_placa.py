import cv2
import pytesseract


def leia(lido):
    global placa_Recorte
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
    # vamos usar arcascade frontalfaces
    xml_Placa = 'haarcascade_russian_plate_number.xml'
    # carregando o classificador para ler a placa do carro
    faceClassifier = cv2.CascadeClassifier(xml_Placa)
    # escolhendo a camera
    im = cv2.imread(f'Fotos/{lido}')
    # O tamango que a imagem sera lida
    imagem = cv2.resize(im, (1266, 780), interpolation=1)
    print('abrindo a imagem')
    # transformando a imagem na escolha cinza
    gray = cv2.cvtColor(imagem, cv2.COLOR_BGR2GRAY)
    face = faceClassifier.detectMultiScale(gray)

    for x, y, l, a in face:
        bordas = cv2.rectangle(imagem, (x, y), (x + l, y + a), (0, 255, 0), 8)
        roi = bordas[y:y + a, x:x + l]

    placa_Recorte = roi[9:-8, 16:-20]  # Recortando no eixo y e x
    cv2.imwrite('placa.jpg', placa_Recorte)
    print('imagem aberta')


    def ProcessamentoPlaca():
        img = cv2.imread('placa.jpg')

        # if img is None:
        #     return
        # transformando a imagem e cinza
        cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # transformando a imagem em preto e branco
        # preto,branco
        # filtrando as imagens
        _, image_bin = cv2.threshold(cinza, 124, 255, cv2.THRESH_TRIANGLE)
        # desfoque= cv2.GaussianBlur(image_bin,(5,5),2.5)
        # cv2.imshow('placa',desfoque)
        # cv2.imshow('placa',desfoque)
        cv2.imwrite('placa1.jpg', image_bin)


    def LerPlaca():
        global placa
        imag = cv2.imread('placa1.jpg')
        # config = r'-c tesseract_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 3 --psm 6' # estamos passando um parametro para a leitura dfa configuração de como a imagem é lida
        # dimencionando a imagem
        dm = cv2.resize(imag, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
        saida = pytesseract.image_to_string(dm, lang='eng')  # ,config=config)
        placa = saida
        image_Text = cv2.putText(imagem, placa.strip(), (x + 50, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2,
                                 cv2.LINE_AA)
        cv2.imshow('license', image_Text)


    if __name__ == '__main__':
        ProcessamentoPlaca()
        LerPlaca()
        key = cv2.waitKey(0)

        if key == 13:
            quit()
    return 'placa:{}'.format(placa.strip())
