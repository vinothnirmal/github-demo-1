lst = [10,20,30,0]
print(lst)
b = bytes(lst)
print(type(b))
barray = bytearray(lst)
print(barray)
barray[2] = 60
print(list(barray))
#Note  : bytes and bytes array can be of range  0 and 255
#No slicing or reptition in allowed in array and arraybytes
#byte is immutable and bytearray allows insertion , updation