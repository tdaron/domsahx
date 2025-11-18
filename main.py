from sanic import Sanic
from sanic.response import html
import ui

app = Sanic("TodoApp")

todos = ["Eat apples"]

def render(l):
    return html(l.render())

@app.get("/")
async def base(request):
    # Rendering index page with todos as context
    return render(ui.base(ui.index, {"todos": todos}))

@app.post("/add")
async def add(request):
    # Adding the user provided todo to the list
    todos.append(request.form["todo"][0])

    # Returning a new render of the list of the todos
    # Important: We only re-render the list of the todos, not the
    #            full index page.
    return render(ui.todos_list(todos, "tl"))

@app.post("/delete/")
async def delete(request):
    item = request.args.get("item")
    todos.remove(item)

    return render(ui.todos_list(todos, "tl"))
