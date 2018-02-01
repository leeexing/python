Bfdhfdf

B
B
> "What I cannot create, I do not understand."
> -- Richard Feynman

## python
    created by leeing on 2017/12/19
    主要目的：
        1、记录python的学习之路
        2、练习使用python
    包含内容：
        1、利用flask框架编写一个blog
        2、记录一下自己的爬虫demo以及经验
        3、自己的一些读书心得
    结构：
        1、blog
        2、crawler
        3、books

## blog
    learn flask frame

### flask
1、session 操作
    app.config[SECRET_KEY] = os.urandom(24)

    session[key] = value -- 添加设置
    session.get(key) -- 获取
    seesion.pop(key) -- 删除某个键值
    session.clear() -- 清除
    机制：
      * 把敏感数据经过加密后放入`session`中，然后再把`session`存放到cookie中，下次请求的时候，再从浏览器发送过来的cookie中读取session，然后再从session中读取敏感信息，并进行解密，获取最终的用户数据

2、如果没有指定时间，那么浏览器关闭那么session就自动结束
    session.permanent = True -- 设置过期时间为31天
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7) -- 设置过期时间为7天

3、get 传参
    url_for(url, q='leeing') -- url?q=leeing
    后台通过
    request.args.get('key') -- 获取get请求参数

4、post请求
    request.form.get('key') -- 获取表单数据
    request.values.get('key') -- 获取所有参数

5、g属性 保存全局变量
    g.username = xxx  |  g.ip = yyy
    g对象是专门用来保存用户的数据的
    g对象在一次请求中的所有代码的地方，都是可以使用的  |  当你第二次请求的时候`g`就不是同一个了 |  范围是当前请求内
      * 所以实用性还不如 session，因为g变量保存的周期不常

6、hook 钩子函数
    before_request  | 在请求之前执行  | 是在视图函数执行之前执行的  |  只是一个装饰器
      * 可以截取所有的访问 | 即在所有请求进入`app.route`装饰的函数前先被处理一次
    after_request
      * 在用户请求得到函数响应后再执行一次 | 这个执行是在`函数返回数据前`被调用  | 形成了`response`，但未返回给用户
    context_processor  | 返回结果必须是 dict  | 上下文处理器，包含上下文共用的变量  |  只是一个装饰器
      * 目的是让所有自定义变量在模板中可见

7、优雅的重定向所有未登录用户到登录界面
    使用`@app.before_request`hook钩子进行登录验证
      * 两个条件判断  | `session.get('username')`  |  `request.endpoint not in ('login','register','static')`  | 否则会不断重定向 `302`
      * request.endpoint | 每个视图函数都有一个endpoint  |  就是 @app.route下面的 `def 函数名`视图函数
      * 视图蓝本 blueprint
        app.register_blueprint(user, url_prefix='user')
        app.register_blueprint(file, url_prefix='file')
        这种情况下如果视图函数重名  |  需要带上前面的 `user`、`file` 才行呢
    安装`flask-login` |  但是每个需要认证的路由都还必须添加一个`@login_required`的装饰器

8、

## crawler
    some crawler demos

## reading
    read some python books and some of my thoughts
