import MeCab

wakati = MeCab.Tagger()
result = wakati.parse("すもももももももものうち")

print(result)