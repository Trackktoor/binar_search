def binar_search(num, list_num):
    if isinstance(num, int) and isinstance(list_num, list):
        for el in list_num:
            if isinstance(el, list):
                print("ERROR")
                raise ValueError("Массив должен содержать только числа")
        low_end = 0
        height_end = len(list_num)-1 
        midle_el = int(height_end / 2)
        
        while list_num[midle_el] != num and low_end < height_end:
            if num > list_num[midle_el]:
                low_end = midle_el + 1
            else:
                height_end = midle_el - 1

            midle_el = int((low_end + height_end) / 2)

        if low_end > height_end:
            raise ValueError("Числа нет в списке")
        else:
            return list_num[midle_el]
    else:
        return TypeError("Не правельные данные")

arr = [i for i in range(100)]
print(binar_search(20, arr))