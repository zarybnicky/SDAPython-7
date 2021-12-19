import asyncio
import queue
import sys


async def ainput(prompt):
    print(prompt)
    return await asyncio.get_event_loop().run_in_executor(None, sys.stdin.readline)


QUEUE = queue.Queue()


async def queuing():
    while True:
        await asyncio.sleep(.1)
        line = await ainput("Q: How many customers are coming in?")
        line = line.strip()
        if line:
            for _ in range(int(line)):
                QUEUE.put(1)
        print("Q: Done, %s customers queuing" % QUEUE.qsize())


async def cashier():
    while True:
        try:
            QUEUE.get_nowait()
            print("C: Ding! %s remaining" % QUEUE.qsize())
        except queue.Empty:
            print("C: Cashier is bored...")
        await asyncio.sleep(1)


if __name__ == '__main__':
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(asyncio.gather(queuing(), cashier()))
