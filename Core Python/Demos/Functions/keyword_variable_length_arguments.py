def emp(**data):
    print(type(data))
    
    for key, val in data.items():
        print(f"{key} : {val}")
        
emp(id = 1, name = "Maithili", sal= 100000, dept="IT")