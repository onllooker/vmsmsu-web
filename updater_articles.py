import pickle
import requests
from bs4 import BeautifulSoup
from modal_employees import employee_data

keys = employee_data.keys()
def find_elements_by_title(url):
    data = []
    try:
        response = requests.get(url)
        if response.status_code == 200:
            soup = BeautifulSoup(response.content, 'html.parser')
            # Поиск всех тегов <ul> с классом "activity"
            ul_elements = soup.find_all('ul', class_='activity')[:10]
            # Обход найденных элементов <ul>
            for ul_element in ul_elements:
                # Извлечение значения атрибута data-year
                data_year = ul_element.get('data-year')
                # Поиск и извлечение всех тегов <a> внутри текущего элемента <ul>
                a_element = ul_element.find_all('a')[0]
                a_element['href'] = 'https://istina.msu.ru'+a_element['href']
                data.append((f'<b class = article_yaer>{data_year+" "}</b>'+str(a_element)))

            return data
        else:
            print(f"Ошибка при получении содержимого. Код статуса: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при отправке запроса: {e}")
        return None

# Загружаем данные из файла (если файл уже существует)
try:
    with open("employees_modal.pkl", "rb") as input:
        data = pickle.load(input)
except FileNotFoundError:
    print('Нет файла или хуй знает что произошло')

# Обновляем словарь
for i in data.keys():
    links = find_elements_by_title(f'https://istina.msu.ru/profile/{i}/')
    data[i]['articles'] = links



# Сохраняем обновленные данные в файл
with open("employees_modal.pkl", "wb") as out:
    pickle.dump(data, out)