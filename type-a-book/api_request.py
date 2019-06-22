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
        return word_info_hc(word_to_request)

    def word_info_hc(self, word_to_request):
        test_file_name = "../resources/api-requests/oxford-dictionary-example-1-awfully.json"
        with open(test_file_name) as json_file:  
            data = json.load(json_file)

        word_info = WordInfo(200, data)

        return word_info

    def word_info_api(self, word_to_request):
        r = requests.get(self.url.format(word_to_request),
                         headers = {'app_id' : self.app_id,
                                    'app_key' : self.app_key})
        print("\nStatus Code {}\n".format(r.status_code))
        # print("text \n" + r.text)
        # print("json \n" + json.dumps(r.json()))
        # assert r.status_code == 200
        return_word_info = WordInfo(r.status_code, r.json())
        return_word_info.verification()

        return return_word_info
        

    def unit_tests(self):
        word_id = 'awfully'
        word_info_hc_result = self.word_info_hc(word_id)
        self.unit_test_helper_awfully(word_info_hc_result)
        # word_info_api_result = self.word_info_api(word_id)
        # self.unit_test_helper_awfully(word_info_api_result)

        try:
            word_info_bad_result = self.word_info_api("whatekker")
            assert False
        except LookupError as e:
            assert str(e).startswith("Status code :{}: is not valid:".format(404))

    def unit_test_helper_awfully(self, awfully_info):
        assert awfully_info.word() == 'awfully'
        assert awfully_info.definitions() == {"very", "very badly or unpleasantly"}
        assert awfully_info.sentences() == {"I'm awfully sorry to bother you so late", 
                                         "an awfully nice man",
                                         "we played awfully"}
        assert awfully_info.part_of_language() == "adverb"

