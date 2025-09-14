import asyncio
import time 

async def process1():
    print("P1 - First Step")
    # don't use time because the processes will freeze
    # Could be an api call here, i.e comeback when its done
    await asyncio.sleep(6)
    print("P1 - Second Step")

async def process2():
    print("P2 - First Step")
    # don't use time because the processes will freeze
    # Could be an api call here, i.e comeback when its done
    await asyncio.sleep(6)
    print("P2 - Second Step")


async def main():
    # If process 1 is in await mode, move on to process 2.
    tasks = await asyncio.gather(process1(), process2())

if __name__ == '__main__':
    asyncio.run(main())