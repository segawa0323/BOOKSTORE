from flask import Flask, render_template
def create_app():
    app = Flask(__name__)
   
    @app.route('/')
    def home():
        return render_template('index.html')
    
    @app.route('/books')
    def book_list():
        return render_template('books/list.html')
   
    @app.route('/about')
    def about():
        return '<h1>このサイトについて</h1>'
 
    return app  