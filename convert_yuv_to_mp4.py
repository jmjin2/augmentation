import os, sys
# ffmpeg \
#   -f rawvideo -pix_fmt yuv420p10le -s:v 1920x1080 -r ${rate} -i {input}.yuv \
#   -c:v libx264 -crf 10 -pix_fmt yuv420p {output}.mp4

texture_paths = {
                '(A01)ClassroomVideo/v14/texture' : ['4096x2048', '30', '\(A01\)ClassroomVideo/v14/texture'],       ## key는 비디오 이름, value는 [해상도, 프레임레이트, 상세 경로]
                '(C01)Hijack/vAll_texture_4096x2048_yuv420p10le' : ['4096x2048', '30', '\(C01\)Hijack/vAll_texture_4096x2048_yuv420p10le'],
                '(C02)Cyberpunk/textures' : ['2048x2048', '30', '\(C02\)Cyberpunk/textures'], 
                '(E01)Frog/textureAllViews' : ['1920x1080', '30', '\(E01\)Frog/textureAllViews'],
                '(E02)Carpark/all_textures' : ['1920x1088', '25', '\(E02\)Carpark/all_textures'], 
                '(E03)Street/all_textures' : ['1920x1088', '25', '\(E03\)Street/all_textures'],
                '(W01)Group/textureAllViews' : ['1920x1080', '30', '\(W01\)Group/textureAllViews'], 
                '(W02)Dancing/texture_v16_v23' : ['1920x1080', '30', '\(W02\)Dancing/texture_v16_v23'],

                '(B01)Museum' : ['2048x2048', '30', '\(B01\)Museum/textures'],
                '(B02)Chess' : ['2048x2048', '30', '\(B02\)Chess/all_textures'],
                '(D01)Painter' : ['2048x1088', '30', '\(D01\)Painter/textures'],
                '(D02)Breakfast' : ['1920x1080', '30', '\(D02\)Breakfast/textures'],
                '(D03)Barn' : ['1920x1080', '30', '\(D03\)Barn/textures'],
                '(J01)Kitchen' : ['1920x1080', '30', '\(J01\)Kitchen/textures'],
                '(J02)Cadillac' : ['1920x1080', '30', '\(J02\)Cadillac/Cadillac_texture'],
                '(J03)Mirror' : ['1920x1080', '30', '\(J03\)Mirror/Mirror_texture'],
                '(J04)Fan' : ['1920x1080', '30','\(J04\)Fan/texturesAllViews']
                }


depth_paths = {
                '(A01)ClassroomVideo/v14/depth' : ['4096x2048', '30', '\(A01\)ClassroomVideo/v14/depth'], 
                '(C01)Hijack/vAll_depth_4096x2048_yuv420p10le' : ['4096x2048', '30', '\(C01\)Hijack/vAll_depth_4096x2048_yuv420p10le'],
                '(C02)Cyberpunk/depths' : ['2048x2048', '30', '\(C02\)Cyberpunk/depths'], 
                '(E01)Frog/depthAllViews' : ['1920x1080', '30', '\(E01\)Frog/depthAllViews'],
                '(E02)Carpark/all_depths' : ['1920x1088', '25', '\(E02\)Carpark/all_depths'], 
                '(E03)Street/all_depths' : ['1920x1088', '25', '\(E03\)Street/all_depths'],
                '(W01)Group/depthAllViews' : ['1920x1080', '30', '\(W01\)Group/depthAllViews'], 
                '(W02)Dancing/depth_v16_v23' : ['1920x1080', '30', '\(W02\)Dancing/depth_v16_v23'],

                '(B01)Museum' : ['2048x2048', '30', '\(B01\)Museum/depts'],
                '(B02)Chess' : ['2048x2048', '30', '\(B02\)Chess/all_depths'],
                '(D01)Painter' : ['2048x1088', '30', '\(D01\)Painter/depths'],
                '(D02)Breakfast' : ['1920x1080', '30', '\(D02\)Breakfast/depthmaps'],
                '(D03)Barn' : ['1920x1080', '30', '\(D03\)Barn/depthmaps'],
                '(J01)Kitchen' : ['1920x1080', '30', '\(J01\)Kitchen/depths'],      ## Kitchen은 depth가 yuv420p10le임
                '(J02)Cadillac' : ['1920x1080', '30', '\(J02\)Cadillac/Cadillac_depth'],
                '(J03)Mirror' : ['1920x1080', '30', '\(J03\)Mirror/Mirror_texture'],
                '(J04)Fan' : ['1920x1080', '30','\(J04\)Fan/Fan_corrected_depth']
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