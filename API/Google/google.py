from google.cloud import vision
import io

from API.Image_API import IMAGEAPI


#  GoogleAPI infers Violence images
class GoogleAPI(IMAGEAPI):
    def __init__(self,
                 meta_path: str = './meta_data/meatadata.json'):
        super.__init__()
        self.__meta_data = GoogleAPI.read_json(meta_path)
        self.__key = self.__meta_data['Kakao']['key']
        self.__urls = self.__meta_data['Kakao']['urls']

        self.__headers = {'Authorization': 'KakaoAK {}'.format(self.__key)}


    def infer(self,
              frame):
        client = vision.ImageAnnotatorClient()

        image = vision.Image(content=frame)

        response = client.safe_search_detection(image=image)
        safe = response.safe_search_annotation

        # Names of likelihood from google.cloud.vision.enums
        likelihood_name = ('UNKNOWN', 'VERY_UNLIKELY', 'UNLIKELY', 'POSSIBLE',
                        'LIKELY', 'VERY_LIKELY')
        print('Safe search:')

        print('adult: {}'.format(likelihood_name[safe.adult]))
        print('medical: {}'.format(likelihood_name[safe.medical]))
        print('spoofed: {}'.format(likelihood_name[safe.spoof]))
        print('violence: {}'.format(likelihood_name[safe.violence]))
        print('racy: {}'.format(likelihood_name[safe.racy]))

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
