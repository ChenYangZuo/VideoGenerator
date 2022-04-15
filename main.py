import cv2
import numpy as np

fourcc = cv2.VideoWriter_fourcc(*'avc1')  # 视频编解码器,需要openh264动态库支持
out = cv2.VideoWriter('./out/result.mp4', fourcc, 30, (256, 256), False)  # 写入视频

for i in range(255):
    img = np.loadtxt(f'./img/{i}.txt').astype(np.uint8)
    out.write(img)  # 写入帧
    cv2.imshow('frame', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):  # 输入q退出
        break

out.release()
cv2.destroyAllWindows()