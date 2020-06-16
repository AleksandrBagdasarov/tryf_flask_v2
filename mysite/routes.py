from flask_login import login_required

from mysite import app
from mysite.views import about, account, cart, confirm, home, login, logout, product, profile, register

app.add_url_rule('/',         view_func=home,                    methods=['GET',])
app.add_url_rule('/about',    view_func=about,                   methods=['GET',])
app.add_url_rule('/account',  view_func=login_required(account), methods=['GET', 'POST'])
app.add_url_rule('/cart',     view_func=cart,                    methods=['GET', 'POST'])
app.add_url_rule('/confirm',  view_func=confirm,                 methods=['GET', 'POST'])
app.add_url_rule('/login',    view_func=login,                   methods=['GET', 'POST'])
app.add_url_rule('/product',  view_func=product,                 methods=['GET', 'POST'])
app.add_url_rule('/profile',  view_func=profile,                 methods=['GET', 'POST'])
app.add_url_rule('/logout',   view_func=login_required(logout))
app.add_url_rule('/register', view_func=register,                methods=['GET', 'POST'])
