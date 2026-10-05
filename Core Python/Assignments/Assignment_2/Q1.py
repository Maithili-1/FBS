# WAP to convert time entered in hh, min, sec in seconds.

hh = int(input("Enter hours : "))
min = int(input("Enter minutes : "))
sec = int(input("Enter seconds : "))

total_sec = (hh*3600) + (min*60) + sec
print(f"{hh} hh: {min} min: {sec} sec means total {total_sec} seconds.")