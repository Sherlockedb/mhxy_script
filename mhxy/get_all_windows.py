from Quartz import (
    CGWindowListCopyWindowInfo,
    kCGWindowListOptionOnScreenOnly,
    kCGNullWindowID
)


class QuartzWindow:
    """兼容 pywinctl 的窗口对象"""
    def __init__(self, window_info):
        bounds = window_info.get('kCGWindowBounds', {})
        self.left = int(bounds.get('X', 0))
        self.top = int(bounds.get('Y', 0))
        self.width = int(bounds.get('Width', 0))
        self.height = int(bounds.get('Height', 0))
        self.right = self.left + self.width
        self.bottom = self.top + self.height

        self.title = window_info.get('kCGWindowName', '')
        self.owner = window_info.get('kCGWindowOwnerName', '')
        self.window_id = window_info.get('kCGWindowNumber', 0)
        self.layer = window_info.get('kCGWindowLayer', 0)
        self.isActive = True  # 假设都是激活状态

    def activate(self):
        """激活窗口（尝试使用 pywinctl）"""
        try:
            import pywinctl as pwc
            # 尝试通过标题激活
            if self.title:
                wins = pwc.getWindowsWithTitle(self.title)
                if wins:
                    wins[0].activate()
                    return
            # 尝试通过应用名激活
            if self.owner:
                wins = pwc.getWindowsWithTitle(self.owner)
                if wins:
                    wins[0].activate()
        except Exception as e:
            print(f"激活窗口失败: {e}")

    def __repr__(self):
        return f"QuartzWindow(title='{self.title}', owner='{self.owner}', pos=({self.left},{self.top}), size={self.width}x{self.height})"


def getWindowsWithTitleQuartz(title_part):
    """
    使用 Quartz API 获取窗口（支持多实例）
    返回值格式与 pywinctl.getWindowsWithTitle() 兼容

    Args:
        title_part: 窗口标题或应用名的部分内容（不区分大小写）

    Returns:
        list: 窗口对象列表，每个对象有 left, top, width, height, title, activate() 等属性

    Example:
        windows = getWindowsWithTitleQuartz('BlueStacks Air')
        for win in windows:
            print(f"窗口: {win.title}, 位置: ({win.left}, {win.top})")
    """
    window_list = CGWindowListCopyWindowInfo(
        kCGWindowListOptionOnScreenOnly,
        kCGNullWindowID
    )

    matched_windows = []
    title_lower = title_part.lower()

    for window in window_list:
        owner = window.get('kCGWindowOwnerName', '')
        name = window.get('kCGWindowName', '')
        bounds = window.get('kCGWindowBounds', {})

        # 匹配条件：标题或应用名包含关键字，且窗口足够大（过滤工具栏等）
        if (title_lower in owner.lower() or title_lower in name.lower()) and \
           bounds.get('Width', 0) > 100 and bounds.get('Height', 0) > 100:
            matched_windows.append(QuartzWindow(window))

    return matched_windows


def get_all_windows_quartz(app_name=None):
    """获取所有窗口信息（原始版本，用于调试）"""
    window_list = CGWindowListCopyWindowInfo(
        kCGWindowListOptionOnScreenOnly,
        kCGNullWindowID
    )

    windows = []
    for window in window_list:
        owner = window.get('kCGWindowOwnerName', '')
        name = window.get('kCGWindowName', '')
        window_id = window.get('kCGWindowNumber', 0)
        bounds = window.get('kCGWindowBounds', {})
        layer = window.get('kCGWindowLayer', 0)

        # 过滤：只要有标题或属于指定应用的窗口
        if app_name is None or app_name.lower() in owner.lower():
            windows.append({
                'owner': owner,
                'name': name,
                'id': window_id,
                'bounds': bounds,
                'layer': layer,
                'left': int(bounds.get('X', 0)),
                'top': int(bounds.get('Y', 0)),
                'width': int(bounds.get('Width', 0)),
                'height': int(bounds.get('Height', 0))
            })

    return windows


if __name__ == '__main__':
    # 使用示例
    print("=" * 60)
    print("测试 getWindowsWithTitleQuartz():")
    print("=" * 60)

    windows = getWindowsWithTitleQuartz('BlueStacksAir')
    print(f"\n找到 {len(windows)} 个窗口:\n")

    for i, win in enumerate(windows):
        print(f"窗口 {i}:")
        print(f"  标题: {win.title}")
        print(f"  应用: {win.owner}")
        print(f"  位置: ({win.left}, {win.top})")
        print(f"  大小: {win.width} x {win.height}")
        print(f"  对象: {win}")
        print()

    print("\n" + "=" * 60)
    print("测试 get_all_windows_quartz() (原始版本):")
    print("=" * 60)

    windows = get_all_windows_quartz('bluestacks')
    for i, win in enumerate(windows):
        print(f"\n窗口 {i + 1}:")
        print(f"  应用: {win['owner']}")
        print(f"  标题: {win['name']}")
        print(f"  ID: {win['id']}")
        print(f"  位置: ({win['left']}, {win['top']})")
        print(f"  大小: {win['width']} x {win['height']}")
        print(f"  层级: {win['layer']}")