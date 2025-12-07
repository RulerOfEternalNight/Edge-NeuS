import os
import cv2
from pathlib import Path

def generate_edges(
    images_dir="image",
    edges_dir="edge",
    low_threshold=100,
    high_threshold=200
):
    images_path = Path(images_dir)
    edges_path = Path(edges_dir)

    # Create output directory if it doesn't exist
    edges_path.mkdir(parents=True, exist_ok=True)

    # Supported extensions
    exts = {".png", ".jpg", ".jpeg", ".bmp", ".tif", ".tiff"}

    img_files = [p for p in images_path.iterdir() if p.suffix.lower() in exts]

    if not img_files:
        print(f"No images found in {images_path}")
        return

    print(f"Found {len(img_files)} images in {images_path}")
    print(f"Saving edges to {edges_path}")

    for img_path in img_files:
        # Read as grayscale
        img = cv2.imread(str(img_path), cv2.IMREAD_GRAYSCALE)
        if img is None:
            print(f"Warning: could not read {img_path}, skipping.")
            continue

        # Canny edge detection (output is already 0–255 uint8)
        edges = cv2.Canny(img, low_threshold, high_threshold)

        # Keep same filename, just different folder
        out_path = edges_path / img_path.name

        # Save edge image
        cv2.imwrite(str(out_path), edges)
        print(f"Saved edges: {out_path}")

if __name__ == "__main__":
    # Adjust thresholds if needed
    generate_edges(
        images_dir="image",
        edges_dir="edge",
        low_threshold=100,
        high_threshold=200,
    )
