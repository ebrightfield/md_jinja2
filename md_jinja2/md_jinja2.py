

from jinja2 import Environment, FileSystemLoader, nodes
from jinja2.ext import Extension

from markdown import markdown

class MarkdownExtension(Extension):
    """
    Add to the `extensions` kwarg when constructing a
    jinja2.Environment.
    """
    tags = {"markdown"}  # Add "markdown" to things jinja2 knows

    def __init__(self, environment):
        super().__init__(environment)


    def parse(self, parser):
        """
        Grab data inside `markdown` block, pass to a
        nodes.CallBlock along with the callback that actually
        runs the markdown conversion on the body.
        """
        lineno = next(parser.stream).lineno

        body = parser.parse_statements(["name:endmarkdown"], drop_needle=True)

        # Very cryptic argument signature, consult jinja2 docs
        return nodes.CallBlock(
            self.call_method("_md_exec", []), [], [], body
                ).set_lineno(lineno)

    def _md_exec(self, caller):
        """Helper callback."""
        tempString = caller()
        return markdown(tempString)


if __name__ == "__main__":
    # Test run
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
    with open("test.html", "w") as f:
        f.write(output)
