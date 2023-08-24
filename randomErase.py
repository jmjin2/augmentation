import cv2
import os
import numpy as np
import argparse
import random

# Training settings
parser = argparse.ArgumentParser(description="Light Field Denoising")
parser.add_argument("--inputDir", type=str,
                    default="./output_video", help="Input video folder")
parser.add_argument("--outputDir", type=str,
                    default="./erased_video", help="Output video folder")

opt = parser.parse_args()


if __name__ == '__main__':
    for root, dirs, files in os.walk(opt.inputDir):
        for file in files:
            if file.endswith(".mp4"):
                input_path = os.path.join(root, file)
                output_subdir = os.path.relpath(root, opt.inputDir)
                output_dir = os.path.join(opt.outputDir, output_subdir)
                os.makedirs(output_dir, exist_ok=True)

                filename = os.path.splitext(file)[0] + "_noised.mp4"
                output_path = os.path.join(output_dir, filename)

                cap = cv2.VideoCapture(input_path)
                fps = int(cap.get(cv2.CAP_PROP_FPS))
                frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)),
                              int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

                fourcc = cv2.VideoWriter_fourcc(*'avc1')
                out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

                while cap.isOpened():
                    ret, frame = cap.read()
                    if not ret:
                        break

                    y1 = random.randint(0, frame_size[1])
                    y2 = random.randint(y1, frame_size[1])
                    x1 = random.randint(0, frame_size[0])
                    x2 = random.randint(x1, frame_size[0])

                    frame[y1:y2, x1:x2] = 128

                    out.write(frame)
                    cv2.imshow('Random Erased Video', frame)

                    if cv2.waitKey(1) & 0xFF == ord('q'):
                        break

                cap.release()
                out.release()
                print("flip complete")
                cv2.destroyAllWindows()
