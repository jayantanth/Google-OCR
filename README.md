# Google-OCR
Google OCR script by Saunak Roy Chowdhury

Follow the Google API authentication as describe here for Drive OCR .. 
See a demo video on installation, setup, usage in here: https://www.youtube.com/watch?v=PH9TnD67oj4&feature=youtu.be

1. install gdcmdtools from https://github.com/tienfuc/gdcmdtools and complete the setup

2. Use "Ghost Script" tool to convert a pdf into individual images.

exaimple:

gs -q -DNOPAUSE -DBATCH -r400 -SDEVICE=a4 -sOutputFile=abcd%d.jpg abcd.pdf

3. Download google-ocr.py script at same JPG image  folder

4. Run python google-ocr.py "abcd"   where abcd name of out text file.
