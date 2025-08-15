This Project uses OpenCV to detect lane lines in a video (e.g., from a car dashcam) by applying image processing techniques like Canny edge detection, region masking, and Hough line transformation.

Loads a test video (Testvideo.mp4) using cv2.VideoCapture.

Reads each frame in a loop until the video ends or the user presses e.

Image Processing (Imgprocessing)

Converts each frame from RGB to grayscale (cv2.cvtColor).

Uses Canny Edge Detection to highlight strong edges in the image (likely lane lines).

Region of Interest (ROI)

Creates a triangular mask that focuses only on the part of the image where lane lines are expected.

Ignores irrelevant areas like the sky or roadside objects.

Line Detection (Display)

Applies the Hough Line Transform (cv2.HoughLinesP) to find straight line segments within the masked region.

Draws these lines on a blank image in red with a thickness of 10 pixels.

Overlay on Original Video

Combines the original frame with the detected lines using cv2.addWeighted, creating a semi-transparent overlay effect.

Display the Result

Shows the final processed video in a window called "Final Test video".

Press e to exit early.
