from app import app, request, render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Joe'}
    posts = [
        {
        'author': {'username': 'John'},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Avengers movie was so cool!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)
