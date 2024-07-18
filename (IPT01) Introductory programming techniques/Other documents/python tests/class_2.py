# class Computer:
#     def __init__(self, CPU , RAM):
#         self.RAM=RAM
#         self.CPU=CPU
    
#     def config(self):
#         print(self.CPU,self.RAM)

# comp1=Computer("i7","32GB")
# comp2=Computer("i9","64GB")

# comp1.config()
# comp2.config()

# print(comp1.RAM)

#basically dot notation and stuff to use 


import requests

response=requests.get('en.wikipedia.org/wiki/Scarlet-chested_sunbird')
print(response.text)

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text)
print(soup.find_all('a'))


    
        