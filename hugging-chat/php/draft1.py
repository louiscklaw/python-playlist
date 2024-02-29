import re

from hugchat import hugchat
from hugchat.login import Login

# Log in to huggingface and grant authorization to huggingchat
EMAIL = "testhelloworld04@gmail.com"
PASSWD = "TgUGLRcL1qCMbmP"
cookie_path_dir = "./cookies"
sign = Login(EMAIL, PASSWD)
cookies = sign.login(cookie_dir_path=cookie_path_dir, save_cookies=True)

# Create your ChatBot
chatbot = hugchat.ChatBot(cookies=cookies.get_dict())

# 0 mistralai/Mixtral-8x7B-Instruct-v0.1
# 1 google/gemma-7b-it
# 2 meta-llama/Llama-2-70b-chat-hf
# 3 NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO
# 4 codellama/CodeLlama-70b-Instruct-hf
# 5 mistralai/Mistral-7B-Instruct-v0.2
# 6 openchat/openchat-3.5-0106

# for i in range(0,6+1):
i = 6
chatbot.switch_llm(i)
chatbot.new_conversation(switch_to = True)
info = chatbot.get_conversation_info()

# Non stream response
query_result = chatbot.query(
"""
Just do what i tell you

draft me a php helloworld:

- regulate code to comply PSR
- return me the code in markdown format only.
- add comment to the source code
""")


query_result = str(query_result)
start_code = query_result.find('```php')+6
end_code = query_result.find('```',start_code+6)
code_body = query_result[start_code:end_code]

print(code_body.strip())

# - tidy up source code in autopep8 format
