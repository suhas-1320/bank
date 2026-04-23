import asyncio
import time
async def create_clock():
    while True:
        print(f"Current time: {time.strftime('%H:%M:%S')}")
        await asyncio.sleep(1)

if __name__ == "__main__":
    asyncio.run(create_clock())