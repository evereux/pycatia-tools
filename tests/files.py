import os
from pathlib import Path

test_files_root = Path(os.getcwd(), 'tests', 'test_files')

cat_part =Path(test_files_root, "Part1.CATPart")
cat_product =Path(test_files_root, "Product1.CATProduct")
cat_drawing = Path(test_files_root, "Drawing1.CATDrawing")