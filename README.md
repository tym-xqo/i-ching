I Ching

A simple little script to cast an I Ching hexagram. While it doesn't try to programmatically recreate the entire yarrow stalk method step by step, it weights output from [random.org](https://random.org) to represent the same probabilites, at least according to [the Wikipedia](https://en.wikipedia.org/wiki/I_Ching_divination#Yarrow_stalks). (Falls back to `secrets` module for random data if offline or random.org otherwise unreachable.)

Uses only standard library. There's are f-strings, so it does require python 3.6 or higher. But otherwise you should be able to clone this repo and then just `python3 i.py` to use.

Sort of a rough draft at this point, but works and produces resonably nice ascii output. Contributions always welcome.
