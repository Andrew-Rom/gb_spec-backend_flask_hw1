from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index/')
@app.route('/index.html/')
def index():
    context = {'page_name': 'Главная'}
    return render_template('index.html', **context)


@app.route('/shoes/')
@app.route('/shoes.html/')
def shoes():
    _shoes = [{'title':'Голубые кеды',
              'desc' : 'Модные голубые супер кеды',
              'img':'shoes_pic1.png',
              'alt' : 'кеды'},
             {'title': 'Оранжевые кеды',
              'desc': 'Модные оранжевые супер кеды',
              'img': 'shoes_pic2.png',
              'alt': 'кеды'},
             {'title': 'Синие кроссовки',
              'desc': 'Спортивные супер кроссовки',
              'img': 'shoes_pic3.png',
              'alt': 'кроссовки'}
             ]
    context = {'shoes': _shoes}
    return render_template('shoes.html', **context)


@app.route('/clothing/')
@app.route('/clothing.html/')
def clothing():
    _clothing = [{'title':'Футболка',
              'desc' : 'Черная футболка',
              'img':'clothing_pic1.jpg',
              'alt' : 'футболка'},
             {'title': 'Штаны',
              'desc': 'Какие-то штаны',
              'img': 'clothing_pic2.jpg',
              'alt': 'штаны'}
             ]
    context = {'clothing': _clothing}
    return render_template('clothing.html', **context)


@app.route('/jacket/')
@app.route('/jacket.html/')
def jacket():
    _jackets = [{'title':'Куртка',
              'desc' : 'Куртка мужская летняя',
              'img':'jacket_pic1.jpg',
              'alt' : 'куртка'}
             ]
    context = {'jackets': _jackets}
    return render_template('jacket.html', **context)


@app.route('/about/')
@app.route('/about.html/')
def about():
    context = {'page_name': 'О нас'}
    return render_template('about.html', **context)


@app.route('/contacts/')
@app.route('/contacts.html/')
def contacts():
    context = {'page_name': 'Контакты',
               'email': 'email@mail.com',
               'site': 'our_web_site.com',
               'location': 'Moscow, Russia'}
    return render_template('contacts.html', **context)


if __name__ == '__main__':
    app.run(debug=True)