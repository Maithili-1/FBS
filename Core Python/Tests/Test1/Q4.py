area = int(input("Enter area of one wall : "))
interior_cost = int(input("Enter cost of interior wall : "))
exterior_cost = int(input("Enter cost of exterior wall : "))

total_interior = area * 8 * interior_cost
total_exterior = area * 6 * exterior_cost

total_cost = total_interior + total_exterior

print("Total interior painting cost : ", total_interior)
print("Total exterior painting cost : ", total_exterior)
print("Total painting cost : ", total_cost)