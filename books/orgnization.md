# 项目结构组织

  项目中总结的一个基本组织结构

## 约定

版本库（Repository）：你的应用的根目录。
包（Package）：包含了你的应用代码的一个包。以包的形式建立应用
模块（Module）：一个模块就是一个简单的，可以被其他`Python`文件引入的`Python`文件。一个包由多个模块组成

## 组织模式

### 单一模式

把所有的代码放在一个单一的文件中，通常是 `app.py`
单一模块的应用的版本库看起来就是这样

```py

Repository
|
|__app.py
|
|__config.py
|
|__requirements.txt
|
|__static/
|
|__templates/
|
|__README.md

```

### 包

当项目开始变得复杂，单一模块就会造成严重的问题
此时需要把应用中不同的组件分开到单独的，高内聚的一组模块 -- 也就是包 -- 之中

看起来是这样的

```py

Repository
|
|__config.py  # 包含了你的应用需要的大多数配置变量
|
|__requirements.txt
|
|__run.py
|
|__instance/
  |__config.py  # 这个文件包含不应该出现在版本控制的配置变量。其中有类似调用密钥和数据库URI连接密码。同样也包括了你的应用中特有的不能放到阳光下的东西
|
|__myapp/
  |__ __init__.py
  |
  |__ views.py
  |
  |__ models.py
  |
  |__ forms.py
  |
  |__ static/
  |
  |__templates/


```

## 项目结构

```css
myproject
|
|___app  项目主模块
    |
    |___business  项目业务模块
    |
    |___common  通用类模块
    |
    |___instance  配置项模块（私有的，可以覆盖config.py里面的配置）
    |
    |___models  模型类模块（包括数据库模型等）
    |
    |___resources  资源类模块
    |
    |___util  工具类模块
    |
    |___db.py  数据库模块
    |
    |___config.py  基本配置想模块
    |
    |___ __init__.py Flask应用模块。也可以定义一个 main.py
|
|___ws  项目第二个模块。Socket模块
|
|docs 项目文档
|
|manage.py  程序入口，可以使用Flask-Script定义相关命令
|
|.pylintrc  定义项目编写规范(基于Pep8)
|
|requirements.txt 项目所需的第三方模块
|
|README.md
```

1. 项目的主文件（myProject）中是不需要建立一个 `__init__.py` 文件的。因为这个文件夹不需要形成一个额外的包(package)被外部文件引用
2. 但是 app 和 ws 这两个文件夹中是必须要有 `__init__.py` 文件的。他们内部文件需要引用兄弟模块，同时 ws 中的文件也可能会引用 app 文件夹(此时称为包)里面的文件（模块）

## 具体每个模块的组织关联

```py __ini__.py main.py
# 主应用模块

from flask import Flask, BluePrint
from flask_restful import Api
from flask_restful_swagger import swagger
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from app.db import MYSQL_DB as db, MONGO_DB as mongo
from app.util.response import ResponseHelper
from datetime import timedelta

# 使用这种返回 app 的方式，可以实现项目组织更加灵活
def create_app():
  """创建App"""
  app = Flask(__name__) # 第一个参数一般是 `__name__`。但是如果项目中产生了两个 app 的初始化，可以考虑传入一个特定的项目名称
  app.config.from_object('config') # 这里默认就是从 app 文件中的 config.py 文件中导入相关的配置信息
  app.config.from_pyfile('config.py') # 这里加载定义在instance文件夹中的配置变量.在instance/config.py中定义的变量可以覆盖在config.py中设定的值

  jwt = JWTManager(app)
  db.init_app(app)                    # 初始化MYSQL数据库
  mongo.init_app(app)                 # 初始化MongoDB数据库
  CORS(app)                           # 跨域支持
  api_bp = BluePrint('api', __name__) # 蓝图支持
  api = swagger.docs(Api(api_bp), apiVersion='0.1', resourcePath='/', description='some_desc', api_spec_url='/swagger')

  bind_resources(api)                 # 绑定资源
  app.register_blueprint(api_bp, url_prefix='./api')

  return app


def bind_resources(api):
  """绑定对应的资源。restful风格的实现"""
  from app.resources.equipment import Equipments
  from app.resources.equipmentmodule import EquipmentModules
  api.add_resource(Equipment, './reqipments')
  api.add_resource(EquipmentModules, '/equipment/<string:eqp_id>/modules')

  from app.resources.otherModule import someModules
  api.add_resource()
```

