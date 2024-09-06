# Movie File Concatenator

A Python script to concatenate movie files that have the same base filename but differ in suffix (e.g., `A`, `B`, `C`, etc.). The script is designed to work with multiple movie file formats such as `.avi`, `.mp4`, and `.wmv`.

## Features

- **Concatenation of movie files**: Automatically finds and concatenates files that start with the same base filename and end with suffixes `A`, `B`, `C`, etc.
- **User Confirmation**: Displays file sizes and asks for confirmation before performing the concatenation.
- **Progress Tracking**: Shows a progress bar during the concatenation process using `tqdm`.
- **File Size Reporting**: After concatenation, reports the total size of the original files, the size of the concatenated file, and the difference in sizes.
- **Original File Deletion**: Offers the option to delete the original files after successful concatenation.

## Prerequisites

Before using the script, ensure you have the following installed:

- [Python 3.x](https://www.python.org/downloads/)
- [FFmpeg](https://ffmpeg.org/download.html) installed and accessible via your system's PATH.
- Install the required Python package:
  ```bash
  pip install tqdm
