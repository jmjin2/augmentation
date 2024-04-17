import os, sys
texture_paths = {
                'classroomvideo/texture' : ['4096x2048', '30', './classroomvideo/texture'],
                }
depth_paths = {
                'classroomvideo/depth' : ['4096x2048', '30', './classroomvideo/depth'],
                }

for texture_path in texture_paths.keys():
    output_path_for_syntax = f'mp4/{texture_paths[texture_path][2]}'        ## 출력 경로, mp4 파일 하단에 출력함
    output_path = f'mp4/{texture_path}'     ## 경로 생성을 위해 있음
    os.makedirs(output_path, exist_ok = True)       ## 경로 생성

    yuv_names = [file for file in os.listdir(texture_path) if file.endswith('.yuv')]        # yuv 파일 이름들
    for yuv_name in yuv_names:
        cmd = [
            'ffmpeg',
            '-f', 'rawvideo',
            '-pix_fmt', 'yuv420p10le',
            '-s:v', texture_paths[texture_path][0],
            '-r', texture_paths[texture_path][1],
            '-i', f'{texture_paths[texture_path][2]}/{yuv_name}',
            '-c:v', 'libx264',
            '-crf', '10',
            '-pix_fmt', 'yuv420p',
            f'{output_path_for_syntax}/{yuv_name[:-4]}.mp4'
        ]
        
        os.system(' '.join(cmd))

for depth_path in depth_paths.keys():
    output_path_for_syntax = f'mp4/{depth_paths[depth_path][2]}'
    output_path = f'mp4/{depth_path}'
    os.makedirs(output_path, exist_ok = True)

    yuv_names = [file for file in os.listdir(depth_path) if file.endswith('.yuv')]

    for yuv_name in yuv_names:
        cmd = [
            'ffmpeg',
            '-f', 'rawvideo',
            '-pix_fmt', 'yuv420p16le',
            '-s:v', depth_paths[depth_path][0],
            '-r', depth_paths[depth_path][1],
            '-i', f'{depth_paths[depth_path][2]}/{yuv_name}',
            '-c:v', 'libx264',
            '-crf', '10',
            '-pix_fmt', 'yuv420p',
            f'{output_path_for_syntax}/{yuv_name[:-4]}.mp4'
        ]
        
        os.system(' '.join(cmd))