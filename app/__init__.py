from flask import Flask
def create_app():
    app = Flask(__name__)
   
    @app.route('/')
    def home():
        return '<h1>📚 書籍注文システム</h1><p>ようこそ!</p>'
    
    @app.route('/books')
    def book_list():
        return '<h1>書籍一覧</h1><p>書籍データはここに表示されます</p>'
   
    @app.route('/about')
    def about():
        return '<h1>このサイトについて</h1>'
 
    return app  