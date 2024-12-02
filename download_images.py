"""
下载网页中的所有图片

该脚本通过异步HTTP请求下载指定网页中所有图片，并将这些图片保存在本地指定的文件夹中。

主要功能：
1. 从指定的URL获取网页内容。
2. 解析HTML文档，提取所有图片的URL。
3. 异步下载每个图片，并根据其URL生成文件名保存到本地指定文件夹。
4. 处理并报告下载过程中的任何HTTP错误或其他异常，确保程序的健壮性。

使用方法：
- 修改脚本中的 `url` 变量，指定需要下载图片的网页地址。
- 修改 `download_folder` 变量，指定想要保存图片的本地文件夹名称。
- 运行脚本即可下载网页中的所有图片。

依赖库：
- httpx：用于异步HTTP请求
- lxml：用于解析HTML
"""

import os
import httpx
from lxml import html
from urllib.parse import urljoin

async def download_images(url, download_folder):
    try:
        # 创建下载文件夹
        os.makedirs(download_folder, exist_ok=True)
        
        async with httpx.AsyncClient() as client:
            # 发送HTTP请求
            response = await client.get(url)
            response.raise_for_status()

            # 解析HTML内容
            tree = html.fromstring(response.content)
            # 找到所有图片标签
            img_urls = tree.xpath('//img/@src')

            # 异步下载图片
            async def fetch_and_save(img_url):
                try:
                    img_url = urljoin(url, img_url)
                    img_response = await client.get(img_url)
                    img_response.raise_for_status()

                    img_name = os.path.join(download_folder, os.path.basename(img_url))
                    with open(img_name, 'wb') as img_file:
                        img_file.write(img_response.content)
                    
                    print(f'Downloaded {img_name}')
                except httpx.HTTPStatusError as e:
                    print(f'Error downloading {img_url}: {e.response.status_code}')
                except httpx.NetworkError as e:
                    print(f'Network error occurred while downloading {img_url}: {e}')
                except Exception as e:
                    print(f'An error occurred while downloading {img_url}: {e}')

            await asyncio.gather(*(fetch_and_save(img_url) for img_url in img_urls))

    except httpx.HTTPStatusError as e:
        print(f'HTTP error occurred: {e.response.status_code}')
    except httpx.NetworkError as e:
        print(f'Network error occurred: {e}')
    except Exception as e:
        print(f'An error occurred: {e}')

if __name__ == "__main__":
    import asyncio
    url = 'https://finasia-group.com/epam/grand-opening-product-launch/'  # 替换为你想要下载图片的网址
    download_folder = 'epam/grand-opening-product-launch/'  # 替换为你想要保存图片的文件夹名称
    asyncio.run(download_images(url, download_folder))
