#!/usr/bin/env python3
"""Simple Markdown preview server."""

import argparse
import os
import subprocess
import sys
import tempfile
import webbrowser
from http.server import HTTPServer, SimpleHTTPRequestHandler


def pandoc_convert(md_path: str, html_path: str) -> bool:
    """Convert markdown to HTML via pandoc if available."""
    try:
        subprocess.run([
            "pandoc",
            md_path,
            "-s",
            "-o",
            html_path,
        ], check=True)
        return True
    except FileNotFoundError:
        return False
    except subprocess.CalledProcessError:
        print("Pandoc failed to convert the file", file=sys.stderr)
        return False


def builtin_convert(md_path: str, html_path: str) -> bool:
    """Fallback converter using python-markdown."""
    try:
        import markdown
    except ImportError:
        print("Missing 'markdown' package. Install with 'pip install markdown'.")
        return False

    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    html = markdown.markdown(text, output_format="html5")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description="Preview markdown as HTML")
    parser.add_argument("file", help="Markdown file to preview")
    parser.add_argument(
        "--port",
        type=int,
        default=8000,
        help="Port for HTTP server",
    )
    args = parser.parse_args()

    md = args.file
    if not os.path.exists(md):
        parser.error(f"{md} does not exist")

    with tempfile.TemporaryDirectory() as tmp:
        html = os.path.join(tmp, "index.html")
        if not pandoc_convert(md, html):
            print("Pandoc not found or failed. Falling back to python-markdown.")
            if not builtin_convert(md, html):
                return 1

        os.chdir(tmp)
        url = f"http://localhost:{args.port}/index.html"
        webbrowser.open(url)
        print(f"Serving preview at {url} (Ctrl+C to stop)")
        server = HTTPServer(("localhost", args.port), SimpleHTTPRequestHandler)
        try:
            server.serve_forever()
        except KeyboardInterrupt:
            pass
    return 0


if __name__ == "__main__":
    sys.exit(main())
