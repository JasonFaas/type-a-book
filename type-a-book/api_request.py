import requests
import json

from api_oxford_dictionary import WordInfo

class ApiRequest():
        # print("\nWHAT\n{}\n".format(word_info.sentences()))


    def __init__(self):
        self.app_id = '9c810c40'
        self.app_key = 'ca8f4511b7ebe8cc0cfc2518d6376e7a'
        language = 'en'
        self.url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/{}/{{}}".format(language)
        # # url Normalized frequency
        # # urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()


    def word_info(self, word_to_request):
        return self.word_info_api(word_to_request)

    def word_info_hc(self, word_to_request, status_code = 200):
        test_file_name = "../resources/api-requests/oxford-dictionary-example-{}.json".format(word_to_request)
        with open(test_file_name) as json_file:  
            data = json.load(json_file)

        word_info = WordInfo(status_code, data, word_to_request)

        return word_info

    def word_info_api(self, word_to_request):
        r = requests.get(self.url.format(word_to_request),
                         headers = {'app_id' : self.app_id,
                                    'app_key' : self.app_key})
        # print("Status Code {}\n".format(r.status_code))
        print("text \n" + r.text)
        # print("json \n" + json.dumps(r.json()))
        # assert r.status_code == 200
        return_word_info = WordInfo(r.status_code, r.json(), word_to_request)
        return_word_info.verification()

        return return_word_info
        

    def unit_tests(self):
        word_id = 'awfully'
        word_info_hc_awfully = self.word_info_hc(word_id)
        print(word_info_hc_awfully)
        self.unit_test_helper_awfully(word_info_hc_awfully)

        word_id = 'unpleasantly'
        word_info_hc_unpleasantly = self.word_info_hc(word_id)
        assert len(word_info_hc_unpleasantly.definitions()) == 0
        assert word_info_hc_unpleasantly.derivative_of() == "unpleasant"
        print(word_info_hc_unpleasantly)

        word_id = 'lady'
        word_info_hc_lady = self.word_info_hc(word_id)
        print(word_info_hc_lady)
        self.unit_test_helper_lady(word_info_hc_lady)

        word_id = 'whatekker'
        word_info_hc_whatekker = self.word_info_hc(word_id, 404)
        print(word_info_hc_whatekker)
        assert word_info_hc_whatekker.general_error() == "No entry found matching supplied source_lang, word and provided filters"

        word_id = 'could'
        word_info_hc_could = self.word_info_hc(word_id)
        assert len(word_info_hc_could.definitions()) > 0
        assert len(word_info_hc_could.sentences()) > 0
        print(word_info_hc_could)
        
        # Good api lookup test (expensive)
        # word_id = 'awfully'
        # word_info_api_result = self.word_info_api(word_id)
        # self.unit_test_helper_awfully(word_info_api_result)

        # Bad api lookup test (expensive)
        # try:
        #     word_info_bad_result = self.word_info_api("whatekker")
        #     assert False
        # except LookupError as e:
        #     assert str(e).startswith("Status code :{}: is not valid:".format(404))
        # assert word_info_hc_whatekker.general_error() == "No entry found matching supplied source_lang, word and provided filters"

    def unit_test_helper_awfully(self, awfully_info):
        assert awfully_info.word() == 'awfully'
        assert awfully_info.definitions() == {"very", "very badly or unpleasantly"}
        assert awfully_info.sentences() == {"I'm awfully sorry to bother you so late.", 
                                         "An awfully nice man.",
                                         "We played awfully."}
        assert awfully_info.part_of_language() == "adverb"

    def unit_test_helper_lady(self, lady_info):
        assert lady_info.word() == 'lady'
        assert lady_info.definitions() == {'a woman of good social position', 
                                           'a polite or formal way of referring to a woman', 
                                           "a man's wife", 
                                           "a women's public toilet"}
        assert lady_info.sentences() == {'Lords and ladies were once entertained at the house.', 
                                         'The vice president and his lady.'}
        assert lady_info.part_of_language() == "noun"

