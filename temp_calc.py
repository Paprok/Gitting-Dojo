def get_correct_input():
    bad_input = True
    while bad_input:
        temp_f = input('Gimmie temp in Fahrenheit my Man: ')
        try:
            float(temp_f)
        except ValueError:
            print('Enter proper temp my Man!')
        else:
            bad_input = False
    temp_f = float(temp_f)
    return(temp_f)


def main():
    temp_f = get_correct_input()
    temp_c = (5/9) * (temp_f - 32)
    print('It equals %.2f Celsius my Man!' % temp_c)

main()

#spierdalaj git :)
#poprawa main


#ushusfhufshdfuhdsugshguh