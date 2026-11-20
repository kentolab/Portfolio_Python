# 全体の計算
def main():
    duration_fee = get_duration_fee()

    needs_quote = duration_fee is None  # この書き方だとTrueかFalseになる。 判断結果をメモしておく
    if needs_quote:
        duration_fee = 0

    edit_fee = get_fee("Do you need video editing? yes/no ")

    color_fee = get_fee("Do you need color grading? yes/no ")

    # 制作本数
    quantity = int(input("How many videos do you need? "))

    unit_price = duration_fee + edit_fee + color_fee
    subtotal = unit_price * quantity

    if needs_quote:
        print(f"Total: ${subtotal} + Custom quote")
    else:
        print(f"Total: ${subtotal}")


# 完成尺の長さ, 30 , 60 , 90
def get_duration_fee():
    while True:
        duration = int(input("How long is the finished video (in seconds)? "))
        if duration > 0:
            break

    if 0 < duration <= 30:
        return 50
    elif 30 < duration <= 60:
        return 100
    elif 60 < duration <= 90:
        return 150
    elif 90 < duration <= 120:
        return 200
    else:
        return None


# 編集は必要か、単価
# def get_editing_fee():
#     while True:
#         edit = input("Do you need video editing? yes/no ")
#         if edit == "yes" or edit == "no":
#             break
#     if edit == "yes":
#         return 50
#     else:
#         return 0

# # カラグレは必要か、　単価

# def get_color_fee():
#     while True:
#         color = input("Do you need color grading? yes/no ")
#         if color == "yes" or color == "no":
#             break
#     if color == "yes":
#         return 50
#     else:
#         return 0


# fee計算
def get_fee(question):
    while True:
        answer = input(question)
        if answer == "yes" or answer == "no":
            break
    if answer == "yes":
        return 50
    else:
        return 0


main()
