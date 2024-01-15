import os 
import shutil 


#When entering in your paths and replacing the ones below. I had to use a dual \ character I recieved a trunticating error that was not reading the path correct until that was added. 
 
#Your Starting directory where you want to pull the files from
source_dir = "C:\\Users\\chris\\Downloads"
#Target drectory to wear you file will be saved 
target_dir = "C:\\Users\\chris\\OneDrive"

#Create destination folders if they don't exist
categories = ['Images', 'Documents', 'Music', 'Videos']
for category in categories:
    category_path = os.path.join(target_dir, category)
    os.makedirs(category_path, exist_ok=True)

# Function to sort files based on file type
def sort_files_by_type(source_dir, target_dir):
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower()
            if file_extension in ('jpg', 'png', 'gif','bmp', 'tiff', 'raw','svg', 'psd', 'ai'):
                shutil.move(file_path, os.path.join(target_dir, 'Images', filename))
            elif file_extension in ('pdf', 'doc', 'txt', 'rtf', 'csv', 'xls', 'xlsx', 'ppt', 'pptx', 'odt', 'pages', 'numbers', 'key', 'md'):
                shutil.move(file_path, os.path.join(target_dir, 'Documents', filename))
            elif file_extension in ('mp3', 'wav', 'flac', 'aac', 'wma', 'ogg', 'm4a', 'midi', 'flp', 'm3u'):
                shutil.move(file_path, os.path.join(target_dir, 'Music', filename))
            elif file_extension in ('mp4', 'avi', 'mkv','mov','wmv', 'flv','3gp','mpeg', 'webm', 'vob', 'rm', 'swf', 'ts'):
                shutil.move(file_path, os.path.join(target_dir, 'Videos', filename))

sort_files_by_type(source_dir, target_dir)
