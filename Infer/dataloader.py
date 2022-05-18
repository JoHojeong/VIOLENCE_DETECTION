import os

import cv2
from API import IMAGEAPI

class Dataloader():
    def __init__(self,
                 API : IMAGEAPI,
                 vid_path : str,
                 total_frame : int,
                 frames_path : str):
        self.__vid_path = vid_path
        self.__total_frame = total_frame
        self.__API  = API
        self.__infos = []
        self.__frames_path = frames_path
        self.read_video()

    def __getitem__(self,
                    idx):
        return self.__infos[idx]


    def __len__(self):
        return len(self.__infos)


    def read_video(self):
        try:
            video = cv2.VideoCapture(self.__vid_path)
        except Exception as e:
            print('Video not readable! Check if your vid is .mp4', e)

        self.__total_frame  = min(self.__total_frame, int(video.get(cv2.CAP_PROP_FRAME_COUNT)))
        batch = int(int(video.get(cv2.CAP_PROP_FRAME_COUNT)) / self.__total_frame)

        count = 0
        while True:
            ret, frame = video.read()
            if ret:
                count += 1
                if count % batch == 0:
                    frame_path = os.path.join(self.__frames_path, f'{count}.jpg')
                    cv2.imwrite(frame_path, frame)
                    self.__infos.append(self.__API.infer(frame_path))

                if cv2.waitKey(0) & 0xFF == ord('q'):
                    break
            else:
                break

        video.release()
        cv2.destroyAllWindows()

