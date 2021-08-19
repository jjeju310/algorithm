'''
# Input Examples : ["119", "97674223", "1195524421"]
# Output Examples : True

'''

phone_book = ["119", "97674223", "1195524421"]
answer = True
hashmap = {}

for phone_num in phone_book:
    hashmap[phone_num]=1

print("hashmap")
print(hashmap)

for phone_num in phone_book: #ex. phone_num=119, phone_book = {11943532:1}
    str = ""
    for num in phone_num: #ex. num:1
        str += num
        if str in hashmap and str != phone_num:
            answer = False
            
print(answer)

