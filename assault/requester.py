import asyncio
import time
import os
import requests

## Requests is not really made to work with asyncio

def fetch(url):
    """ Make the request and return the results """
    ## Synchronous code
    started_at = time.monotonic()
    response = requests.get(url)
    request_time = time.monotonic() - started_at 
    return {"status code": response.status_code, "request time": request_time} 

async def worker(name, queue, results):
    """ A function to take unmade requests from a que, perform the task, then add the results to the results list """
    ## Listen forever, if anything comes into the que, take it off the queue and execute it, then return to results
    loop = asyncio.get_event_loop()
    while True:
        ## Utilize await to wait for an item to enter the queue
        url = await queue.get()
        
        if os.getenv("DEBUG"):
            print(f"{name} - Fetching {url}")

        ## Schedule for network request to be made with the given URL
        future_result = loop.run_in_executor(None, fetch, url)
        
        ## wait for the results
        result = await future_result
        
        ## When results are received, add to results list
        results.append(result)
        
        ## Task is done! Mark complete and remove from the queue
        queue.task_done()
        

async def distribute_work(url, request_count, concurrency, results):
    """devide up the work into batches and collect the final results """
    ## Hold on to all the jobs we want to run
    queue = asyncio.Queue()
    
    
    # Add URL's to queue
    for _ in range(request_count):
        queue.put_nowait(url) 

    ## Create workers equal to the ammount of concurrency we want to have, pass in queue and results for it to give information to.
    tasks = []
    for i in range(concurrency):
        task = asyncio.create_task(worker(f"worker-{i+1}", queue, results))
        tasks.append(task)
    
    # When do we start?
    started_at = time.monotonic()
    # Execute everything inside the que!
    await queue.join()
    # When do we finish?
    total_time = time.monotonic() - started_at
    
    # Cancel long running workers.
    for task in tasks:
        task.cancel()

    print("---")
    print(f"{concurrency} workers took {total_time:.2f} seconds to complete {len(results)} requests")


def assault(url, request_count, concurrency):
    """ Entrypoint to making requests """
    results = []
    asyncio.run(distribute_work(url, request_count, concurrency, results))
    print(results)

    
