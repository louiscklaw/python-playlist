import os,sys

def helloworldLog():
    print("helloworld")

def logToTextFile(log_path, content):
    try:
      with open(log_path, 'a+') as fo:
         fo.truncate(0)
         fo.writelines(content)

    except Exception as e:
       print("Exception when logToTextFile")    
       print(e)

    
    