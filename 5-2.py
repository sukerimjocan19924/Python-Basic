import asyncio


async def job(name, delay):
    await asyncio.sleep(delay)

    return name


async def main():
    results = await asyncio.gather(job("A", 2), job("B", 1))
    print(results)


if __name__ == "__main__":
    asyncio.run(main())
