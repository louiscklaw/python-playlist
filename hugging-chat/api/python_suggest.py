from multiprocessing import Pool, cpu_count
import time
import os, sys
import re

from hugchat import hugchat
from hugchat.login import Login

from config import HELLO

LLM=int(sys.argv[1])
PHP_PRE_PROMPT=""
PHP_REQUIREMENTS=""

with open('./prompts/PHP_PRE_PROMPT.md','r+') as f_pre_prompt:
    PHP_PRE_PROMPT=''.join(f_pre_prompt.readlines())

with open('./prompts/PHP_REQUIREMENTS.md','r+') as f_pre_prompt:
    PHP_REQUIREMENTS=''.join(f_pre_prompt.readlines())

def extract_php_comments(code):
    # Regex patterns for PHP comments
    prompt_comment_pattern = r'/\* PROMPT:.*?\*/'
    
    # Find all matches using regex patterns
    prompt_comments = re.findall(prompt_comment_pattern, code, re.MULTILINE|re.DOTALL)
    
    return prompt_comments[0]


example_php=''
with open ('./example_php/index.php','r') as f_php:
    example_php = ''.join(f_php.readlines())

# Custom exception handler for InterruptedError
class MyInterruptException(BaseException):
    pass

class HuggingChatProcessor:
    def __init__(self):
        # missing password here
        self.cookie_path_dir = "./cookies"
        self.chatbot = ''

    def login_huggingface(self):
        # Log in to huggingface and grant authorization to huggingchat
        sign = Login(self.email, self.password)
        cookies = sign.login(cookie_dir_path=self.cookie_path_dir, save_cookies=True)
        sign.save_cookies(self.cookie_path_dir)
        return cookies

    def create_chatbot(self):
        cookies = self.login_huggingface()
        chatbot = hugchat.ChatBot(cookies=cookies, default_llm=LLM)
        return chatbot


    def clear_all_chat(self):
        self.chatbot = self.create_chatbot()
        self.chatbot.delete_all_conversations()

        print('clean all conversations done')

    def get_code(self, content_py, comment_for_prompt=''):
        self.chatbot = self.create_chatbot()
        
        self.chatbot.new_conversation(switch_to=True,system_prompt=PHP_PRE_PROMPT)

        query_question = f'''
{PHP_REQUIREMENTS}
        
REPLY="""
```php 
[your_code] 
```

[LIST_YOUR_CHANGE_HERE]
[your changed]
[/LIST_YOUR_CHANGE_HERE]
"""

Can you optimize the below PHP code for me ? 

PHP=```
{content_py}
```

state your change with reason

'''

        query_result = self.chatbot.chat(query_question)
        # print(query_question)
        print(query_result)

        query_result = str(query_result)
        start_code = query_result.find("```php") + 6
        end_code = query_result.rfind("```")
        code_body = query_result[start_code:end_code].strip()

        # comment_for_prompt = f'/* PROMPT:' + '\n'+comment_for_prompt+'\n'+'*/'

        # return code_body.replace('<?php','<?php' +'\n'+comment_for_prompt)
        self.chatbot.delete_conversation()

        return [code_body, query_result]
        

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
    full_answer_path = i[3]

    try:
        my_instance = HuggingChatProcessor()
        # comment_for_prompt = extract_php_comments(py_content)
        [code_body, query_result] = my_instance.get_code(py_content, '')
        print(code_body)
        with open(dest_file_path,'a+') as f_suggest:
            f_suggest.truncate(0)
            f_suggest.writelines([code_body])
            
        with open(full_answer_path,'a+') as f_full_ans:
            f_full_ans.truncate(0)
            f_full_ans.writelines([query_result])
            
        
        print("done: "+ origina_file_path)
    except Exception as e:
        print("exception occured while processing "+ origina_file_path)
        print(e)
        pass

if __name__ == "__main__":
    try:
      
      # root_paths = ["./test_dir_ci"
      root_paths = [
          r"D:\_workspace\carousell-comission-playlist\ryankochun91735\task1\dist\source\src\php74-httpd\example-app\database\seeders",
      #     # r"D:\_workspace\carousell-comission-playlist\ryankochun91735\task1\dist\source\src\php74-httpd\example-app\app\Models",
      #     # r"D:\_workspace\carousell-comission-playlist\ryankochun91735\task1\dist\source\src\php74-httpd\example-app\app\Http\Controllers",
      #     # r"D:\_workspace\carousell-comission-playlist\ryankochun91735\task1\dist\source\src\php74-httpd\example-app\routes"
          ]
      
      i = 0
      task_list = []
      for root_path in root_paths:
        dw = DirectoryWalker(root_path)
        for py_file in sorted(dw.get_all_files()):
            try:
                with open(py_file, 'r') as f:
                    print("Reading from:", py_file)
                    content = f.read()

                    py_file_suggest = py_file +f"""_suggest_llm_{LLM}"""
                    py_file_full_answer = py_file +f"""_full_answer_llm_{LLM}"""
                    task_list.append([py_file, content, py_file_suggest, py_file_full_answer])

                i += 1
                if i >= 3:
                    break

            except Exception as e:
                print(f"Error reading {py_file}:", str(e))

      print(str(len(task_list)) + ' files loaded...')
      
      my_instance = HuggingChatProcessor()
      my_instance.clear_all_chat()

      num_threads = min(cpu_count(), 1)  # Set maximum number of threads to be equal to the number of available CPUs, but not more than 2

      # Create pool of workers (processes)
      with Pool(num_threads) as p:
          results = p.map(worker, task_list)  # Execute worker function on all numbers from 0 to 9

      print("All processes have completed.")

    except KeyboardInterrupt:
        raise MyInterruptException("Program interrupted")
        
    finally:
        print("\nExiting...")
