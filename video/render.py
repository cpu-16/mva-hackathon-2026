import asyncio, sys
from playwright.async_api import async_playwright

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        pg = await b.new_page(viewport={"width":1920,"height":1080}, device_scale_factor=1)
        await pg.goto(f"file:///home/gar16/datos/HACKATHON-MVA-2026/video/slides.html")
        await pg.wait_for_timeout(700)
        n = await pg.locator("section.slide").count()
        for i in range(n):
            await pg.locator("section.slide").nth(i).screenshot(path=f"slide{i+1:02d}.png")
        print(f"{n} slides renderizadas")
        await b.close()

asyncio.run(main())
