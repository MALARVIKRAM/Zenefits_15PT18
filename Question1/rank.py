

n=input("Enter the no of letters: ")
#print n
letters=list()
print "Enter the letters"
for i in range(n):
    letters.append(raw_input())
word=raw_input("Enter the Word: ")
#print letters
#print word

permuted_string=list()
def permutation(fixed_num,tot_list):
    print tot_list
    print fixed_num
    per_string=tot_list[fixed_num]
    tot_list1=tot_list
    tot_list1.remove(tot_list[fixed_num])
    if len(tot_list1)==0:
        return per_string
    for j in range(len(tot_list1)):
        per_string=per_string + permutation(j,tot_list1)
        if len(tot_list)==n:
            permuted_string.append(per_string)
            print permuted_string
        else:
            return per_string
        

for i in range(n):
    permutation(i,letters)
