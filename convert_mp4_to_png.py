import cv2
import os

def save_frames_from_video(video_path, save_path):
    try:
        os.makedirs(save_path, exist_ok = True)
        video = cv2.VideoCapture(video_path)
        frame_num = video.get(cv2.CAP_PROP_FRAME_COUNT)
        i = 0
        while(True):
            ret, frame = video.read()
            if ret:
                image_path = os.path.join(f"{save_path}/{i:08d}.jpg")
                cv2.imwrite(image_path, frame)
                i += 1

            else:
                break
    except:
        print(f'{video_path}: raise error!')

saved_frame_path_root = './jpg' # 추출될 프레임들이 저장될 폴더
root_path = './mp4'


for path, _, files in os.walk(root_path):
    dir_path = os.path.join(saved_frame_path_root, path)
    
    for file in files:
        if file.endswith('.mp4'):
            video_path = os.path.join(f'{path}', file)
            file_name, _  = os.path.splitext(file)
            save_path = os.path.join(dir_path, f'{file_name}')
            os.makedirs(save_path, exist_ok=True)
            save_frames_from_video(video_path, save_path)



    # now_save_path = now_dir.replace("./mp4", saved_frame_path_root)
    # os.makedirs(now_save_path, exist_ok = True)

    # for file in contents:
    #     if os.path.isdir(file):
    #         abs_path = os.path.join(f'', file)
    #         dir_queue.put(abs_path)

    #     else:
    #         file_name, extension = os.path.splitext(file)
    #         if extension == '.mp4':
    #             saved_frame_path = os.path.join(now_save_path, f'{file_name}')
    #             video_path = os.path.join(f'', file)
    #             save_frames_from_video(video_path, saved_frame_path)
    #         else:
    #             print(f'\'{file}\' is not mp4 file!')