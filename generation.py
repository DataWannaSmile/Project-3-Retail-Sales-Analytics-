import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random
import time

# Инициализация Faker
fake = Faker('ru_RU')
Faker.seed(42)
np.random.seed(42)
random.seed(42)

# НАСТРОЙКИ ОБЪЕМА ДАННЫХ
n_products = 500
n_stores = 15
n_customers = 5000
n_sales = 25000
start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)


start_time = time.time()

# 1. Генерация таблицы продуктов
def generate_products(n):
    categories = {
        'Электроника': ['Смартфоны', 'Ноутбуки', 'Телевизоры', 'Наушники', 'Планшеты', 'Фотоаппараты', 'Игровые консоли', 'Умные часы'],
        'Одежда': ['Мужская одежда', 'Женская одежда', 'Детская одежда', 'Обувь', 'Аксессуары', 'Спортивная одежда', 'Нижнее белье'],
        'Продукты': ['Молочные продукты', 'Мясо и птица', 'Овощи и фрукты', 'Бакалея', 'Напитки', 'Хлеб и выпечка', 'Консервы', 'Замороженные продукты'],
        'Дом и сад': ['Мебель', 'Текстиль', 'Посуда', 'Инструменты', 'Освещение', 'Декор', 'Садовый инвентарь', 'Бытовая техника'],
        'Красота и здоровье': ['Косметика', 'Парфюмерия', 'Уход за кожей', 'Витамины', 'Гигиена', 'Волосы', 'Макияж'],
        'Автотовары': ['Шины', 'Масла', 'Аксессуары', 'Запчасти', 'Электроника', 'Уход'],
        'Спорт и отдых': ['Велосипеды', 'Тренажеры', 'Туризм', 'Рыбалка', 'Зимний спорт', 'Игры']
    }
    
    products = []
    product_brands = {
        'Электроника': ['Samsung', 'Apple', 'Xiaomi', 'Sony', 'LG', 'Philips', 'Lenovo', 'Asus'],
        'Одежда': ['Nike', 'Adidas', 'Zara', 'H&M', 'LC Waikiki', 'Reserved', 'Colin\'s'],
        'Продукты': ['Простоквашино', 'Домик в деревне', 'Белый медведь', 'Моя цена', 'Фермерский', 'Слобода'],
        'Дом и сад': ['IKEA', 'Leroy Merlin', 'Hoff', 'OBI', 'Ашан', 'Метрика'],
        'Красота и здоровье': ['L\'Oreal', 'Nivea', 'Garnier', 'Maybelline', 'Black Pearl'],
        'Автотовары': ['Michelin', 'Castrol', 'Bosch', 'Mobil', 'Shell'],
        'Спорт и отдых': ['Adidas', 'Nike', 'Salomon', 'Columbia', 'The North Face']
    }
    
    for i in range(1, n + 1):
        category = random.choice(list(categories.keys()))
        subcategory = random.choice(categories[category])
        brand = random.choice(product_brands[category])
        
        
        if category == 'Электроника':
            cost_price = round(random.uniform(5000, 150000), 2)
            markup = random.uniform(1.1, 1.4)
        elif category == 'Одежда':
            cost_price = round(random.uniform(300, 8000), 2)
            markup = random.uniform(1.5, 2.5)
        elif category == 'Продукты':
            cost_price = round(random.uniform(30, 1000), 2)
            markup = random.uniform(1.3, 2.0)
        elif category == 'Автотовары':
            cost_price = round(random.uniform(1000, 30000), 2)
            markup = random.uniform(1.2, 1.8)
        else:
            cost_price = round(random.uniform(200, 15000), 2)
            markup = random.uniform(1.3, 2.0)
        
        unit_price = round(cost_price * markup, 2)
        
        products.append({
            'ProductID': i,
            'ProductName': f"{brand} {fake.word().capitalize()} {random.randint(100, 9999)}",
            'Category': category,
            'Subcategory': subcategory,
            'Brand': brand,
            'CostPrice': cost_price,
            'UnitPrice': unit_price
        })
    
    return pd.DataFrame(products)

# 2. Генерация таблицы магазинов 
def generate_stores(n):
    cities_regions = {
        'Москва': 'Центральный регион',
        'Санкт-Петербург': 'Северо-Западный регион',
        'Новосибирск': 'Сибирский регион',
        'Екатеринбург': 'Уральский регион',
        'Казань': 'Приволжский регион',
        'Нижний Новгород': 'Приволжский регион',
        'Челябинск': 'Уральский регион',
        'Самара': 'Приволжский регион',
        'Омск': 'Сибирский регион',
        'Ростов-на-Дону': 'Южный регион',
        'Краснодар': 'Южный регион',
        'Воронеж': 'Центральный регион',
        'Пермь': 'Приволжский регион',
        'Волгоград': 'Южный регион',
        'Красноярск': 'Сибирский регион'
    }
    
    stores = []
    city_list = list(cities_regions.keys())
    
    for i in range(1, n + 1):
        city = random.choice(city_list)
        region = cities_regions[city]
        store_size = random.choice([80, 120, 150, 200, 250, 300, 400, 500])
        
        # Разные форматы магазинов
        formats = ['Гипермаркет', 'Супермаркет', 'Магазин у дома', 'Торговый центр']
        store_format = random.choice(formats)
        
        
        open_date = fake.date_between_dates(
            date_start=datetime.now() - timedelta(days=7*365),  # 7 лет назад
            date_end=datetime.now() - timedelta(days=365)       # 1 год назад
        )
        
        stores.append({
            'StoreID': i,
            'StoreName': f"{store_format} '{city}' №{i}",
            'City': city,
            'Region': region,
            'Size': store_size,
            'Format': store_format,
            'OpenDate': open_date
        })
    
    return pd.DataFrame(stores)

