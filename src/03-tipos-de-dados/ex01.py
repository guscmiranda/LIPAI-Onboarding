""" EX01 """

nums = []

for i in range(3):
    num = int(input(f"Digite o {i+1}° número: "))
    nums.append(num)

maior = max(nums)
menor = min(nums)

print(nums)
print(f"Maior: {maior}\nMenor: {menor}")
