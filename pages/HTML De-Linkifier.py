import os
import re

def remove_hyperlinks(html_content):
    # This function removes all hyperlinks from the HTML content
    return re.sub(r'<a\s+[^>]*>(.*?)</a>', r'\1', html_content, flags=re.DOTALL)

def process_html_files():
    # Get the current directory
    current_dir = os.getcwd()
    
    # List all files in the current directory
    for filename in os.listdir(current_dir):
        # Check if the file is an HTML file
        if filename.endswith('.html'):
            # Construct the full file path
            file_path = os.path.join(current_dir, filename)
            
            # Read the content of the HTML file
            with open(file_path, 'r', encoding='utf-8') as file:
                html_content = file.read()
            
            # Remove hyperlinks from the HTML content
            modified_content = remove_hyperlinks(html_content)
            
            # Create the new file name with " - LINKS_REMOVED" appended
            new_filename = filename.replace('.html', ' - LINKS_REMOVED.html')
            new_file_path = os.path.join(current_dir, new_filename)
            
            # Save the modified content to the new file
            with open(new_file_path, 'w', encoding='utf-8') as file:
                file.write(modified_content)
            
            print(f'Processed {filename} and saved as {new_filename}')

if __name__ == '__main__':
    process_html_files()