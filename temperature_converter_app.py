def fahrenheit_to_celsius(f_temp):
    assert type(f_temp) in (int, float)
    assert f_temp >= -459.67, "Under absolute zero"
    return (f_temp - 32) / 1.8

temp = input("Enter a temperature in Fahrenheit: ")
temp = int(temp)
c_temp = fahrenheit_to_celsius(temp)
print("That is {0:.2f} degrees Celsius".format(c_temp))
