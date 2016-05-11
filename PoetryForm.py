import re


class PoetryForm:

    def __init__(self):

        self.pronouncing_dict = open("pronouncing_dictionary.txt").readlines()

    def get_structure(self, input_poem_file):

        input_poem = open(input_poem_file).readlines()
        last_words = [line.split(" ").pop().replace("\n", " ").replace(".", "").upper() for line in input_poem]
        rhyming_lines = [None]*len(last_words)

        last_pronunciations = []
        for word in last_words:
            while 1:
                result = self.find_in_dict(word)
                if result:
                    last_pronunciations.append(result)
                    break
                else:
                    word = word[:-1]

        current_letter = 'a'
        for ind_pronunciation, pronunciation in enumerate(last_pronunciations):
            for ind_sound, sound in enumerate(pronunciation):
                subset = "".join(pronunciation[-(ind_sound+1):])
                for ind_other, other_pronunciation in enumerate(last_pronunciations):
                    if ind_pronunciation == ind_other or rhyming_lines[ind_other]:
                        continue
                    if subset in other_pronunciation:
                        rhyming_lines[ind_pronunciation] = current_letter
                        rhyming_lines[ind_other] = current_letter
                        continue
                    #rhyming_lines[ind_pronunciation] = current_letter
            current_letter = chr(ord(current_letter) + 1)
        print("".join(rhyming_lines))

    def find_in_dict(self, word):

        for line in self.pronouncing_dict:
            if bool(re.search('^' + word, line)):
                line = line.split(" ")[2:]
                line.append(line.pop().rstrip())
                # print(line)
                return line
        return False

myPoem = PoetryForm()
myPoem.get_structure("input_poem.txt")



