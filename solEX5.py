# Vamos renomear urllib.request como ur
import urllib.request as ur

# inclua sua API key, lembre-se que 
# deve ser uma string
APIKEY = 'trnsl.1.1.20141019T153920Z.c2ea774a4c45ef4b.4d2fccbf061f8f6903690b716126f7cd8ff79345'

# pegue o texto do usuario
# e substitua os espacos pelo sinal de +
texto = input('Entre com o texto para traduzir')
texto.replace(' ','+')

# preencha a lista de idiomas
# e pegue a escolha com o usuario
idiomas = ['pt-en', 'en-pt']
escolha = int(input('Pt-ingles (0) ou Ingles-PT (1)?'))

# monte a urla concatenando os dados
url = 'https://translate.yandex.net/api/v1.5/tr.json/translate?key=' + APIKEY + '&lang=' + idiomas[escolha] + '&text=' + texto

# o comando urlopen(url) abre a pagina
saida = ur.urlopen(url)

# o comando saida.read() recupera o conteudo
print saida.read()
