import threading
import asyncio

@asyncio.coroutine
def hello():
    print('Hello world! (%s)' % threading.currentThread())
    yield from asyncio.sleep(1)
    print('Hello again! (%s)' % threading.currentThread())

# coroutine asyncio.sleep(delay, result=None, *, loop=None)
# Create a coroutine! that completes after a given time (in seconds). 
# If result is provided, it is produced to the caller when the coroutine completes.

# result = yield from coroutine – wait for another coroutine to produce a result 
# (or raise an exception, which will be propagated).

loop = asyncio.get_event_loop()
tasks = [hello(), hello()]
loop.run_until_complete(asyncio.wait(tasks))
loop.close()
