from re_scan import Scanner


scanner = Scanner([
    ('bold', '\*\*'),
    ('link_special', '\[\[(?P<target>.*?)\|(?P<text>.*?)\]\]'),
    ('link', '\[\[(.*?)\]\]'),
    ('underline', '_'),
])

input_text = 'Hello **World**! [[Stuff|extra]] _[[Stuff]]_.'

for token, match in scanner.scan_with_holes(input_text):
    if token is None:
        print 'hole', match
    else:
        print 'token', (token, match.groups(),
                        match.groupdict(), match.group())
