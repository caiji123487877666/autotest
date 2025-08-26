import os
import logging
import time
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor, as_completed
from PIL import Image
from io import BytesIO
# 读五次
# 配置日志
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def file_generator(folder_path):
    """生成器，逐个返回文件路径，并记录日志"""
    start_time = time.time()  # 开始计时
    stack = [folder_path]
    while stack:
        current_dir = stack.pop()
        try:
            with os.scandir(current_dir) as entries:
                for entry in entries:
                    if entry.is_file():
                        file_path = str(Path(current_dir) / entry.name)
                        logging.debug(f"发现文件: {file_path}")  # 使用 debug 级别日志
                        yield file_path
                    elif entry.is_dir():
                        stack.append(str(Path(current_dir) / entry.name))
        except PermissionError:
            logging.warning(f"无法访问目录: {current_dir}")
            continue
    end_time = time.time()  # 结束计时
    return end_time - start_time  # 返回获取文件名称所花费的时间

def read_file_binary(file_path):
    """以二进制模式读取文件"""
    try:
        with open(file_path, 'rb') as file:
            content = file.read()
            return content
    except Exception as e:
        logging.error(f"读取文件失败: {file_path}, 错误: {e}")
        return None

def process_image(file_path, content):
    """处理图片文件"""
    try:
        with Image.open(BytesIO(content)) as img:
            return True
    except Exception as e:
        logging.error(f"读取图片失败: {file_path}, 错误: {e}")
        return False

def process_file(file_path):
    """根据文件扩展名读取文件"""
    content = read_file_binary(file_path)
    if content is None:
        logging.error(f"无法读取文件内容: {file_path}")
        return False

    if file_path.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp')):
        return process_image(file_path, content)
    else:
        return True

def read_files_once(folder_path):
    """单次读取所有文件"""
    file_time = file_generator(folder_path)  # 获取文件名称所花费的时间
    all_files = list(file_generator(folder_path))  # 重新生成文件列表
    if not all_files:
        logging.warning("没找到文件路径")
        return 0, 0, file_time

    logging.info(f"Found {len(all_files)} files. 开始读取文件...")

    read_count = 0
    failed_count = 0

    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = [executor.submit(process_file, file) for file in all_files]
        for future in as_completed(futures):
            success = future.result()
            read_count += 1
            if not success:
                failed_count += 1
            if read_count % 10 == 0:
                logging.info(f"已读取文件数量: {read_count}/{len(all_files)}，失败数量: {failed_count}")

    logging.info(f"文件读取完成。总文件数: {len(all_files)}，成功: {read_count - failed_count}，失败: {failed_count}")
    return read_count - failed_count, failed_count, file_time

def main():
    folder_path = "./999"  # 固定路径

    if not os.path.isdir(folder_path):
        logging.error(f"Error: {folder_path} 没有这个路径")
        return

    total_success = 0
    total_failed = 0
    total_file_time = 0.0

    for i in range(5):
        logging.info(f"开始第 {i + 1} 次读取...")
        success, failed, file_time = read_files_once(folder_path)
        total_success += success
        total_failed += failed
        total_file_time += file_time

    logging.info(f"所有读取完成。总成功: {total_success}，总失败: {total_failed}")
    logging.info(f"获取文件名称总时间: {total_file_time:.2f} 秒")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    logging.info(f"程序执行时间: {end_time - start_time:.2f} 秒")