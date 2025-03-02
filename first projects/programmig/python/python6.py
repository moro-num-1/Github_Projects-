int_total_seconds = int(input("please type the numer of seconds\n"))
hours = int_total_seconds//3600
minutes = (int_total_seconds%3600)//60
seconds = int_total_seconds%60
print(f'the duration is {hours} hours {minutes} minuts {seconds} seconds')