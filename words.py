
"""word_list=[
    'encyclopedia',
    
    'hello'
    
]
"""

x="Water ocean forest mountain valley sunset sunrise horizon nature garden flower meadow spring autumn winter summer planet galaxy meteor rocket starry celestial telescope jungle savannah safari wildlife dolphin turtle penguin giraffe elephant butterfly rainbow sunshine thunder lightning hurricane avalanche blizzard tornado volcano island desert oasis mirage canyon waterfall rapids adventure exploration discovery heritage ancient ruins archaeology history culture tradition festival music dance artistic theater perform symphony melody painting sculpture literature poetic novella romance mystery thriller fantasy fiction biography memoir journey reflection meditation wisdom knowledge curiosity wonder inspiration motivation creativity imagination dreamer visionary innovate inspire enchant captivate fascinate embrace cherish whisper secret solitude treasure melody melody blossom majestic harmony tranquil spirit enchanted picturesque masterpiece serenade exquisite serenity elegant captivating cathedral treasure vibrant treasure passionate radiant brilliant treasure ethereal adventure treasure cascade gentle cascade reverie luminous treasure cascade resplendent treasure nostalgia cherished cherished cherished solace wonderland timeless enchanted enchantment delightful breathtaking treasure euphoria treasure mystical sanctuary timeless timeless vibrant delightful divine celestial infinite cherished serendipity whimsical symphony whimsical whimsical whimsical whimsical whimsical whimsical treasure mellifluous scintillating wanderlust journey serendipity."
x=x.strip()
sep=[]
word_list=x.split()
for word in word_list:
    word_list.remove(word)
    word=word.replace(".","")
    word_list.append(word)
