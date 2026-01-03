import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'


def leia(placa):

    def encontrarPlaca(source):
        img = cv2.imread(source)

        # cv2.imshow('Normal',img)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Cinza',gray)
        _, bin = cv2.threshold(gray, 90, 255, cv2.THRESH_BINARY)
        # cv2.imshow('bin',bin)
        desfoque = cv2.GaussianBlur(bin, (5, 5), 0)
        # cv2.imshow('des',desfoque)

        contornos, hier = cv2.findContours(desfoque, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)

        # cv2.drawContours(img,contornos,-1,(0,255,0),2)
        # cv2.imshow('cont',img)

        for c in contornos:
            parametro = cv2.arcLength(c, True)
            aprox = cv2.approxPolyDP(c, 0.010 * parametro,
                                     True)  # PARTE DE FRENTE TROCA O VALOR POR 0.03 PARA MULTIPLICAR
            if parametro > 120:
                if len(aprox) == 4:
                    (x, y, alt, lar) = cv2.boundingRect(c)
                    cv2.rectangle(img, (x, y), (x + alt, y + lar), (0, 255, 0), 2)

                    roi = img[y:y + lar, x:x + alt]  # : - dividir
                    cv2.imwrite(f'{source}', roi)
        # cv2.imshow('draw',img)
        # cv2.waitKey(0)
        # cv2.destroyAllWindows()

    def ProcessamentoPlaca():
        img = cv2.imread(f'{source}')

        if img is None:
            return
        # transformando a imagem e cinza
        cinza = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        # transformando a imagem em preto e branco
        # preto,branco
        _, image_bin = cv2.threshold(cinza, 112, 255, cv2.THRESH_BINARY)
        # salvando a imagem
        cv2.imwrite("placa_Preto_Branco.png", image_bin)
        cv2.imshow('imagem', image_bin)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    def LerPlaca():
        imag = cv2.imread('placa_Preto_Branco.png')
        # dimencionando a imagem
        config = r'-c tesseract_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 3 --psm 6'  # estamos passando um parametro para a leitura dfa configuração de como a imagem é lida
        dm = cv2.resize(imag, None, fx=4, fy=4, interpolation=cv2.INTER_CUBIC)
        saida = pytesseract.image_to_string(dm, lang='eng', config=config)
        # print('placa: {}'.format(saida.strip()))
        teste = saida.strip()
        teste = teste.split()
        print('placa:\033[33m {} \033[m'.format("".join(teste)))
        return teste

    source = f'Fotos/{placa}'
    encontrarPlaca(source)
    ProcessamentoPlaca()
    teste = LerPlaca()
    return f'{"".join(teste)}'
