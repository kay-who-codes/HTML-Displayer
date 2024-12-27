import os
import pyperclip

def detect_html_files(folder_path):
    # List all files in the given folder
    all_files = os.listdir(folder_path)
    
    # Filter out only the .html files
    html_files = [file for file in all_files if file.endswith('.html')]
    
    return html_files

def create_formatted_list(html_files):
    formatted_text = "document.addEventListener('DOMContentLoaded', () => {\n"
    formatted_text += "    const pages = [\n"
    
    for file in html_files:
        title = os.path.splitext(file)[0]
        formatted_text += f"        {{ title: '{title}', file: '{file}' }},\n"
    
    formatted_text += "    ];\n"
    formatted_text += "});\n"
    
    return formatted_text

def main():
    folder_path = os.path.dirname(os.path.abspath(__file__))
    
    html_files = detect_html_files(folder_path)
    formatted_text = create_formatted_list(html_files)
    
    # Copy the formatted text to the clipboard
    pyperclip.copy(formatted_text)
    print("Formatted text has been copied to the clipboard")

if __name__ == "__main__":
    main()