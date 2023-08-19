import cv2
import os
import numpy as np
import argparse

def noisy(frame, noise_level=0.5):
    row, col, ch = frame.shape
    noise = np.random.normal(scale=noise_level, size=(row, col, ch))
    noisy_frame = np.clip(frame + noise, 0, 255).astype(np.uint8)
    return noisy_frame

# Training settings
parser = argparse.ArgumentParser(description="Light Field Denoising")
parser.add_argument("--inputDir", type=str, default="./video", help="Input video folder")
parser.add_argument("--outputDir", type=str, default="./noising_video", help="Output video folder")
parser.add_argument("--noise_level", type=int, default=50, help="Level of noise")

opt = parser.parse_args()


if __name__ == '__main__':
    for file in os.listdir(opt.inputDir):
        input_path = os.path.join(opt.inputDir, file)
        filename = os.path.splitext(file)[0] + "_noised.mp4"
        output_path = os.path.join(opt.outputDir, filename)

        cap = cv2.VideoCapture(input_path)
        fps = int(cap.get(cv2.CAP_PROP_FPS))
        frame_size = (int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)), int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))

        fourcc = cv2.VideoWriter_fourcc(*'H264')
        out = cv2.VideoWriter(output_path, fourcc, fps, frame_size)

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            noisy_frame = noisy(frame, opt.noise_level)
            out.write(noisy_frame)
            
            cv2.imshow('Noisy Video', noisy_frame)

        cap.release()
        out.release()
        print("Noising complete")
