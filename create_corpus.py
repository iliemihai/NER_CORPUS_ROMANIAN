import sys, time
from cube.api import Cube

def load_wiki_corpus(input_file):
    print("Loading corpus...")
    time1 = time.time()
    corpus_file = open(input_file, "r")
    corpus = corpus_file.read()
    time2 = time.time()
    total_time = time2-time1
    print("Took %0.3f seconds"%total_time)

    return corpus

LOCATIONS = ["București", ]
ORGANIZATIONS = ["Google"]
PERSONS = ["George", "Maria"]

if __name__ == "__main__":

    if len(sys.argv) !=2:
        print("Nu ai adaugat argument pt corpus!")
        sys.exit(1)

    file_out = open("NER.conll", "w")
    cube = Cube(verbose=True)
    cube.load("ro")
    corpus = load_wiki_corpus(sys.argv[1])
    sentences = cube(corpus)

    for sentence in sentences:
        for entry in sentence:
            if ("PROPN" in entry.upos):
                if (entry.word in PERSONS):
                    file_out.write(entry.word + "\t" + "PER")
                elif (entry.word in ORGANIZATIONS):
                    file_out.write(entry.word + "\t" + "ORG")
                elif (entry.word in LOCATIONS):
                    file_out.write(entry.word + "\t" + "LOC")
                else:
                    file_out.write(entry.word + "\t" + "MISC")
            else:
                file_out.write(entry.word + "\t" + "O")

            file_out.write("\n")
        file_out.write("\n")
        
