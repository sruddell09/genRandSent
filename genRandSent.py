import random, sys

def pad(n, line):
    pad_line = '<s> ' * (n - 1)
    pad_line += line.strip()
    pad_line += ' </s>'

    return pad_line

def update_dict(n, line, d):
    line = pad(n, line)
    words = line.split()

    for i in range(0, len(words) - (n - 1)):
        n_gram = words[i: i + n]
        prefix = ' '.join(n_gram[:-1])
        word = n_gram[-1]
        if not prefix in d:
            d[prefix] = []
        d[prefix].append(word)

    return d

def rand_sent(n, d):
    sent = ''
    prefix = '<s> ' * (n - 1)
    prefix = prefix.strip()
    word = ''
    while word != '</s>':
        rand = d[prefix]
        word = random.choice(rand)
        if word != '</s>':
            sent += word + ' '
            n_gram = prefix + ' ' + word
            suffix = n_gram.split()[1:]
            prefix = ' '.join(suffix)

    return sent.strip()
    

if __name__ == '__main__':

    d = {}
    n = int(raw_input("Enter size of n-gram: "))
    sents = int(raw_input("Enter amount of sentence you would like to generate: "))
    
    f = open("bs.txt")
    for line in lines:
        update_dict(n, line, d)
    f.close()

    for i in range(sents):
        print str(i + 1) + ' ' + rand_sent(n, d)
