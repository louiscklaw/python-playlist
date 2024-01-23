from playwright.async_api import async_playwright

import asyncio
import nest_asyncio

async def main():

  async with async_playwright() as pw:
    browser = await pw.chromium.launch(headless=False)
    page = await browser.new_page()

    await page.goto("https://books.toscrape.com")

    await page.wait_for_timeout(1000)

    title_element = await page.query_selector("title")
    title_text = await title_element.inner_text()
    print(title_text)

    await browser.close()
nest_asyncio.apply()

asyncio.run(main())