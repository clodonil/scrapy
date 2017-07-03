#Exercicio para buscar links

import requests
from bs4 import BeautifulSoup


class Scrapy:
      def __init__(self,url):
          #conecta na pagina     
          fonte = requests.get(url)

          #Verifica se o status é de sucesso
          if fonte.status_code == 200:
             self.fonte_bs = BeautifulSoup(fonte.text,"lxml")
          else:
              #Apresenta a mensagem de erro
              return(false)

      
      def busca_tag(self, tag):
          return self.fonte_bs.find_all(tag)

      def busca_links(self):
          links=[]
          for link in self. busca_tag("a"):
              hlink = link.get('href')
              alink = self.clear(link.text)
              if len(alink) > 0:
                 links.append([alink,hlink]) 
          return links
      
      def clear(self, tag):
           return tag.replace("\n","").replace("\t","")




if __name__ == "__main__":
     url = "http://www.medparc.com.br"
     site_connect = Scrapy(url)
     if site_connect:
        for link,hlink in site_connect.busca_links():
            print("--> {0} [{1}]".format(link,hlink))
     else:
        print("Erro ao conectar na pagina solicitada")

