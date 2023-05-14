mock_emotion = {
    "EmoStats": {
        'annoyance': 1.288855193328279,
        'joy': 6.444275966641396,
        'anger': 0.6065200909780136,
        'amusement': 0.9855951478392722,
        'nervousness': 0.22744503411675512,
        'embarrassment': 0.1516300227445034,
        'desire': 1.8953752843062925,
        'disapproval': 0.9097801364670205,
        'remorse': 0.3032600454890068,
        'disappointment': 2.122820318423048,
        'approval': 3.639120545868082,
        'surprise': 2.805155420773313,
        'pride': 0.3032600454890068,
        'curiosity': 3.4874905231235784,
        'love': 10.159211523881728,
        'confusion': 1.4404852160727823,
        'optimism': 3.4874905231235784,
        'sadness': 3.790750568612585,
        'excitement': 13.267626990144048,
        'realization': 1.9711902956785443,
        'grief': 0.3032600454890068,
        'disgust': 0.1516300227445034,
        'caring': 0.6823351023502654,
        'gratitude': 3.8665655799848366,
        'admiration': 35.02653525398029,
        'fear': 0.6823351023502654
    }
}

mock_named_keywords = {
    "Entities": {
        "james cameron": "james cameron and all the actors are truly incredible and have incredible talents - and they are able to create this stunning movie is beyond me",
        "pandora": "the beauty of pandora is overwhelming and its creatures utterly captivating"
    }
}

mock_summary = {
    "Summary": "i was one of the first creature designers who worked on this film. james cameron and all the actors are truly incredible and have incredible talents - and they are able to create this stunning movie is beyond me. the film's positive environmental theme is admirable, the beauty of pandora is overwhelming and its creatures utterly captivating."
}

mock_all = {}
mock_all.update(mock_emotion)
mock_all.update(mock_named_keywords)

new_mock = {
    "Emostats": {
        "admiration": 18.556701030927837,
        "amusement": 20.618556701030926,
        "annoyance": 1.0309278350515463,
        "approval": 8.24742268041237,
        "caring": 3.0927835051546393,
        "confusion": 3.0927835051546393,
        "curiosity": 1.0309278350515463,
        "desire": 2.0618556701030926,
        "disapproval": 1.0309278350515463,
        "embarrassment": 2.0618556701030926,
        "excitement": 7.216494845360824,
        "gratitude": 4.123711340206185,
        "joy": 10.309278350515463,
        "love": 13.402061855670103,
        "optimism": 1.0309278350515463,
        "surprise": 3.0927835051546393
    },
    "Keywords": {
        "buff": 1.2038021923512996,
        "fame": 0.8900463408119658,
        "gordon": 1.023,
        "green": 1.012,
        "kay": 2.637470366191348,
        "ken": 1.887303914835165,
        "lee": 3.9975938344889235,
        "lol": 1.7877980578449324,
        "master": 1.8310194215506714,
        "ramsay": 1.023,
        "rhett": 1.153633585164835,
        "sen": 1.012,
        "sensei": 1.2844715735653236,
        "supreme": 1.0544117826617825,
        "tobasco": 1.023
    },
    "Summary": "lee is a champ for keeping this tradition alive this is the first time we see kay actually eat. the science experiment subject has become the scientist! happy early mums day!"
}
mock_all.update()
