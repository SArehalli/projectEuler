encrypted = list(map(int,open("059_cipher.txt").read().split(',')))
wordlist = open("059_wordlist.txt").read().split()

Solution = [0,""]
for key in [[a,b,c] for a in range(ord('a'), ord('z')+1) for b in range(ord('a'), ord('z')+1) for c in range(ord('a'), ord('z')+1)]:
    decrypted = []
    for i in range(len(encrypted)):
        decrypted.append(encrypted[i] ^ key[i % 3])
    decrypted = list(map(chr,decrypted))
    stringDecrypted = "".join(decrypted).split(" ")
    if len([word for word in wordlist if word in stringDecrypted]) > Solution[0]:
        Solution[0] = len([word for word in wordlist if word in stringDecrypted])
        Solution[1] = stringDecrypted

print(" ".join(Solution[1]))
print(sum(map(ord,list(" ".join(Solution[1])))))



