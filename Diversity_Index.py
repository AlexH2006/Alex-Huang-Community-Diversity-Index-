import csv
import math

def evenness(sequence):
    sum = 0
    for number in sequence:
        sum+=number
    ans = 0
    for number in sequence:
        ans+=(number/sum)*(math.log(sum/number, math.exp(1)))
    max=float(math.log(len(sequence), math.exp(1)))
    return ans/max

def simpson(sequence):
    sum=0
    for number in sequence:
        sum+=number
    ans = 0.0
    for number in sequence:
        ans+=float((number/sum)*(number/sum))
    return ans

def count_spaces(input):
    spaces_count = 0
    for index in range(0, len(input)):
        if input[index] == " ":
            spaces_count += 1
        else:
            break
    return spaces_count

def cultural_parameter(sequence):
    l=[]
    for row in sequence:
        if row[0]=="Mother tongue":
            l.append(row)
    return l

def economic_parameter(sequence):
    l=[]
    start=0
    for row in sequence:
        if row[0]=="Industry - North American Industry Classification System (NAICS) 2012":
            break
        start+=1
    i=start+3
    while i<=start+22:
        l.append(sequence[i])
        i+=1
    return l

def social_parameter(sequence):
    l=[]
    count=0
    for row in sequence:
        if row[0]=="Major field of study - Classification of Instructional Programs (CIP) 2016":
            if count_spaces(row[1])==4:
                l.append(row)
            if count_spaces(row[1])==0:
                count+=1
            if count>=2:
                break
    return l

def list_compression(sequence, pos, type):
    l=[]
    if type == 1:
        for row in sequence:
            l.append(int(row[pos]))
    if type == 2:
        for row in sequence:
            l.append(row[pos])
    return l

with open ("Canada_Census.csv", newline='') as csvdata:
    reader = csv.reader(csvdata)
    national_data=list(reader)

national_economic=economic_parameter(national_data)
national_cultural=cultural_parameter(national_data)
national_social=social_parameter(national_data)

national_social_compressed=list_compression(national_social,3,1)
national_social_index=simpson(national_social_compressed)

national_cultural_compressed=list_compression(national_social,3,1)
national_cultural_index=simpson(national_cultural_compressed)

national_economic_compressed=list_compression(national_economic,3,1)
national_economic_index=simpson(national_economic_compressed)

print("National average (Canada, 2016):")
print("Economic:", national_economic_index)
print("Cultural:", national_cultural_index)
print("Social:", national_social_index)
print("")

def regional_index(name):
    with open (name, newline='') as csvdata:
        reader = csv.reader(csvdata)
        regional_data=list(reader)
    
    regional_cultural=cultural_parameter(regional_data)
    regional_economic=economic_parameter(regional_data)
    regional_social=social_parameter(regional_data)
    
    regional_social_compressed=list_compression(regional_social,3,1)
    regional_social_index=simpson(regional_social_compressed)

    regional_economic_compressed=list_compression(regional_economic,3,1)
    regional_economic_index=simpson(regional_economic_compressed)
    
    regional_cultural_compressed=list_compression(regional_cultural,3,1)
    regional_cultural_index=simpson(regional_cultural_compressed)
    
    print("Regional Index (2016):", name)
    print("Economic (Unweighted):", regional_economic_index)
    print("Cultural (Unweighted):", regional_cultural_index)
    print("Social (Unweighted):", regional_social_index)
    print("Economic (Weighted):", regional_economic_index/national_economic_index)
    print("Cultural (Weighted):", regional_cultural_index/national_cultural_index)
    print("Social (Weighted):", regional_social_index/national_social_index)

regional_index("Parkdale_Highpark_Census.csv")
