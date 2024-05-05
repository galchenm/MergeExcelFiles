import gdown
import glob
import os
import pandas as pd


outdir = 'excel_files_merge'
if not os.path.exists(outdir):
  url = 'https://drive.google.com/drive/folders/1J5UwgPlsUHIZ0729G9uk4HKpiJPSpMpE?usp=sharing'
  gdown.download_folder(url, quiet=True, use_cookies=False)

files = glob.glob(os.path.join(outdir, '*.xlsx'))

frames = [pd.read_excel(file) for file in files]
result = pd.concat(frames, ignore_index=True)
result.to_excel(f'{outdir}/modified_file.xlsx', index=False)