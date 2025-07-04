# #１次元配列の平均
# resultを0で初期化
# iを1からnまで繰り返し
#     resultにiを足す
# 繰り返し終わり
# result=result/n
# resultを表示

# #並べ替え
# a=input("1と入力")
# b= input("2と入力")
# a, b = b, a

# print(f"入れ替え後 a={a}, b={b}")

# #カレンダー
# #うるう年判定(4で割り切れる年をうるう年とする。100で割り切れて400で割り切れない年は平年とする)
# def うるう年関数(yr)
#     if(yrが4で割り切れる)
#         if(yrが100で割り切れる and yrが400で割り切れない)
#             return False
#     else return True

#     year = input("年を入力")
# print (うるう年関数(year))

def leap_year(yr):

    if(yr % 4 == 0):
        if(yr % 100 == 0 and yr % 400 != 0 ):
            return False
        else : return True
    else : return False


year = int(input("年を入力= "))
print({leap_year(year)})




