
import asyncio
import time

async def brewing(name):
    print(f"brewing {name } tea .....")
    await asyncio.sleep(3)
    #time.sleep(3)
    print(f"{name} is ready")


async def main():

    await asyncio.gather(
        brewing("masala tea"),
        brewing("green tea"),
        brewing("ginger tea"),
       
    )


print("hello")
asyncio.run(main())    
