def generate_hashtag(s):
    if len(s)>140 or len(s)==0:
        return False
    s=s.split()
    s1='#'
    for i in s:
        if i==" ":
            continue
        s1+=i.capitalize()
    return (s1)
print(generate_hashtag("Hello there thanks for trying my Kata"))
print(generate_hashtag("    Hello    World    "))
print(generate_hashtag(''))