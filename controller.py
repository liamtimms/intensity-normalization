from intensity_normalization.normalize import nyul
import os

base_dir = os.path.abspath('../..')
datasink_dir = os.path.join(base_dir, 'derivatives', 'datasink')
manualwork_dir = os.path.join(base_dir, 'derivatives', 'manualwork')
cropped_dir = os.path.join(manualwork_dir, 'for_normalization', 'crop')

image_dir = os.path.join(manualwork_dir, 'for_normalization', 'images')
roi_dir = os.path.join(manualwork_dir, 'for_normalization', 'masks')
output_dir = os.path.join(manualwork_dir, 'for_normalization', 'out_nyul')

normalized = nyul.nyul_normalize(image_dir, roi_dir, output_dir)
