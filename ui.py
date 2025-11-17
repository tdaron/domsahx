import dominate
from dominate.tags import *


# Base is the "main page" shared by all pages
# content is what will be in that page
def base(content, context):
    with dominate.document() as doc:
        with doc.head:
            script(src="https://cdn.jsdelivr.net/npm/htmx.org@2.0.8/dist/htmx.min.js")

        # Inside HTML body
        with doc:

            # Render whatever content is, providing it with context
            content(context)        

    return doc

# Renders a simple HTML list with every todo inside
def todos_list(todos, id):
    with ul(id=id) as t_list:
        for t in todos:
            li(t)
    return t_list


# Shows list of todos with a form to add one to the list
def index(context):
    todos = context["todos"]
    with div() as d:
        p("Welcome to this TODO app !")
        todos_list(todos, "tl")

        # This form has some HTMLX magic:
        #     hx-post="/add" means "hey when this form is submitted, make a post REQUEST to /add"
        #     hx-target="#tl" means "replace the #tl element (todo_list) by whatever the /add returns"
        #     (detail) hx-swap="outerHTML" tells htmx to replace the full #tl element and not only what's inside of #tl
        with form(data_hx_post="/add", data_hx_target="#tl", data_hx_swap="outerHTML"):
            input_(placeholder="New todo", name="todo")
            button("Add", type="submit")
