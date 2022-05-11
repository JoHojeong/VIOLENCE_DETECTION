from API.API import API


#  GoogleAPI infers Violence images
class GoogleAPI(API):
    def __init__(self,
                 meta_path: str = './meta_data/meatadata.json'):
        super.__init__()
        self.__meta_data = GoogleAPI.read_json(meta_path)
        self.__key = self.__meta_data['Kakao']['key']
        self.__urls = self.__meta_data['Kakao']['urls']

        self.__headers = {'Authorization': 'KakaoAK {}'.format(self.__key)}


    def infer(self,
              image_path: str):
        url = self.__urls['adult_detection']

        return GoogleAPI.send_requests(url,
                                       image_path,
                                       self.__headers)
