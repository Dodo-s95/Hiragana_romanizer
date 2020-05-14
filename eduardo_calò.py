#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""Supplementary excercise: Hepburn romanization by Eduardo Calò"""


def extract_hiragana():
    """Extracts hiragana from the csv"""
    with open("hiragana.csv") as hiragana:
        return ",".join(list(hiragana)).split(",")


def extract_transcriptions():
    """Extracts transcriptions from the csv"""
    with open("transcriptions.csv") as transcriptions:
        return ",".join(list(transcriptions)).split(",")


def dictionary():
    """Creates a dictionary with all the 107 hiragana.
    The method used is combination of basic hiragana with other elements.
    """

    # Creates dirty preliminary dictionary
    # with what's been extracted from the csv files
    raw_dict = dict(zip(extract_hiragana(), extract_transcriptions()))

    # Cleaning process
    # Changes last key to solve tabulation error in original file
    raw_dict["ん"] = raw_dict.pop("ん\t\t\u3000 \t\u3000 \t\u3000 \t\n")
    raw_dict["ん"] = "n"  # To eliminate end-of-line

    # Creates clean gojuon by deleting unwanted data from raw_dict
    gojuon = {k: v for k, v in raw_dict.items() if k != v}
    gojuon["ん"] = "ん"  # To allow proper handling later

    # Creation of dictionaries for dakuten, handakuten and palatalized sounds
    # finally merged into a final one

    # Dakuten and handakuten
    dict_g = {k + "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}":
              v.replace("k", "g") for k, v in gojuon.items() if v[0] == "k"}
    dict_z = {k + "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}":
              v.replace("s", "z") for k, v in gojuon.items() if v[0] == "s"}
    dict_d = {k + "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}":
              v.replace("t", "d") for k, v in gojuon.items() if v[0] == "t"}
    dict_b = {k + "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}":
              v.replace("h", "b") for k, v in gojuon.items() if v[0] == "h"}
    dict_p = {k + "\N{COMBINING KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK}":
              v.replace("h", "p") for k, v in gojuon.items() if v[0] == "h"}
    dak_dic = {**gojuon, **dict_g, **dict_z, **dict_d, **dict_b, **dict_p}

    # Palatalized sounds
    dict_ya = {k + "\N{HIRAGANA LETTER SMALL YA}": v.replace(
        "i", "ya") for k, v in dak_dic.items() if v[-1] == "i" and len(v) != 1}
    dict_yu = {k + "\N{HIRAGANA LETTER SMALL YU}": v.replace(
        "i", "yu") for k, v in dak_dic.items() if v[-1] == "i" and len(v) != 1}
    dict_yo = {k + "\N{HIRAGANA LETTER SMALL YO}": v.replace(
        "i", "yo") for k, v in dak_dic.items() if v[-1] == "i" and len(v) != 1}
    final_dict = {**dak_dic, **dict_ya, **dict_yu, **dict_yo}

    # Adding exceptions
    final_dict["ふ" +
               "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}"] = "bu"
    final_dict["ふ" +
               "\N{COMBINING KATAKANA-HIRAGANA SEMI-VOICED SOUND MARK}"] = "pu"
    final_dict["つ" +
               "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}"] = "zu"
    final_dict["し" +
               "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}"] = "ji"
    final_dict["ち" +
               "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}"] = "ji"
    final_dict["し" + "\N{HIRAGANA LETTER SMALL YA}"] = "sha"
    final_dict["し" + "\N{HIRAGANA LETTER SMALL YU}"] = "shu"
    final_dict["し" + "\N{HIRAGANA LETTER SMALL YO}"] = "sho"
    final_dict["し" + "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}" +
               "\N{HIRAGANA LETTER SMALL YA}"] = "ja"
    final_dict["し" + "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}" +
               "\N{HIRAGANA LETTER SMALL YU}"] = "ju"
    final_dict["し" + "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}" +
               "\N{HIRAGANA LETTER SMALL YO}"] = "jo"
    final_dict["ち" + "\N{HIRAGANA LETTER SMALL YA}"] = "cha"
    final_dict["ち" + "\N{HIRAGANA LETTER SMALL YU}"] = "chu"
    final_dict["ち" + "\N{HIRAGANA LETTER SMALL YO}"] = "cho"
    final_dict["ち" + "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}" +
               "\N{HIRAGANA LETTER SMALL YA}"] = "ja"
    final_dict["ち" + "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}" +
               "\N{HIRAGANA LETTER SMALL YU}"] = "ju"
    final_dict["ち" + "\N{COMBINING KATAKANA-HIRAGANA VOICED SOUND MARK}" +
               "\N{HIRAGANA LETTER SMALL YO}"] = "jo"
    final_dict["っ"] = "っ"  # To allow proper handling later
    return final_dict


