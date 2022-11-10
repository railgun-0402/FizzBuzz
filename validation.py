# 入力値が以下の条件を満たすかチェック
# 1 <= a,b <= 10000
# a,bは整数

max_num = 10000
min_num = 1


# 入力値a,bが数字か確認
def check_num(input_a, input_b):

    if input_a.isdigit() and input_b.isdigit():
        # 数値の場合
        return True
    else:
        # 数字以外が入力されてる場合
        print("文字列が入力されています！数字を入力してください。 \n")
        return False


# 入力値a,bが範囲内か確認
def check_scope(a, b):

    if (min_num <= int(a) <= max_num) and (min_num <= int(b) <= max_num):
        # 範囲内の場合
        return True
    else:
        # 条件範囲外の数値を入力した場合
        print("入力範囲は1〜10000です。 \n")
        return False
