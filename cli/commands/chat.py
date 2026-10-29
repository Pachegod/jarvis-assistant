"""
Chat command for CLI.
"""

import click


@click.command()
@click.option('--interactive', is_flag=True, help='Start interactive chat')
@click.argument('message', required=False)
def chat_cmd(interactive, message):
    """Send a chat message or start interactive chat."""
    if interactive:
        click.echo("Starting interactive chat...")
        # Implementation
    elif message:
        click.echo(f"Sending: {message}")
        # Implementation
    else:
        click.echo("Use --interactive for chat or provide a message")
