def match_pattern(text, pattern):
    pattern = pattern[1:-1]
    matches = []

    if pattern.startswith('[') and pattern.endswith(']'):
        content = pattern[1:-1]

        if content.startswith('^'):
            excluded = content[1:]
            for i, ch in enumerate(text):
                if ch not in excluded:
                    matches.append((i, ch))
        else:
            allowed = content
            for i, ch in enumerate(text):
                if ch in allowed:
                    matches.append((i, ch))
    else:
        plen = len(pattern)
        for i in range(len(text) - plen + 1):
            if text[i:i+plen] == pattern:
                matches.append((i, text[i:i+plen]))

    return matches

text = input("Enter the string: ")
pattern = input("Enter the pattern (e.g., /at/): ")

result = match_pattern(text, pattern)

print("\nMatches found:")
for pos, val in result:
    print(f"Position {pos}: {val}")