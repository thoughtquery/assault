import click 
from .requester import assault

@click.command()
@click.option("--request_count", "-r", default=500, help="Number of requests")
@click.option("--concurrency", "-c", default=1, help="Number of concurrency requests")
@click.option("--json-file", "-j", default=None, help="Path to JSON file")
@click.argument("url")
def cli(request_count, concurrency, json_file, url):
    print(f"Request_Count: {request_count}")
    print(f"Concurrenct: {concurrency}")
    print(f"JSON file: {json_file}")
    print(f"URL: {url}")
    assault(url, request_count, concurrency)

if __name__ == '__main__':
    cli()
