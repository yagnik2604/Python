
# import time
# import asyncio

# async def brewing():
#     print(f"tea is brewing........")
#     await asyncio.sleep(3)
#     print(f"tea is ready.......")

# print("hello1")
# asyncio.run(brewing())
# print("hello1")

import asyncio

async def say_hello():
    await asyncio.sleep(2)
    print("Hello")

async def main():
    await say_hello()  # waits, but non-blocking
    print("Done")

asyncio.run(main())
