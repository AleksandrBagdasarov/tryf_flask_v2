from mysite import app
from mysite.views import *

app.add_url_rule('/', view_func=home)
app.add_url_rule('/about', view_func=about, methods=['GET',])
app.add_url_rule('/register', view_func=register, methods=['GET', 'POST'])
