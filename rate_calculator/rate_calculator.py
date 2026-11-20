# 全体の計算
def main():
    total = 0
    quote_counter = 0
    while True:
        duration_fee = get_duration_fee()

        needs_quote = duration_fee is None  # この書き方だとTrueかFalseになる。 判断結果をメモしておく
        if needs_quote:
            duration_fee = 0

        edit_fee = get_fee("Do you need video editing? yes/no ", 100)

        color_fee = get_fee("Do you need color grading? yes/no ", 50)

        # 制作本数
        quantity = int(input("How many videos do you need? "))

        unit_price = duration_fee + edit_fee + color_fee
        subtotal = unit_price * quantity
        total += subtotal
        if needs_quote:
            quote_counter += 1

        # 追加するかどうかの繰り返し処理
        while True:
            add_more = input("Would you like to add anything else? yes/no ")
            if add_more == "yes" or add_more == "no":
                break

        # yesが来た時は最初からループして、noならprintに行く
        if add_more == "no":
            break

    if quote_counter == 1:
        print(f"Total: ${total} + Custom quote ({quote_counter} Video)")
    elif quote_counter > 1:
        print(f"Total: ${total} + Custom quote ({quote_counter} Videos)")
    else:
        print(f"Total: ${total}")


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

# fee計算


def get_fee(question, rate):
    while True:
        answer = input(question)
        if answer == "yes" or answer == "no":
            break
    if answer == "yes":
        return rate
    else:
        return 0


main()
