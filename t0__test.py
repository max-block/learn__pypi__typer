import typer

__version__ = "0.1.2"


def version_callback(value: bool):
    if value:
        typer.echo(f"v{__version__}")
        raise typer.Exit()


app = typer.Typer(add_completion=False)


@app.command()
def hello(name: str):
    typer.echo(f"Hello {name}")


@app.command()
def goodbye(name: str, formal: bool = False):
    if formal:
        typer.echo(f"Goodbye Ms. {name}. Have a good day.")
    else:
        typer.echo(f"Bye {name}!")


@app.callback()
def main(
    _version: bool = typer.Option(
        None,
        "--version",
        callback=version_callback,
        is_eager=True,
    ),
):
    pass


if __name__ == "__main__":
    app()
