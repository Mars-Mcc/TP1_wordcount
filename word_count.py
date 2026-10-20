"""
Project TP1: Word Count
Le code te dit combien de mots et de charactères il y a dans une phrase que tu saisis (ne marche pas si tu saisis rien)
By: Mars McCullough groupe 404
2026-09-09
"""


def word_count():   
    nombre = sentence.split()
    print(f"le nombre de mots dans ta phrase est: {len(nombre)} ")


sentence = input("saisir votre phrase içi! ").strip()
print(f"le nombre de charactères dans ta phrase est:{str(len(sentence))}")
word_count()
