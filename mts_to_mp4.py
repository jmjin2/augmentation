import os, sys
import argparse
# ffmpeg -i {input}.mts -c:v libx264 -crf 10 {output}.mp4


def mts_to_mp4(input_path, output_path):
    cmd = [
            'ffmpeg',
            '-i', input_path,
            '-crf', '10',
            '-c:v', 'libx264',
            '-c:a', 'aac',
            f'{output_path}.mp4'
        ]
        
    os.system(' '.join(cmd))

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_path', type=str, default='./mts')
    parser.add_argument('--output_path', type=str, default='./output')

    args = parser.parse_args()

    os.makedirs(args.output_path, exist_ok=True)

    for file in os.listdir(args.input_path):
        file_name, _ = file.split(".")
        input_mts = os.path.join(args.input_path, file)
        print(input_mts)
        print(args.output_path)
        print(file_name)
        output_mp4 = os.path.join(args.output_path, file_name)
        mts_to_mp4(input_mts, output_mp4)

if __name__ == '__main__':
    main()