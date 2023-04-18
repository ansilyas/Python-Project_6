#%%
#get sentence from user:
original=input("Please enter a sentence:").strip().lower()
#split sentence into word:
words=original.split()
#loop throught words and convert to pig latin:
new_words=[]

for word in words:
    if word[0] in "aeiou":
        new_word=word+"yay"
        new_word.append(new_word)
    else:
            vowel_pos=0
            for letter in word:
                if letter not in "aeiou":
                    vowel_pos=vowel_pos +1
                else:
                 break
                cons=word[:vow_pos]
                the_rest+word[vowel_pos:]
                new_word=the_rest+cons+"ay"
                new_words.append(new_world)
#stick word back together:
output=" ".join(new_words)
print(output)
                
# %%
