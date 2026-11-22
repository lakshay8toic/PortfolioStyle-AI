"""
Pure Python helper to convert BMP images to PNG format using standard library zlib.
No external PIL/cv2 dependencies needed.
"""
import struct
import zlib
import os

def bmp_to_png(bmp_path, png_path):
    with open(bmp_path, 'rb') as f:
        header = f.read(54)
        if header[:2] != b'BM':
            raise ValueError("Not BMP")
        width = struct.unpack('<i', header[18:22])[0]
        height = struct.unpack('<i', header[22:26])[0]
        offset = struct.unpack('<I', header[10:14])[0]
        f.seek(offset)
        
        row_bytes = width * 3
        padding = (4 - (row_bytes % 4)) % 4
        
        rows = []
        for _ in range(abs(height)):
            data = f.read(row_bytes)
            f.read(padding)
            # BMP is BGR, convert to RGB
            rgb_row = bytearray()
            for i in range(0, len(data), 3):
                b, g, r = data[i], data[i+1], data[i+2]
                rgb_row.extend([r, g, b])
            rows.append(rgb_row)
            
        if height > 0:
            rows.reverse()
            
    # Encode PNG
    raw_scanlines = bytearray()
    for row in rows:
        raw_scanlines.append(0) # Filter type 0 (None)
        raw_scanlines.extend(row)
        
    compressed = zlib.compress(bytes(raw_scanlines))
    
    def chunk(tag, data):
        length = len(data)
        crc = zlib.crc32(tag + data) & 0xffffffff
        return struct.pack('>I', length) + tag + data + struct.pack('>I', crc)
        
    ihdr_data = struct.pack('>IIBBBBB', width, abs(height), 8, 2, 0, 0, 0)
    
    png_data = b'\x89PNG\r\n\x1a\n'
    png_data += chunk(b'IHDR', ihdr_data)
    png_data += chunk(b'IDAT', compressed)
    png_data += chunk(b'IEND', b'')
    
    with open(png_path, 'wb') as f:
        f.write(png_data)

if __name__ == '__main__':
    base_dir = "/Users/lakshay/.gemini/antigravity/scratch/PortfolioStyle-AI"
    for subdir in ["data/raw", "outputs/standardized", "outputs/comparisons"]:
        full_sub = os.path.join(base_dir, subdir)
        for f in os.listdir(full_sub):
            if f.endswith('.bmp'):
                png_name = f.replace('.bmp', '.png')
                bmp_to_png(os.path.join(full_sub, f), os.path.join(full_sub, png_name))
    print("All BMP images converted to web-compatible PNG format!")
