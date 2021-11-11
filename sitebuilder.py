
import sys 
from datetime import datetime

from flask import Flask, render_template, url_for, render_template_string
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask_flatpages_pandoc import FlatPagesPandoc
import markdown
import mkdcomments
import pymdownx.arithmatex as arithmatex

#FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
DEBUG = True
# attr_list: heading anchor
# pymdownx.arithmatex: latex
# tables: table

# configs = {
#     "pymdownx.arithmatex": {
#         "block_syntax" : ['dollar', 'square'],
#         "inline_syntax": ['dollar', 'round', 'begin']
#     }
# }

# extension_configs=configs

comments = mkdcomments.CommentsExtension()

extension_config = {
    "pymdownx.inlinehilite": {
        "custom_inline": [
            {"name": "math1", "class": "highlight", "format": arithmatex.arithmatex_inline_format(which="generic")}
        ]
    },
    "pymdownx.superfences": {
            "custom_fences": [
                {"name": "math2", "class": "highlight", "format": arithmatex.arithmatex_fenced_format(which="generic")}
            ]
    }
}

# extended_pygments_lang = [
#     {"name": "tex", "lang": "tex", "options": ""},
#     {"name": "python", "lang": "python", "options": ""}
# ]

md = markdown.Markdown(extensions=['tables', 'attr_list', 'pymdownx.highlight', 'pymdownx.inlinehilite', 'pymdownx.arithmatex', comments, 'pymdownx.superfences'], extension_configs=extension_config)

def my_renderer(text):
    return md.convert(text)

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
