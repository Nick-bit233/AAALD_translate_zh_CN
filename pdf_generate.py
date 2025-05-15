import glob
import markdown
from weasyprint import HTML, CSS 
import os
import traceback

def merge_markdown_to_pdf_weasyprint(markdown_file_paths, output_pdf_path, source_directory, custom_css_path=None):
    """
    将多个 Markdown 文件合并并使用 WeasyPrint 转换为一个 PDF 文件。
    使用 base_url 来帮助解析相对图片路径。

    参数:
    markdown_file_paths (list): 按合并顺序列出的 Markdown 文件路径列表。
    output_pdf_path (str): 输出的 PDF 文件路径。
    source_directory (str): Markdown 文件所在的源目录 (例如 "finished_md")。
                            将用作 HTML 解析时的 base_url。
    custom_css_path (str, optional): 自定义 CSS 文件的路径。
    """
    html_parts = []
    md_extensions = ['extra', 'codehilite', 'tables', 'fenced_code', 'toc']

    print("\n开始使用 WeasyPrint 方法处理文件...")
    for md_file in markdown_file_paths:
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                md_content = f.read()
                html_part = markdown.markdown(md_content, extensions=md_extensions)
                html_parts.append(f'<div class="document-part">{html_part}</div>')
                print(f"  [WeasyPrint] 已处理文件: {os.path.basename(md_file)}")
        except FileNotFoundError:
            print(f"  [WeasyPrint] 警告: 文件 {md_file} 未找到，已跳过。")
        except Exception as e:
            print(f"  [WeasyPrint] 处理文件 {md_file} 时出错: {e}")
            print(traceback.format_exc())

    if not html_parts:
        print("[WeasyPrint] 没有可处理的 Markdown 文件内容。PDF 未生成。")
        return

    full_html_content = "".join(html_parts)
    base_css_string = """
    @page { size: A4; margin: 2cm; }
    body { font-family: "Helvetica Neue", Helvetica, Arial, sans-serif; line-height: 1.6; color: #333; }
    .document-part { page-break-after: always; } .document-part:last-child { page-break-after: auto; }
    h1, h2, h3, h4, h5, h6 { page-break-after: avoid; font-weight: bold; margin-top: 1.5em; margin-bottom: 0.5em; color: #111; }
    h1 { font-size: 2.2em; } h2 { font-size: 1.8em; } h3 { font-size: 1.5em; }
    pre, code { font-family: "SFMono-Regular", Consolas, "Liberation Mono", Menlo, Courier, monospace; background-color: #f6f8fa; border: 1px solid #dfe2e5; border-radius: 6px; font-size: 0.9em; }
    pre { padding: 16px; overflow-x: auto; line-height: 1.45; } code { padding: .2em .4em; margin: 0; }
    table { border-collapse: collapse; width: 100%; margin-bottom: 1em; border-spacing: 0; }
    th, td { border: 1px solid #dfe2e5; padding: 8px 12px; text-align: left; } th { background-color: #f6f8fa; font-weight: bold; }
    img { max-width: 100%; height: auto; display: block; margin-left: auto; margin-right: auto; border-radius: 4px; }
    blockquote { border-left: .25em solid #dfe2e5; padding: 0 1em; color: #586069; margin-left: 0; margin-right: 0; }
    ul, ol { margin-bottom: 1em; padding-left: 2em; }
    .toc { border: 1px solid #dfe2e5; padding: 1em 1.5em; margin-bottom: 2em; background-color: #f6f8fa; border-radius: 6px; }
    .toc ul { list-style-type: none; padding-left: 0; } .toc > ul { padding-left: 0; } .toc ul ul { padding-left: 1.5em; }
    .toc li { margin-bottom: 0.6em; } .toc a { text-decoration: none; color: #0366d6; } .toc a:hover { text-decoration: underline; }
    figure { margin: 1.5em auto; page-break-inside: avoid; text-align: center; }
    figure img { display: inline-block; margin-bottom: 0.5em; }
    figcaption { font-size: 0.9em; font-style: italic; color: #555; text-align: center; margin-top: 0.3em; padding: 0 1em;}
    """
    stylesheets = [CSS(string=base_css_string)]
    if custom_css_path:
        try:
            stylesheets.append(CSS(filename=custom_css_path))
            print(f"  [WeasyPrint] 已加载自定义 CSS: {custom_css_path}")
        except Exception as e:
            print(f"  [WeasyPrint] 加载自定义 CSS '{custom_css_path}' 失败: {e}")

    final_html = f"""
    <!DOCTYPE html><html lang="zh-CN"><head><meta charset="UTF-8"><title>合并文档</title></head>
    <body>{full_html_content}</body></html>
    """
    try:
        # 设置 base_url 为 Markdown 文件所在的目录 (例如 "finished_md")
        # 这使得 HTML 中的相对路径 (如 <img src="media/image.png">)
        # 可以被正确解析为相对于 source_directory。
        # 使用 abspath 确保路径的明确性。
        abs_source_directory = os.path.abspath(source_directory)
        print(f"  [WeasyPrint] 使用 base_url: {abs_source_directory} 以解析本地图片")
        html_doc = HTML(string=final_html, base_url=abs_source_directory)
        html_doc.write_pdf(output_pdf_path, stylesheets=stylesheets)
        print(f"[WeasyPrint] PDF 文件已成功生成: {output_pdf_path}")
    except Exception as e:
        print(f"[WeasyPrint] 使用 WeasyPrint 生成 PDF 时发生错误: {e}")
        # ... (错误提示与之前相同)

if __name__ == "__main__":

    source_markdown_dir = "finished_md" # 源目录

    # 检查源目录是否存在
    if not os.path.isdir(source_markdown_dir):
        print(f"错误: 目录 '{source_markdown_dir}' 不存在。请创建该目录并将您的 Markdown 文件放入其中。")
        print(f"您的 Markdown 文件应按 '00.md', '01.md', ... 的顺序命名。")
        exit()

    # --- 使用 WeasyPrint ---
    print("\n--- 开始 WeasyPrint 示例 ---")
    output_filename_weasy = "merged_document.pdf"
    files_to_merge_weasy = sorted(glob.glob(os.path.join(source_markdown_dir, "*.md")))

    if not files_to_merge_weasy:
        print(f"在目录 '{source_markdown_dir}' 中没有找到 Markdown 文件。")
    else:
        print(f"将要使用 WeasyPrint 合并以下文件到 {output_filename_weasy}:")
        for f_path in files_to_merge_weasy:
            print(f" - {os.path.basename(f_path)}")

        custom_css_file_path = None # 可选: "my_styles.css"
        
        merge_markdown_to_pdf_weasyprint(
            files_to_merge_weasy, 
            output_filename_weasy,
            source_directory=source_markdown_dir, # 传递源目录
            custom_css_path=custom_css_file_path
        )

    print("\n--- 脚本执行完毕 ---")
    if os.path.exists(output_filename_weasy):
         print(f"如果成功，您应该能在当前目录下找到生成的 PDF 文件。")
    print(f"请确保您的 Markdown 文件位于 '{source_markdown_dir}' 目录中，")
    print(f"并且图片位于 '{os.path.join(source_markdown_dir, 'media')}' 子目录中。")

