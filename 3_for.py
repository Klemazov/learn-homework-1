'''

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
'''

def main():
    school_scores = [
        {'school_class': '1a', 'scores': [5,4,4,5,2]},
        {'school_class': '1b', 'scores': [3,2,4,5,2]},
        {'school_class': '1c', 'scores': [3,4,2,5,2]},
        {'school_class': '1d', 'scores': [5,4,4,5,2]},
        {'school_class': '2a', 'scores': [3,2,4,5,2]},
        {'school_class': '2b', 'scores': [3,4,4,5,2]},
        {'school_class': '2c', 'scores': [5,4,4,5,5]},
        {'school_class': '2d', 'scores': [3,4,2,5,2]},
        {'school_class': '3a', 'scores': [3,2,4,5,2]},
        {'school_class': '3b', 'scores': [3,4,4,5,2]},
        {'school_class': '3c', 'scores': [3,4,4,5,5]},
        {'school_class': '3d', 'scores': [3,5,4,5,2]},
        {'school_class': '4a', 'scores': [3,4,4,5,3]},
        {'school_class': '1a', 'scores': [5,4,4,5,2]},
        {'school_class': '1a', 'scores': [3,4,2,5,3]},
        {'school_class': '1a', 'scores': [2,4,4,5,2]},
        {'school_class': '1a', 'scores': [3,4,5,5,2]},
        {'school_class': '1a', 'scores': [5,4,4,5,2]},
        {'school_class': '1a', 'scores': [3,4,4,5,2]},
        {'school_class': '1a', 'scores': [3,2,2,2,1]},

    ]

    for classes_dict in school_scores:
        mean = (sum(classes_dict['scores'])/len(classes_dict['scores']))
        print('средний балл в классе {school_class} \'{mean}\' '.format(school_class = classes_dict['school_class'].upper(), mean = mean))
    school_scores_sum = 0
    for classes_dict in school_scores:
        school_scores_sum += sum(classes_dict['scores'])
    school_scores_mean = school_scores_sum / (len(school_scores * len(classes_dict['scores']))) 
    print( f'Средний балл по школе: {school_scores_mean}')

        
    
if __name__ == '__main__':
    main()
