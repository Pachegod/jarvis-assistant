"""
Sync command for CLI.
"""

import click


@click.command()
@click.option('--service', type=click.Choice(['all', 'gmail', 'calendar', 'slack']), default='all')
def sync_cmd(service):
    """Sync data with external services."""
    click.echo(f"Syncing {service}...")
    # Implementation
