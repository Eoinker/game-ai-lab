from pathlib import Path
import sys
sys.path.append(str(Path(__file__).parents[1]))

from ollama import chat
from util.llm_utils import pretty_stringify_chat, ollama_seed as seed

# Add you code below
sign_your_name = 'Owen Larmon'
model = 'llama3.2'
options = {'temperature': 0.34, 'max_tokens': 40}
messages = [
  {'role': 'system', 'content': 'You are a dungeon master. Present the user with fantasy scenarios.'},
  {'role': 'system', 'content': 'Allow player decisions to backfire if they are unlikely to succeed.'},
  {'role': 'system', 'content': 'Give the player a set of potential options but make it clear they are able to type in custom resposes.'}
]
# But before here.

options |= {'seed': seed(sign_your_name)}
# Chat loop
while True:
  response = chat(model=model, messages=messages, stream=False, options=options)
  # Add your code below
  message = {'role': 'user', 'content': input('Player: ')}
  if message['content'] == '/exit':
    break
  messages.append(message)
  response = chat(model=model, messages=messages, stream=False, options=options)
  print(f'DM: {response.message.content}')
  messages.append({'role': 'assistant', 'content': response.message.content})
  # But before here.
  

# Save chat
with open(Path('lab03/attempts.txt'), 'a') as f:
  file_string  = ''
  file_string +=       '-------------------------NEW ATTEMPT-------------------------\n\n\n'
  file_string += f'Model: {model}\n'
  file_string += f'Options: {options}\n'
  file_string += pretty_stringify_chat(messages)
  file_string += '\n\n\n------------------------END OF ATTEMPT------------------------\n\n\n'
  f.write(file_string)

