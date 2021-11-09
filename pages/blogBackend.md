title: How do I build my blog   
date: 2021-11-08   
category: category 3


Issue 1: markdown files with Latex syntax were not rendered well   
Solution:  
By default, *Flask-FlatPages* renders flatpage body using Markdown with Pygments format. ([according to FlatPages](https://flask-flatpages.readthedocs.io/en/latest/#module-flask_flatpages)) 
My understanding is that Pygments is the default rendering engine that FlatPags works with to convert .md files into .html files. Pygments is well-known for its syntax highlighting and the broad coverage of programming and markup languages. It's worthwhile exploring [its website](https://pygments.org/) at reader's will.  

However, for Math/Latex users the default rendering process might not work as desired. The problems are usually due to the conflicts between different meanings of `_` and `*` in Latex and Markdown. A common workaround is to tweak the Latex syntax inside Latex delimiters, which brings more or less hassles into the blog writings. For example, what I have experienced was that: inside a math block encircled by `$$`, instead of typing `_` for subscript, I have to type `\_`; instead of typing `*` for multiplication, I have to type `\*`; instead of typing `\\` for linebreak, I have to type `\\\\`.

Fortunately, Flask-Flatpage gives users the flexibiltiy to specify the render engine as well as self-define the conversion function. Also, a render engine, $Python-Markdown$ along with [python-markdown-math](https://pypi.org/project/python-markdown-math/) and the suggested configuration, could convert Latex syntax in .md files smoothly into .html files.   

More Markdown processors:  
| Name             | Language         | Output Formats | Description                                | 
| -----------------| -----------------| -------------- | ---------------------------------------    |
| Hoep             | Python           | (X)HTML        | A Python binding to Hoedown                |
| Python-Discount  | Python           | (X)HTML        | A Python binding to Discount               |
| python-hoedown   | Python           | (X)HTML        | A Python binding to Hoedown                |
| Python-Markdown2 | Python           | (X)HTML        | A direct port of markdown.pl to Python     |
| Misaka           | Python 2&3       | (X)HTML        | A Python binding for Sundown               |
| Python-Markdown  | Python 2&3       | (X)HTML        | A Python implementation with extensions    |
| Mistune          | Python 2&3 &pypy | (X)HTML        | A Python port of Marked                    |


The steps that I have taken:   
1. install Python-Markdown and python-markdown-math   
2. configure python-markdown-math according to its recommendation   
    - include MathJax library in HTML files    
    - convert configuration for MathJax 2.x to the one for MathJax 3.x; [MathJax converter](https://mathjax.github.io/MathJax-demos-web/convert-configuration/convert-configuration.html)    
    - pass the extension [python-markdown-math] to Python-Markdown   
3. cc

