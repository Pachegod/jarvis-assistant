"""
Voice command for CLI.
"""

import click


@click.command()
@click.option('--record', is_flag=True, help='Record audio from microphone')
@click.argument('audio_file', required=False)
def voice_cmd(record, audio_file):
    """Handle voice input and output."""
    if record:
        click.echo("Recording audio...")
        # Implementation
    elif audio_file:
        click.echo(f"Processing: {audio_file}")
        # Implementation
    else:
        click.echo("Use --record to record or provide audio file")
