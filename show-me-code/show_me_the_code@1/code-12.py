'''
## 第 0012 题： 敏感词文本文件 filtered_words.txt，里面的内容 和 0011题一样，当用户输入敏感词语，则用 星号 * 替换，例如当用户输入「北京是个好城市」，则变成「**是个好城市」。
'''
import os

path_file = './_assets/doc'

sensitive_words = set()

def main():
    global sensitive_words
    with open(os.path.join(path_file, 'filter_words.txt'), encoding='utf-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            if line != '':
                sensitive_words.update({line})
                # sensitive_words |= {line}
    print(sensitive_words)
    civilization()

def civilization():
    '''文明'''
    while True:
        word = input()
        info = is_sensive_in_words(word)
        print(info)
        if word == 'exit':
            break
        elif info[0]:
            print(word.replace(info[1], '*'*(len(info[1]))))

def is_sensive_in_words(word):
    '''是否包含敏感词'''
    print(word)
    for item in sensitive_words:
        if item in word:
            return True, item
        continue
    return False, 0

if __name__ == '__main__':
    main()
