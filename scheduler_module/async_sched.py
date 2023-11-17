import asyncio
import datetime as dt

from scheduler.asyncio import Scheduler


async def foo():
    print("foo")


async def main():
    loop = asyncio.get_running_loop()
    schedule = Scheduler(loop=loop)

    schedule.once(dt.timedelta(seconds=5), foo)
    schedule.once(dt.timedelta(seconds=6), foo)
    schedule.once(dt.timedelta(seconds=7), foo)
    schedule.cyclic(dt.timedelta(minutes=10), foo)

    while True:
        await asyncio.sleep(1)

asyncio.run(main())
