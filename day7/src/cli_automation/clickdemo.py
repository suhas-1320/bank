#create click cli automation
import click

@click.group()
def cli():
    pass

@cli.command()
@click.option('--ipaddress', prompt='network IP Address', help='The IP address of the network')
@click.option('--username', prompt='port', help='The port of the network')
@click.option('--password', prompt='username', help='The username of the network')
@click.option('--port', prompt='password', help='The password of the network')
def mysqlconfig(ipaddress, username, password, port):
    click.echo(f'configuring MySql with the following settings:')
    click.echo(f'IP Address: {ipaddress}')
    click.echo(f'Username: {username}')
    click.echo(f'Password: {password}')
    click.echo(f'Port: {port}')



@click.command()
@click.option('--endpoint', prompt='API Endpoint', help='The endpoint of the API')
@click.option('--method', prompt='HTTP Method', help='The HTTP method to use (e.g., GET, POST, PUT, DELETE)')
def accessapi(endpoint, method):
    click.echo(f'Accessing API with the following settings:')
    click.echo(f'Endpoint: {endpoint}')
    click.echo(f'Method: {method}')

cli.add_command(mysqlconfig)
cli.add_command(accessapi)

if __name__ == '__main__':
    cli()
