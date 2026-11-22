"""
Helper script using pure Python standard library to generate sample synthetic hotel images (PPM format converted to BMP/PNG representation)
so that the project has real image files to analyze and process without external library dependencies!
"""
import os
import math

def write_ppm(filename, width, height, pixels):
    """Write PPM (Portable Pixmap) image - simple uncompressed RGB format."""
    with open(filename, 'wb') as f:
        f.write(f"P6\n{width} {height}\n255\n".encode('ascii'))
        f.write(bytearray(pixels))

def write_bmp(filename, width, height, pixels_rgb):
    """Write standard 24-bit uncompressed BMP file using pure Python."""
    # BMP rows must be padded to multiples of 4 bytes
    row_bytes = width * 3
    padding = (4 - (row_bytes % 4)) % 4
    image_size = (row_bytes + padding) * height
    file_size = 54 + image_size
    
    header = bytearray(54)
    # BM header
    header[0:2] = b'BM'
    header[2:6] = file_size.to_bytes(4, 'little')
    header[10:14] = (54).to_bytes(4, 'little') # offset to pixel data
    # DIB Header (BITMAPINFOHEADER)
    header[14:18] = (40).to_bytes(4, 'little') # header size
    header[18:22] = width.to_bytes(4, 'little', signed=True)
    header[22:26] = height.to_bytes(4, 'little', signed=True) # positive means bottom-to-top
    header[26:28] = (1).to_bytes(2, 'little') # color planes
    header[28:30] = (24).to_bytes(2, 'little') # bits per pixel
    header[34:38] = image_size.to_bytes(4, 'little')
    
    # Pack pixel data (BGR order, bottom-up)
    body = bytearray()
    for y in range(height - 1, -1, -1):
        for x in range(width):
            idx = (y * width + x) * 3
            r, g, b = pixels_rgb[idx], pixels_rgb[idx+1], pixels_rgb[idx+2]
            body.extend([b, g, r]) # BMP uses BGR
        if padding > 0:
            body.extend([0] * padding)
            
    with open(filename, 'wb') as f:
        f.write(header)
        f.write(body)

def create_sample_images():
    output_dir = "/Users/lakshay/.gemini/antigravity/scratch/PortfolioStyle-AI/data/raw"
    os.makedirs(output_dir, exist_ok=True)
    
    W, H = 512, 512
    
    # 1. hotel_lobby_cool.bmp: Cool fluorescent lighting, blue-ish tint, marble floor
    lobby = bytearray(W * H * 3)
    for y in range(H):
        for x in range(W):
            idx = (y * W + x) * 3
            if y < 200: # Ceiling & wall
                r, g, b = 160, 180, 220
            elif y < 350: # Reception counter / pillars
                if 180 < x < 330: # Desk
                    r, g, b = 130, 140, 170
                else:
                    r, g, b = 180, 190, 210
            else: # Marble floor
                val = (x // 30 + y // 30) % 2 * 20
                r, g, b = 170 + val, 185 + val, 215 + val
            lobby[idx] = min(255, max(0, r))
            lobby[idx+1] = min(255, max(0, g))
            lobby[idx+2] = min(255, max(0, b))
    write_bmp(os.path.join(output_dir, "hotel_lobby_cool.bmp"), W, H, lobby)

    # 2. hotel_deluxe_room_dim.bmp: Low-light, yellowish/underexposed bedroom
    room = bytearray(W * H * 3)
    for y in range(H):
        for x in range(W):
            idx = (y * W + x) * 3
            if y < 220: # Dark wall & headboard
                r, g, b = 90, 75, 50
                if 150 < x < 360 and y > 100: # Headboard
                    r, g, b = 110, 80, 40
            elif y < 400: # Bed & duvet
                if 140 < x < 370: # Bed
                    r, g, b = 160, 140, 100
                else: # Side tables
                    r, g, b = 80, 60, 40
            else: # Carpet
                r, g, b = 70, 55, 45
            room[idx] = min(255, max(0, r))
            room[idx+1] = min(255, max(0, g))
            room[idx+2] = min(255, max(0, b))
    write_bmp(os.path.join(output_dir, "hotel_deluxe_room_dim.bmp"), W, H, room)

    # 3. hotel_exterior_harsh.bmp: Overexposed sunlight exterior building facade
    exterior = bytearray(W * H * 3)
    for y in range(H):
        for x in range(W):
            idx = (y * W + x) * 3
            if y < 180: # Harsh washed-out sky
                r, g, b = 230, 240, 255
            elif y < 430: # Hotel building facade with windows
                # Window grid
                is_window = (x % 40 < 18) and (y % 40 < 22) and (60 < x < 450)
                if is_window:
                    r, g, b = 100, 130, 160
                else:
                    r, g, b = 245, 235, 220 # Pale concrete
            else: # Entrance lawn and driveway
                r, g, b = 90, 140, 60
            exterior[idx] = min(255, max(0, r))
            exterior[idx+1] = min(255, max(0, g))
            exterior[idx+2] = min(255, max(0, b))
    write_bmp(os.path.join(output_dir, "hotel_exterior_harsh.bmp"), W, H, exterior)

    # 4. hotel_poolside_mixed.bmp: Resort swimming pool with mixed outdoor shadows
    pool = bytearray(W * H * 3)
    for y in range(H):
        for x in range(W):
            idx = (y * W + x) * 3
            if y < 160: # Sky and distant palm trees
                r, g, b = 150, 190, 230
            elif y < 280: # Pool deck / loungers
                r, g, b = 180, 160, 140
            else: # Pool water
                r, g, b = 30, 150, 200
            pool[idx] = min(255, max(0, r))
            pool[idx+1] = min(255, max(0, g))
            pool[idx+2] = min(255, max(0, b))
    write_bmp(os.path.join(output_dir, "hotel_poolside_mixed.bmp"), W, H, pool)

    print("Created 4 sample hotel raw images in BMP format.")

if __name__ == "__main__":
    create_sample_images()
