from re_scan import Scanner

scanner = Scanner([
    ('whitespace', r'\s+'),
    ('plus', r'\+'),
    ('minus', r'\-'),
    ('mult', r'\*'),
    ('div', r'/'),
    ('num', r'\d+'),
    ('paren_open', r'\('),
    ('paren_close', r'\)'),
])

for token, match in scanner.scan('(1 + 2) * 3'):
    print (token, match.group())
