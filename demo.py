card_number = '5610591081018250'

card_number_list = list(card_number)

odd_sum = 0
even_sum = 0

for idx, num in enumerate(card_number_list):
    if idx % 2 != 0:
        odd_sum += int(num)
    else:
        if idx % 2 == 0:
            doubled_nums = int(num) * 2
            str_nums = str(doubled_nums)
            for num in str_nums:
                even_sum += int(num)

total = odd_sum + even_sum

if total % 2 != 0:
    print('Invalid card!')
else:
    print('Valid card!')
