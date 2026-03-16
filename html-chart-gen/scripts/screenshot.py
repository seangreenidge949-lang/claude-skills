#!/usr/bin/env python3
"""
HTML Chart Screenshot Tool
将 HTML 图表文件截图为 PNG，自动裁剪到卡片区域。

用法:
    python3 screenshot.py <html_file> [--output <png_path>]

自动检测 playwright 安装位置（pipx venv 或系统 pip）。
"""

import argparse
import http.server
import os
import socket
import subprocess
import sys
import threading
import time
from pathlib import Path


def find_free_port():
    """找一个空闲端口"""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(("", 0))
        return s.getsockname()[1]


def start_server(directory, port):
    """在指定目录启动 HTTP 服务"""
    os.chdir(directory)
    handler = http.server.SimpleHTTPRequestHandler

    class QuietHandler(handler):
        def log_message(self, format, *args):
            pass  # 静默日志

    httpd = http.server.HTTPServer(("127.0.0.1", port), QuietHandler)
    httpd.serve_forever()


def _ensure_playwright():
    """尝试导入 playwright，支持 pipx venv 和系统 pip 两种安装方式"""
    try:
        from playwright.sync_api import sync_playwright
        return sync_playwright
    except ImportError:
        pass

    # 尝试从 pipx venv 导入
    pipx_venv = Path.home() / ".local/pipx/venvs/playwright"
    if pipx_venv.exists():
        import glob
        site_packages = glob.glob(str(pipx_venv / "lib/python*/site-packages"))
        if site_packages:
            sys.path.insert(0, site_packages[0])
            try:
                from playwright.sync_api import sync_playwright
                return sync_playwright
            except ImportError:
                pass

    print("错误: 需要安装 playwright")
    print("  pipx install playwright && playwright install chromium")
    print("  或 pip3 install playwright && playwright install chromium")
    sys.exit(1)


def screenshot_with_playwright(url, output_path):
    """用 Playwright 截图"""
    sync_playwright = _ensure_playwright()

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(
            viewport={"width": 1200, "height": 800},
            device_scale_factor=2,  # 2x 清晰度
        )
        page.goto(url, wait_until="networkidle")
        # 等内容渲染完成
        page.wait_for_timeout(500)

        # 截取 .card 元素（精确裁剪到卡片区域）
        card = page.query_selector(".card")
        if card:
            card.screenshot(path=str(output_path))
        else:
            # 如果没有 .card，截全页
            page.screenshot(path=str(output_path), full_page=True)

        browser.close()


def main():
    parser = argparse.ArgumentParser(description="HTML 图表截图工具")
    parser.add_argument("html_file", help="HTML 文件路径")
    parser.add_argument("--output", "-o", help="PNG 输出路径（默认与 HTML 同名）")
    args = parser.parse_args()

    html_path = Path(args.html_file).resolve()
    if not html_path.exists():
        print(f"错误: 文件不存在 — {html_path}")
        sys.exit(1)

    # 确定输出路径
    if args.output:
        output_path = Path(args.output).resolve()
    else:
        output_path = html_path.with_suffix(".png")

    output_path.parent.mkdir(parents=True, exist_ok=True)

    # 启动本地服务
    port = find_free_port()
    server_dir = str(html_path.parent)
    server_thread = threading.Thread(
        target=start_server, args=(server_dir, port), daemon=True
    )
    server_thread.start()
    time.sleep(0.3)  # 等服务启动

    url = f"http://127.0.0.1:{port}/{html_path.name}"

    try:
        screenshot_with_playwright(url, output_path)
        print(f"截图已保存: {output_path}")
    except Exception as e:
        print(f"截图失败: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
