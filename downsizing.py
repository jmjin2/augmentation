# ffmpeg -i "$input_file" -vf "scale=iw/4:ih/4" -c:a copy "$output_file"
import cv2
import os

def downsizing(frame_path, save_path):
    cmd = [
            'ffmpeg',
            '-i', frame_path,
            '-vf', '"scale=iw/4:ih/4"',
            '-c:a', 'copy',
            f'{save_path}.jpg'
        ]
        
    os.system(' '.join(cmd))

saved_frame_path_root = './x4' # 추출될 프레임들이 저장될 폴더
root_path = './jpg'


for path, _, files in os.walk(root_path):
    dir_path = os.path.join(saved_frame_path_root, path)
    
    for file in files:
        if file.endswith('.jpg'):
            frame_path = os.path.join(f'{path}', file)
            file_name, _  = os.path.splitext(file)
            save_path = os.path.join(dir_path, f'{file_name}')
            os.makedirs(dir_path, exist_ok=True)
            downsizing(frame_path, save_path)