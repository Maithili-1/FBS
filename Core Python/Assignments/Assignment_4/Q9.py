# Print all numbers in a range divisible by a given number 

n = int(input("Enter a number : "))

start = int(input("Enter starting number of range : "))
end = int(input("Enter ending number of range : "))

print(f"\nFollowing are the numbers in range {start} to {end} that are divisible by {n} : ")
for i in range(start, end+1):
    if i%n==0:
        print(i)