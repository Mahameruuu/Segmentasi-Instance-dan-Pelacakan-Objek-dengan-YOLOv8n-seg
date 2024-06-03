import os
from collections import defaultdict
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors

# Create output directory if it doesn't exist
if not os.path.exists('output'):
    os.makedirs('output')

# Dictionary to store tracking history with default empty lists
track_history = defaultdict(lambda: [])

# YOLO model 
model = YOLO("yolov8n-seg.pt")

cap = cv2.VideoCapture("mobil.mp4")

# width, height, and frames per second
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

# Check if fps is valid, set a default fps value if it's invalid
if fps < 1:
    fps = 30  

# save the output video with the specified properties
output_file = "output/instance-segmentation-object-tracking.avi"
out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*"MJPG"), fps, (w, h))

if not out.isOpened():
    print(f"Error: Failed to open video writer for {output_file}")
    exit(1)

while True:
    ret, im0 = cap.read()
    if not ret:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    annotator = Annotator(im0, line_width=2)

    results = model.track(im0, persist=True)

    # Check tracking IDs and masks are present in the results
    if results[0].boxes.id is not None and results[0].masks is not None:
        # Extract masks and tracking IDs
        masks = results[0].masks.xy
        track_ids = results[0].boxes.id.int().cpu().tolist()

        # Annotate each mask with its corresponding tracking ID and color
        for mask, track_id in zip(masks, track_ids):
            annotator.seg_bbox(mask=mask, mask_color=colors(track_id, True), track_label=str(track_id))

    out.write(im0)
    cv2.imshow("instance-segmentation-object-tracking", im0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

out.release()
cap.release()
cv2.destroyAllWindows()