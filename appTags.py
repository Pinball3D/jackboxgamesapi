from enum import Enum

json = {'PROTOTYPE': 'prototype', 'ECASTTESTCLIENT': 'ecast-test-client', 'QUIPLASH2INTERLASHIONAL': 'quiplash2-international',
        'GUESSPIONAGECROWDPLAY': 'guesspionage-crowdplay', 'DRAWFUL2': 'drawful2', 'DRAWFUL2INTERNATIONAL': 'drawful2international',
        'ACQUISITIONS,INC.': 'acquisitions-inc', "YOUDON'TKNOWJACK2015": 'ydkj2015', 'DRAWFUL': 'drawful', 'WORDSPUD': 'wordspud',
        'LIESWATTER': 'lieswatter', 'FIBBAGE': 'fibbage', 'FIBBAGE2': 'fibbage2', 'EARWAX': 'earwax', 'BIDIOTS': 'auction',
        'BOMBCORP': 'bombintern', 'QUIPLASH': 'quiplash', "FAKIN'IT": 'fakinit', 'TEEK.O.': 'awshirt',
        'QUIPLASH2': 'quiplash2', 'TRIVIAMURDERPARTY': 'triviadeath', 'GUESSPIONAGE': 'pollposition', 'FIBBAGE3': 'fibbage3',
        'SURVIVETHEINTERNET': 'survivetheinternet', 'MONSTERSEEKINGMONSTER': 'monstermingle',
        'BRACKETEERING': 'bracketeering', 'CIVICDOODLE': 'overdrawn', "YOUDON'TKNOWJACK:FULLSTREAM": 'ydkj2018',
        'SPLITTHEROOM': 'splittheroom', 'MADVERSECITY': 'rapbattle', 'ZEEPLEDOME': 'slingshoot', 'PATENTLYSTUPID': 'patentlystupid',
        'TRIVIAMURDERPARTY2': 'triviadeath2', 'ROLEMODELS': 'rolemodels', 'JOKEBOAT': 'jokeboat',
        'DICTIONARIUM': 'ridictionary', 'PUSHTHEBUTTON': 'pushthebutton', 'TALKINGPOINTS': 'jackbox-talks',
        'QUIPLASH3': 'quiplash3', 'THEDEVILSANDTHEDETAILS': 'everyday', "CHAMP'DUP": 'worldchamps',
        "BLATHER'ROUND": 'blanky-blank', 'JOBJOB': 'apply-yourself', 'DRAWFULANIMATE': 'drawful-animate',
        'THEWHEELOFENORMOUSPROPORTIONS': 'the-wheel', 'THEPOLLMINE': 'survey-bomb', 'WEAPONSDRAWN': 'murder-detectives',
        'QUIPLASH3STARTER': 'quiplash3-tjsp', 'TEEK.O.STARTER': 'awshirt-tjsp', 'TRIVIAMURDERPARTY2STARTER': 'triviadeath2-tjsp',
        'FIBBAGE4': 'fourbage', 'ROOMERANG': 'htmf', 'JUNKTOPIA': 'antique-freak', 'NONSENSORY': 'range-game', 'QUIXORT': 'lineup'}

appTags = Enum('appTags', json)

