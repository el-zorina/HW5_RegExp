import os
import re
import shutil


def to_salty(text):
    # Add "с" + same vowel after every vowel.
    vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯ'
    result = ''
    for ch in text:
        result = result + ch
        if ch in vowels:
            result = result + 'с' + ch
    return result


def find_chords(path):
    # A chord line: every word starts with a Latin letter A-G.
    chords = set()
    f = open(path, encoding='utf-8')
    for line in f:
        line = line.strip()
        if line == '':
            continue
        words = line.split()
        ok = True
        for w in words:
            if w[0] not in 'ABCDEFG':
                ok = False
                break
        if ok:
            for w in words:
                chords.add(w)
    f.close()
    return chords


def rename_files(dir, pattern, new_pattern=None, sample_names=None, to_replace=False):
    files = os.listdir(dir)
    for f in files:
        if not re.search(pattern, f):
            continue

        new_f = f
        if new_pattern is not None:
            new_f = re.sub(pattern, new_pattern, new_f)
        if sample_names is not None:
            for key in sample_names:
                new_f = new_f.replace(key, sample_names[key])

        old_path = os.path.join(dir, f)
        new_path = os.path.join(dir, new_f)

        if old_path == new_path:
            continue

        if to_replace:
            os.rename(old_path, new_path)
        else:
            shutil.copy(old_path, new_path)
