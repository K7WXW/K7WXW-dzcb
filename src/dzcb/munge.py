"""
dzcb.munge - replacements, filters, and modifications of the data
"""
import re

# These are used when generating channel names
Talkgroup_Channel_name_replacements = {
    "Audio Test": "A.Test",
    "California": "CA",
    "English": "Eng",
    "Hawaii": "HI",
    "Idaho": "ID",
    "Montana": "MT",
    "North America": "NA",
    "Oregon": "OR",
    "Utah": "UT",
    "Washington": "WA",
    "Worldwide": "WW",
}

def channel_name(ch_name, max_length):
    # Replace Long strings with shorter ones
    replacements = Talkgroup_Channel_name_replacements.copy()
    while len(ch_name) > max_length:
        if not replacements:
            break
        ch_name = ch_name.replace(*replacements.popitem())

    
    # Truncate the channel name (try to preserve the tail  characters
    # which are typically TG# and 3-digit Code)
    tail_code = re.search(r"[12]?\s[A-Z]+$", ch_name)
    if len(ch_name) > max_length and tail_code:
        n_tail = len(tail_code.group())
        if max_length > n_tail + 1:
            n_trunc = len(ch_name) - max_length
            ch_name = ch_name[:-n_trunc-n_tail] + ch_name[-n_tail:]

    return ch_name[:max_length]


def zone_name(zone_name, max_length):
    return zone_name[:max_length]
