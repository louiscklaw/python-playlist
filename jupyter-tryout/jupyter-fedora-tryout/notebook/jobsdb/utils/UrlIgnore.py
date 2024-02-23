import os, sys
import requests
import json


class UrlIgnore:
    def __init__(self):
        cwd = os.path.dirname(__file__)
        self.file_path =  cwd+'/url_ignore.json'
        self.url_list = []
    
    def store(self):
        print('store temporary ignored')
        # with open(self.file_path,'w+') as f_store:
        #     json.dump(self.url_list,f_store)

    def load(self):
        with open(self.file_path,'r+') as f_load:
            self.url_list = json.load(f_load)

    def add(self, url_to_add):
      self.load()
      if (self.check(url_to_add)):
          pass
      else:
          self.url_list.append(url_to_add)
          self.store()
    
    def check(self,url_to_check):
        self.load()

        try:
            return self.url_list.index(url_to_check) > -1
        except Exception as e :
            return False
