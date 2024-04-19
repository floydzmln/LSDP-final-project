import cv2
import os

def extract_frames(video_path, output_dir):
    # Create output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Open the video file
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print("Error: Could not open video file.")
        return

    frame_count = 0
    saved_count = 0
    while True:
        ret, frame = cap.read()
        if not ret:
            break  # Break the loop when the video ends

        frame_count += 1

        # Skip the first 1200 frames
        if frame_count <= 1200:
            continue

        # Save every 25th frame
        if frame_count % 25 == 0:
            saved_count += 1
            frame_name = f"frame_{saved_count:05d}.jpg"
            frame_path = os.path.join(output_dir, frame_name)
            cv2.imwrite(frame_path, frame)

    cap.release()
    print(f"Frames extracted: {saved_count}")

# Replace 'video_path' and 'output_dir' with your actual paths
video_path = "DJI_0199.mov"
output_dir = "video_frames"

extract_frames(video_path, output_dir)
