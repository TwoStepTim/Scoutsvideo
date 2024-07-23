import os

def list_files_in_folder(folder_path):
    """
    Lists all files in the specified folder.
    
    Args:
    - folder_path (str): The path to the folder.
    
    Returns:
    - file_names (list): A list of file names in the folder.
    """
    # Check if the folder exists
    if not os.path.exists(folder_path):
        print("Folder does not exist.")
        return []
    
    # Get all files in the folder
    file_names = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))]
    
    return file_names

def write_to_file(file_names, output_file):
    """
    Writes the list of file names to a text file.
    
    Args:
    - file_names (list): A list of file names.
    - output_file (str): The path to the output text file.
    """
    with open(output_file, 'w') as f:
        for file_name in file_names:
            f.write(file_name + '\n')

# Example usage:
folder_path = r"D:\GithubRepo\NewScouts\img"  # Using raw string literal
output_file = "file_names.txt"

files = list_files_in_folder(folder_path)
write_to_file(files, output_file)
print("File names have been written to:", output_file)
