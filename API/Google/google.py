import os
import io

from google.cloud import vision

from API.Image_API import IMAGEAPI


#  GoogleAPI infers Violence images
class GoogleAPI(IMAGEAPI):
    def __init__(self,
                 meta_path: str = './meta_data/My First Project-7a9a14ddc396.json'):
        os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = meta_path


    def infer(self,
              frame_path):
        """Detects unsafe features in the file."""
        client = vision.ImageAnnotatorClient()
    
        with io.open(frame_path, 'rb') as image_file: 
            content = image_file.read()

        image = vision.Image(content=content)

        response = client.safe_search_detection(image=image)
        safe = response.safe_search_annotation

        return_dict = {}
        return_dict["adult"] = safe.adult
        return_dict["medical"] = safe.medical
        return_dict["spoof"] = safe.spoof
        return_dict["violence"] = safe.violence
        return_dict["racy"] = safe.racy

        if response.error.message:
            raise Exception(
                '{}\nFor more info on error messages, check: '
                'https://cloud.google.com/apis/design/errors'.format(
                    response.error.message))
        return return_dict
