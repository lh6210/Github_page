title: How do I build my blog   
date: 2021-11-08   
category: tech 
keywords: Latex-to-HTML rendering, Flask, Flask-FlatPages


This blog is built upon _Flask_ and _Flask-Flatpages_ and posted on Github Page.
What's fun about the building experience is a list of things:  
1) relearn Python and learn microframework Flask;   
2) learn to write blogs in Markdown language;    
3) mix Jinja2, Python, CSS (Bootstrap), and Javascript in HTML templates;    
4) search for desirable extensions for specific functions (eg. code highlight, Markdown to HTML conversion, Latex to HTML conversion, etc);   
5) get to know MathJax for Latex rendering in web pages;     
6) lots of space to improve in the future (webpage design, integrate database for searching, comment section, etc)


Along the way of building this blog, I have met with several challenging but interesting technical issues. I will try to describe them below.

###### Issue 1: Latex-to-HTML rendering
One of the main technical issues that I have encountered was how to render Latex syntax in markdown files under my Flask backend.
By default, Flask-FlatPages renders flatpage body using Markdown with Pygments format ([according to FlatPages Doc](https://flask-flatpages.readthedocs.io/en/latest/#module-flask_flatpages)).
However, for Math/Latex users the default rendering process might not work as desired. The problems are usually due to the conflicts between different meanings of `_` and `*` in Latex and Markdown. A common workaround is to tweak the Latex syntax inside Latex delimiters, which brings more or less hassles into the blog writings. For example, what I have experienced was that: inside a math block encircled by `$$`, instead of typing `_` for subscript, I have to type `\_`; instead of typing `*` for multiplication, I have to type `\*`; instead of typing `\\` for linebreak, I have to type `\\\\`.

Fortunately, Flask-Flatpage gives users the flexibiltiy to specify the render engine as well as self-define the rendering function. I ended up using [Python-Markdown](https://python-markdown.github.io/) along with [Arithmatex](https://facelessuser.github.io/pymdown-extensions/extensions/arithmatex/) for the rendering part. This combination allows me to write pure Latex inside most of math environments. One caveat that I have found lies in inline math environments. Instead of `$ Latex expressions $`, I would have to type `$\(  Latex expressions \)$` so that MathJax recognizes the math expressions and renders them seamlessly on the webpages. Other than that, everything is fine so far.  

Besides the rendering engine that I am using, I just want to mention that [Pandoc](https://pandoc.org/index.html) is another good candidate. There is a technical issue as of how to integrate Pandoc into Python and Flask framework though. Regarding its powerful features, the effort should be worthwhile.

The steps that I have taken for Latex-to-HTML rendering:   
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
4. configure MathJax in HTML templates' head section [optional] 
    ```js 
    <script> 
    window.MathJax = {
      tex: {
        inlineMath: [['$', '$'],['\\(', '\\)']],
        displayMath: [['$$', '$$'], ['\\[', '\\]']],
        processEscapes: true,
        processEnvironments: true
      },
      options: {
        processHtmlClass: "arithmatex"
      }
    };
    </script>
    ```

###### Issue 2: group pages under the same category in the index page
Right now in my home page there is only one category - Linear Algebra and there's only one article below it. But imagine that later I might add another category - Calculus into this page. The way I want my home page functions is that once Flask-Flatpages fetches all of my Markdown posts in the backend, a certain component would sort these posts by their category set in the YAML heading and list them under their category automatically.   

In another word, I don't need to edit my index page anymore whenever I add a new post. The component that magically does the job is several lines of Javascript code below:  

``` html
    <div class="container-fluid la">
        <p>
        <h4>Linear Algebra </h4> 
        <small> -- in reference to 'Introduction to Linear Algebra' written by Prof. Gilbert Strang</small> 
        </p>
    </div>

    {% for page in pages %}
        {% if page.category == 'la' %}
            <script>
                var newItem = $("<div></div>", {
                    "class": "la-item"})
                $(" <a href={{url_for('page', page.path)}}>  &#9834 {{ page.title}}</a> <br>").appendTo(newItem)
                $("<small> &nbsp; &nbsp; &#128197Published on {{page.date.strftime('%B %d, %Y')}} </small>").appendTo(newItem)  
                $("<small> &#9749Keywords: {{page.keywords}} </small> <br>").appendTo(newItem) 
                $(".la").append(newItem)
            </script>
            
        {% endif %}
    {% endfor %}
```

My home page consists of one or more categories (such as Linear Algebra, Calculus, etc). Each category takes up one Bootstrap-styled container. Inside each container, the name of the category and a brief description are placed at the top wrapped by <p> tags. Contents following them are entries of articles of this category.

The for loop inside the Jinja2 tags will search through all of my posts, whenever it finds out some post belonging to _la_ (self-defined code for Linear Algebra) category, it will put it under _la_ category by running Javascript/JQuery commands.  
In fact, I was pretty amazed at mixing several languages (CSS, Jinja2, and Javascript) in HTML files to achieve the functionality. 

Above all, the automatic sorting and DOM manipulation ease writer's effort to manage the layout. Thanks for your reading.
