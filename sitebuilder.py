
import sys 
from datetime import datetime

from flask import Flask, render_template, url_for, render_template_string
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask_flatpages_pandoc import FlatPagesPandoc
import markdown

#FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
DEBUG = True

def my_renderer(text):
    # prerendered_body = render_template_string(text)
    return markdown.markdown(text, extensions=['tables', 'mdx_math', 'attr_list', 'pymdownx.arithmatex'])

app = Flask(__name__)
app.config.from_object(__name__)
app.config['FLATPAGES_HTML_RENDERER'] = my_renderer

pages = FlatPages(app)
# FlatPagesPandoc("markdown", app, ["--mathjax"], pre_render=True)
freezer = Freezer(app)

@app.route('/')
def index():
    return render_template('index.html', pages=pages)

@app.route('/cal2')
def cc():
    return render_template('doubleintegral.html')


@app.route('/<path:path>.html')
def page(path):
    print('Page function running')
    page = pages.get_or_404(path)
    print(f'{page}')
    return render_template('page.html', page=page)

@freezer.register_generator
def pagelist():
    for page in pages:
        yield url_for('page', path=page.path)



if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == 'build':
        freezer.freeze()
    else:
        app.run(host='0.0.0.0', port= 5001)
