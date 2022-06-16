try:
    x = int(input())
    y = int(input())

    print(x/y)
except ZeroDivisionError as e: #except (ZeroDivisionError, ValueError) is another usage.
    print("You should not try to divide integers by 0")
    print(e) #prints division by zero
except ValueError as m:
    print("All of the inputs must be integers.")
    print(m)# invalid literal for int() with base 10: 'a'
else: #except calısmadıgında çalışır.
    print("All is well.")
#if you write except Exception as ex:
    #print(ex) it will include all errors.
finally:#try except blogundan çıkarken çalışır. HER ZAMAN ÇALIŞIR. Dosya okumada çok işlevlidir.
