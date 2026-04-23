import asyncio
import aiohttp

from src.configurations.conf import config


# -------------------- SERVICES --------------------

async def user_service(base_url, user_id, session):
    url = f"{base_url}/users/{user_id}"
    print(url)

    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return {
                "id": data["id"],
                "name": data["name"],
                "email": data["email"]
            }
        print(f"User service failed. Status code: {response.status}")
        return None


async def post_service(base_url, post_id, session):
    url = f"{base_url}/posts/{post_id}"
    print(url)

    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return {
                "id": data["id"],
                "title": data["title"],
                "body": data["body"]
            }
        print(f"Post service failed. Status code: {response.status}")
        return None


async def album_service(base_url, album_id, session):
    url = f"{base_url}/albums/{album_id}"
    print(url)

    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return {
                "userId": data["userId"],
                "id": data["id"],
                "title": data["title"]
            }
        print(f"Album service failed. Status code: {response.status}")
        return None


async def photo_service(base_url, photo_id, session):
    url = f"{base_url}/photos/{photo_id}"
    print(url)

    async with session.get(url) as response:
        if response.status == 200:
            data = await response.json()
            return {
                "albumId": data["albumId"],
                "id": data["id"],
                "title": data["title"],
                "url": data["url"],
                "thumbnailUrl": data["thumbnailUrl"]
            }
        print(f"Photo service failed. Status code: {response.status}")
        return None


# -------------------- DASHBOARD --------------------

async def dashboard(base_url):
    async with aiohttp.ClientSession() as session:
        user, post, album, photo = await asyncio.gather(
            user_service(base_url, 1, session),
            post_service(base_url, 1, session),
            album_service(base_url, 1, session),
            photo_service(base_url, 1, session)
        )

        return {
            "user": user,
            "post": post,
            "album": album,
            "photo": photo
        }


# -------------------- MAIN --------------------

if __name__ == "__main__":
    conf = config()
    print("Base URL:", conf.url)

    try:
        result = asyncio.run(dashboard(conf.url))
        print("\n--- DASHBOARD DATA ---")
        print(result)

    except aiohttp.ClientError as e:
        print(f"HTTP error occurred: {e}")

    except Exception as e:
        print(f"Unexpected error occurred: {e}")