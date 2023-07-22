# Lane Detection for self driving cars

This project demonstrates lane detection in images and videos using the Hough transform algorithm. The Hough transform is a popular technique used for detecting lines in images and is commonly applied to identify lane markings on roads in computer vision and self-driving car applications.

## Project Overview

The lane detection process involves the following steps:

1. Convert the image to grayscale: The color image is converted to a grayscale image to simplify the edge detection process.

2. Canny Edge Detection: The Canny edge detection algorithm is applied to identify the edges of objects in the grayscale image.

3. Region of Interest (ROI) Selection: A specific region of interest (ROI) is defined to focus the lane detection within the relevant area.

4. Hough Transform: The Hough transform algorithm is used to detect lines in the edges detected within the ROI. This step is essential for identifying lane lines.

5. Draw Lane Lines: The detected lane lines are drawn on a separate blank image and then overlaid onto the original image to visualize the detected lanes.

## How to Run the Project

1. Install Dependencies: Ensure you have Python and OpenCV installed. You can install OpenCV using `pip install opencv-python`.

2. Clone the Repository: Clone this repository to your local machine.

3. Prepare the Video: If you want to test lane detection on a video, place the video file in the same directory as the Python script. Ensure the video file is named "lane_detection_video.mp4" or modify the file path in the script accordingly.

4. Run the Script: Execute the `video.py` script to start the lane detection process on the video. The detected lane lines will be displayed in a new window.

5. Fine-tuning: You can experiment with various parameters like Canny thresholds, Hough transform parameters, and ROI size to optimize the lane detection for different scenarios.

## Files in the Repository

- `video.py`: The main Python script that performs lane detection on the video.
- 'algo.ipynb' : basic working jupyter file for rough demonstrates
- `male_face.png`: Sample image for testing lane detection on single frames (optional).

## Notes

- The lane detection algorithm is primarily designed for straight lanes, and it may not work optimally in complex scenarios such as curved roads or extreme lighting conditions.

- Ensure that the video file is in a supported format (e.g., MP4) and located in the same directory as the script.

- The script uses a simple ROI for lane detection. For more robust lane detection, advanced techniques like deep learning-based methods can be explored.

## References

- Hough Transform: https://en.wikipedia.org/wiki/Hough_transform

- OpenCV Documentation: https://docs.opencv.org/

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

Feel free to contribute to the project and extend the lane detection capabilities for various scenarios and environments. Happy lane detection!