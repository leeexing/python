'''
## 第 0007 题： 有个目录，里面是你自己写过的程序，统计一下你写过多少行代码。包括空行和注释，但是要分别列出来。
'''
import re
import os

path_file = r'./_assets/code'
ret = {}

def main():
    files_names = []
    files = [f for f in os.walk(path_file)]
    for f in files:
        path_head = f[0].replace('\\', '/')
        files_f = [(path_head + '/' +  item) for item in f[2]]
        files_names.extend(files_f)
    print(files_names)
    counter_code(files_names[4:5])

def counter_code(filenames):
    '''统计代码行数'''
    docu_flag = False
    for item in filenames:
        ret[item] = 0
        with open(item, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip()
                if line.startswith(r'//') or line.startswith(r'#'):
                    print(line)
                    continue
                if line.startswith(r'/*') and line.endswith(r'*/'):
                    print(line) 
                    continue
                if line.startswith(r'/*') and not line.endswith(r'*/'):
                    print(line)
                    docu_flag = True
                    continue
                if not line.startswith(r'/*') and line.endswith(r'*/'):
                    print(line)
                    docu_flag = False
                    continue
                if line != '' and docu_flag:
                    print(line)
                else:
                    ret[item] += 1
                    # print(line, end='')
    print('='*20)
    print(ret)

def get_files(pathname):
    files = os.listdir(path_file)
    return [x for x in files if is_file(x)]

def is_file(path_name):
    return os.path.isfile(os.path.join(path_file, path_name))

if __name__ == '__main__':
    main()