# 3. Генерация таблицы клиентов 
def generate_customers(n):
    customers = []
    loyalty_levels = ['Обычный', 'Серебряный', 'Золотой', 'Платиновый']
    
    for i in range(1, n + 1):
        # ИСПРАВЛЕННАЯ СТРОКА
        registration_date = fake.date_between_dates(
            date_start=datetime.now() - timedelta(days=5*365),  # 5 лет назад
            date_end=datetime.now()                             # сегодня
        )
        
        # Определяем уровень лояльности на основе давности регистрации
        days_since_reg = (datetime.now().date() - registration_date).days
        if days_since_reg > 1000:
            loyalty = random.choices(loyalty_levels, weights=[10, 30, 40, 20])[0]
        elif days_since_reg > 500:
            loyalty = random.choices(loyalty_levels, weights=[30, 40, 20, 10])[0]
        else:
            loyalty = random.choices(loyalty_levels, weights=[60, 30, 8, 2])[0]
        
        customers.append({
            'CustomerID': i,
            'CustomerName': fake.name(),
            'Email': fake.email(),
            'Phone': fake.phone_number(),
            'City': fake.city(),
            'RegistrationDate': registration_date,
            'LoyaltyLevel': loyalty,
            'BirthDate': fake.date_of_birth(minimum_age=18, maximum_age=80)
        })
    
    return pd.DataFrame(customers)

# 4. Генерация таблицы продаж
def generate_sales(n, products_df, stores_df, customers_df, start_date, end_date):
    sales = []
    
    # Создаем сезонные коэффициенты
    seasonal_factors = {
        1: 1.1,  # Январь - распродажи
        2: 0.9,  # Февраль
        3: 1.0,  # Март
        4: 1.0,  # Апрель
        5: 1.1,  # Май - подготовка к лету
        6: 1.2,  # Июнь - начало лета
        7: 1.3,  # Июль - пик сезона
        8: 1.2,  # Август
        9: 1.1,  # Сентябрь - подготовка к школе
        10: 1.0, # Октябрь
        11: 1.1, # Ноябрь - подготовка к зиме
        12: 1.4  # Декабрь - новогодние покупки
    }
    
    print("Генерация продаж...")
    for i in range(1, n + 1):
        if i % 5000 == 0:
            print(f"Обработано {i} из {n} записей...")
        
        product = products_df.sample(1).iloc[0]
        store = stores_df.sample(1).iloc[0]
        customer = customers_df.sample(1).iloc[0]
        
        # Генерация даты продажи с учетом сезонности
        sale_date = fake.date_time_between_dates(
            datetime_start=start_date, 
            datetime_end=end_date
        )
        month = sale_date.month
        seasonal_factor = seasonal_factors[month]
        
        # Количество товара с учетом сезонности
        base_quantity = max(1, int(np.random.poisson(1.3)))
        quantity = max(1, int(base_quantity * seasonal_factor * random.uniform(0.8, 1.2)))
        
        # Учитываем время суток и день недели
        hour = sale_date.hour
        weekday = sale_date.weekday()
        
        # Больше продаж в рабочее время и в выходные
        if 10 <= hour <= 20 or weekday >= 5:
            quantity = min(quantity * random.uniform(1.2, 2.0), 15)
        
        # Скидки для постоянных клиентов
        loyalty_discounts = {'Обычный': 0, 'Серебряный': 0.05, 'Золотой': 0.1, 'Платиновый': 0.15}
        discount = loyalty_discounts[customer['LoyaltyLevel']]
        
        total_amount = round(quantity * product['UnitPrice'] * (1 - discount), 2)
        
        sales.append({
            'SaleID': i,
            'Date': sale_date,
            'ProductID': product['ProductID'],
            'StoreID': store['StoreID'],
            'CustomerID': customer['CustomerID'],
            'Quantity': quantity,
            'UnitPrice': product['UnitPrice'],
            'TotalAmount': total_amount,
            'Discount': discount
        })
    
    return pd.DataFrame(sales)

# 5. Генерация календарной таблицы
def generate_calendar(start_date, end_date):
    dates = pd.date_range(start=start_date, end=end_date, freq='D')
    
    calendar = []
    for date in dates:
        # Определяем праздники
        holidays_ru = [
            (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7), (1, 8),  # Новогодние
            (2, 23), (3, 8), (5, 1), (5, 9), (6, 12), (11, 4)  # Остальные праздники
        ]
        is_holiday = 1 if (date.month, date.day) in holidays_ru else 0
        
        calendar.append({
            'Date': date.date(),
            'Year': date.year,
            'Month': date.month,
            'MonthName': date.strftime('%B'),
            'Quarter': f"Q{(date.month-1)//3 + 1}",
            'DayOfWeek': date.strftime('%A'),
            'DayOfWeekNumber': date.weekday() + 1,
            'IsWeekend': 1 if date.weekday() >= 5 else 0,
            'IsHoliday': is_holiday,
            'Season': 'Зима' if date.month in [12, 1, 2] else 
                     'Весна' if date.month in [3, 4, 5] else 
                     'Лето' if date.month in [6, 7, 8] else 'Осень'
        })
    
    return pd.DataFrame(calendar)

# ГЕНЕРАЦИЯ ДАННЫХ

products_df = generate_products(n_products)
stores_df = generate_stores(n_stores)
customers_df = generate_customers(n_customers)
sales_df = generate_sales(n_sales, products_df, stores_df, customers_df, start_date, end_date)
calendar_df = generate_calendar(start_date, end_date)

end_time = time.time()
execution_time = end_time - start_time