```py db.py

"""数据库数据"""
from flask_sqpalchemy import SQLAlchemy
from flask_pymongo import PyMongo

MYSQL_DB = SQLAlchemy()
MONGO_DB = PyMongo()
```

|
|__resource/  # 这个文件夹里面主要存放 flask_restful 对应的资源文件

一般就是定义一些类，里面包含一些 get、post、put 或者 delete 相关的方法。
这些方法需要在`主文件(main.py)`中被引入，并通过 `api.add_resource()` 这个方法注册


```py resource.py
"""flask_restful 搭配 flask_restful_swagger"""

from flask_restful import Resource
from flask_restful_swagger import swagger
from app.common.fields import EquipmentFields
from app.common.parsers import EQUIPMENT_PARSER
from app.business.equipment import EquipmentManager

class Equipments(Resource):
  """设备信息"""

  def __ini__(self):
    self.equipment_manager = EquipmentManager()

  @swagger.operation(
    notes='',
    nickname='get',
    summary='',
    parameters=[
      {'name':'eqp_id', 'dateType':'string', 'paramType':'query'},
      {'name':'location', 'dateType':'string', 'paramType':'query'}
    ]
  )
  def get(self):  # get就是表示接口是通过 ‘GET’ 方法发起请求的
    args = EUIPMENT_PARSER.parse_args()   # 通过flask——restful 自带的方法获取参数
    // 也可以通过 args = request.args; request.args.get('eqp_id')
    result = self.equipment_manager.find_equipment(args)
    return result
```

|
|__business/  # 这个文件夹里面就是存放和业务相关的具体的代码逻辑

简单来说，就是和数据库打交道的地方。
restful中定义的 get，post之类的方法，调用通过引入过来相应的文件中方法，获取相对应的接口数据
这里的数据库可以是 SQLAlchemy，也可以是MongoDB

```py business.equipment.py

from app.models.equip.equipment import Equipment
from app.db import MYSQL_DB as db

class EquipmentManager():
  """设备处理业务类"""

  def __init__(self):
    self.logger = create_logger('EDMP_API')

  def find_equipment(self, args=None):
    """查询设备"""
    try:
      filters = []
      if args.eqp_id:
        filters.append(Equipment.EQP_ID == args.eqp_id)
      if args.location:
        filters.append(Equipment.Location.like('%' + args.location + '%'))
      items = db.session.query(
        Equipment.Latitude, Equipment.Location, Equipment.Type
      ).filter(and_(*filters)).order_by(Equipment.EQP_ID).all()

      eqps = [dict(EQP_ID=item.EQP_ID, Location=item.Location, Type=item.Type) for item in items]
      data = marshal(eqps, EquipmentFields.resource_fileds)
      return ResponseHelper.return_true_data(data)
    except Exception as ex:
      self.logger.error('服务器发生错误:%', str(ex))
      return ResponseHelper.return_false_data(msg='Server Error', status=500)
```

```py util/ response.py
"""输出类"""

class ResponseHelper:
  """输出帮助类"""
  @staticmethod
  def return_true_data(data, msg='success', **kwargs):
    """返回正确结果"""
    result = {
      'result': 100,
      'data': data,
      'msg': msg,
      **kwargs
    }
    return result

  @staticmethod
  def return_false_data(data=None, msg='error', status=None, **kwargs):
    """返回错误结果"""
    return {
      'result': status,
      'data': data,
      'msg': msg,
      **kwargs
    }

```

```py util/ logger.py
"""日志模块"""

import logging
import os

def create_logger(name):
  """创建logger"""
    logger = logging.getLogger(name)
    logger.setLevel(logging.INFO)
    formatter = logger.Formatter(

    )
    if not logger.handlers:
        chandler = logging.StreamHandler()
        chandler.setFormatter(formatter)
        chandler.setLevel(logging.INFO)
        logger.addHandler(chandler)

        fhandler = logging.FileHandler(os.path.join('./', 'log.log'), encoding='utf-8', delay='true')
        fhandler.setLever()
        fhandler.setFormatter(formatter)
        logger.addHnadler(fhandler)
    return logger
```