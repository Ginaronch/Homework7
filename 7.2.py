def correct_sentence(text):
    text = text[0].capitalize() + text[1:]
    if text.endswith("."):
        return text
    else:
        return text+"."
assert correct_sentence("greetings, friends") == "Greetings, friends."
assert correct_sentence("hello") == "Hello."
assert correct_sentence("Greetings. Friends") == "Greetings. Friends."
assert correct_sentence("Greetings, friends.") == "Greetings, friends."
assert correct_sentence("greetings, friends.") == "Greetings, friends."
print('ОК')