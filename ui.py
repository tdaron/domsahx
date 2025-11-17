import dominate
from dominate.tags import *


# Base is the "main page" shared by all pages
# content is what will be in that page
def base(content, context):
    with dominate.document() as doc:
        with doc.head:
            script(src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.8/dist/htmx.min.js")

        with doc:
            content(context)        

    return doc


def todos_list(todos, id):
    with ul(id=id) as t_list:
        for t in todos:
            li(t)
    return t_list

def index(context):
    todos = context["todos"]
    with div() as d:
        p("Welcome to this TODO app !")
        todos_list(todos, "tl")

        with form(data_hx_post="/add", data_hx_target="#tl", data_hx_swap="outerHTML"):
            input_(placeholder="New todo", name="todo")
            button("Add", type="submit")
