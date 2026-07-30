import asyncio

from app.tools.visit_tools import get_pet_visits


async def main():
    result = await get_pet_visits.ainvoke({"pet_id": 1})
    print(result)


if __name__ == "__main__":
    asyncio.run(main())