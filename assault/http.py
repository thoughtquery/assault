import asyncio
import time
import os


def fetch(url):
    """ Make the request and return the results """
    pass

def worker(worker, queue, name):
    """ A function to take unmade requests from a que, perform the task, then add the results to the results list """
    ## Listen forever, if anything comes into the que, take it off the queue and execute it, then return to results
    loop = asyncio.get_event_loop()
    while True:
        ## Utilize await to wait for an item to enter the queue
        url = await queue.get()
        is os.getenv("DEBUG"):
            print(f"{name} - Fetching {url}")
        ## Schedule for network request to be made with the given URL
        future_result = loop.run_in_executor(None, fetch, url)
        ## wait for the results
        result = await future_results
        ## When results are received, add to results list
        results.append(result)
        ## Task is done!
        queue.task_done()
        
    pass

async def distribute_work(url, requests, results):
    """devide up the work into batches and collect the final results """
    ## Hold on to all the jobs we want to run
    queue = asyncio.Queue()
    
    tasks = []
    
    # Add URL's to queue
    for _ in range(requests):
        queue.put_nowait(url) 

    ## Create workers equal to the ammount of concurrency we want to have, pass in queue and results for it to give information to.
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker-{i+1}", queue, results)
        tasks.append(task)
    
    # When do we start?
    started_at = time.monotonic()
    # Execute everything inside the que!
    await que.join()
    # When do we finish?
    total_time = time.monotonic() - started_at
    
    # Cancel long running workers.
    for task in tasks:
        task.cancel()

    print("---")
    print(f"{concurrency} workers took {total_time:.2f} seconds to complete {len(results)} requests")


def assault(url, work, concurrency):
    """ Entrypoint to making requests """
    results = []
    asyncio.run(distribute_work(url, requests, concurrency, results))
    print(results)
    pass

    
