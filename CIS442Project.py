import os
path = "/Users/ncabr/Desktop/School Work/cis442/projectTests"
dir_list = os.listdir(path)
file_signatures = {}

def getFileType():
    global file_signatures
    file_signatures = {
        b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': 'PNG',
        b'\xff\xd8\xff\xe0\x00\x10JF': 'PNG',
        b'\xff\xd8\xff\xdb\x00\x84\x00\x08': 'PNG',   
        b'\xff\xd8\xff\xdb\x00\x84\x00\x09': 'PNG',
        b'\xff\xd8\xff\xdb\x00\x84\x00\x0c': 'PNG',
        b'\xff\xd8\xff\xdb\x00\x84\x00\x0d': 'PNG', 
        b'\xFF\xD8\xFF': 'JPEG',
        b'\xff\xd8\xff\xe0\x00\x10JFIF\x00\x01\x01\x01\x00H': 'JPEG',
        b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00': 'JPEG',
        b'\xff\xd8\xff\xe2\x00\x18ICC_PROFILE\x00\x00': 'JPEG',
        b'\xff\xd8\xff\xe3\x00\x18Photoshop 3.0\x00\x00': 'JPEG', 
        b'\xff\xd8\xff\xe8\x00\x10Ducky\x00\x00': 'JPEG',
        b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00': 'JPEG',
        b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00': 'JPEG',
        b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00': 'JPEG',
        b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00': 'JPEG',
        b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00': 'JPEG',
        b'\xff\xd8\xff\xe1\x00\x18Exif\x00\x00': 'JPEG',
        b'\x47\x49\x46\x38\x37\x61': 'GIF',
        b'\x47\x49\x46\x38\x39\x61': 'GIF',
        b'%PDF': 'PDF',
        b'%PDF-1.3': 'PDF',
        b'%PDF-1.4': 'PDF',
        b'%PDF-1.5': 'PDF',
        b'%PDF-1.6': 'PDF',
        b'%PDF-1.7': 'PDF',
        b'BM': 'BMP',
        b'\x4D\x5A\x90\x00': 'EXE',
        b'\x74\x65\x78\x74': 'TXT',
        b'\x50\x4B\x05\x06': 'JAR',
        b'\xEC\xA5\xC1\x00': 'DOC',
        b'\xFF\xD8\xFF\xE0': 'JPG',
        b'\x25\x50\x44\x46': 'PDF',
        b'\x00\x00\x00 ftyp': 'MP4',
        b'\xFF\xD8\xFF\xDB': 'JPEG',
        b'\xFF\xD8\xFF\xEE': 'JPEG',
    }
    
def compareFileTypes():
    for file in dir_list:
     with open(os.path.join(path, file), 'rb') as f:
        signature = f.read(8)
        if signature in file_signatures:
                pass
        else:
                print(f"{file} signature does not match.")

def main():
    getFileType()
    compareFileTypes()


if __name__ == "__main__":
    main()