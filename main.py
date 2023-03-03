import pandas as pd
import csv

def createCandidate(lastName, firstName, phone, birthDate, sex, education, experience, specialty):
  birthDay, birthMonth, birthYear = birthDate
  return {
    'Прізвище': lastName, 
    'ім’я': firstName,
    'телефон': phone,
    'дата': birthDay,
    'місяць': birthMonth,
    'рік народження': birthYear,
    'стать': sex,
    'освіта': education,
    'стаж': experience,
    'спеціальність': specialty
    }

def generateData():
  candidates = [
    createCandidate('Зеленський', 'Володимир', '0501112233', ('10', '10', '1980'), 'ч', '10 років', 'актор, комік, президент', 'політик'),
    createCandidate('Супрун', 'Ульяна', '0501333233', ('11', '8', '1976'), 'ж', '15 років', 'міністр охорони здоров\'я', 'лікар вищої категорії'),
    createCandidate('Шевченко', 'Андрій', '0501112244', ('10', '10', '1989'), 'ч', '11 років', 'зірка футболу, футболіст', 'тренер'),
    createCandidate('Усик', 'Олександр', '0501133244', ('10', '10', '1987'), 'ч', '10 років', 'чемпіон світу', 'боксер'),
    createCandidate('Кіцмей', 'Тарас', '0505542233', ('10', '10', '1975'), 'ч', '20 років', 'співзасновник SoftServe', 'CEO'),
    createCandidate('Кук', 'Тім', '0981112233', ('9', '1', '1968'), 'ч', '25 років', 'Генеральний директор, Apple', 'CEO'),
    createCandidate('Цукерберг', 'Марк', '0502212233', ('9', '4', '1984'), 'ч', '12 років', 'засновник Facebook', 'програміст'),
    createCandidate('Маск', 'Ілон', '0501133233', ('1', '9', '1983'), 'ч', '25 років', 'Розробка космічних кораблів', 'науковець')
  ]
  with open('candidates.csv', 'wt', newline='') as frecord:
    crecord = csv.DictWriter(frecord, ['Прізвище', 'ім’я', 'телефон', 'дата', 'місяць', 'рік народження', 'стать', 'освіта', 'стаж', 'спеціальність'])
    crecord.writeheader()
    crecord.writerows(candidates)

def analizeCandidates():
  data = pd.read_csv('candidates.csv')
  print('General info:')
  print('-----------------')
  data.info()
  print('-----------------')
  print('')
  print('head:')
  print('-----------------')
  print(data.head(5))
  print('-----------------')
  print('')
  print('tail:')
  print('-----------------')
  print(data.tail(5))
  print('Середній вік:', 2023 - data['рік народження'].mean())
  print('Найменьший рік народження:', data['рік народження'].min())
  print('Медіана року народження:', data['рік народження'].median())
  print('Набільний рік народження:', data['рік народження'].max())
  print('Найчастіше повторювана спеціальність:', data['спеціальність'].mode()[0])
  
def analizeBillionaires():
  data = pd.read_csv('billionaire_list_20yrs.csv')
  print('General info:')
  print('-----------------')
  data.info()
  print('-----------------')
  print('')
  print('head:')
  print('-----------------')
  print(data.head(5))
  print('-----------------')
  print('')
  print('tail:')
  print('-----------------')
  print(data.tail(5))
  print('Середній вік:', data['age'].mean())
  print('Найстарший мільйонер:', data['age'].max())
  print('Медіана віку:', data['age'].median())
  print('Наймолодший мільйонер:', data['age'].min())
  print('Найчастіше повторювана країна:', data['permanent_country'].mode()[0])

print(pd.__version__)
generateData()
analizeCandidates()
analizeBillionaires()
