dna=input("enter the DNA sequence=").upper()
complement={"G":"C","A":"T","C":"G","T":"A"}
new_strand=""
for i in dna:
    if i not in "ATGC":
        print("Invalid sequence entered")
        exit()
    else:
        new_strand+=complement[i]    
rev=new_strand[::-1]                
print("The reverse complementary strand is:",rev) 
if dna==rev:
    print("It is also a palindromic sequence")       