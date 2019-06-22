

class WordInfo():

    def __init__(self, data):
        self.word_info = data

        p1 = self.word_info["results"][0]["lexicalEntries"][0]["entries"]
        self.senses = p1[0]["senses"]

    def verification(self):
        # TODO so much possible here
        raise NotImplementedError("WordInfo.verification not yet implemented")

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
