import asyncio

from app.tools.pet_tools import get_pet


async def main():
    result = await get_pet.ainvoke({"pet_id": 1})
    print(result)


if __name__ == "__main__":
    asyncio.run(main())