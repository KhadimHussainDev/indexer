from collections import defaultdict
import os
import re

dic = defaultdict(set)
path = './documents'

def main():
  readAllDocument()
  while True:
    print("1. Search document")
    print("2. Search word")
    print("e. Exit")
    op = input("Choose an option: ")
    if op == '1':
      searchDocument()
    elif op == '2':
      searchWord()
    elif op == 'e':
      break
    else:
      print("Choose correct option")
    input("Press Enter to continue...") 
    os.system('cls') 


def searchDocument():
  name = input("Enter name of document : ")
  
  files = os.listdir(path)
  if name in files:
    file_path = os.path.join(path,name)
    with open(file_path,'r') as file:
      content = file.read()
      print(content)
  else:
      print(f"Document '{name}' not found in '{path}'.")


def searchWord():
  word = input("Enter word to search : ")
  if word.lower() in dic:
    print(f"{word} is in these files : {dic[word.lower()]}")
  else:
    print(f"{word} is not found in any file.")
  return 0

def readAllDocument():
  files = os.listdir(path)
  for f_path in files:
    file_path = os.path.join(path, f_path)
    with open(file_path , 'r') as file:
      content = file.read()
      cleaned_content = re.sub(r'[^\w\s]', '', content)
      words = [word.lower() for word in cleaned_content.split() if len(word) > 3]
      for word in words:
        dic[word].add(f_path)



if __name__ == '__main__':
  main()