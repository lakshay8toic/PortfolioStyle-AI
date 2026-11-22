"""
Dataset Preprocessing & Statistical Analysis Module
Reads image data, extracts dimensions, channels, brightness, contrast, color temperature,
and generates JSON and Markdown summary reports.
"""
import os
import struct
import json
import math

def read_bmp(file_path):
    """Read 24-bit uncompressed BMP file using Python standard library."""
    with open(file_path, 'rb') as f:
        header = f.read(54)
        if header[0:2] != b'BM':
            raise ValueError(f"Not a valid BMP file: {file_path}")
        
        file_size = struct.unpack('<I', header[2:6])[0]
        offset = struct.unpack('<I', header[10:14])[0]
        width = struct.unpack('<i', header[18:22])[0]
        height = struct.unpack('<i', header[22:26])[0]
        bpp = struct.unpack('<H', header[28:30])[0]
        
        f.seek(offset)
        # 24-bit BMP row size is padded to 4 bytes
        row_bytes = width * 3
        padding = (4 - (row_bytes % 4)) % 4
        
        pixels_rgb = []
        # BMP is stored bottom-up
        rows = []
        for _ in range(abs(height)):
            row_data = f.read(row_bytes)
            f.read(padding)
            row_pixels = []
            for i in range(0, len(row_data), 3):
                b, g, r = row_data[i], row_data[i+1], row_data[i+2]
                row_pixels.append((r, g, b))
            rows.append(row_pixels)
        
        # If height was positive, invert rows to top-down
        if height > 0:
            rows.reverse()
            
        return {
            'width': width,
            'height': abs(height),
            'bpp': bpp,
            'rows': rows
        }

def analyze_image_characteristics(bmp_data, file_name):
    width = bmp_data['width']
    height = bmp_data['height']
    total_pixels = width * height
    
    sum_r = sum_g = sum_b = 0
    luminances = []
    
    for row in bmp_data['rows']:
        for r, g, b in row:
            sum_r += r
            sum_g += g
            sum_b += b
            # Perceived luminance (ITU-R BT.601)
            lum = 0.299 * r + 0.587 * g + 0.114 * b
            luminances.append(lum)
            
    avg_r = sum_r / total_pixels
    avg_g = sum_g / total_pixels
    avg_b = sum_b / total_pixels
    avg_lum = sum(luminances) / total_pixels
    
    # Calculate contrast (standard deviation of luminance)
    variance = sum((lum - avg_lum) ** 2 for lum in luminances) / total_pixels
    contrast = math.sqrt(variance)
    
    # Estimate color temperature bias
    if avg_b > avg_r + 15:
        tone = "Cool / Blueish (Needs Warmth)"
    elif avg_r > avg_b + 20:
        tone = "Overly Warm / Amber"
    else:
        tone = "Neutral / Balanced"
        
    return {
        'file_name': file_name,
        'dimensions': f"{width}x{height}",
        'aspect_ratio': f"{width/height:.2f}:1",
        'avg_rgb': [round(avg_r, 1), round(avg_g, 1), round(avg_b, 1)],
        'mean_brightness': round(avg_lum, 1),
        'contrast_std': round(contrast, 1),
        'detected_tone': tone,
        'target_recommendation': "Apply Warm Editorial Preset (Golden 3200K, Contrast +15%, Shadows Lifted +10%)"
    }

def run_dataset_preparation(raw_dir, output_report_path):
    files = [f for f in os.listdir(raw_dir) if f.endswith('.bmp')]
    analysis_results = []
    
    for f in sorted(files):
        img_data = read_bmp(os.path.join(raw_dir, f))
        analysis = analyze_image_characteristics(img_data, f)
        analysis_results.append(analysis)
        
    os.makedirs(os.path.dirname(output_report_path), exist_ok=True)
    with open(output_report_path, 'w') as out_f:
        json.dump(analysis_results, out_f, indent=2)
        
    print(f"Analyzed {len(analysis_results)} images. Report saved to {output_report_path}")
    return analysis_results

if __name__ == '__main__':
    raw_dir = "/Users/lakshay/.gemini/antigravity/scratch/PortfolioStyle-AI/data/raw"
    out_json = "/Users/lakshay/.gemini/antigravity/scratch/PortfolioStyle-AI/data/processed/dataset_analysis.json"
    run_dataset_preparation(raw_dir, out_json)
