# Завдання 1
# Використовуючи механізм маршрутизації, створіть вебдодаток, який відображатиме різні розділи з інформацією
# про ваше місто. Додаток мають містити такі розділи:
# ■ Головна;
# ■ Новини міста;
# ■ Голови міста;
# ■ Факти про місто;
# ■ Контактні телефони міських служб.
# Доступ до різних розділів має здійснюватися за різними адресами. Наприклад, якщо користувач вказав 127.0.0.1:8000,
# відкриється розділ «Головна». Якщо було вказано 127.0.0.1:8000/news, має відкритися
# розділ «Новини міста». Якщо було вказано 127.0.0.1:8000/management, має відкритися розділ «Керівництво міста» і т. п.

# Завдання 3
# Додайте розділ «Історія» до проєкту із першого завдання.Якщо вказаний шлях 127.0.0.1:8000/history, має відображатися
# розділ із загальною інформацією про історію міста.
# Якщо було вказано шлях 127.0.0.1:8000/history/people, має відображатися інформація про відомих мешканців вашого міста.
# Якщо було вказано шлях 127.0.0.1:8000/history/photos, має відображатися розділ з історичними фотографіями вашого міста.



from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/news')
def news():
    return render_template('news.html')

@app.route('/mayor')
def mayor():
    return render_template('mayor.html')

@app.route('/facts')
def facts():
    return render_template('facts.html')

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/history/people')
def history_people():
    return render_template('history_people.html')

@app.route('/history/photos')
def history_photos():
    return render_template('history_photos.html')

@app.route('/contacts')
def contacts():
    return render_template('contacts.html')




# Завдання 2
# Додайте до проєкту з першого завдання можливість обробки неправильних адрес.
# Наприклад, при зазначенні 127.0.0.1:8000/news/satisfaction або 127.0.0.1:8000/news/angie, або 127.0.0.1: 8000/news/wildhorses і т.д.,
# має відображатися вміст розділу News. Той же принцип застосуйте і до інших розділів.



@app.route('/<path:path>')
def wrong_path(path):
    if path.startswith('news'):
        return redirect(url_for('news'))

    elif path.startswith('mayor'):
        return redirect(url_for('mayor'))

    elif path.startswith('facts'):
        return redirect(url_for('facts'))

    elif path.startswith('history/photos'):
        return redirect(url_for('history_photos'))

    elif path.startswith('history/people'):
        return redirect(url_for('history_people'))

    elif path.startswith('history'):
        return redirect(url_for('history'))

    elif path.startswith('contacts'):
        return redirect(url_for('contacts'))

    else:
        return redirect(url_for('index'))





if __name__ == "__main__":
    app.run(debug=True)
