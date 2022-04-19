# OCR-Plate-Detection
Fast APNR using OpenCV dnn inferences, with 10 FPS on cpu.

https://user-images.githubusercontent.com/18560386/164028898-161f4e23-2843-4fe1-a810-fe0a59ad8ae6.mov


# Installation

1. Clone this repo
2. Setup a python environment, e.g. `python3 -m venv venv && source venv/bin/activate`
3. Install dependencies: `pip install -r requirements.txt` (OpenCV and Numpy)
And that's it!

# Inference

Run inference on:
- Live camera
- Video
- Photo

For live camera:
`python src/main.py --camera 0`

For video or photo:
`python src/main.py --input path/of/your/file`

Results will be displayed on screen.

# How does it work?

- First, a SSD model will detect the localisation of a plate in the frame (if any)
- Then, we will reposition the bounding box with basic plate heuristics (aspect ratio of 120 x 48), before using a RefineNet to improve it
- Finally, character recognition will be performed using a SegmentationFree InceptionNet

I have found models weights and architectures on a undocumented MIT-Licence Github repository, so I have no idea how these models were trained initially or by who.
