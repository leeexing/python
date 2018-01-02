## python 命名规范

### 文件名
    全小写，可使用下划线

### 包
    简短的、小写的名字。如 mypackage

### 模块
    与包的规范相同。如 mymodule

### 类
    总是使用首字母大写单词串。如 MyClass

### 函数&方法
    函数名小写，可以用下划线风格--增加可读性。如 myfunction、my_example_function

### 函数和方法的参数
    总是用 `self` 作为实例方法的第一个参数。总是用 `cls` 作为类方法的第一个参数
    如果一个函数的参数名称和保留的关键字冲突，使用一个后缀下划线

### 变量
    变量名全部小写，由下划线连接各个单词
    *Attention*
    不论是类成员变量还是全局变量，均不使用 'm' 或 'g' 前缀
    私有类成员使用单一下划线前缀标识，多定义公开成员，少定义私有成员
    变量名不应该带有类型信息--因为python是动态类型语言

### 常量
    常量名所有字母大写，由下划线连接各个单词

### 前导后缀下划线
    一个前导下换线 -- 表示非公有
    一个后缀下划线 -- 避免关键字冲突
    两个前导下划线 -- 当命名一个类属性引起名称冲突时使用
    两个前导和后缀下划线 -- ‘魔’对象或者属性；如 __init__

### Google Python 命名规范
    module_name, package_name, ClassName, method_name, ExceptionName
    function_name, GLOBAL_VAR_NAME
    instance_var_name, function_parameter_name, local_var_name