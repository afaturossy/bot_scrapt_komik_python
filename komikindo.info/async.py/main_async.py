import asyncio
import http
import httpx

async def get(session,value):
    while True:
        try:
            r = await session.get("https://mail.ex-school.com/artikel/cara-mudah-mendaftarkan-situs-website-ke-google-di-tahun-2020")

            print(f'{value} ststus {r.status_code}')
            return value
        #     break
        except:
            return "gagal"
            await asyncio.sleep(5)

async def main():
    task = []
    async with httpx.AsyncClient() as client:
        for i in range(1000):
            task.append(get(client,i))
        
        r  = await asyncio.gather(* task)
        # a = await task[0]
        print(r)

if __name__ == '__main__':
    asyncio.run(main())