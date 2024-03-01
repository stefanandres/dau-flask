from random import randint

from flask import Flask, request

app = Flask(__name__)


class Dau():
    def __init__(self, text):
        self.text = text
    
    def switchchars(self, word):
        # Switch random neighbour Characters
        # e.g. "hello" becomes "ehllo"

        chars = list(word)
        if len(chars) < 1:
          return "".join(chars)

        first = randint(0, len(chars) - 1)
        if first == (len(chars) -1):
            first = first -1
        second = first + 1

        # Swap chars
        tmp = chars[first]
        chars[first] = chars[second]
        chars[second] = tmp
        return "".join(chars)

    def misspell(self, words):
        # Misspell words 1/3 of the time

        i = 0 
        ret = ""

        words = words.split(" ")
        for word in words:
            i += 1
            if randint(1, 3) % 3 == 0:
                ret += " " + self.switchchars(word)
            else:
                ret += " " + word

        return ret

    def repeat(self, x, y):
        return x * y

    def repeat_single_chars(self, chars, rand=1):

        if not chars:
            return chars

        random_index = randint(0, len(chars)) % len(chars)
        random_char = chars[random_index]
        new_char = self.repeat(random_char, 1 + (randint(0, rand) % rand))
        chars.insert(random_index, new_char)
        return chars

    def moron(self, words):

        i = 0
        ret = ""
        words = words.split(" ")

        for word in words:
            if randint(1, 2) % 2 == 0:
                chars = list(word)

                if randint(1, 4) % 4 == 0:
                    ret += " " + "".join(self.repeat_single_chars(chars, 1))

                ret += " " + word
            else:
                ret += " " + word

        return ret
            

    def get_fillword(self):
      fillwords = ['EH', 'EEH', 'EHH', 'AEH', 'AEEH', 'AEEHHH'];
      ret = fillwords[randint(0, len(fillwords)) % len(fillwords)]
      return ret;

    def stutter(self, words):
        # Insert get_fillword() every 50% of time to the text

        ret = ""
        words = words.split(" ")

        for word in words:
            if randint(1, 2) % 2 == 0:
                ret += " " + self.get_fillword() + " , "
            ret += " " + word

        return ret

    def eol(self, words):
        # Add end-of-line exclamations
        base = ' !?!?!?!1';
        chars = list(base)

        for _ in range(5):
            chars = self.repeat_single_chars(chars, 3)

        return words + "".join(chars)

    def dauify(self):
        dauify = self.text.upper()
        dauify = self.misspell(dauify)
        dauify = self.moron(dauify)
        dauify = self.stutter(dauify)
        dauify = self.eol(dauify) + '\n'

        return dauify

    def __repr__(self):
        return self.dauify()
    def __str__(self):
        return self.dauify()


@app.route('/')
def root():
    return '🫠'

@app.route('/<path:Url>')
def dauify(Url):
    dau = Dau(Url)

    return str(dau)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
