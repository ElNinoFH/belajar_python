fruits = ("apple","banana","mango")

# menambahkan "jackfruit" ke dalam fruits
fruits_list = list(fruits)
fruits_list.append("jackfruit")
fruits = tuple(fruits_list)
print(fruits)

# mengubah data dalam tuple
fruits_list = list(fruits)
fruits_list[1] = "melon"
fruits = tuple(fruits_list)
print(fruits)

# cara untuk menghapus data di dalam tuple
fruits_list = list(fruits)
fruits_list.remove("apple")
fruits = tuple(fruits_list)
print(fruits)