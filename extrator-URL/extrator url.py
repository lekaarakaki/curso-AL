import re 

class ExtratorURL:
    def __init__(self, url):
        self.url = self.sanitiza_url(url)
        self.valida_url()


    def sanitiza_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""

    def valida_url(self):
        if not self.url :
            raise ValueError("A URL está vazia")
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)
        if not match:
            raise ValueError("A URL não é válida")
    def get_url_base(self):
        indice_interrogação = self.url.find('?')
        url_bas = self.url[0: indice_interrogação]
        return url_bas

    def get_url_parametro(self):
        indice_interrogação = self.url.find('?')
        url_parametro = self.url[indice_interrogação:]
        return url_parametro

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametro().find(parametro_busca)
        indice_valor = indice_parametro + len(parametro_busca) +1
        indice_e_comercial = self.get_url_parametro().find('&', indice_valor)
        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor: indice_e_comercial]
        return valor
    
    def conversao_moedas(self):
        if self.get_valor_parametro('moedaOrigem') == 'real' and self.get_valor_parametro('moedaDestino') == 'dolar':
            antes = float(self.get_valor_parametro('quantidade'))
            dinheiro = antes/ 5.50
            return 'R$ ' + str(antes) + ' reais equivalem a $ ' + str(dinheiro) + ' dolars' 
            
        else:
            antes = float(self.get_valor_parametro('quantidade'))
            dinheiro = antes * 5.50
            print('passei por aqui')
            return 'R$ ' + str(antes) + ' reais equivalem a $ ' + str(dinheiro) + ' dolars' 
            
            
    
    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + 'parâmetro: ' + self.get_url_parametro() + '\n' +'URL base: ' + self.get_url_base()

    def __eq__(self, other):
        return self.url == self.url

extrator_url = ExtratorURL("http://bytebank.com/cambio?moedaDestino=real&moedaOrigem=dolar&quantidade=100") 
#valor_quantidade = extrator_url.get_valor_parametro("quantidade")
#print(valor_quantidade)
#print(len(extrator_url))
#print(extrator_url)
url = "http://bytebank.com/cambio?moedaDestino=dolar&moedaOrigem=real&quantidade=100"
#extrator_url_2 = ExtratorURL(url)
#extrator_url_1 = ExtratorURL(url)

#print(extrator_url_1 == extrator_url_2)

conversao = extrator_url.conversao_moedas()
print(conversao)