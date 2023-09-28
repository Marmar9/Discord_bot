from yt_dlp import YoutubeDL
import asyncio
import time
url = 'https://www.youtube.com/watch?v=h_D3VFfhvs4&ab_channel=michaeljacksonVEVO'
youtubedl_options = {
    'format': 'bestaudio/best',
}
ydl = YoutubeDL(youtubedl_options)




async def run():
    loop = asyncio.get_event_loop()
    data = await loop.run_in_executor(None, lambda: ydl.extract_info(url, download=False))
    while True:
        print(data['url'])
        print('----------------------')
        time.sleep(1)

asyncio.run(run())