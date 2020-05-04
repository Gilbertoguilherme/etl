import requests, urllib.error, csv, socket, time, xml.etree.ElementTree, bs4
from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
import lxml.html as parser
from lxml import html
from urllib.parse import urlsplit, urljoin

url = 'https://raw.githubusercontent.com/Gilbertoguilherme/ansibleaws/master/offers.csv'

print ("baixando a tabela")
Download = requests.get(url)
with open("tabela.csv", "wb") as code:
    code.write(Download.content)
    code.close()

with open('tabela.csv','r') as arquivo:
    linhas = csv.reader(arquivo)
    
    for linha in linhas:
        emp=linha[0][14:15]
        if not linha:
                continue            
        try:
            cons = urlopen(linha[0], timeout=5)
            conn = cons.status
            #conn = requests.get(linha[0])
             
        except HTTPError as e:
            print(e)
        except URLError:
            print("Server down or incorrect domain")
        except socket.timeout:
            print('timeout')
        else:
            if emp == 'g':
                magalu = 'Magazineluiza'
                #objemp=BeautifulSoup(conn.text,features='html.parser')
                objemp = BeautifulSoup(cons, 'lxml')
                #vetor_nome = objemp.select(".header-product__title")[0]
                vetor_nome = objemp.find('a', {'class' :'floater-menu__product-title js-floater-menu-link'})
                vetor_price = objemp.find('span', {'class':'floater-menu__product-price'})
            
                print('E-commerce {} \nproduto {} \nvalor {}\n' .format(magalu,vetor_nome,vetor_price))
            
                #print('valor = {} '.format(vetor_price.text))
                #lista=objSoup.select('div')            
                arquivo2 = open("dados.log","a")
                arquivo2.writelines(objemp.title)
                arquivo2.write('\n')
                arquivo2.close()       

            elif emp == 's':
                casas ='casasbahia'
                objemp=bs4.BeautifulSoup(cons,features='html.parser')
                vetor_emp = objemp.find('div', class_='container-left-top-header')
                vetor_nome = objemp.find('a', {'class' :'floater-menu__product-title js-floater-menu-link'})
                #vetor_nome = objemp.find('h1', {'class': 'header-product__title'})
                vetor_price = objemp.find('span', {'class':'floater-menu__product-price'})
                #vetor_big_date = objSoup.find('div', class_='header-product js-header-product')
                #emp = vetor_emp.a
                #produ = vetor_nome.a
                #print(vetor_emp.a.text)
                print('E-commerce {} \nproduto {} \nvalor {}\n' .format(casa,vetor_nome,vetor_price))
                arquivo2 = open("dados.log","a")
                arquivo2.writelines(objemp.title)
                arquivo2.write('\n')
                arquivo2.close()
                arquivo2.close()
            
            elif emp == 'o' or 'r':
                mercado = 'mercado livre'
                merc = emp[14:15]
                if merc == 'p':
                    objemp=BeautifulSoup(cons,features='html.parser')
                    vetor_nome = objemp.find('h1', {'class':'item-title__primary '})
                    vetor_price = objemp.find('span', {'class':'price-tag-fraction'})
                    nome = objemp.title
                    print('E-commerce {} \nproduto {} \nvalor {}\n' .format(mercado,vetor_nome,vetor_price))
                    arquivo2 = open("dados.log","a")
                    arquivo2.writelines(objemp.title)
                    arquivo2.write('\n')
                    arquivo2.close()
                
                else:
                    objemp=BeautifulSoup(cons,features='html.parser')
                    vetor_nome = objemp.find('h1', {'class' :'ui-pdp-title'})
                    vetor_price = objemp.find('span', {'class':'price-tag-fraction'})
                    print('E-commerce {} \nproduto {} \nvalor {}\n' .format(mercado,vetor_nome,vetor_price))
                    arquivo2 = open("dados.log","a")
                    arquivo2.writelines(objemp.title)
                    arquivo2.write('\n')
                    arquivo2.close()
                    arquivo3 = open("teste.log","a")
                    dadoslog = requests.get(linha[0])
                    arquivo3.write(dadoslog.text)
                    arquivo3.write('\n')
                    arquivo3.close()

arquivo.close()