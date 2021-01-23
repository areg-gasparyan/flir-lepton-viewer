import cv2
import argparse
import numpy as np


def getColorMap(colorFilter):
    if colorFilter == "COLORMAP_AUTUMN":
        return cv2.COLORMAP_AUTUMN
    if colorFilter == "COLORMAP_BONE":
        return cv2.COLORMAP_BONE
    if colorFilter == "COLORMAP_JET":
        return cv2.COLORMAP_JET
    if colorFilter == "COLORMAP_WINTER":
        return cv2.COLORMAP_WINTER
    if colorFilter == "COLORMAP_RAINBOW":
        return cv2.COLORMAP_RAINBOW
    if colorFilter == "COLORMAP_OCEAN":
        return cv2.COLORMAP_OCEAN
    if colorFilter == "COLORMAP_SUMMER":
        return cv2.COLORMAP_SUMMER
    if colorFilter == "COLORMAP_SPRING":
        return cv2.COLORMAP_SPRING
    if colorFilter == "COLORMAP_COOL":
        return cv2.COLORMAP_COOL
    if colorFilter == "COLORMAP_HSV":
        return cv2.COLORMAP_HSV
    if colorFilter == "COLORMAP_PINK":
        return cv2.COLORMAP_PINK
    if colorFilter == "COLORMAP_HOT":
        return cv2.COLORMAP_HOT
    return None


def run(device, width, height, colorMap):
    cap = cv2.VideoCapture(device)
    originalWidth = cap.get(3)
    originalHeight = cap.get(4)
    print("Original resolution:", originalWidth, originalHeight)

    cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"Y16 "))
    cap.set(cv2.CAP_PROP_CONVERT_RGB, 0)

    while(True):
        ret, frame = cap.read()
        frame = frame[:-2,:]

        frame = frame.astype(np.float32)
        frame = cv2.resize(frame, (width, height))
        frame = 255 * (frame - frame.min()) / (frame.max() - frame.min())
        frame = frame.astype(np.uint8)
        cm = getColorMap(colorMap)
        if cm != None:
            frame = cv2.applyColorMap(frame, cm)

        cv2.imshow('Lepton Viewer', frame.astype(np.uint8))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

    
def main():

    try:
        parser = argparse.ArgumentParser(description='This is a fast and easy python script in Linux envirenment for configur and capture FLIR Lepton 3.5 thermal camera images.')
        parser.add_argument("--device", type=str, default="/dev/video0", help="Input thermal camera device path --device=/dev/video0")

        parser.add_argument("--width", type=int, default=640, help="Resize width. Default is --width=640")
        parser.add_argument("--height", type=int, default=480, help="Resize height. Default is --height=480")

        parser.add_argument("--color-map", type=str, choices=["COLORMAP_GRAY", "COLORMAP_AUTUMN", "COLORMAP_BONE", "COLORMAP_JET",
                                                           "COLORMAP_WINTER", "COLORMAP_RAINBOW", "COLORMAP_OCEAN", "COLORMAP_SUMMER",
                                                           "COLORMAP_SPRING", "COLORMAP_COOL", "COLORMAP_HSV", "COLORMAP_PINK", "COLORMAP_HOT"],
                                                           default="COLORMAP_GRAY", help="Map corresponding color --color-map=COLORMAP_BONE")


        opt = parser.parse_known_args()[0]
    except Exception as e:
        parser.print_help()
        sys.exit(0)

    args = parser.parse_args()
    device = args.device
    width = args.width
    height = args.height
    colorMap = args.color_map
    run(device, width, height, colorMap)


if __name__ == "__main__":
    main()                                                                                                                                                                              92,1          Bot
