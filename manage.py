# 导入flask模块
from flask import Flask


# 创建flask应用
app = Flask(__name__)


# 创建视图函数
@app.route('/')
def index():
    return 'index'


# 运行flask应用
if __name__ == '__main__':
    app.run(debug=True)