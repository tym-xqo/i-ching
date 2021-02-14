#!/usr/bin/env python
# -*- coding: utf-8 -*-
import secrets

# TODO: get these  unicode hexagrams into the output
"""
01 ䷀	02 ䷁	03 ䷂	04 ䷃	05 ䷄	06 ䷅	07 ䷆	08 ䷇	09 ䷈	10 ䷉	11 ䷊	12 ䷋	13 ䷌	14 ䷍	15 ䷎	16 ䷏
17 ䷐	18 ䷑	19 ䷒	20 ䷓	21 ䷔	22 ䷕	23 ䷖	24 ䷗	25 ䷘	26 ䷙	27 ䷚	28 ䷛	29 ䷜	30 ䷝	31 ䷞	32 ䷟
33 ䷠	34 ䷡	35 ䷢	36 ䷣	37 ䷤	38 ䷥	39 ䷦	40 ䷧	41 ䷨	42 ䷩	43 ䷪	44 ䷫	45 ䷬	46 ䷭	47 ䷮	48 ䷯
49 ䷰	50 ䷱	51 ䷲	52 ䷳	53 ䷴	54 ䷵	55 ䷶	56 ䷷	57 ䷸	58 ䷹	59 ䷺	60 ䷻	61 ䷼	62 ䷽	63 ䷾	64 ䷿
"""


def throw_hexagram():
    prob = [6, 8, 8, 8, 8, 8, 8, 8, 9, 9, 9, 7, 7, 7, 7, 7]
    hexagram = []
    for i in range(0, 6):
        x = secrets.choice(prob)
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


def lookup_hexagram_number(hexagram):
    bingram = binary_hexagram(hexagram)
    bhex = {}
    bhex["111111"] = 1
    bhex["000000"] = 2
    bhex["100010"] = 3
    bhex["010001"] = 4
    bhex["111010"] = 5
    bhex["010111"] = 6
    bhex["010000"] = 7
    bhex["000010"] = 8
    bhex["111011"] = 9
    bhex["110111"] = 10
    bhex["111000"] = 11
    bhex["000111"] = 12
    bhex["101111"] = 13
    bhex["111101"] = 14
    bhex["001000"] = 15
    bhex["000100"] = 16
    bhex["100110"] = 17
    bhex["011001"] = 18
    bhex["110000"] = 19
    bhex["000011"] = 20
    bhex["100101"] = 21
    bhex["101001"] = 22
    bhex["000001"] = 23
    bhex["100000"] = 24
    bhex["100111"] = 25
    bhex["111001"] = 26
    bhex["100001"] = 27
    bhex["011110"] = 28
    bhex["010010"] = 29
    bhex["101101"] = 30
    bhex["001110"] = 31
    bhex["011100"] = 32
    bhex["001111"] = 33
    bhex["111100"] = 34
    bhex["000101"] = 35
    bhex["101000"] = 36
    bhex["101011"] = 37
    bhex["110101"] = 38
    bhex["001010"] = 39
    bhex["010100"] = 40
    bhex["110001"] = 41
    bhex["100011"] = 42
    bhex["111110"] = 43
    bhex["011111"] = 44
    bhex["000110"] = 45
    bhex["011000"] = 46
    bhex["010110"] = 47
    bhex["011010"] = 48
    bhex["101110"] = 49
    bhex["011101"] = 50
    bhex["100100"] = 51
    bhex["001001"] = 52
    bhex["001011"] = 53
    bhex["110100"] = 54
    bhex["101100"] = 55
    bhex["001101"] = 56
    bhex["011011"] = 57
    bhex["110110"] = 58
    bhex["010011"] = 59
    bhex["110010"] = 60
    bhex["110011"] = 61
    bhex["001100"] = 62
    bhex["101010"] = 63
    bhex["010101"] = 64
    with open("iching-title.txt", "r") as i:
        chis = i.readlines()
    chi = chis[bhex[bingram] - 1]
    return chi


def transform_changing_lines(hexagram):
    new_hexagram = []
    for i in hexagram:
        if i == 6:
            i = 7
        elif i == 9:
            i = 8
        new_hexagram.append(i)
    return new_hexagram


def render_lines(hexagram):
    bottom_up = list(reversed(hexagram))
    map = {6: "== x ==", 7: "=======", 8: "==   ==", 9: "== o =="}
    lines = [map[x] for x in bottom_up]
    render = "\n".join(lines)
    return render


def main():
    hex_ = throw_hexagram()
    number = lookup_hexagram_number(hex_)
    next_hex = transform_changing_lines(hex_)
    next_number = lookup_hexagram_number(next_hex)
    lines = render_lines(hex_)
    next_lines = render_lines(next_hex)
    output = (
        f"Hexagram number: {number}{lines}\n" f"Changing to: {next_number}{next_lines}"
    )
    print(output)


if __name__ == "__main__":
    main()
