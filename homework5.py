print(1)
immutable_var = 1, True, 'Snow'
print(immutable_var)
#immutable_var[0] = 2
#print(immutable_var) #Кортеж не изменяемый
mutable_list = [1, True, 'Snow']
print(mutable_list)
mutable_list[0] = 3
mutable_list[1] = False
print(mutable_list)