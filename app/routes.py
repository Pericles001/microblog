from app import app, request, render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username':'Joe'}
    return render_template('index.html', title='Home', user=user)
