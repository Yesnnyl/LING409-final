import nltk
from nltk import parse_cfg, ChartParser
from random import choice

def produce(finalgrammar, symbol):
    words = []
    productions = finalgrammar.productions(lhs = symbol)
    production = choice(productions)
    for sym in production.rhs():
        if isinstance(sym, str):
            words.append(sym)
        else:
            words.extend(produce(finalgrammar, sym))
    return words

finalgrammar = nltk.data.load('file:grammarfinal.cfg',cache=False)

parser = ChartParser(finalgrammar)
gr = parser.finalgrammar()
print ' '.join(produce(gr,gr.start()))
