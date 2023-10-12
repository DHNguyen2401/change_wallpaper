import ctypes
import os
import random
import time

def change_wallpaper(path):
    """Thay đổi hình nền của máy tính."""
    SPI_SETDESKWALLPAPER = 20

    # Kiểm tra xem tệp tin hình nền có tồn tại không
    if not os.path.exists(path):
        print(f"Tệp tin {path} không tồn tại.")
        return

    # Thay đổi hình nền
    ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, path, 3)

if __name__ == "__main__":
    # Thay đổi hình nền tự động sau mỗi 10 giây
    while True:
        # Đường dẫn đến thư mục chứa hình nền (thay đổi thành thư mục của bạn)
        wallpaper_directory = r"C:\Users\ADMIN\Pictures\Camera Roll"

        # Lấy danh sách các tệp tin trong thư mục hình nền
        wallpapers = [f for f in os.listdir(wallpaper_directory) if f.endswith(('.jpg', '.png', '.jpeg'))]

        # Nếu có ít nhất một tệp tin hình nền
        if wallpapers:
            # Chọn ngẫu nhiên một tệp tin hình nền
            selected_wallpaper = os.path.join(wallpaper_directory, random.choice(wallpapers))

            # Thay đổi hình nền
            change_wallpaper(selected_wallpaper)

            print(f"Hình nền đã được thay đổi: {selected_wallpaper}")

        # Đợi 10 giây trước khi thay đổi hình nền tiếp theo
        time.sleep(10)
