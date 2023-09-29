import asyncio
import time


async def some_async_function():
    while True:
        print("Async function is running...")
        await asyncio.sleep(1)

def main():
    loop = asyncio.get_event_loop()

    # Run the asyncio function indefinitely
    loop.create_task(some_async_function())

    loop.run_forever()
  

if __name__ == "__main__":
    main()
