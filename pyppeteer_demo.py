import asyncio
from pyppeteer import launch


async def main():
    browser = await launch()
    print(browser)
    page = await browser.newPage()
    await page.goto('http://seo.chinaz.com/www.ynu.edu.cn')
    element = await page.querySelector('#seo_BaiduSiteIndex > a > font')
    title = await page.evaluate('(element) => element.textContent', element)
    dimensions = await page.evaluate('''() => {
        return {
            width: document.documentElement.clientWidth,
            height: document.documentElement.clientHeight,
            deviceScaleFactor: window.devicePixelRatio,
        }
    }''')
    print(dimensions)
    await browser.close()

# asyncio.get_event_loop().create_task(main())
asyncio.get_event_loop().run_until_complete(main())
