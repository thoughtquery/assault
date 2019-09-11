import click 

@click.command()
@click.option("--requests", "-r", default=500, help="Number of requests")
@click.option("--concurrency", "-c", default=1, help="Number of concurrency requests")
@click.option("--json-file", "-j", default=None, help="Path to JSON file")
@click.argument("url")
def cli(requests, concurrency, json_file, url):
    print(f"Requests: {requests}")
    print(f"Concurrenct: {concurrency}")
    print(f"JSON file: {json_file}")
    print(f"URL: {url}")
    pass


if __name__ == '__main__':
    cli()
