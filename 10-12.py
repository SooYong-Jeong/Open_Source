s = [64, 89, 100, 85, 77, 58, 79, 67, 96, 87, 87, 36, 82, 98, 84, 76, 63, 69, 53, 22]

count_su = 0
count_woo = 0
count_mi = 0
count_yang = 0
count_ga = 0

for i in s: 
    if i < 60:
        count_ga += 1
        continue
    if i < 70:
        count_yang += 1
        continue
    if i < 80:
        count_mi += 1
        continue
    if i < 90:
        count_woo += 1
        continue
    if i <= 100:
        count_su += 1
        continue

print(f"수 : {count_su}명")
print(f"우 : {count_woo}명")
print(f"미 : {count_mi}명")
print(f"양 : {count_yang}명")
print(f"가 : {count_ga}명")