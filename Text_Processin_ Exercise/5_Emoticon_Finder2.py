text = input()
print("\n".join([f"{text[x]}{text[x+1]}" for x in range(len(text)) if text[x] ==":" and not text[x+1].isdigit()]))
