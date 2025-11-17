from sanic import Sanic
from sanic.response import html
import ui

app = Sanic("TodoApp")

todos = ["Eat apples"]

def render(l):
    return html(l.render())

@app.get("/")
async def base(request):
    return render(ui.base(ui.index, {"todos": todos}))

@app.post("/add")
async def add(request):
    todos.append(request.form["todo"])
    return render(ui.todos_list(todos, "tl"))
