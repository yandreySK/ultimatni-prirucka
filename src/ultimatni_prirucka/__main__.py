"""Command-line interface."""
import click


@click.command()
@click.version_option()
def main() -> None:
    """Ultimatni Prirucka."""


if __name__ == "__main__":
    main(prog_name="ultimatni-prirucka")  # pragma: no cover
