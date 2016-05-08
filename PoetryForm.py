

class PoetryForm:

    def __init__(self):

        self.pronouncing_dict = open("pronouncing_dictionary.txt").readlines()

    def get_structure(self, input_poem_file):

        input_poem = open(input_poem_file).readlines()
        last_words = [line.split(" ").pop().replace("\n", " ").replace(".", "").upper() for line in input_poem]

        last_pronunciations = []
        for word in last_words:
            while 1:
                result = self.find_in_dict(word)
                if result:
                    last_pronunciations.append(result)
                    break
                else:
                    word = word[:-1]

    def find_in_dict(self, word):

        for line in self.pronouncing_dict:
            if word in line:
                line = line.split(" ")[2:]
                print(line)
                return line
        return False

myPoem = PoetryForm()
myPoem.get_structure("input_poem.txt")



