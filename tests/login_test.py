import asyncio
from msmcauthaio import MsMcAuth

async def main():
    client = MsMcAuth()
    print(await client.login("your-email-here", "your-password-here"))

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())