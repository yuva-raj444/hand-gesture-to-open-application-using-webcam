import win32gui
import win32con

# Function to get the OpenCV window handle
def get_opencv_window_handle(window_name="Hand Gesture App Launcher"):
    def callback(hwnd, window_list):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd) == window_name:
            window_list.append(hwnd)
    result = []
    win32gui.EnumWindows(callback, result)
    return result[0] if result else None

# Function to close the most recent visible window excluding OpenCV and VS Code
def close_recent_window(exclude_hwnd):
    def enum_handler(hwnd, result_list):
        if win32gui.IsWindowVisible(hwnd) and win32gui.GetWindowText(hwnd):
            result_list.append(hwnd)

    hwnds = []
    win32gui.EnumWindows(enum_handler, hwnds)

    for hwnd in hwnds:
        if hwnd != exclude_hwnd:
            window_title = win32gui.GetWindowText(hwnd)
            if "Visual Studio Code" in window_title or "Code" in window_title:
                continue
            print("🛑 Closing:", window_title)
            win32gui.PostMessage(hwnd, win32con.WM_CLOSE, 0, 0)
            break
