t = ( 0, 4, 132.42222, 10000, 12345.67)

print(f'day_{t[0]:02}, ex_{t[1]:02} :', end = ' ')
print("{:.2f}".format(t[2]),", ", "{:.4e}".format(t[3]),", ", "{:.2e}".format(t[4]), sep ="")