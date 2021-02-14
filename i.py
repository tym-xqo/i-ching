#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import secrets
import urllib.request
from urllib.error import URLError

# TODO: use these cool unicode hexagrams in the output
"""
01 ䷀	02 ䷁	03 ䷂	04 ䷃	05 ䷄	06 ䷅	07 ䷆	08 ䷇	09 ䷈	10 ䷉	11 ䷊	12 ䷋	13 ䷌	14 ䷍	15 ䷎	16 ䷏
17 ䷐	18 ䷑	19 ䷒	20 ䷓	21 ䷔	22 ䷕	23 ䷖	24 ䷗	25 ䷘	26 ䷙	27 ䷚	28 ䷛	29 ䷜	30 ䷝	31 ䷞	32 ䷟
33 ䷠	34 ䷡	35 ䷢	36 ䷣	37 ䷤	38 ䷥	39 ䷦	40 ䷧	41 ䷨	42 ䷩	43 ䷪	44 ䷫	45 ䷬	46 ䷭	47 ䷮	48 ䷯
49 ䷰	50 ䷱	51 ䷲	52 ䷳	53 ䷴	54 ䷵	55 ䷶	56 ䷷	57 ䷸	58 ䷹	59 ䷺	60 ䷻	61 ䷼	62 ䷽	63 ䷾	64 ䷿
"""


def throw_hexagram():
    url = (
        "https://www.random.org/integers/"
        "?num=6&min=0&max=15&col=1&base=10&format=plain&rnd=new"
    )
    try:
        get = urllib.request.urlopen(url).read().decode("utf-8").strip()
        throw = get.split("\n")
        throw = [int(i) for i in throw]
    except URLError:
        throw = [secrets.randbelow(16) for i in range(6)]

    prob = [6, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 7, 7, 7, 7, 7]
    hexagram = []
    for i in throw:
        x = prob[i]
        hexagram.append(x)
    return hexagram


def binary_hexagram(hexagram):
    binary_list = []
    for i in hexagram:
        if i in (7, 9):
            binary_list.append("1")
        else:
            binary_list.append("0")
    binary_hexagram = "".join(binary_list)
    return binary_hexagram


def lookup_hexagram_title(hexagram):
    titles = {
        "111111": "1. Ch'ien / The Creative",
        "000000": "2. K'un / The Receptive",
        "100010": "3. Chun / Difficulty at the Beginning",
        "010001": "4. Mêng / Youthful Folly",
        "111010": "5. Hsü / Waiting (Nourishment)",
        "010111": "6. Sung / Conflict",
        "010000": "7. Shih / The Army",
        "000010": "8. Pi / Holding Together [union]",
        "111011": "9. Hsiao Ch'u / The Taming Power of the Small",
        "110111": "10. Lü / Treading [conduct]",
        "111000": "11. T'ai / Peace",
        "000111": "12. P'i / Standstill [Stagnation]",
        "101111": "13. T'ung Jên / Fellowship with Men",
        "111101": "14. Ta Yu / Possession in Great Measure",
        "001000": "15. Ch'ien / Modesty",
        "000100": "16. Yü / Enthusiasm",
        "100110": "17. Sui / Following",
        "011001": "18. Ku / Work on what has been spoiled [ Decay ]",
        "110000": "19. Lin / Approach",
        "000011": "20. Kuan / Contemplation (View)",
        "100101": "21. Shih Ho / Biting Through",
        "101001": "22. Pi / Grace",
        "000001": "23. Po / Splitting Apart",
        "100000": "24. Fu / Return (The Turning Point)",
        "100111": "25. Wu Wang / Innocence (The Unexpected)",
        "111001": "26. Ta Ch'u / The Taming Power of the Great",
        "100001": "27. I / Corners of the Mouth (Providing Nourishment)",
        "011110": "28. Ta Kuo / Preponderance of the Great",
        "010010": "29. K'an / The Abysmal (Water)",
        "101101": "30. Li / The Clinging, Fire",
        "001110": "31. Hsien / Influence (Wooing)",
        "011100": "32. Hêng / Duration",
        "001111": "33. TUN / Retreat",
        "111100": "34. Ta Chuang / The Power of the Great",
        "000101": "35. Chin / Progress",
        "101000": "36. Ming I / Darkening of the light",
        "101011": "37. Chia Jên / The Family [The Clan]",
        "110101": "38. K'uei / Opposition",
        "001010": "39. Chien / Obstruction",
        "010100": "40. Hsieh / Deliverance",
        "110001": "41. Sun / Decrease",
        "100011": "42. I / Increase",
        "111110": "43. Kuai / Break-through (Resoluteness)",
        "011111": "44. Kou / Coming to Meet",
        "000110": "45. Ts'ui / Gathering Together [Massing]",
        "011000": "46. Shêng / Pushing Upward",
        "010110": "47. K'un / Oppression (Exhaustion)",
        "011010": "48. Ching / The Well",
        "101110": "49. Ko / Revolution (Molting)",
        "011101": "50. Ting / The Caldron",
        "100100": "51. Chên / The Arousing (Shock, Thunder)",
        "001001": "52. Kên / Keeping Still, Mountain",
        "001011": "53. Chien / Development (Gradual Progress)",
        "110100": "54. Kuei Mei / The Marrying Maiden",
        "101100": "55. Fêng / Abundance [Fullness]",
        "001101": "56. Lü / The Wanderer",
        "011011": "57. Sun / The Gentle (The Penetrating, Wind)",
        "110110": "58. Tui / The Joyous, Lake",
        "010011": "59. Huan / Dispersion [Dissolution]",
        "110010": "60. Chieh / Limitation",
        "110011": "61. Chung Fu / Inner Truth",
        "001100": "62. Hsiao Kuo / Preponderance of the Small",
        "101010": "63. Chi Chi / After Completion",
        "010101": "64. Wei Chi / Before Completion",
    }
    bingram = binary_hexagram(hexagram)
    title = titles[bingram]
    return title


def render_lines(hexagram):
    bottom_up = list(reversed(hexagram))
    map = {
        6: "         == x ==",
        7: "         =======",
        8: "         ==   ==",
        9: "         == o ==",
    }
    lines = [map[x] for x in bottom_up]
    render = "\n".join(lines)
    return render


def transform_changing_lines(hexagram):
    new_hexagram = []
    for i in hexagram:
        if i == 6:
            i = 7
        elif i == 9:
            i = 8
        new_hexagram.append(i)
    return new_hexagram


def main():
    hex_ = throw_hexagram()
    title = lookup_hexagram_title(hex_)
    lines = render_lines(hex_)
    hex_out = f"Hexagram: {title}\n{lines}"
    print(hex_out)
    if 6 in hex_ or 9 in hex_:
        next_hex = transform_changing_lines(hex_)
        next_title = lookup_hexagram_title(next_hex)
        next_lines = render_lines(next_hex)
        next_out = f"Changing to: {next_title}\n{next_lines}"
        print(next_out)


if __name__ == "__main__":
    main()
    # throw_hexagram()
