alpha = " abcdefghijklmnopqrstuvwxyz"
vowel = list("aeiou")

fp = open("secret.txt")
decoded = ""  # this is your decoded message. It gets one letter per line of file decoded
#start adding code here
for line in fp:
    numbers_vowels = 0
    for letter in line:
        if letter in vowel:
            numbers_vowels=numbers_vowels+1
    decoded=decoded+alpha[numbers_vowels]


#end the code here
print(decoded)
fp.close()



homework

dir= eng to your language yes :si no:no one:1 two:2 (cincuenta def)
    i see a dog : def i see a dog
you split that text if the word is in the dic, replace the word by the definition
d={"yes":"da","no":"no"}
text