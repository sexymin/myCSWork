bDays = ["05_07_06", "05_12_13", "07_08_17", "06_08_25", "06_09_27", "06_05_23", "07_10_01", "06_02_01", "06_07_05", "07_06_02", "06_03_17", "05_11_17", "06_04_03", "07_07_11"]
names = ["Daeju", "Richard", "Kevin", "James", "Warren", "Hwanmin", "Donghyuk", "Taehoon", "Taeyoon", "Beomkyu", "Sieon", "Devyn", "Seoyoung", "Hayoung"]
name_birthday_dict = dict(zip(names, bDays))

'''
for each in temp:
    print(each)
    result = list()
    for e in each.split("_"):
        result.append(int(e))
    print(result)
'''
young_and_old_birthdays= {}
'''
for each in bDays:
    year, month, day = map(int, each.split("_"))
    date = (month, day)
    
    if year not in young_and_old_birthdays:
        young_and_old_birthdays[year] = []
    young_and_old_birthdays[year].append(date)

for year, dates in sorted(young_and_old_birthdays.items()):
    earliest_date = min(dates)  
    latest_date = max(dates)    
    print(f"Year: 20{year:02d}")
    print(f"Oldest Date: {earliest_date[0]:02d}-{earliest_date[1]:02d}")
    print(f"Youngest Date: {latest_date[0]:02d}-{latest_date[1]:02d}")
'''



for name, bDay in name_birthday_dict.items():
    year, month, day = map(int, bDay.split("_"))
    date = (month, day)

    # Add the birth date to the year key, along with the name
    if year not in young_and_old_birthdays:
        young_and_old_birthdays[year] = []
    young_and_old_birthdays[year].append((date, name))

# Print earliest and latest birth dates for each year
for year, dates in sorted(young_and_old_birthdays.items()):
    # Sort dates within each year to get the earliest and latest with names
    sorted_dates = sorted(dates)
    earliest_date, earliest_name = sorted_dates[0]
    latest_date, latest_name = sorted_dates[-1]

    print(f"Year: 20{year:02d}")
    print(f"Oldest Date: {earliest_date[0]:02d}-{earliest_date[1]:02d}, Name: {earliest_name}")
    print(f"Youngest Date: {latest_date[0]:02d}-{latest_date[1]:02d}, Name: {latest_name}")
