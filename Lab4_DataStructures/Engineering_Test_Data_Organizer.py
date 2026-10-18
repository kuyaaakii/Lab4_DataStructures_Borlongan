from constants import *
T1, T2, T3, T4, T5 = {}, {}, {}, {}, {}
tests = [T1, T2, T3, T4, T5]
# Generate five sources using LAST_NAME with  the labels T1, T2, T3, T4, and T5
for n in range(5):
    tests[n]["source"] = LAST_NAME[n].capitalize()

# Assign categories to each test
tests[0]["category"] = "TEMPERATURE"
tests[1]["category"] = "CURRENT"
tests[2]["category"] = "PRESSURE"
tests[3]["category"] = "VOLTAGE"
tests[4]["category"] = "CURRENT"

# Generate numerical values using SEED_NUM and character positions of FAVORITE_ARTIST
for n in range(5):
    tests[n]["value"] = SEED_NUM + (ord(FAVORITE_ARTIST[n].lower()) - 96)  # Convert letter to position in alphabet
tests[1]['value'] = tests[4]['value']
# Print the generated test data
print("=" * 30, "   Generated Test Data ", "=" * 30)
n = 0
for t in tests:
    n += 1
    print(f"Test {n}:")
    print(f"Source: {t['source']}")
    print(f"Category: {t['category']}")

    if t["category"] == "VOLTAGE":
        print(f"Value: {t['value']}V")
    elif t["category"] == "CURRENT":
        print(f"Value: {t['value']}A")
    elif t["category"] == "PRESSURE":
        print(f"Value: {t['value']}atm")
    elif t["category"] == "TEMPERATURE":
        print(f"Value: {t['value']}°C")
    if n == 5:
        print("=" * 30, "   Organized Test Data ", "=" * 30)
    else:       
        print("-" * 30)
    
# Organize the records by source and category
organized_by_source_and_category = {}

for t in tests:
    source = t["source"]
    category = t["category"]
    value = t["value"]

    if source not in organized_by_source_and_category:
        organized_by_source_and_category[source] = {}

    if category not in organized_by_source_and_category[source]:
        organized_by_source_and_category[source][category] = []

    organized_by_source_and_category[source][category].append(value)

for source, categories in organized_by_source_and_category.items():
    print(f"Source: {source}")

    for category, values in categories.items():
        print(f"  Category: {category}")
        if category == "VOLTAGE":
            print(f"    Value: {values}V")
        elif category == "CURRENT":
            print(f"    Value: {values}A")
        elif category == "PRESSURE":
            print(f"    Value: {values}atm")
        elif category == "TEMPERATURE":
            print(f"    Value: {values}°C")        
    print("-" * 30)

# Identify repeated and distinc data within the generated records
repeated_distinc_data = {}
for source, categories in organized_by_source_and_category.items():
    for category, values in categories.items():
        if len(values) > 1 and all(x == values[0] for x in values):
            status = "repeated"
        else:
            status = "distinc"
    repeated_distinc_data[source] = status

print("=" * 30, "   Repeated/Distinc Data ", "=" * 30)
for source, status in repeated_distinc_data.items():
    print(f"Source: {source}")
    print(f"  Status: {status}")
    print("-" * 30)

#Determine numerical and categorical summaries from the measurements
final_summarry = {}
for source, categories in organized_by_source_and_category.items():
    for category, values in categories.items():
        if category == "VOLTAGE":
            if values[0] < 20:
                status = "Normal Voltage"
            else:
                status = "HIGH VOLTAGE!!"
        elif category == "CURRENT":
            if values[0] < 8:
                status == "Normal Current Draw"
            else:
                status = "SHORT CIRCUIT!!"             
        elif category == "PRESSURE":
            if values[0] < 20:
                status = "Normal Pressure"
            else:
                status = "HIGH PRESSURE!!"  
        elif category == "TEMPERATURE":  
            if values[0] < 30:
                status = "Normal Temperature"
            else:
                status = "OVERHEATING!!"                 
        if repeated_distinc_data[source] == "repeated":
            m = ",for both tests."
        else:
            m = ""
    final_summarry[source] = {"category": category,
                              "values": value,
                              "status": status,
                              "message": m
                              }
# Print Final Summary  
print("=" * 30, "   Final Summary ", "=" * 30)    
for source, info in final_summarry.items():
    print(f"Source: {source}")
    print(f"  Category: {info['category']}")
    if info['category'] == "VOLTAGE":
        print(f"    Value: {info['values']}V")
    elif info['category'] == "CURRENT":
        print(f"    Value: {info['values']}A")
    elif info['category'] == "PRESSURE":
        print(f"    Value: {info['values']}atm")
    elif info['category'] == "TEMPERATURE":
        print(f"    Value: {info['values']}°C")
    print(f"    Status: {info['status']}{info['message']}")
    print("-" * 30)
    

