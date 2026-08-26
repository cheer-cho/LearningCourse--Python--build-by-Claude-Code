# Idiom drill: "if key in d: ... else: ..." ladders -> .get,
# .setdefault, try/except KeyError. The clunky "before" for the first
# two (kept out here, not inside any function, since tests inspect each
# function's own source for a stray `if`):
#
#     def _price_or_default_clunky(prices, item):
#         if item in prices:
#             return prices[item]
#         else:
#             return 0
#
#     def _tally_word_clunky(counts, word):
#         if word in counts:
#             counts[word] = counts[word] + 1
#         else:
#             counts[word] = 1
#         return counts
#
# Your job: replace each `raise NotImplementedError` with a rewrite
# that never uses the `if` keyword — reach for .get(), .setdefault(),
# or try/except KeyError instead.
# Run: uv run pytest 09-pythonic-deep-dive -k drill03


def price_or_default(prices, item):
    """Look up `item` in the `prices` dict, or 0 when it isn't priced.

    price_or_default({"apple": 2}, "apple") -> 2
    price_or_default({"apple": 2}, "banana") -> 0
    """
    raise NotImplementedError


def tally_word(counts, word):
    """Increment `word`'s count in `counts` (creating the entry the
    first time it's seen), and return `counts`.

    tally_word({}, "hi") -> {"hi": 1}
    tally_word({"hi": 1}, "hi") -> {"hi": 2}
    """
    raise NotImplementedError


def group_words_by_letter(bucket, word):
    """File `word` under its first letter in `bucket` (creating that
    letter's list the first time it's needed), and return `bucket`.

    group_words_by_letter({}, "cat") -> {"c": ["cat"]}
    group_words_by_letter({"c": ["cat"]}, "car") -> {"c": ["cat", "car"]}
    """
    raise NotImplementedError


def required_setting(config, key):
    """Return `config[key]`, or raise a clear KeyError naming the
    missing setting.

    required_setting({"host": "x"}, "host") -> "x"
    required_setting({}, "host") raises KeyError
    """
    raise NotImplementedError
