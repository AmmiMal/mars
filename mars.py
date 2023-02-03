from flask import Flask
from flask import url_for

app = Flask(__name__)


@app.route('/')
def mission():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return """<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                  <h>Жди нас, Марс!</h>
                    <p><b>Человечество вырастает из детства.</b></p>
                    <p><b>Человечеству мала одна планета.</b></p>
                    <p><b>Мы сделаем обитаемыми безжизненные пока планеты.</b></p>
                    <p><b>И начнем с Марса!</b></p>
                    <p><b>Присоединяйся!</p></b>
                  </body>
                </html>"""


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                  <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars.gif')}" 
           alt="здесь должна была быть картинка, но не нашлась">
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')