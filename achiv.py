import psycopg2

connect1 = psycopg2.connect(
    dbname='postgres',
    host='localhost',
    port=5432,
    user='postgres',
    password='postgres'
)


def set_select(animal_name):  # Функция выбора характеристик для шкал
    # Тамагочи
    cursor1 = connect1.cursor()
    cursor1.execute(
        f"SELECT animal_type, animal_color, age, is_male, "
        f"health, hunger, craving, mood, vivacity, cleanliness, "
        f"upbringing, is_sleep FROM achivs "
        f"WHERE animal_name = '{animal_name}'"
    )
    date_properties = cursor1.fetchall()
    # date_return = {}
    for i in date_properties:
        print(i)
        # date_return = {"animal_type": i[0], "animal_color": i[1], "}
    return date_properties


def set_update(animal_name, scale, new_value):  # Функция для внесения изменений в характеристики
    # Тамагочи
    cursor1 = connect1.cursor()
    cursor1.execute(
        f"UPDATE achivs "
        f"SET {scale} = {new_value} "
        f"WHERE animal_name = '{animal_name}'"
    )
    connect1.commit()
    cursor1.close()


def insert_properties(animal_name, animal_type, animal_color, age, is_male,
                      health, hunger, craving, mood, vivacity, cleanliness,
                      upbringing, is_sleep):  # Функция для внесения изменений в характеристики
    # Тамагочи
    cursor1 = connect1.cursor()
    cursor1.execute(
        f"INSERT INTO achivs(animal_name, animal_type, animal_color, age, is_male,"
        f"health, hunger, craving, mood, vivacity, cleanliness, "
        f"upbringing, is_sleep) VALUES "
        f"('{animal_name}', '{animal_type}', '{animal_color}', {age},"
        f"{is_male}, {health}, {hunger}, {craving}, {mood}, {vivacity},"
        f"{cleanliness}, {upbringing}, {is_sleep})"
    )
    connect1.commit()
    cursor1.close()

def healt100():  # Первое достижение 100% уровня жизни
    pass


def ages():  #
    pass


def hunger100():  # сытость 100%
    pass


def crawing100():  #
    pass


def jovial():  # Весельчак
    pass
