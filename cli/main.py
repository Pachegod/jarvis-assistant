"""
Jarvis Assistant CLI - Main entry point.
"""

import click
from commands.chat import chat_cmd
from commands.voice import voice_cmd
from commands.sync import sync_cmd
from commands.config import config_cmd


@click.group()
@click.version_option(version="1.0.0")
def cli():
    """Jarvis Assistant - Personal AI Assistant CLI"""
    pass


# Add command groups
cli.add_command(chat_cmd, name='chat')
cli.add_command(voice_cmd, name='voice')
cli.add_command(sync_cmd, name='sync')
cli.add_command(config_cmd, name='config')


if __name__ == '__main__':
    cli()
