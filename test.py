# 單位整合換算程式（輸入數字，同時顯示兩種單位）
# 長度: 1 km = 0.621371 mi , 1 mi = 1.60934 km
# 溫度: F = C * 9/5 + 32 , C = (F - 32) * 5/9
# 重量: 1 kg = 2.20462 lb , 1 lb = 0.453592 kg

print("====== 單位換算工具 ======")
print("請選擇要轉換的類型:")
print("1) 長度 (公里 <-> 英里)")
print("2) 溫度 (攝氏 <-> 華氏)")
print("3) 重量 (公斤 <-> 磅)")

type_choice = input("輸入選項 (1-3): ")

if type_choice == "1":
    print("\n你選擇了【長度轉換】")
    value = float(input("請輸入數值: "))
    km_to_miles = value * 0.621371
    miles_to_km = value * 1.60934
    print(f"\n你輸入的數字: {value}")
    print(f"解釋1: 如果把它視為公里 → 英里 = 公里 * 0.621371")
    print(f"計算: {value} km * 0.621371 = {km_to_miles:.6f} mi")
    print(f"\n解釋2: 如果把它視為英里 → 公里 = 英里 * 1.60934")
    print(f"計算: {value} mi * 1.60934 = {miles_to_km:.6f} km")

elif type_choice == "2":
    print("\n你選擇了【溫度轉換】")
    value = float(input("請輸入數值: "))
    c_to_f = value * 9/5 + 32
    f_to_c = (value - 32) * 5/9
    print(f"\n你輸入的數字: {value}")
    print(f"解釋1: 如果把它視為攝氏 → 華氏 = 攝氏 * 9/5 + 32")
    print(f"計算: {value} °C * 9/5 + 32 = {c_to_f:.2f} °F")
    print(f"\n解釋2: 如果把它視為華氏 → 攝氏 = (華氏 - 32) * 5/9")
    print(f"計算: ({value} - 32) * 5/9 = {f_to_c:.2f} °C")

elif type_choice == "3":
    print("\n你選擇了【重量轉換】")
    value = float(input("請輸入數值: "))
    kg_to_lb = value * 2.20462
    lb_to_kg = value * 0.453592
    print(f"\n你輸入的數字: {value}")
    print(f"解釋1: 如果把它視為公斤 → 磅 = 公斤 * 2.20462")
    print(f"計算: {value} kg * 2.20462 = {kg_to_lb:.6f} lb")
    print(f"\n解釋2: 如果把它視為磅 → 公斤 = 磅 * 0.453592")
    print(f"計算: {value} lb * 0.453592 = {lb_to_kg:.6f} kg")

else:
    print("輸入錯誤！請輸入 1~3。")
