title: How do I build my blog   
date: 2021-11-08   
category: category 3


#### Issue 1: markdown files with Latex syntax were not rendered well   
Solution:  
By default, *Flask-FlatPages* renders flatpage body using Markdown with Pygments format([according to FlatPages](https://flask-flatpages.readthedocs.io/en/latest/#module-flask_flatpages)).

However, for Math/Latex users the default rendering process might not work as desired. The problems are usually due to the conflicts between different meanings of `_` and `*` in Latex and Markdown. A common workaround is to tweak the Latex syntax inside Latex delimiters, which brings more or less hassles into the blog writings. For example, what I have experienced was that: inside a math block encircled by `$$`, instead of typing `_` for subscript, I have to type `\_`; instead of typing `*` for multiplication, I have to type `\*`; instead of typing `\\` for linebreak, I have to type `\\\\`.

Fortunately, Flask-Flatpage gives users the flexibiltiy to specify the render engine as well as self-define the conversion function. I ended up using $Python-Markdown$ along with [Arithmatex](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/) as the rendering part. This combination allows me to write pure Latex inside math blocks and works well so far.

The steps that I have taken:   
1. install Python-Markdown and pymdown-extensions   
    ``` python
    pip install markdown
    pip install pymdown-extensions
    ```
2. include Arithmatex extension in Python Markdown's configuration  
    ``` python
    import markdown   
    md = markdown.Markdown(extensions=['pymdownx.arithmatex'])
    ```
3. define HTML renderer for Flask-FlatPages and update app configuration
    ``` python
    def my_renderer(text):
        return md.convert(text)
    
    app.config['FLATPAGES_HTML_RENDERER'] = my_renderer
    ```
```json
{
  "firstName": "John",
  "lastName": "Smith",
  "age": 25
}
```
    ``` python
    from sympy import *
    ```
    
More Markdown processors:  

| Name             | Language     | Output Formats   | Description                               |
| :------          | :-------     | ---------------- | ----------------------------------------- |
| Hoep             | Python       | (X)HTML          | A Python binding to Hoedown               |
| Python-Discount  | Python       | (X)HTML          | A Python binding to Discount              |
| Python-hoedown   | Python       | (X)HTML          | A Python binding to Hoedown               |
| Python-Markdown2 | Python       | (X)HTML          | A direct port of markdown.pl to Python    |
| Misaka           | Python 2 & 3 | (X)HTML          | A Python binding for Sundown              |
| Python-Markdown  | Python 2 & 3 | (X)HTML          | A Python implementation with extensions   |
| Mistune          | Python 2 & 3 | (X)HTML          | A Python port of Marked                   |

