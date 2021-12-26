# Xətti alqoritm

# 1. Düzbucaqlı üçbucaq katetlərinin qiymətlərini klaviaturadan ayrı sətirdə yazmaqla
# daxil edin. Üçbucağın sahəsini hesablayan proqram yazın.

# a = int(input('a: '))
# b = int(input('b: '))


# s = (a*b)/2

# print(s)

# 2. Üçrəqəmli natural ədəd verilib. Bu ədədin rəqəmləri arasına boşluq simvolu qoymaqla
# çıxışa verin.

# a = int(input('a: '))
# b = int(input('b: '))
# c = int(input('c: '))

# print(f'{a} {b} {c}')

# 3. Tam ədədi verilmişdir. Onun cüt olduğunu müəyyən edin.

# sayi = int(input('sayi: '))
# if sayi>0:
#     if sayi % 2 ==0:
#         print('cut ededdir.')
#     else:
#         print('tek edidir.')
# else:
#     print('eror')


# 4. x, y həqiqi ədədlər verilmişdir. Bu ədədlərin ən böyüyünü (maksimal olanı) tapın.

# x= int(input('x: '))
# y= int(input('y: '))

# if x>0 and y>0:
#     print(max(x,y))

# 5. 1-den 100e qeder ededlerin icinde 7e bolunenlerin cemini hesablayin funksiya yazmaq.
# a = int(input('7e bolunen eded: '))
# mylist = 0
for i in range(1,101):
    if i%7==0:
        print('7e bolunen ededler')
    else:
        print('eror')

        
# a = [1,2,46,85,96]
# mylist = 0
# for i in a:
#     if mylist<i:
#         mylist = i
# print(mylist)  
      
      
# numbers = [2,2,4,3,6,9,1,5,1]

# index = 0
# listen = len(numbers)

# while listen > index:
#     if numbers[index] > 3:
#         numbers.pop(index)
#         listen -=1
#         continue
#     index +=1
# print(numbers)