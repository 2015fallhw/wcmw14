from flask import Blueprint, render_template

# 這裡設定的 template_folder 為 template 搜尋目錄, 表示位於 user/g1/templates 目錄中
# 但是若 wcmw14/templates 目錄中有相同名稱的 template file, 則優先取外部的檔案
# 這樣的設計希望可以在統整各藍圖時, 可以隨時根據需要改寫 template 配置
g1app = Blueprint('g1', __name__, url_prefix='/g1', template_folder='templates')

@g1app.route('/')
def helloworld():
    user = "Yen"
    # 若 template 檔案名稱與位於外部 templates 目錄中的檔案同名, 則取外部的 template
    return render_template('g1index.html', user=user)
