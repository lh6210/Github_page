title: How do I build my blog   
date: 2021-11-08   
category: category 3


Issue 1: markdown files with Latex syntax were not rendered well   
Solution:  
By default, *Flask-FlatPages* renders flatpage body using Markdown with Pygments format.[according to FlatPages](https://flask-flatpages.readthedocs.io/en/latest/#module-flask_flatpages) 
My understanding is that Pygments is the default rendering engine that FlatPags works with to convert .md files into .html files. Pygments is well-known for its syntax highlighting and the broad coverage of programming and markup languages. It's worthwhile exploring [its website](https://pygments.org/) at reader's will.  

However, for Math/Latex users the default rendering process might not work as desired. The problems are usually due to the conflicts between different meanings of `_` and `*` in Latex and Markdown. A common workaround is to tweak the Latex syntax inside Latex delimiters, which brings more or less hassles into the blog writings.

The good news is that Flask-Flatpage gives users the flexibiltiy to specify the render engine as well as self-define the conversion function. Also, a render engine, $Python-Markdown$ with its extension $[Arithmatex](https://facelessuser.github.io/pymdown-extensions/)$, could convert Latex syntax in .md files smoothly into .html files.


