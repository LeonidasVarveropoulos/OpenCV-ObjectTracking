import cv2
import sys
cv2 = cv2.cv2
video = cv2.VideoCapture(0)
tracker = cv2.TrackerCSRT_create()
 
    # Exit if video not opened.
if not video.isOpened():
    print("Could not open video")
    sys.exit()
 
# Read first frame.
ok, frame = video.read()
if not ok:
    print ('Cannot read video file')
    sys.exit()
     
    # Define an initial bounding box
bboxs = []
count = 0

# Select ROI
while count< 2:
    bboxs.append(cv2.selectROI("frame",frame))
    print(bboxs)
    count += 1

def create_tracker():
    tracker = cv2.TrackerCSRT_create()
    return tracker

multiTracker = cv2.MultiTracker_create()

# Initialize tracker with first frame and bounding box
for bbox in bboxs:
    multiTracker.add(create_tracker(),frame,bbox)
 
while True:
        # Read a new frame
    ok, frame = video.read()
    if not ok:
        break
         
        # Start timer
    timer = cv2.getTickCount()
 
        # Update tracker
    ok, bboxes = multiTracker.update(frame)
 
        # Calculate Frames per second (FPS)
    fps = cv2.getTickFrequency() / (cv2.getTickCount() - timer);
    print(fps)
 
        # Draw bounding box
    if ok:
        for i, newbox in enumerate(bboxes):
            p1 = (int(newbox[0]), int(newbox[1]))
            p2 = (int(newbox[0] + newbox[2]), int(newbox[1] + newbox[3]))
            cv2.rectangle(frame, p1, p2, (200,59,100), 2, 1)
    else :
            # Tracking failure
        cv2.putText(frame, "Tracking failure detected", (100,80), cv2.FONT_HERSHEY_SIMPLEX, 0.75,(0,0,255),2)
 
        # Display tracker type on frame
    
 
        # Display result
    cv2.imshow("Tracking", frame)
 
        # Exit if ESC pressed
    k = cv2.waitKey(1) & 0xff
    if k == 27 : break