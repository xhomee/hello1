#Рік вважається високосним, якщо він ділиться на 4. Винятком є роки, які кратні 100 (такі роки є високосними тільки тоді, якщо вони ще діляться на 400).

year = 2018

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 ==0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")





# if year % 4 == 0 and year % 100 == 0 and year % 400 == 0 or year % 4 == 0 and year % 100 != 0 and year % 400 != 0:
#     print("Leap year.")
# else:
#     print("Not leap year.")