def vowel(string: str, long_vowel) -> str:
    """Handles the values for long_vowel keyword argument"""
    if long_vowel == "native":
        return string
    elif long_vowel == "h":
        new_a = string.replace("aa", "ah")
        new_e = new_a.replace("ee", "eh")
        new_i = new_e.replace("ii", "ih")
        new_o = new_i.replace("oo", "oh")
        new_u = new_o.replace("ou", "oh")
        new_string = new_u.replace("uu", "uh")
        return new_string
    elif long_vowel == "macron":
        new_a = string.replace("aa", "\N{LATIN SMALL LETTER A WITH MACRON}")
        new_e = new_a.replace("ee", "\N{LATIN SMALL LETTER E WITH MACRON}")
        new_i = new_e.replace("ii", "\N{LATIN SMALL LETTER I WITH MACRON}")
        new_o = new_i.replace("oo", "\N{LATIN SMALL LETTER O WITH MACRON}")
        new_u = new_o.replace("ou", "\N{LATIN SMALL LETTER O WITH MACRON}")
        new_string = new_u.replace(
            "uu", "\N{LATIN SMALL LETTER U WITH MACRON}")
        return new_string


def hepburn_sing(text: str, long_vowel) -> str:
    """Basic function to transcribe single token string

    Input = string

    The function processes the string by splitting it
    into smaller strings made of 3, 2 and 1 characters.

    The function begins the process with the first 3-gram of the string.
    It looks for that 3-gram in the dictionary keys.
    If the function finds the 3-gram, then it replaces the key with the value.
    And it goes on with the next 3-gram.

    If the function doesn't find the first 3-gram, it tries the above process
    with the first 2-gram of the string. If positive, replacement occurs,
    the function goes on and tries the process with the next 3-gram.
    If negative, it goes with the single character.
    If even the single character is not in the dictionary, raises ValueError.

    It keeps doing this until the end of the word.
    Then it handles "っ" and "ん" specificities.

    It finally calls vowel() function to handle the vowels properly.

    Output = transcribed string
    """

    if text == "":  # To prevent empty string output
        raise ValueError

    get_dictionary = dictionary()
    transcript = ""
    # These values are the initial and final indexes of n-grams
    i = 0
    t = 0
    a = 0
    y = 3
    z = 2
    b = 1
    while y < len(text) + 3 and z < len(text) + 3 and b < len(text) + 3:
        # To avoid infinite loop
        split_3_by_3 = text[i:y]
        split_2_by_2 = text[t:z]
        ch = text[a:b]
        if split_3_by_3 in get_dictionary.keys():
            transcript += get_dictionary[split_3_by_3]
            i += 3
            y += 3
            t += 3
            z += 3
            a += 3
            b += 3
        elif split_2_by_2 in get_dictionary.keys():
            transcript += get_dictionary[split_2_by_2]
            i += 2
            y += 2
            t += 2
            z += 2
            a += 2
            b += 2
        elif ch in get_dictionary.keys():
            transcript += get_dictionary[ch]
            i += 1
            y += 1
            t += 1
            z += 1
            a += 1
            b += 1
        else:
            raise ValueError

    # Specificities handling
    if "っ" in transcript:  # Handles sokuon according to the following letter
        transcript = transcript.replace(
            "っ", transcript[transcript.index("っ") + 1])
    if "ん" in transcript:  # To handle "n" accordingly
        if transcript[-1] == "ん":
            transcript = transcript.replace("ん", "n")
        elif transcript[-1] != "ん":
            if transcript[transcript.index(
                    "ん") + 1] in ["a", "e", "i", "o", "u", "n"]:
                transcript = transcript.replace("ん", "n'")
            else:
                transcript = transcript.replace("ん", "n")
    final_transcript = vowel(transcript, long_vowel)
    return final_transcript


def hepburn_multi(*text: str, long_vowel) -> list:
    """Handles the cases when input is made of multiple strings"""
    for token in text:
        if " " in token:
            raise ValueError  # To prevent multiple words in single string
    return [hepburn_sing(token, long_vowel) for token in text]


def hepburn_list(list_text: list, long_vowel) -> list:
    """Handles the cases when input is made of single list"""
    for token in list_text:
        if " " in token:
            raise ValueError  # To prevent multiple words in single string
    return [hepburn_sing(token, long_vowel) for token in list_text]


def hepburn_space(text: str, long_vowel) -> list:  # Only U+0020 space
    """Handles the cases when input is made of single string with spaces"""
    return [hepburn_sing(item, long_vowel) for item in text.split(" ")]


def hepburn(*data: str or list, long_vowel="macron", **kwargs) -> list:
    """Main function:

    After checking validity of arguments,
    redirects each case to the dedicated function
    """

    # Check correctness of keyword argument
    if len(kwargs.items()) > 0:
        raise ValueError

    # Check validity of long_vowel flag
    if long_vowel not in ["macron", "h", "native"]:
        raise ValueError

    # Check validity of input data
    if len(data) == 1:
        if isinstance(data[0], list):
            if len(data[0]) == 1:  # To prevent single string in list
                raise ValueError
            else:
                pass
        elif isinstance(data[0], str):
            pass
        else:
            raise ValueError
    elif len(data) > 1:
        for element in data:
            if not isinstance(element, str):
                raise ValueError
    else:
        raise ValueError

    # Main function
    if isinstance(data[0], list):
        return hepburn_list(data[0], long_vowel)
    elif len(data) > 1:
        return hepburn_multi(*data, long_vowel=long_vowel)
    elif " " in data[0]:
        if data[0][-1] == " " or data[0][0] == " ":
            raise ValueError
        else:
            return hepburn_space(data[0], long_vowel)
    else:
        return [hepburn_sing(data[0], long_vowel)]
