from multiprocessing import Pool, cpu_count
import time
import os, sys
import re

from hugchat import hugchat
from hugchat.login import Login

example_php=''
with open ('./example_php/index.php','r') as f_php:
    example_php = ''.join(f_php.readlines())

# Custom exception handler for InterruptedError
class MyInterruptException(BaseException):
    pass

class HuggingChatProcessor:
    def __init__(self):
        self.email = "testhelloworld04@gmail.com"
        self.password = "TgUGLRcL1qCMbmP"
        self.cookie_path_dir = "./cookies"
        self.chatbot = ''

    def login_huggingface(self):
        # Log in to huggingface and grant authorization to huggingchat
        sign = Login(self.email, self.password)
        cookies = sign.login(cookie_dir_path=self.cookie_path_dir, save_cookies=True)
        return cookies

    def create_chatbot(self):
        cookies = self.login_huggingface()
        chatbot = hugchat.ChatBot(cookies=cookies)
        return chatbot

    def switch_model(self, model_index):
        self.chatbot = self.create_chatbot()
        self.chatbot.delete_all_conversations()
        self.chatbot.switch_llm(model_index)
        self.chatbot.new_conversation(switch_to=True)
        info = self.chatbot.get_conversation_info()
        return info

    def get_code(self, content_py):
        info = self.switch_model(6)
        self.chatbot = self.create_chatbot()

        init_result = self.chatbot.chat(f"""
Imagine you are a programmer that knows PHP and laravel framework.
                                        
These are the references:
  - php offical documentation
  - laravel v10 offical documentation
""")
        query_question = f"""
PHP='''
{content_py}
'''

## tasks:
  - analyse the PHP code above

## requirements:
  - use only PHP to analyse the code
  - return me the code inside markdown (e.g. ```php [result code...] ```) format only.
  - add comment to the source code, mark it with "SUGGESTIONS: " beginning.
  - rewrite code to comply "PHP Standards Recommendations"
  - no need explain your answer
  - comment the line out when the line is not useful
  - comment the line out when the line is debug output, add comment starting with "DEBUG:" at the line above it
  - make some typo to the comment
  - add comment to the table field creation
"""

        query_result = self.chatbot.query(query_question)
        print(query_question)
        print(query_result)

        query_result = str(query_result)
        start_code = query_result.find("```php") + 6
        end_code = query_result.rfind("```")
        code_body = query_result[start_code:end_code].strip()

        return code_body

class DirectoryWalker:
    def __init__(self, root_path):
        self.root_path = root_path
        
    # Method to drill down into directories and subdirectories
    def get_all_files(self):
        for dirpath, dirnames, filenames in os.walk(self.root_path):
            for filename in filenames:
                if filename.endswith('.php'):
                    yield os.path.join(dirpath, filename)
        
# Function to be executed by each process
def worker(i):
    origina_file_path = i[0]
    py_content = i[1]
    dest_file_path= i[2]

    try:
        my_instance = HuggingChatProcessor()
        suggested_content = my_instance.get_code(py_content)
        with open(dest_file_path,'a+') as f_suggest:
            f_suggest.truncate(0)
            f_suggest.writelines([suggested_content])
            
        
        print("done: "+ origina_file_path)
    except Exception as e:
        print("exception occured while processing "+ origina_file_path)
        print(e)
        pass

if __name__ == "__main__":
    try:
      
      # root_paths = ["./test_dir_ci"]  
      root_paths = [
          r"D:\_workspace\carousell-comission-playlist\ryankochun91735\task1\dist\source\src\php74-httpd\example-app\database\seeders",
          # r"D:\_workspace\carousell-comission-playlist\ryankochun91735\task1\dist\source\src\php74-httpd\example-app\app\Models",
          # r"D:\_workspace\carousell-comission-playlist\ryankochun91735\task1\dist\source\src\php74-httpd\example-app\app\Http\Controllers",
          # r"D:\_workspace\carousell-comission-playlist\ryankochun91735\task1\dist\source\src\php74-httpd\example-app\routes"
          ]
      
      task_list = []
      for root_path in root_paths:
        dw = DirectoryWalker(root_path)
        for py_file in dw.get_all_files():
            try:
                with open(py_file, 'r') as f:
                    print("Reading from:", py_file)
                    content = f.read()

                    py_file_suggest = py_file +'.suggest'
                    task_list.append([py_file, content, py_file_suggest])

            except Exception as e:
                print(f"Error reading {py_file}:", str(e))

      print(str(len(task_list)) + ' files loaded...')
      num_threads = min(cpu_count(), 4)  # Set maximum number of threads to be equal to the number of available CPUs, but not more than 2

      # Create pool of workers (processes)
      with Pool(num_threads) as p:
          results = p.map(worker, task_list)  # Execute worker function on all numbers from 0 to 9

      print("All processes have completed.")

    except KeyboardInterrupt:
        raise MyInterruptException("Program interrupted")
        
    finally:
        print("\nExiting...")
