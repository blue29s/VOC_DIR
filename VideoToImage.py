import cv2
import os

def video_to_images(video_path, output_folder):
    # 读取视频文件
    video = cv2.VideoCapture(video_path)
    fps = int(video.get(cv2.CAP_PROP_FPS))
    frame_count = int(video.get(cv2.CAP_PROP_FRAME_COUNT))

    # 创建输出文件夹
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # 逐帧读取视频并保存为图片
    for i in range(0, frame_count, fps):
        video.set(cv2.CAP_PROP_POS_FRAMES, i)
        ret, frame = video.read()
        if ret:
            print("现在是第"+ str(i/30)+ "s")
            img_name = os.path.join(output_folder, f"frame_{i/30}s.jpg")
            cv2.imwrite(img_name, frame)
        else:
            break

    # 释放视频资源
    video.release()

if __name__ == "__main__":
    video_path = "Video/mp4.mp4"  # 替换为你的视频文件路径
    output_folder = "Images"  # 输出图片的文件夹
    video_to_images(video_path, output_folder)
