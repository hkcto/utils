import os

def batch_rename(directory, prefix):
    # 獲取目錄中的所有文件
    files = os.listdir(directory)
    
    # 遍歷所有文件並重命名
    for index, filename in enumerate(files):
        # 獲取文件擴展名
        file_extension = os.path.splitext(filename)[1]
        # 生成新的文件名
        new_filename = f"{prefix}-{index + 1}{file_extension}"
        # 獲取完整的舊文件和新文件路徑
        old_file = os.path.join(directory, filename)
        new_file = os.path.join(directory, new_filename)
        # 重命名文件
        os.rename(old_file, new_file)
        print(f"Renamed: {old_file} -> {new_file}")

if __name__ == "__main__":
    directory = "epam/listing-ceremony"  # 替換為你想要重新命名文件的目錄路徑
    prefix = "photos"  # 替換為你想要的新文件名前綴
    batch_rename(directory, prefix)
