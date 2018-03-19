'''
## 第 0006 题： 你有一个目录，放了你一个月的日记，都是 txt，为了避免分词的问题，假设内容都是英文，请统计出你认为每篇日记最重要的词。
'''
import re, os, collections

word = re.compile('\w+')
path_file = r'./_assets/doc'
def main():
    files = os.listdir(path_file)
    print(files)
    obj = {}
    for filename in files:
        with open(os.path.join(path_file, filename), encoding='utf-8') as f:
            data = f.read()
            words = word.findall(data)
            words_freq = list(sorted(collections.Counter(words).items(), key = lambda x: x[1], reverse = True))
            # print(words_freq)
            obj[filename] = words_freq[0]
    print(obj)


if __name__ == '__main__':
    main()
