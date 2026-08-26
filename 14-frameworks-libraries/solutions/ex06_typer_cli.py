import typer

app = typer.Typer()

_TODOS: list[dict[str, object]] = []


def reset_todos() -> None:
    _TODOS.clear()


@app.command()
def add(text: str, priority: int = typer.Option(1, "--priority")) -> None:
    _TODOS.append({"text": text, "priority": priority, "done": False})
    typer.echo(f"Added: {text}")


@app.command(name="list")
def list_todos(
    show_all: bool = typer.Option(False, "--all"),
    show_done: bool = typer.Option(False, "--done"),
) -> None:
    if show_all:
        todos = _TODOS
    elif show_done:
        todos = [todo for todo in _TODOS if todo["done"]]
    else:
        todos = [todo for todo in _TODOS if not todo["done"]]

    for todo in todos:
        mark = "x" if todo["done"] else " "
        typer.echo(f"[{mark}] {todo['text']}")
