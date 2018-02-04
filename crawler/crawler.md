# crawler

> 爬虫也不是那么简单啦

## 编码问题

1、一般情况下是不需要改动默认的编码格式的

```python
import io
import sys
# 改变默认的编码方式sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030')
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='gb18030'
```

因为有些网页默认的编码方式就是 `utf-8`,使用了上面的代码修改默认的编码格式之后，反而会造成网页的部分汉字显示出现乱码的现象
正确的做法就应该是 先不要一上来就使用修改默认的方式，先输出查看，如果是有乱码问题存在，再使用之

2、