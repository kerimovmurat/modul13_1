import asyncio

async def start_strongman(name, power): # Функция имитации соревнований силача
    print(f'Силач {name} начал соревнования.')
    for i in range(1, 6): # 5 шаров
        await asyncio.sleep(1 / power) # Задержка обратно пропорционально силе
        print(f'Силач {name} поднял {i}')
    print(f'Силач {name} закончил соревнования.')

async def start_tournament():
    # Создаем 3 задачи для участников
    task1 = asyncio.create_task(start_strongman("Иван", 2))
    task2 = asyncio.create_task(start_strongman("Пётр", 3))
    task3 = asyncio.create_task(start_strongman("Алексей", 1))

    # Ожидаем завершения задач
    await task1
    await task2
    await task3
if __name__ == "__main__":
    asyncio.run(start_tournament())
