import argparse
from importlib.resources import path
from typing import Union
import json

from API import GoogleAPI, KakaoAPI
from Infer import Dataloader


def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)


def get_argument():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--vid_path', type=str, default=None,
                        help='an path to vid')
    parser.add_argument('--total_frame', type=int, default=None,
                        help='Number of frames to read. It is ')
    parser.add_argument('--save_path', type=str, default=None,
                        help='Path to save result')
    args = parser.parse_args()
    return args


if __name__ == "__main__":
    args = get_argument()

    Violence_Dataloader = Dataloader(
        API=GoogleAPI(),
        vid_path=args.vid_path,
        total_frame=args.total_frame)
    
    Adult_Dataloader = Dataloader(
        API=KakaoAPI(),
        vid_path=args.vid_path,
        total_frame=args.total_frame)

    save_dict = {
        "Video_path" : args.vid_path,
        "Violence" : [],
        "Adult" : []
    }

    for i in range(len(Violence_Dataloader)):
        save_dict["Violence"].append(Violence_Dataloader[i])
        save_dict["Adult"].append(Adult_Dataloader[i])

    save_json(save_dict, args.save_path)
