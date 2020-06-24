
# Markdown Extension for Jinja2

Convert blocks of Markdown into HTML in a Jinja2 template!

## How to use

In a nutshell, simply import `MarkdownExtension` from this package and include it in the `extensions` kwarg upon initialization of your Jinja2 `Environment`. This will enable you to use `markdown` blocks in your templates, which will in turn be compiled to HTML!

Let's say you have a file called `test.j2` that looks like this:
```
{% markdown %}
{{ content }}
{% endmarkdown %}
```
Then, in the same working directory, executing the following code:
```
from jinja2 import FileSystemLoader, Environment
from md_jinja2 import MarkdownExtension

file_loader = FileSystemLoader("./")
env = Environment(loader=file_loader, extensions=[MarkdownExtension])
template = env.get_template("test.j2")
data = {
        "content" : "# Testing\n"
        "**1 2 3**\n"
        "\"One, two, three\"\n"
        "''\n"
        "```print(i)```\n"
        }
output = template.render(**data)

print(output)
```

would yield the following output:

```
<h1>Testing</h1>
<p><strong>1 2 3</strong>
"One, two, three"
''
<code>print(i)</code></p>
```
