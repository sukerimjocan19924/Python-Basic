import os
import aiohttp
import asyncio
from config import get_secret
import aiofiles


async def img_downloader(session, img):
    # https://example.com/cat.jpg?type=w800
    img_name = img.split("/")[-1].split("?")[0]

    try:
        os.mkdir("./images")
    except FileExistsError:
        pass

    try:
        async with session.get(img) as response:
            if response.status == 200:
                async with aiofiles.open(f"./images/{img_name}", mode="wb") as file:
                    img_data = await response.read()
                    await file.write(img_data)
            else:
                print("이미지 다운로드 실패", response.status, img)
    except aiohttp.ClientError as e:
        print("이미지 요청 오류", img)
        print(e)


async def fetch(session, url, i):
    print(i + 1)
    headers = {
        "X-Naver-Client-Id": get_secret("NAVER_API_ID"),
        "X-Naver-Client-Secret": get_secret("NAVER_API_SECRET"),
    }
    async with session.get(url, headers=headers) as response:
        result = await response.json()

        items = result["items"]

        images = [item["link"] for item in items]

        await asyncio.gather(*[img_downloader(session, img) for img in images])


async def main():
    BASE_URL = "https://openapi.naver.com/v1/search/image"

    keyword = "Gat"

    urls = [f"{BASE_URL}?query={keyword}&display=20&start={1+i*20}" for i in range(10)]

    async with aiohttp.ClientSession() as session:
        await asyncio.gather(*[fetch(session, url, i) for i, url in enumerate(urls)])


if __name__ == "__main__":
    asyncio.run(main())
