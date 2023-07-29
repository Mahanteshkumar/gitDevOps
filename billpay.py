import random
names = "Angela Ben Jenny Michael Chloe"
names_list = names.split(" ")
print(names_list)
bill_payer=random.randint(0,len(names_list)-1)
print(names_list[bill_payer])
#we can also use choise function from randome madule
#print(random.choice(names_list))
states_india = ["Andhra Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh"]
new_list=[names_list, states_india]
print(new_list)
print(new_list[1][1])
print(f"{names_list}\n{states_india}")