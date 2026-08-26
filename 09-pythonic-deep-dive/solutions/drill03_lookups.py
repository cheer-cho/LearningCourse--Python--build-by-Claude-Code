def price_or_default(prices, item):
    """Look up `item` in the `prices` dict, or 0 when it isn't priced.

    price_or_default({"apple": 2}, "apple") -> 2
    price_or_default({"apple": 2}, "banana") -> 0
    """
    return prices.get(item, 0)


def tally_word(counts, word):
    """Increment `word`'s count in `counts` (creating the entry the
    first time it's seen), and return `counts`.

    tally_word({}, "hi") -> {"hi": 1}
    tally_word({"hi": 1}, "hi") -> {"hi": 2}
    """
    counts[word] = counts.get(word, 0) + 1
    return counts


def group_words_by_letter(bucket, word):
    """File `word` under its first letter in `bucket` (creating that
    letter's list the first time it's needed), and return `bucket`.

    group_words_by_letter({}, "cat") -> {"c": ["cat"]}
    group_words_by_letter({"c": ["cat"]}, "car") -> {"c": ["cat", "car"]}
    """
    bucket.setdefault(word[0], []).append(word)
    return bucket


def required_setting(config, key):
    """Return `config[key]`, or raise a clear KeyError naming the
    missing setting.

    required_setting({"host": "x"}, "host") -> "x"
    required_setting({}, "host") raises KeyError
    """
    try:
        return config[key]
    except KeyError:
        raise KeyError(f"missing required setting: {key}") from None
