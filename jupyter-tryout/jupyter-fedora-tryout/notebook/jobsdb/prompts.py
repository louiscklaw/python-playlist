import os, sys
import requests
import json

def MakeMarkdownString(md_string):
    start = '```markdown'
    end = '```'
    
    return start + md_string + end

def helloworld():
    print('say helloworld')
    return "say helloworld"
