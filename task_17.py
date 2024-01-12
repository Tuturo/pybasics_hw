#17
# Дано множество работников
workers = {'Вася', 'Коля', 'Маша', 'Вера'}
# И подмножества
fast_workers = {'Коля', 'Маша'} # работают быстро
quality_workers = {'Маша', 'Вера'} # работают качественно
cheap_workers = {'Коля',  'Вера'} # работают бюджетно
# кто работает быстро, хорошо и дешево?
# кто работает криво, медленно и дорого?

def get_super_workers(worker_list, features_list):

    super_workers = []
    for id, worker in enumerate(worker_list):
        for id, feature in enumerate(features_list):
            if worker == feature:
                super_workers.append(worker)

    text = ''

    if features_list == fast_workers:
        text = 'Быстрее всех работают: '
    elif features_list == quality_workers:
        text = 'Качественнее всех работают: '
    elif features_list == cheap_workers:
        text = 'Бюджетнее всего обходятся: '
    
    print(text + ', '.join(super_workers))

get_super_workers(workers, fast_workers)