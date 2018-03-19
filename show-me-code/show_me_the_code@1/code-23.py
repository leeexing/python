'''
## 第 0023 题： 使用 Python 的 Web 框架，做一个 Web 版本 留言簿 应用。

阅读资料：Python 有哪些 Web 框架

留言簿参考
'''
from flask import Flask
from sqlalchemy import String, DATETIME, Interger, Column

app = Flask(__name__)

class Post(base):
    __tablename__ = 'todo'

    postID = Column(Interge, primary_key=True)
    postName = Column(String(50))
    createdAt = Column(DATETIME)
    content = Column(String(15000))

class DataBase(object):
    def __init__(self):
        self.info = {
            'uesr': '',
            'password': '',
            'ip': '',
            'port': '',
            'database': ''
        }
        self.session = self.make_connect()
    
    def __del__(self):
        if self.session:
            self.session.close()

    def make_connect(self):
        connect_str = 'mysql + pymysql: //{user}:{password}@{ip}:{port}/{database}'.format(self.info)
        engine = create_engine(connect_str)
        DBSession = sessionmaker(engine)
        session = DBSession()
        return session

    def query_all_post(self):
        items = self.session.query(Post).order_by(Post.postID).all()
        if not isinstance(items, list):
            return [items]
        return items

    def add_post(self, item):
        self.session.add(item)
        self.session.commit()


@app.route('/', methods=['GET'])
def index():
    pass

@app.route('/add', methods=['POST','GET'])
def add():
    pass

if __name__ == '__main__':
    app.run(debug=True)