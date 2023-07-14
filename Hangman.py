import random
from words import word_list
randword=random.choice(word_list).upper()
#print(lrandword)
#c=1


def frequency(randword): #To find the frequnecy of a perticular letter in a randomly chosen word
    dic_freq={}
    for i in randword:
        if i in dic_freq:
            dic_freq[i]+=1
        else:
            dic_freq[i]=1
    return dic_freq

def stages(tries):
    list_stages=["""
                  ______
                 |/     |
                 |     (_)
                 |     \|/
                 |  YOU LOOSE  
                 |      |
             ____|____ | |
                 """,
                 """
                  ______
                 |/     |
                 |     (_)
                 |     \|/
                 |      |
                 |     / 
             ____|____
                 """,
                 """
                  ______
                 |/     |
                 |     (_)
                 |     \|/
                 |      |
                 |      
             ____|____
                 """,
                 """
                  ______
                 |/     |
                 |     (_)
                 |     \|
                 |      |
                 |      
             ____|____
                 """,
                 """
                  ______
                 |/     |
                 |     (_)
                 |      |
                 |      |
                 |      
             ____|____
                 """,
                 """
                  ______
                 |/     |
                 |     (_)
                 |     
                 |     
                 |     
             ____|____
                 """,
                 """
                  ______
                 |/     |
                 |     
                 |     
                 |      
                 |     
             ____|____
                 """
                ]
    print(list_stages[tries])


    





def game(randword): #main game logic is written here
    global a
    global b
    tries=6
    freq={}
    result="loose"
    guessed=False
    guessed_letters=[] #To store already guessed letters
    lrandword=list(randword)
    word_completed='-'*len(lrandword)
    #print(word_completed)
    compword=list(word_completed)#this variable holds the progress we made guessing the word as list
    a=random.randint(0,len(lrandword)-1)
    try_=False
    while (try_==False):
        b=random.randint(0,len(lrandword)-1)
        if b==a:
            try_=False
        else:
            try_=True
    compword[a]=lrandword[a] #it will randomly assign a letter into compword as a hint
    compword[b]=lrandword[b] #it will randomly assign another letter into compword as a hint
    compword_="".join(compword)#this joins to list elements into single string
    guessed_letters.append(lrandword[a])
    guessed_letters.append(lrandword[b])
    print("\n\n",compword_,"\n\n") #display mechanism
    stages(tries)
    


    
    while guessed==False and (tries>0): 
        ans=input("Please guess letter or word:").upper()
        if(len(ans)==1 and ans.isalpha()):
            if(ans in guessed_letters):
                freq=frequency(randword)
                nfreq=freq[str(ans)]

                if (nfreq>1):
                    print("Nice,{0} is in the word".format(ans))
                
                    for i in range(0,len(lrandword)):
                        if(str(lrandword[i])==str(ans)):
                            if (lrandword[i]!=lrandword[a] and lrandword[i]!=lrandword[b]):
                                 global value
                                 value=i
                                 compword[value]=ans 
                                 
                            else:
                                value=i
                                compword[value]=ans 
                            guessed_letters.append(ans)
                            
                            compword_="".join(compword)
                            print(compword_)
                            stages(tries)
                            if(compword==lrandword):
                                print("Congratulations:) you win!")
                                guessed=True
                                result="win"
                                
                                
                     
                else:
                    print("{0} is already in the word".format(ans))

            elif(ans not in randword):
                print("{0} is not in the word".format(ans))
                print(compword_)
                tries=tries-1
                stages(tries)
                if(tries==0):
                    print("\t\tbetter luck next time! \n\nThe word was",randword)
                    result="loose"

                
            else:
                print("Nice,{0} is in the word".format(ans))
                guessed_letters.append(ans)
                for i in range(0,len(lrandword)):
                    if(str(lrandword[i])==str(ans)):
                        
                        value=i
                        compword[value]=ans
                        compword_="".join(compword)
                        print(compword_)  
                        stages(tries)
                        
                        if(compword==lrandword):
                                print("Congratulations:) you win!")
                                guessed=True
                                result="win"
                               
                    
        #elif(len(ans)==len(randword)):

        else:
            print("invalid entry")
    global response
    response=str(input("Do you wish to play again? (y/n) ").upper()) 
    return response
def main():
    game(randword)
    
    
    while(response=="Y"):
        game(randword)

main()







        

