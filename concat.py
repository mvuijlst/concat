import os
import subprocess
import sys
from tqdm import tqdm

def get_file_size(file):
    return os.path.getsize(file)

def display_file_sizes(files):
    print("Matching files:")
    total_size = 0
    for file in files:
        size = get_file_size(file)
        print(f"{file}: {size / (1024 * 1024):.2f} MB")
        total_size += size
    return total_size

def concatenate_videos(input_files, output_file):
    # Create a temporary file listing all input files
    with open('inputs.txt', 'w') as f:
        for file in input_files:
            f.write(f"file '{file}'\n")

    command = [
        'ffmpeg', '-f', 'concat', '-safe', '0', '-i', 'inputs.txt',
        '-c', 'copy', output_file
    ]
    
    # Run the ffmpeg command with progress bar
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    for line in process.stderr:
        print(line.strip())
    
    os.remove('inputs.txt')  # Clean up temporary file

def process_folder(folder_path, partial_filename):
    files = os.listdir(folder_path)
    matching_files = sorted([os.path.join(folder_path, f) for f in files if f.startswith(partial_filename) and f[-4:] in ['.avi', '.mp4', '.wmv']])

    if not matching_files:
        print(f"No matching files found for {partial_filename}")
        return

    # Display file sizes and ask for confirmation
    total_original_size = display_file_sizes(matching_files)
    
    confirm = input(f"\nDo you want to concatenate these files into {partial_filename}.mp4? (y/n): ").lower()
    if confirm != 'y':
        print("Concatenation aborted.")
        return

    output_file = os.path.join(folder_path, f"{partial_filename}.mp4")

    print("\nStarting concatenation...")
    concatenate_videos(matching_files, output_file)

    # Calculate size of the concatenated file
    concatenated_size = get_file_size(output_file)
    size_difference = total_original_size - concatenated_size

    print(f"\nConcatenated file size: {concatenated_size / (1024 * 1024):.2f} MB")
    print(f"Original total size: {total_original_size / (1024 * 1024):.2f} MB")
    print(f"Size difference: {size_difference / (1024 * 1024):.2f} MB")

    # Ask for confirmation to delete the original files
    delete_confirm = input("\nDo you want to delete the original files? (y/n): ").lower()
    if delete_confirm == 'y':
        for file in matching_files:
            os.remove(file)
            print(f"Deleted {file}")
    else:
        print("Original files retained.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python concat.py <partial_filename>")
        sys.exit(1)

    partial_filename = sys.argv[1]
    folder_path = os.getcwd()  # Get the current working directory
    process_folder(folder_path, partial_filename)
