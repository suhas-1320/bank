#create typer cli automation
import typer
app = typer.Typer()

@app.command()
def mysqlconfig(ipaddress : str, username : str, password : str,port:str):
    print(f"Configuring MySQL with IP Address: {ipaddress}, Username: {username}, Password: {password}, Port: {port}")


@app.command()
def accessapi(endpoint : str, method : str):
    print(f"Accessing API with Endpoint: {endpoint}, Method: {method}")

if __name__ == "__main__":
    app()