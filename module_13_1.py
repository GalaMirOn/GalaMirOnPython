import asyncio
import time


async def start_strongman(name, power):
    print(f'Силач {name} начал соревнования')
    for shar in range(1,6):
        await asyncio.sleep(1/power)
        print(f'Силач {name} поднял {shar} шар')
    print(f'Силач {name} закончил соревнования')

async def start_tournament():
    task1 = asyncio.create_task(start_strongman('Илья Муромец', 3))
    task2 = asyncio.create_task(start_strongman('Алёша Попович', 4))
    task3 = asyncio.create_task(start_strongman('Добрыня Никитич', 5))
    await task1
    await task2
    await task3
    print('Турнир окончен!')


asyncio.run(start_tournament())