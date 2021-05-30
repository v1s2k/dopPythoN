import random
import sys
def intsconv(a):

    #Преобразование элементов списка s из строковой в числовую форму.
    return [int(i) for i in a]
print(intsconv(["1", "2", "2", "2000"]))
def anywords(a):
   
    #Подсчёт количества различных элементов в последовательности s.
    return len(set(a))
print(anywords(["sameword", "1stword", "2ndword", "sameword"]))
def reverse(l):#развернуть список без функций
    return l[::-1]
print(reverse([1, 2, 3, 4, 5,6,7,8,9,10]))

def finder(x, l):#Выдача списка индексов, на которых найден элемент x в последовательности s.
    return [i for i in range(len(l)) if x == l[i]]
print(finder(5,[1,0,5,5,0,5]))

def sumofidx(l):#Сложение элементов списка s с чётными индексами.
    return sum(l[::2])
print(sumofidx([2, 0, 2, 0, 2, 8, 1, 1]))

def maxstr(l): #Поиск строки максимальной длины в списке строк s.
    return max(l, key=len)

print(maxstr(["lets","find","looooongest","word"]))

def shorts():
    #Сократите код до 19 символов без использования функций.
    #return ["much", "code", "wow"][i] # 24 символа
    i=0
    return "muchcodewow"[:i + 4]  # 19 символов
print(shorts() == "much")#если да,то true

# Изучите, как работает функция zip().


def generate_groups(str):
    return "{0}{1}".format(str[1], int(str[5:7]))
print(generate_groups("ИКБО-20-19"))#K20


def do_zip():
    a = [86, 52, 4]
    b = [1.7, 0.0, -1.7]
    c = ["task", "python", "zip"]
    zipped = zip(a, b, c)
    return list(zipped)  # список из кортежей

# Разберите роль операции * в создании функций с переменным числом
# аргументов, а также для распаковки последовательностей.
# *digits переменное число входных параметров
# возврат  произведения
def multiplydigits(*digits):
    res = 1
    for d in digits:
        res *= d
    return res
print(multiplydigits(-1, 3, 5,10))#-150

def transpose(matrix):
    #Реализуйте с помощью zip() функцию transpose() для транспонирования матрицы.
    #matrix: Исходная матриица.
    
    return list(list(i) for i in zip(*matrix))
print(transpose([[1, 2, 3], [4, 5, 6]]))# == [[1, 4], [2, 5], [3, 6]],транспонированная

def digital_economygenerator():#Реализуйте генератор докладов по цифровой экономике.
    
    
    part1 = ["Экономический", "доклад", "с эффектом",
             "автоматической генерации", "универсального создания"]
    part2 = ["Здесь будут", "много терминов",
             "опасных экспериментов.", "государственно-частных партнёрств.",
             "цифровых следов граждан.", "нежелательных последствий.", "внезапных открытий."]
    part3
    return random.choice(part1) + " " + random.choice(part2)

# Реализуйте свою версию print(). Постарайтесь использовать максимум
# возможностей настоящей print(). Для вывода используйте функцию
# sys.stdout.write().
# *args - входные аргументы
# sep - раделитель данных, end - последний символ строки
# sys.stdout.write - вывод
def analogprint(*args, sep=" ", end="\n"):
    sys.stdout.write(sep.join(str(i) for i in args) + end)

analogprint("my_print():", "java", [1, 2], None, True, sep="\t->\t", end="%\n")

def get_only_init_args(**args):
    return args
print(get_only_init_args(
            group="ИКБО-20-19",
            university="РТУ МИРЭА",
            year=2021))# == {
                # "group": "ИКБО-20-19", "university": "РТУ МИРЭА", "year": 2021}
                                            


def generate_array(*dim):
    #Напишите функцию generate_array(dim1, dim2, dim3, ...) для создания
    #многомерного массива с помощью вложенных списков.
     return [*dim]
print(generate_array([1, 2], [3, 4], [5, 6]))
   

    
   
      
