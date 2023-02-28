import psycopg2

### Create connections
connect1 = psycopg2.connect(
    dbname='postgres',
    host='localhost',
    port=5432,
    password='postgres',
    user='postgres'
)


def achiv():
    pass


def set_properties(animal_name, animal_type, animal_color, age, sex,
                   health, hunger, craving, mood, vivacity, cleanliness,
                   upbringing):     # Функция для внесения изменений в характеристики
                                    # Тамагочи
    cursor1 = connect1.cursor()
    cursor1.execute(
        f"INSERT INTO achivs(animal_name, animal_type, animal_color, age, sex,"
        f"health, hunger, craving, mood, vivacity, cleanliness,"
        f"upbringing) VALUES"
        f"('{animal_name}', '{animal_type}', '{animal_color}', '{age}',"
        f"'{sex}', '{health}', '{hunger}', '{craving}', '{mood}', '{vivacity}',"
        f"'{cleanliness}', '{upbringing}')"
    )


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
