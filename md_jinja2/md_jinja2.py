

from jinja2 import Environment, FileSystemLoader, nodes
from jinja2.ext import Extension

from markdown import markdown

class MarkdownExtension(Extension):
    tags = {"markdown"}

    def __init__(self, environment):
        super().__init__(environment)


    def parse(self, parser):
        lineno = next(parser.stream).lineno

        body = parser.parse_statements(["name:endmarkdown"], drop_needle=True)
        #for output in body:
        #    for i in range(len(output.nodes)):
        #        output.nodes[i] = nodes.MarkSafe(output.nodes[i])

        return nodes.CallBlock(
            self.call_method("_md_exec", []), [], [], body
                ).set_lineno(lineno)

    def _md_exec(self, caller):
        """Helper callback."""
        tempString = caller()
        return markdown(tempString)


if __name__ == "__main__":
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
