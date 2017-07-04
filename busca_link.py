'''
classe: Scrapy
descrição: Exercicio para buscar todos os links de um site
autor: Clodonil Honorio Trigo
email: clodonil@nisled.org
data: 04 de julho de 2017
'''

import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class Scrapy:
      def __init__(self):
          # links
          self.links = []
          self.domain = ""
          self.list_link = []

      def get_page(self,url):    
          '''
             Metodo que conecta na pagina
          '''
          #Domain
          self.domain = urlparse(url).netloc

          #conecta na pagina     
          fonte = requests.get(url)

          #Verifica se o status é de sucesso
          if fonte.status_code == 200:
              return  BeautifulSoup(fonte.text,"lxml")
          else:
              #Apresenta a mensagem de erro
              return(False)

      
      def busca_tag(self, page,tag):
          return page.find_all(tag)

      def busca_links(self,page):
          ''' 
              Metodo para buscar o links da pagina e verifica se pertece ao mesmo dominio
          '''
          for link in self.busca_tag(page,"a"):
              hlink = link.get('href')
              if len(link.text) > 0:
                 if not hlink in self.links:
                    self.links.append(hlink)
                    self.list_link.append([hlink,self.check_domain(hlink)]) 
      
      def clear(self, tag):
           '''
              Limpar lixo da tag
           '''
           return tag.replace("\n","").replace("\t","")

      def check_domain(self,url):
           if self.domain == urlparse(url).netloc:
               return True
           else:
               return False

      def run(self, site):
          '''
             Metodo para iniciar acao da classe
          '''
          #Domain
          self.domain = urlparse(site).netloc
          self.list_link.append([site,True])
          self.links.append(site)

          while self.list_link:
               url = self.list_link.pop()
               if url[1]:
                  self.busca_links(self.get_page(url[0]))


          return self.links


if __name__ == "__main__":
     url="http://www.medparc.com.br"
     site_connect = Scrapy()
     links = site_connect.run(url)
     cont = 1
     for link in links:
         print("[{0}] - {1} ".format(cont,link))
         cont = cont + 1

