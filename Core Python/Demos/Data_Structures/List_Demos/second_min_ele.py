def secMin(li):
    min = li[0]
    sec_min = li[1]
    
    if sec_min < min:
        min, sec_min = sec_min, min
    for i in range(2, len(li)):
        if li[i]<min:
            sec_min = min
            min = li[i]
        elif li[i]<sec_min:
            sec_min = li[i]
    return sec_min

li = [10, 20, 30, 40, 50, 60 ,70, 80, 90, 100]
print(f"Second Min in {li} = {secMin(li)}.")       