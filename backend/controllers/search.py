import aiobungie
import os
from dotenv import load_dotenv

load_dotenv()
client_id = os.getenv('CLIENT_ID')
client = aiobungie.Client(client_id)

async def query() -> None:
    # Search for Destiny 2 players.
    async with client.rest:
        users = await client.search_users("HeroSyndicate")
        for user in users:
            # Print all Destiny 2 memberships for this user.
            print(user.memberships)


# You can either run it using the client or just asyncio.run(main())

client.run(query())