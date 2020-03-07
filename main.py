from hasher import get_hash
from wikirator import Wikirator

'''
Сктрипт использует итератор wiki_counters для получения ссылок на страницу страны в Википедии.
Обработка всего файла counters.json занимает довольно продолжительное время, 
для теста итератор получает ссылки на 20 первых стран. Для обработки всего файла 
итератор нужно запустить без параметра "end".
После получения ссылок и записи полученого в файл result, этот же файл обрабатываю вторым скриптом(который генератор).

'''
wiki_countries = Wikirator('countries.json', 'result', end=0)
string_hashes = get_hash('result')
if __name__ == '__main__':
    for item in wiki_countries:
        print(item)
    for item in string_hashes:
        print(item)
