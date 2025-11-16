"""使用 Quartz 直接获取 Retina 分辨率截图"""
from Quartz import (
    CGWindowListCreateImage,
    CGRectInfinite,
    CGRectMake,
    kCGWindowListOptionOnScreenOnly,
    kCGWindowImageDefault,
    kCGNullWindowID
)
from PIL import Image
import Quartz

def _screenshot_quartz(region=None):
    """
    使用 Quartz 截图（支持 Retina 物理像素）
    
    Args:
        region: (x, y, width, height) 或 None
    
    Returns:
        PIL.Image (Retina 分辨率)
    """
    if region is None:
        # 全屏
        cg_rect = CGRectInfinite
    else:
        # 指定区域 (逻辑像素)
        cg_rect = CGRectMake(region[0], region[1], region[2]/2, region[3]/2)
    
    # 截图 (kCGWindowImageDefault 会返回 Retina 分辨率)
    cg_image = CGWindowListCreateImage(
        cg_rect,
        kCGWindowListOptionOnScreenOnly,
        kCGNullWindowID,
        kCGWindowImageDefault
    )
    
    if cg_image is None:
        return None
    
    # 转换为 PIL Image
    width = Quartz.CGImageGetWidth(cg_image)
    height = Quartz.CGImageGetHeight(cg_image)
    bytes_per_row = Quartz.CGImageGetBytesPerRow(cg_image)
    
    # 获取像素数据
    data_provider = Quartz.CGImageGetDataProvider(cg_image)
    pixel_data = Quartz.CGDataProviderCopyData(data_provider)
    
    # 创建 PIL Image
    img = Image.frombytes(
        'RGBA',
        (width, height),
        pixel_data,
        'raw',
        'BGRA',
        bytes_per_row
    )
    
    # 转换为 RGB
    img = img.convert('RGB')
    
    return img

def screenshot_quartz(imageFilename=None, region=None):
    """使用 Quartz 截图（完美支持 Retina）"""
    img = _screenshot_quartz(region)
    
    if imageFilename:
        img.save(imageFilename)
    
    return img