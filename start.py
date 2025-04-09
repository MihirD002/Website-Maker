import os
import cv2
from ultralytics import YOLO
from detectWebsite import build_website_from_detections
from previewServer import serve_html
import threading

images_dir = os.path.join('.', 'test_images')
image_name = '158.png'
image_path = os.path.join(images_dir, image_name)

model_path = os.path.join('.', 'runs', 'detect',
                          'train6', 'weights', 'best.pt')
model = YOLO(model_path)


def detect_component(image_path):
    img = cv2.imread(image_path)
    height, width, channels = img.shape
    detection_results = model(img)[0]
    return detection_results, height, width


def main():
    detections, v_height, v_width = detect_component(image_path)
    html = build_website_from_detections(detections, v_width, v_height)

    # Define the output HTML path
    output_html = "generated_website16.html"

    # Write the HTML to a file
    with open(output_html, "w") as f:
        f.write(html)

    print("Website generated successfully!")

    # Start the preview server in a separate thread
    server_thread = threading.Thread(
        target=serve_html,
        args=(output_html,),
        daemon=True
    )
    server_thread.start()

    # Keep the main thread running to maintain the server
    try:
        print("Server is running. Press Ctrl+C to stop.")
        # This keeps the main thread alive
        while server_thread.is_alive():
            # Join with timeout to keep the main thread responsive
            server_thread.join(1)
    except KeyboardInterrupt:
        print("Stopping server and exiting...")


if __name__ == "__main__":
    main()
