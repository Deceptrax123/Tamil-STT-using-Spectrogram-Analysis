import json

if __name__ == '__main__':
    phonetic_tamil_dict = {
        "க": ["Ka", "0"],
        "கா": ["Kaa", "1"],
        "கி": ["Ki", "2"],
        "கீ": ["Kee", "3"],
        "கு": ["Ku", "4"],
        "கூ": ["Koo", "5"],
        "கெ": ["Ke", "6"],
        "கே": ["Kee", "7"],
        "கை": ["Kai", "8"],
        "கொ": ["Ko", "9"],
        "கோ": ["Koa", "10"],
        "கௌ": ["Kou", "11"],
        "ங": ["Gna", "12"],
        "ஙா": ["Gnaa", "13"],
        "ஙி": ["Gni", "14"],
        "ஙீ": ["Gnee", "15"],
        "ஙு": ["Gnu", "16"],
        "ஙூ": ["Gnoo", "17"],
        "ஙெ": ["Gne", "18"],
        "ஙே": ["Gnee", "19"],
        "ஙை": ["Gnaye", "20"],
        "ஙொ": ["Gno", "21"],
        "ஙோ": ["Gnoa", "22"],
        "ஙௌ": ["Gnou", "24"],
        "ச": ["Cha", "25"],
        "சா": ["Chaa", "26"],
        "சி": ["Chi", "27"],
        "சீ": ["Chee", "28"],
        "சு": ["Chu", "29"],
        "சூ": ["Choo", "30"],
        "செ": ["Che", "31"],
        "சே": ["Chee", "32"],
        "சை": ["Chai", "33"],
        "சொ": ["Cho", "34"],
        "சோ": ["Choa", "35"],
        "சௌ": ["Chou", "36"],
        "ஞ": ["Gna", "37"],
        "ஞா": ["Gnaa", "38"],
        "ஞி": ["Gni", "39"],
        "ஞீ": ["Gnee", "40"],
        "ஞு": ["Gnu", "41"],
        "ஞூ": ["Gnoo", "42"],
        "ஞெ": ["Gne", "43"],
        "ஞே": ["Gnee", "44"],
        "ஞை": ["Gnae", "45"],
        "ஞொ": ["Gno", "46"],
        "ஞோ": ["Gnoa", "47"],
        "ஞௌ": ["Gnou", "48"],
        "ட": ["Ta", "49"],
        "டா": ["Taa", "50"],
        "டி": ["Ti", "51"],
        "டீ": ["Tee", "52"],
        "டு": ["Tu", "53"],
        "டூ": ["Too", "54"],
        "டெ": ["Te", "55"],
        "டே": ["Tee", "56"],
        "டை": ["Tai", "57"],
        "டொ": ["To", "58"],
        "டோ": ["Toa", "59"],
        "டௌ": ["Tou", "60"],
        "ண": ["Na", "73"],
        "ணா": ["Naa", "74"],
        "ணி": ["Ni", "75"],
        "ணீ": ["Nee", "76"],
        "ணு": ["Nu", "77"],
        "ணூ": ["Noo", "78"],
        "ணெ": ["Ne", "79"],
        "ணே": ["Nee", "80"],
        "ணை": ["Nai", "81"],
        "ணொ": ["No", "82"],
        "ணோ": ["Noa", "83"],
        "ணௌ": ["Nou", "84"],
        "த": ["Tha", "61"],
        "தா": ["Thaa", "62"],
        "தி": ["Thi", "63"],
        "தீ": ["Thee", "64"],
        "து": ["Thu", "65"],
        "தூ": ["Thoo", "66"],
        "தெ": ["The", "67"],
        "தே": ["Thee", "68"],
        "தை": ["Thai", "69"],
        "தொ": ["Tho", "70"],
        "தோ": ["Thoa", "71"],
        "தௌ": ["Thou", "72"],
        "ந": ["Na"],
        "நா": ["Naa"],
        "நி": ["Ni"],
        "நீ": ["Nee"],
        "நு": ["Nu"],
        "நூ": ["Noo"],
        "நெ": ["Ne"],
        "நே": ["Nee"],
        "நை": ["Nai"],
        "நொ": ["No"],
        "நோ": ["Noa"],
        "நௌ": ["Nou"],
        "ப": ["Pa", "85"],
        "பா": ["Paa", "86"],
        "பி": ["Pi", "87"],
        "பீ": ["Pee", "88"],
        "பு": ["Pu", "89"],
        "பூ": ["Poo", "90"],
        "பெ": ["Pe", "91"],
        "பே": ["Pee", "92"],
        "பை": ["Pai", "93"],
        "பொ": ["Po", "94"],
        "போ": ["Poa", "95"],
        "பௌ": ["Pou", "96"],
        "ம": ["Ma", "97"],
        "மா": ["Maa", "98"],
        "மி": ["Mi", "99"],
        "மீ": ["Mee", "100"],
        "மு": ["Mu", "101"],
        "மூ": ["Moo", "102"],
        "மெ": ["Me", "103"],
        "மே": ["Mee", "104"],
        "மை": ["Mai", "105"],
        "மொ": ["Mo", "106"],
        "மோ": ["Moa", "107"],
        "மௌ": ["Mou", "108"],
        "ய": ["Ya", "109"],
        "யா": ["Yaa", "110"],
        "யி": ["Yi", "111"],
        "யீ": ["Yee", "112"],
        "யு": ["Yu", '113'],
        "யூ": ["Yoo", "114"],
        "யெ": ["Ye", "115"],
        "யே": ["Yee", "116"],
        "யை": ["Yai", "117"],
        "யொ": ["Yo", "118"],
        "யோ": ["Yoa", "119"],
        "யௌ": ["You", "120"],
        "ர": ["Ra", "121"],
        "ரா": ["Raa", "122"],
        "ரி": ["Ri", "123"],
        "ரீ": ["Ree", "124"],
        "ரு": ["Ru", "125"],
        "ரூ": ["Roo", "126"],
        "ரெ": ["Re", "127"],
        "ரே": ["Ree", "128"],
        "ரை": ["Rai", "129"],
        "ரொ": ["Ro", "130"],
        "ரோ": ["Roa", "131"],
        "ரௌ": ["Rou", "132"],
        "ல": ["La", "133"],
        "லா": ["Laa", "134"],
        "லி": ["Li", "135"],
        "லீ": ["Lee", "136"],
        "லு": ["Lu", "137"],
        "லூ": ["Loo", "138"],
        "லெ": ["Le", "139"],
        "லே": ["Lee", "140"],
        "லை": ["Lai", "141"],
        "லொ": ["Lo", "143"],
        "லோ": ["Loa", "144"],
        "லௌ": ["Lou", "145"],
        "வ": ["Va", "146"],
        "வா": ["Vaa", "147"],
        "வி": ["Vi", "148"],
        "வீ": ["Vee", "149"],
        "வு": ["Vu", "150"],
        "வூ": ["Voo", "151"],
        "வெ": ["Ve", "152"],
        "வே": ["Vee", "153"],
        "வை": ["Vai", "154"],
        "வொ": ["Vo", "155"],
        "வோ": ["Voa", "156"],
        "வௌ": ["Vou", "157"],
        "ழ": ["Zha", "171"],
        "ழா": ["Zhaa", "172"],
        "ழி": ["Zhi", "173"],
        "ழீ": ["Zhee", "174"],
        "ழு": ["Zhu", "175"],
        "ழூ": ["Zhoo", "176"],
        "ழெ": ["Zhe", "177"],
        "ழே": ["Zhee", "178"],
        "ழை": ["Zhai", "179"],
        "ழொ": ["Zho", "180"],
        "ழோ": ["Zhoa", "181"],
        "ழௌ": ["Zhou", "182"],
        "ள": ["La", "158"],
        "ளா": ["Laa", "159"],
        "ளி": ["Li", "160"],
        "ளீ": ["Lee", "161"],
        "ளு": ["Lu", "162"],
        "ளூ": ["Loo", "163"],
        "ளெ": ["Le", "164"],
        "ளே": ["Lee", "165"],
        "ளை": ["Lai", "166"],
        "ளொ": ["Lo", "167"],
        "ளோ": ["Loa", "168"],
        "ளௌ": ["Lou", "169"],
        "ற": ["Ra", "183"],
        "றா": ["Raa", "184"],
        "றி": ["Ri", "185"],
        "றீ": ["Ree", "186"],
        "று": ["Ru", "187"],
        "றூ": ["Roo", "188"],
        "றெ": ["Re", "189"],
        "றே": ["Ree", "190"],
        "றை": ["Rai", "191"],
        "றொ": ["Ro", "192"],
        "றோ": ["Roa", "193"],
        "றௌ": ["Rou", "194"],
        "ன": ["Na", "195"],
        "னா": ["Naa", "196"],
        "னி": ["Ni", "197"],
        "னீ": ["Nee", "198"],
        "னு": ["Nu", "199"],
        "னூ": ["Noo", "200"],
        "னெ": ["Ne", "201"],
        "னே": ["Nee", '202'],
        "னை": ["Nai", "203"],
        "னொ": ["No", "204"],
        "னோ": ["Noa", "205"],
        "னௌ": ["Nou", "206"],
        "அ": ["A", "207"],
        "ஆ": ["Aa", "208"],
        "இ": ["I", "209"],
        "ஈ": ["Ee", "210"],
        "உ": ["U", "211"],
        "ஊ": ["Oo", "212"],
        "எ": ["E", "213"],
        "ஏ": ["Yae", "214"],
        "ஐ": ["Ye", "215"],
        "ஒ": ["O", "216"],
        "ஓ": ["Oh", "217"],
        "ஔ": ["Ow", "218"],
        "ஃ": ["Ak", "219"],
        "க்": ["ik", "220"],
        "ங்": ["ing", "221"],
        "ச்": ["ich", "222"],
        "ஞ்": ["inj", "223"],
        "ட்": ["it", "224"],
        "ண்": ["in", "225"],
        "த்": ["ith", "226"],
        "ந்": ["inth", "227"],
        "ப்": ["ip", "228"],
        "ம்": ["im", "229"],
        "ய்": ["iy", "230"],
        "ர்": ["ir", "231"],
        "ல்": ["il", "232"],
        "வ்": ["iv", "233"],
        "ழ்": ["izh", "234"],
        "ள்": ["il", "235"],
        "ற்": ["ir", "236"],
        "ன்": ["in", "237"],
    }

    with open("tamil_phonetic.json", "w") as file:
        json.dump(phonetic_tamil_dict, file)
