#import argparse
import sys
import calc_library
import os
'''
write a program to get the download folders using os module using > 5mb
list all folder/files in cdrive 

pathlib 
'''
def greet(name:str,time:int):
   for _ in range(time):
    print(f'Hi  {name} How are you doing')


def main():
 # print(sys.argv)
  #print(os.get_exec_path())
  print(os.walk(sys.argv[1]))

  txt_files =[]
  max = 5 * (1024 * 2)
  for root,dirs,files in os.walk(sys.argv[1]):
    for file in  files:
       if os.path.getsize(os.path.join(root,file))/1024 *2 > max:
        txt_files.append(os.path.join(root,file))
        print(txt_files)
        break
 # print(sys.argv[1::])
  #clac = calc_library.CalcLib()
  #print(clac.add(int(sys.argv[1]),int(sys.argv[2])))
  

if __name__ == '__main__':
 main()