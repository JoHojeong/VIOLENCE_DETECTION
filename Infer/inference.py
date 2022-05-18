import argparse
import datetime
from importlib.resources import path
from typing import Union
import json
from pathlib import Path
from pathlib import PurePath
import os

from API import GoogleAPI, KakaoAPI
from Infer import Dataloader


def save_json(data, path):
    with open(path, 'w') as f:
        json.dump(data, f)


def get_argument():
    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--vid_path', type=str, default=None,
                        help='an path to vid, vid has to be mp4')
    parser.add_argument('--total_frame', type=int, default=None,
                        help='Number of frames to read. It is ')
    args = parser.parse_args()
    return args


def make_dirs(save_root):
    if not os.path.exists(save_root):
        os.mkdir(save_root)
    
    if not os.path.exists(os.path.join(save_root, "frames")):
        os.mkdir(os.path.join(save_root, "frames"))

    if not os.path.exists(os.path.join(save_root, "result")):
        os.mkdir(os.path.join(save_root, "result"))

    return os.path.join(save_root, "frames")

if __name__ == "__main__":
    args = get_argument()

    vid_name = Path(args.vid_path).stem
    save_root = os.path.join(PurePath(args.vid_path).parents[0],f'{vid_name}_{datetime.datetime.now()}')
    save_root = os.path.join("result", save_root)

    frames_path = make_dirs(save_root)

    Violence_Dataloader = Dataloader(
        API=GoogleAPI(),
        vid_path=args.vid_path,
        total_frame=args.total_frame,
        frames_path = frames_path)
    
    Adult_Dataloader = Dataloader(
        API=KakaoAPI(),
        vid_path=args.vid_path,
        total_frame=args.total_frame,
        frames_path = frames_path)

    save_dict = {
        "Video_path" : args.vid_path,
        "Violence" : {},
        "Adult" : {}
    }

    for i in range(len(Violence_Dataloader)):
        save_dict["Violence"][str(i)] = Violence_Dataloader[i]
        save_dict["Adult"][str(i)] = Adult_Dataloader[i]

    save_json(save_dict, os.path.join(save_root, 'result/result.json'))
