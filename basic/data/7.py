from bs4 import BeautifulSoup
import asyncio
import aiohttp


async def fetch(session, url, i):
    print(i + 1)

    async with session.get(url) as response:
        html = await response.text()

        soup = BeautifulSoup(html, "html.parser")

        cont_thumb = soup.find_all("div", "cont_thumb")

        for cont in cont_thumb:
            title = cont.find("p", "txt_thumb")
            if title is not None:
                print(title.text)


async def main():

    BASE_URL = "https://bjpublic.tistory.com/category/전체%20출간%20도서"

    urls = [f"{BASE_URL}?page={i}" for i in range(1, 10)]

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.run(main())
