import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com.br/')
except urllib.error.URLEerror:
    print('O site pudim não esta ativo no momento')
else:
    print('Site acessivel')
    print(site.read())
