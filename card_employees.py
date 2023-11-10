data = {
    'Администрация': [
        {'employee_id': 'Yaroslavov', 'img': 'blue_logo.png', 'name': 'Ярославов А.А.', 'dolzh': 'зав. кафедры',
         'sci_step': 'член корр. РАН',
         'sci_zvan': 'профессор', 'phone': '+7(495)939-55-83', 'email': 'yaroslav@belozersky.msu.ru'},
        {'employee_id': 'jyrnoff','img': 'blue_logo.png', 'name': 'Жирнов А.Е.', 'dolzh': 'зам. декана химфака', 'sci_step': 'к.х.н.',
         'sci_zvan': 'доцент', 'phone': '+7(495)939-33-61', 'email': 'jy@vms.chem.msu.ru'},
        {'employee_id': 'chernikova_elena', 'img': 'blue_logo.png', 'name': 'Черникова Е.В.', 'dolzh': 'зам. зав. кафедры', 'sci_step': 'д.х.н.',
         'sci_zvan': 'профессор РАН', 'phone': '+7(495)939-54-06', 'email': 'chernikova_elena@mail.ru'},
    ],
    'Лаборатория полиэлектролитов и биополимеров': [
        {'employee_id':'Sergeyev','img': 'blue_logo.png', 'name': 'Сергеев В.Г.', 'dolzh': 'зав. лаборатори', 'sci_step': 'д.х.н.',
         'sci_zvan': 'доцент', 'phone': '89299349039', 'email': 'хуй@mail.ru'},
        {'employee_id':'pyshkina','img': 'blue_logo.png', 'name': 'Пышкина О.А.', 'dolzh': 'с.н.с.', 'sci_step': 'к.х.н.',
         'sci_zvan': '', 'phone': '89299349039', 'email': 'хуй@mail.ru'},
        {'employee_id':'elit','img': 'blue_logo.png', 'name': 'Литманович Е.А.', 'dolzh': '', 'sci_step': 'к.х.н.',
         'sci_zvan': 'доцент', 'phone': '89299349039', 'email': 'хуй@mail.ru'}
    ], 'Лаборатория полимеризационных процессов': [
        {'img': 'blue_logo.png', 'name': 'Герасин В.А.', 'dolzh': 'зав. лаборатори', 'sci_step': 'к.х.н.',
         'sci_zvan': 'к.х.н.', 'phone': '89299349039', 'email': 'хуй@mail.ru'},
        {'img': 'blue_logo.png', 'name': 'Менделеев Д.И.', 'dolzh': 'Карточка 3', 'sci_step': 'к.х.н.',
         'sci_zvan': 'к.х.н.', 'phone': '89299349039', 'email': 'хуй@mail.ru'},
        {'img': 'blue_logo.png', 'name': 'Антипов Е.А.', 'dolzh': 'зам. декана ФФФХИ', 'sci_step': 'к.х.н.',
         'sci_zvan': 'д.х.н., профессор', 'phone': '89299349039', 'email': 'хуй@mail.ru'}
    ]
}
import sqlite3

def create_table(cursor, table_name):
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS {table_name} (
            id INTEGER PRIMARY KEY,
            employee_id TEXT,
            img TEXT,
            name TEXT,
            dolzh TEXT,
            sci_step TEXT,
            sci_zvan TEXT,
            phone TEXT,
            email TEXT
        )
    ''')

conn = sqlite3.connect('polymer_lab.db')
cursor = conn.cursor()

tables = [
    'Администрация',
    'Лаборатория_полимеризационных_процессов',
    'Лаборатория_полиэлектролитов_и_биополимеров',
    'Лаборатория_химических_превращений_полимеров',
    'Лаборатория_функциональных_полимеров_и_полимерных_материалов',
    'Лаборатория_структуры_полимеров',
    'Лаборатория_нанобиоструктур',
    'Лаборатория_функциональных_органических_и_гибридных_полимерных_систем'
]

for table in tables:
    create_table(cursor, table)

conn.commit()
conn.close()

print("Таблицы успешно созданы без данных.")

