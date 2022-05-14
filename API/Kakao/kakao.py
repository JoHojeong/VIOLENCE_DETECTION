from API.Image_API import IMAGEAPI


#  KakaoAPI infers adult images
class KakaoAPI(IMAGEAPI):
    def __init__(self,
                 meta_path: str = './meta_data/meatadata.json'):
        super.__init__()
        self.__meta_data = KakaoAPI.read_json(meta_path)
        self.__key = self.__meta_data['Kakao']['key']
        self.__urls = self.__meta_data['Kakao']['urls']

        self.__headers = {'Authorization': 'KakaoAK {}'.format(self.__key)}


    def infer(self,
              image):
        url = self.__urls['adult_detection']

        return KakaoAPI.send_requests(url,
                                      image,
                                      self.__headers)
