
emoticon_dict={
':‑)':'happy',
':\)':'happy',
':-]':'happy',
':]':'happy',
':-3':'happy',
':3':'happy',
':->':'happy',
':>':'happy',
'8-)':'happy',
'8)':'happy',
':-}':'happy',
':}':'happy',
':o)':'happy',
':c)':'happy',
':^)':'happy',
'=]':'happy',
'=)':'happy',
':‑D':'laughing',
':D':'laughing',
'8‑D':'laughing',
'8D':'laughing',
'x‑D':'laughing',
'xD':'laughing',
'X‑D':'laughing',
'XD':'laughing',
'=D':'laughing',
'=3':'laughing',
'B^D':'laughing',
':-))':'very happy',
':‑(':'sad',
':(':'sad',
':‑c':'sad',
':c':'sad',
':‑<':'sad',
':<':'sad',
':‑[':'sad',
':[':'sad',
':-||':'sad',
'>:[':'sad',
':{':'sad',
':@':'sad',
'>:(':'sad',
":'‑(":'cying',
":'(":'cying',
":'‑)":'happiness',
":')":'happiness',
'D8':'horror',
"DX" :'horror',
"D=" : 'horror',
":‑O":'surprise',
":O":'surprise',
":‑o":'surprise',
":o":'surprise',
":-0":'surprise',
"8‑0":'surprise',
">:O":'surprise',
":-*":'kiss',
":*":'kiss',
":×":'kiss',
";‑)":'wink',
";)":'wink',
"*-)":'wink',
"*)":'wink',
";‑]":'wink',
";]":'wink',
";^)":'wink',
":‑,":'wink',
";D":'wink',
":‑P":'playful',
":P":'playful',
"X‑P":'playful',
"XP":'playful',
"x‑p":'playful',
"xp":'playful',
":‑p":'playful',
":p":'playful',
":‑Þ":'playful',
":Þ":'playful',
":‑þ":'playful',
":þ":'playful',
":‑b":'playful',
":b":'playful',
"d:":'playful',
"=p":'playful',
">:P":'playful',
":‑/":'skeptical',
":/":'skeptical',
":‑.":'skeptical',
">:/":'skeptical',
"=/":'skeptical',
":L":'skeptical',
"=L\ ":'skeptical',
":S":'skeptical',
":‑|":'indecision',
":|":'indecision',
":$":'embarrassed',
"O:‑)":'innocent',
"O:)":'innocent',
"0:‑3":'innocent',
"0:3":'innocent',
"0:‑)":'innocent',
"0:)":'innocent',
"0;^)":'innocent',
">:‑)":"evil",
">:)":"evil",
"}:‑)":"evil",
"}:)":"evil",
"3:‑)":"evil",
"3:)":"evil",
">;)":"evil",
"|;‑)":"cool",
"|‑O":"cool",
"<_<": "guilty",
">_>": "guilty",
}

new_sentence =[]
    for word in review.split():
        if word in emoticon_dict:
            new_sentence.append(emoticon_dict[word])
        else:
            new_sentence.append(word)
    return ''.join(new_sentence)


