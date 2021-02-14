#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

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
        x = random.choice(prob)
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
    ahex = {}
    ahex["111111"] = 1
    ahex["000000"] = 2
    ahex["100010"] = 3
    ahex["010001"] = 4
    ahex["111010"] = 5
    ahex["010111"] = 6
    ahex["010000"] = 7
    ahex["000010"] = 8
    ahex["111011"] = 9
    ahex["110111"] = 10
    ahex["111000"] = 11
    ahex["000111"] = 12
    ahex["101111"] = 13
    ahex["111101"] = 14
    ahex["001000"] = 15
    ahex["000100"] = 16
    ahex["100110"] = 17
    ahex["011001"] = 18
    ahex["110000"] = 19
    ahex["000011"] = 20
    ahex["100101"] = 21
    ahex["101001"] = 22
    ahex["000001"] = 23
    ahex["100000"] = 24
    ahex["100111"] = 25
    ahex["111001"] = 26
    ahex["100001"] = 27
    ahex["011110"] = 28
    ahex["010010"] = 29
    ahex["101101"] = 30
    ahex["001110"] = 31
    ahex["011100"] = 32
    ahex["001111"] = 33
    ahex["111100"] = 34
    ahex["000101"] = 35
    ahex["101000"] = 36
    ahex["101011"] = 37
    ahex["110101"] = 38
    ahex["001010"] = 39
    ahex["010100"] = 40
    ahex["110001"] = 41
    ahex["100011"] = 42
    ahex["111110"] = 43
    ahex["011111"] = 44
    ahex["000110"] = 45
    ahex["011000"] = 46
    ahex["010110"] = 47
    ahex["011010"] = 48
    ahex["101110"] = 49
    ahex["011101"] = 50
    ahex["100100"] = 51
    ahex["001001"] = 52
    ahex["001011"] = 53
    ahex["110100"] = 54
    ahex["101100"] = 55
    ahex["001101"] = 56
    ahex["011011"] = 57
    ahex["110110"] = 58
    ahex["010011"] = 59
    ahex["110010"] = 60
    ahex["110011"] = 61
    ahex["001100"] = 62
    ahex["101010"] = 63
    ahex["010101"] = 64
    with open("iching-title.txt", "r") as i:
        chis = i.readlines()
    chi = chis[ahex[bingram] - 1]
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
