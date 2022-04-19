import os
import cv2
import argparse
from time import time
from hyperlpr import HyperLPR_plate_recognition


def main(args):
    cap = get_cap(args)
    cv2.namedWindow("HLPR")
    idx_img = 1
    fps_counter = 5
    fps_value = None
    start = time()
    try:
        while True:
            ret, img = cap.read()
            if ret:
                results = HyperLPR_plate_recognition(img)
                # results = moving_avg(results)
                for result in results:
                    img = add_bbox(img, *result)
                img = add_fps(img, fps_value)
                cv2.imshow("HLPR", img)

            else:
                if args.input:
                    print("No video")
                    cap.set(cv2.CAP_PROP_POS_FRAMES, 0)
                else:
                    break

            key = cv2.waitKey(30)
            if key == ord("q") or key == 27:
                break

            if idx_img % fps_counter == 0:
                time_delta = (time() - start) / fps_counter
                fps_value = round(1 / time_delta, 2)
                start = time()
            idx_img += 1
    finally:
        cap.release()


def add_bbox(img, y_hat, conf, bbox):
    print(y_hat, conf, bbox)
    x1, y1, x2, y2 = bbox
    font_face = cv2.FONT_HERSHEY_DUPLEX
    font_scale = 1
    font_color = (255, 255, 255)
    font_thickness = 1
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
    (w, h), _ = cv2.getTextSize(y_hat, font_face, font_scale, font_thickness)
    cv2.rectangle(img, (x1, y1 - h), (x1 + w, y1), (0, 255, 0), -1)
    font_scale *= 0.9
    cv2.putText(img, y_hat, (x1, y1), font_face, font_scale, font_color, font_thickness)
    return img


def add_fps(img, fps_value):
    font_face = cv2.FONT_HERSHEY_DUPLEX
    font_scale = 1
    font_color = (255, 255, 255)
    font_thickness = 1
    if fps_value:
        txt = f"{fps_value} FPS"
    else:
        txt = ""
    (w, h), _ = cv2.getTextSize(txt, font_face, font_scale, font_thickness)
    cv2.rectangle(img, (0, 0), (w, h), (0, 0, 0), -1)
    font_scale *= 0.9
    cv2.putText(img, txt, (0, h), font_face, font_scale, font_color, font_thickness)
    return img


def get_cap(args):
    if args.input:
        cap = cv2.VideoCapture(args.input)
    else:
        cap = cv2.VideoCapture(args.camera)
    return cap


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="HyperLPR app")
    parser.add_argument("--camera", help="Camera ID", default=0, type=int)
    parser.add_argument("--input", help="Input Media", default="", type=str)
    args = parser.parse_args()
    main(args)
