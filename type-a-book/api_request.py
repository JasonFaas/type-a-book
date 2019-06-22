import requests
import json

from api_oxford_dictionary import WordInfo

class ApiRequest():

    def unit_tests(self):
        # app_id = '9c810c40'
        # app_key = 'ca8f4511b7ebe8cc0cfc2518d6376e7a'
        # language = 'en'
        word_id = 'awfully'
        # url = 'https://od-api.oxforddictionaries.com:443/api/v2/entries/'  + language + '/'  + word_id.lower()
        # # url Normalized frequency
        # # urlFR = 'https://od-api.oxforddictionaries.com:443/api/v2/stats/frequency/word/'  + language + '/?corpus=nmc&lemma=' + word_id.lower()
        # r = requests.get(url, headers = {'app_id' : app_id, 'app_key' : app_key})
        # print("code {}\n".format(r.status_code))
        # print("text \n" + r.text)
        # print("json \n" + json.dumps(r.json()))
        # assert r.status_code == 200

        test_file_name = "../resources/api-requests/oxford-dictionary-example-1-awfully.json"
        with open(test_file_name) as json_file:  
            data = json.load(json_file)

        word_info = WordInfo(data)

        assert word_info.word() == word_id
        assert word_info.definitions() == {"very", "very badly or unpleasantly"}
        print("\nWHAT\n{}\n".format(word_info.sentences()))
        assert word_info.sentences() == {"I'm awfully sorry to bother you so late", 
                                         "an awfully nice man",
                                         "we played awfully"}
        assert word_info.part_of_language() == "adverb"

        assert 1 == 2

        assert r.text == "ADVERB"
        assert r.text == "very"
        assert r.text == "we played awfully"
