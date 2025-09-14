import asyncio
import time 

async def process1():
    print("P1 - First Step")
    # don't use time because the processes will freeze
    # Could be an api call here, i.e comeback when its done
    await asyncio.sleep(6)
    completed = await process2()
    print("P1 - Second Step")
    print(f"Process 2 result : {completed}")

async def process2():
    print("P2 - First Step")
    # don't use time because the processes will freeze
    # Could be an api call here, i.e comeback when its done
    await asyncio.sleep(6)
    print("P2 - Second Step")

    return "Process 2 completed"


def main():
    asyncio.run(process1())

if __name__ == '__main__':
    main()