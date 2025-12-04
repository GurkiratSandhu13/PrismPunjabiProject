import os
import glob
import re

# --- Configuration ---

# IMPORTANT: Change this path to the directory containing your audio files
TARGET_DIR = '/Users/admin/University/Samsung Prism/Novel Dataset/Spoofed /f2 spoofed 1/IP14 plus 1m'

# The template for the new file names. 
# {SESSION_NUM} will be replaced by 01, 02, ..., 31.


NEW_NAME_TEMPLATE = "pa_S{SESSION_NUM}_f2_female_IP14Pl_MBP15_1m_90_east_60db_1_S"
#pa_S01_f2_female_IP14Pl_MBP15_1m_90_east_60db_1_S


# Maximum number of sessions/files to rename
MAX_SESSIONS = 50

# --- Script Logic ---

def rename_audio_files(target_dir, new_name_template, max_sessions):
    """
    Renames audio files in a directory sequentially based on a template.

    Args:
        target_dir (str): The path to the directory containing the files.
        new_name_template (str): The template for the new file names.
        max_sessions (int): The maximum number of files to rename (e.g., 31).
    """
    print(f"Starting renaming process in directory: {target_dir}")

    # 1. Get all audio files with common extensions
    audio_files = []
    # Use a set of common audio extensions
    extensions = ('*.wav', '*.mp3', '*.flac', '*.ogg', '*.m4a') 

    for ext in extensions:
        # Use glob to find files matching the extension and sort them alphabetically
        # This assumes your original files are ordered correctly when sorted.
        files = sorted(glob.glob(os.path.join(target_dir, ext)))
        audio_files.extend(files)

    if not audio_files:
        print("Error: No audio files found in the specified directory.")
        return

    # Sort the combined list again to ensure consistent order
    audio_files = sorted(audio_files)

    # Determine how many files we will actually process
    files_to_process = min(max_sessions, len(audio_files))

    if files_to_process < max_sessions:
        print(f"Warning: Only found {len(audio_files)} files. Will only rename up to S{files_to_process:02d}.")

    # 2. Iterate and rename
    renamed_count = 0
    for i in range(files_to_process):
        # Calculate the session number (1-based index)
        session_num_int = i + 1
        # Format the number as a two-digit string (e.g., 1 -> '01', 10 -> '10')
        session_num_str = f"{session_num_int:02d}"

        # Get the current full file path
        old_path = audio_files[i]
        
        # Extract the original file extension (e.g., .wav, .mp3)
        _, ext = os.path.splitext(old_path)

        # Construct the new filename using the template and session number
        new_filename_base = new_name_template.format(SESSION_NUM=session_num_str)
        new_filename = new_filename_base + ext.lower() # Ensure consistent lowercase extension
        
        # Construct the new full file path
        new_path = os.path.join(target_dir, new_filename)

        try:
            # Check if the new name already exists to prevent accidental overwrites
            if os.path.exists(new_path):
                print(f"Skipping: New file name {new_filename} already exists!")
                continue
                
            os.rename(old_path, new_path)
            print(f"Renamed: '{os.path.basename(old_path)}' -> '{new_filename}'")
            renamed_count += 1
            
        except Exception as e:
            print(f"Failed to rename file {os.path.basename(old_path)}: {e}")

    print(f"\n--- Renaming Complete ---")
    print(f"Successfully renamed {renamed_count} files.")


if __name__ == "__main__":
    # Ensure the target directory exists before running
    if not os.path.isdir(TARGET_DIR):
        print(f"Error: The directory '{TARGET_DIR}' was not found.")
        print("Please edit the TARGET_DIR variable in the script to the correct path.")
    else:
        rename_audio_files(TARGET_DIR, NEW_NAME_TEMPLATE, MAX_SESSIONS)
