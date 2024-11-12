import requests

response = requests.get('https://jsonplaceholder.typicode.com/posts')
if response.status_code == 200:
    data = response.json()
    print("Полученные данные:")
    print(data[:5])
else:
    print("Ошибка при получении данных:", response.status_code)
    import pandas as pd


    data = pd.read_csv('data.csv')

    
    print("Первые 5 строк данных:")
    print(data.head())


    print("\nСтатистика по числовым столбцам:")
    print(data.describe())


    grouped = data.groupby('category')['value'].sum()
    print("\nСумма значений по категориям:")
    print(grouped)
    import matplotlib.pyplot as plt


    categories = ['A', 'B', 'C', 'D']
    values = [3, 7, 2, 5]


    plt.bar(categories, values, color='blue')
    plt.title('Пример столбчатой диаграммы')
    plt.xlabel('Категории')
    plt.ylabel('Значения')
    plt.show()


    plt.plot(categories, values, marker='o', color='red')
    plt.title('Пример линейного графика')
    plt.xlabel('Категории')
    plt.ylabel('Значения')
    plt.grid(True)
    plt.show()