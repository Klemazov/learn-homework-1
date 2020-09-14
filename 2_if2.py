"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def main():
    def string_compare(string1 = 1,string2 = 'straaa'):
        if type(string1) is str and type(string2) is str:
            if string1 is string2:
                return 1
            elif len(string1) > len(string2):
                return 2
            elif string1 != string2 and string2 == 'learn':
                return 3
        else:
            return 0
    print(string_compare())
if __name__ == "__main__":
    main()