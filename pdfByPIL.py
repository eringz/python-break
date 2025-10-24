import cv2
import numpy as np
from PIL import Image

# === Step 1: Load and Enhance Image ===
img_path = "ALS BLDG - 1F.jpg"         # Original file
output_image = "ALS BLDG - 1F_sharp.jpg"
output_pdf = "ALS BLDG - 1F_sharp.pdf"

# Load image
image = cv2.imread(img_path)

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Sharpening kernel
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])
sharpened = cv2.filter2D(gray, -1, kernel)

# Optional: Increase contrast
contrast_enhanced = cv2.convertScaleAbs(sharpened, alpha=1.5, beta=20)
# alpha = contrast, beta = brightness

# Optional: Upscale for better print resolution
upscaled = cv2.resize(contrast_enhanced, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)

# Save as intermediate JPG
cv2.imwrite(output_image, upscaled)

# === Step 2: Convert to High-Quality PDF ===
image = Image.open(output_image)

# Convert to RGB if needed
if image.mode in ("RGBA", "P"):
    image = image.convert("RGB")

# Save as PDF with 300 DPI
image.save(output_pdf, "PDF", resolution=300.0)

print("✅ Done! PDF saved as:", output_pdf)
