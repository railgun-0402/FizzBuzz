# 整数a,bの積が偶数か奇数かを判定するプログラム
# 1 <= a,b <= 10000
# a,bは整数

# a,bの積が偶数なら「Even」を出力
# 奇数の場合は「Odd」を出力

import validation

answer_even = "Even"
answer_odd = "Odd"


# 整数を入力し、その値を返す
def input_num():
    while True:

        # 整数の入力
        print('整数aを決めてください')
        a = input()

        print('整数bを決めてください')
        b = input()

        if validation.check_num(a, b) and validation.check_scope(a, b):
            # バリデーションチェックが正であればループを抜ける
            return a, b


# 入力値の積を算出し、奇数か偶数か求める
def judge_product(a, b):
    # 積を管理
    product = int(a) * int(b)

    if product % 2 == 0:
        # 偶数の場合
        print(answer_even)
    else:
        # 奇数の場合
        print(answer_odd)


if __name__ == '__main__':
    # 入力値取得
    a, b = input_num()

    # 積から偶数か奇数か判定
    judge_product(a, b)
