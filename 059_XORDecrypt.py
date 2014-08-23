import time

#Start the timer
init_time = time.clock()
#Open the encrypted text file as an list of encrypted chars
encrypted = list(map(int,open("059_cipher.txt").read().split(',')))
#Open a list of the 100 most common English words
wordlist = open("059_wordlist.txt").read().split()

#Solution = [number of English words, plaintext]
Solution = [0,""]

#Iterate through all possible 3 character keys and save the one with the most 
#English words
for key in [[a,b,c] for a in range(ord('a'), ord('z')+1) for b in range(ord('a'), ord('z')+1) for c in range(ord('a'), ord('z')+1)]:
    decrypted = []
    for i in range(len(encrypted)):
        decrypted.append(encrypted[i] ^ key[i % 3])
    decrypted = list(map(chr,decrypted))
    decrypted = "".join(decrypted).split(" ")
    if len([word for word in wordlist if word in decrypted]) > Solution[0]:
        Solution[0] = len([word for word in wordlist if word in decrypted])
        Solution[1] = decrypted

#Print the plaintext, the Project Euler solution, and the time taken
print(" ".join(Solution[1]), end = "\n\n")
print(sum(map(ord,list(" ".join(Solution[1])))), end="\n\n")
print("Solved in " + str(time.clock() - init_time), end = " seconds. \n\n")



