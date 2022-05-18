from API.Image_API import IMAGEAPI


#  KakaoAPI infers adult images
class KakaoAPI(IMAGEAPI):
    def __init__(self,
                 meta_path: str = './meta_data/metadata.json'):
        self.__meta_data = KakaoAPI.read_json(meta_path)
        self.__key = self.__meta_data['Kakao']['key']
        self.__urls = self.__meta_data['Kakao']['urls']

        self.__headers = {'Authorization': 'KakaoAK {}'.format(self.__key)}


    def infer(self,
              image_path):
        url = self.__urls['adult_detection']

        result = KakaoAPI.send_requests(url,
                                        self.__headers,
                                        open(image_path, 'rb'))

        result = eval(result)
        return_dict = {}
        return_dict["soft"] = result["result"]["soft"]
        return_dict["adult"] = result["result"]["adult"]
        return_dict["normal"] = result["result"]["normal"]
        
        return return_dict
