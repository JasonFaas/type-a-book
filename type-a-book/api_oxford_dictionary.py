

class WordInfo():

    def __init__(self, status_code, data):
        self.status_code = status_code
        self.word_info = data

        if status_code == 200:
            p1 = self.word_info["results"]
            p2 = p1[0]
            p3 = p2["lexicalEntries"]
            p4 = p3[0]
            p5 = p4["entries"]
            p6 = p5[0]
            self.senses = p6["senses"]

    def verification(self):
        if self.status_code != 200:
            LookupError("Status code :{}: is not valid:\n:{}\n".format(self.status_code, self.word_info))
        # TODO so much possible here

    def word(self):
        return self.word_info["id"]

    def definitions(self):
        definition_set = set()
        for definition_group in self.senses:
            for definition in definition_group["definitions"]:
                definition_set.add(definition)
        return definition_set

    def sentences(self):
        sentence_set = set()
        for sentence_group in self.senses:
            for examples in sentence_group["examples"]:
                sentence_set.add(examples["text"])
        return sentence_set

    def part_of_language(self):
        lexical_category = self.word_info["results"][0]["lexicalEntries"][0]["lexicalCategory"]["id"]


        if not isinstance(lexical_category, str):
            print("Likely muliple Lexical Categories:" + str(lexical_category) + ":")
            raise TypeError(str(self.word_info))

        return lexical_category

    def audio_pronunciation_link(self):
        raise NotImplementedError("WordInfo.audio_pronunciation_link not yet implemented")
