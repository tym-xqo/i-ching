# I Ching

A simple little Python 3 script to cast an I Ching hexagram using real random data from [random.org](https://random.org). While it doesn't even attempt to programmatically recreate the entire yarrow stalk method step by step, it does proceed line by line, and the random output is weighted across old and young, yin and yang, to represent that method's probabilites, at least according to [the Wikipedia](https://en.wikipedia.org/wiki/I_Ching_divination#Yarrow_stalks). (It gracefully falls back to the Python [`secrets` module](https://docs.python.org/3/library/secrets.html) for random data if offline or random.org otherwise unreachable.)

Uses only standard library. There are a couple f-strings, so it requires python 3.6 or higher. Given that, you should be able to clone this repo and then just `python3 i.py` to use.

Output gives the [King Wen sequence](https://en.wikipedia.org/wiki/King_Wen_sequence) number, the name of the cast hexagram according to [the Wilhelm translation](http://www2.unipr.it/~deyoung/I_Ching_Wilhelm_Translation.html), and a unicode symbol of the hexagram, followed by a plain-text diagram of the hexagram indicating which lines are changing; — then the same for the hexagram derived by transforming the changing lines. (In case all lines in the cast hexagram are stable, only the one hexagram is printed.) For example:

```txt
Hexagram: 64. Wei Chi / Before Completion ䷿
         =======
         ==   ==
         =======
         == x ==
         ===o===
         ==   ==
Changing to: 56. Lü / The Wanderer ䷷
         =======
         ==   ==
         =======
         =======
         ==   ==
         ==   ==
```

Contributions always welcome.
