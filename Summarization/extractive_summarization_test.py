from extractive_summarization import get_extractive_summ

if __name__=="__main__":
    test_data = [
        "It's like watching your parents wedding video after they divorced",
        "The fact they are using a Snapdragon chip for all worldwide phones is definitely a good change.",
        "Charlie being a Walmart shopper makes him more brave than everything he listed off combined",
        "This brings tears to my eyes everytime I watch it just on how much I love this series, and how disappointing the actual game was. Just an incredible amount of wasted potential with this game",
        "I've literally played this 100 times already and I'm genuinely not exaggerating",
        "Not only is the cooking worse, but the personality too. Kay adds some spunk into her videos at the very least.",
        "It's like watching your parents wedding video after they divorced",
        "The fact they are using a Snapdragon chip for all worldwide phones is definitely a good change.",
        "Charlie being a Walmart shopper makes him more brave than everything he listed off combined",
        "This brings tears to my eyes everytime I watch it just on how much I love this series, and how disappointing the actual game was. Just an incredible amount of wasted potential with this game",
        "I've literally played this 100 times already and I'm genuinely not exaggerating",
        "Not only is the cooking worse, but the personality too. Kay adds some spunk into her videos at the very least.",
        "It's like watching your parents wedding video after they divorced",
        "The fact they are using a Snapdragon chip for all worldwide phones is definitely a good change.",
        "Charlie being a Walmart shopper makes him more brave than everything he listed off combined",
        "This brings tears to my eyes everytime I watch it just on how much I love this series, and how disappointing the actual game was. Just an incredible amount of wasted potential with this game",
        "I've literally played this 100 times already and I'm genuinely not exaggerating",
        "Not only is the cooking worse, but the personality too. Kay adds some spunk into her videos at the very least.",
        "It's like watching your parents wedding video after they divorced",
        "The fact they are using a Snapdragon chip for all worldwide phones is definitely a good change.",
        "Charlie being a Walmart shopper makes him more brave than everything he listed off combined",
        "This brings tears to my eyes everytime I watch it just on how much I love this series, and how disappointing the actual game was. Just an incredible amount of wasted potential with this game",
        "I've literally played this 100 times already and I'm genuinely not exaggerating",
        "Not only is the cooking worse, but the personality too. Kay adds some spunk into her videos at the very least."
    ]
    print(get_extractive_summ(test_data))