import pdb

def strings(set,k):

    n = len(set)
    allstrings(set,"",n,k)

def allstrings(set, prefix,n,k):
    if (k == 0):
        print(prefix)
        return
    
    for i in range(n):
        newPrefix = prefix + set[i]
        allstrings(set, newPrefix, n, k - 1)

arr = ['H', 'T']
k=3
strings(arr,k)