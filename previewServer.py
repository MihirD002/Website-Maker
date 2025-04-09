import http.server
import socketserver
import webbrowser
import os
import threading


def serve_html(html_file_path, port=8000):
    """
    Serve the generated HTML file on a local web server.
    """
    # Get the directory containing the HTML file
    file_dir = os.path.dirname(os.path.abspath(html_file_path))
    if file_dir == '':
        file_dir = os.getcwd()

    # Change to the directory containing the HTML file
    os.chdir(file_dir)

    # Get the file name from the path
    file_name = os.path.basename(html_file_path)

    # Set up the HTTP server
    Handler = http.server.SimpleHTTPRequestHandler

    try:
        with socketserver.TCPServer(("", port), Handler) as httpd:
            print(f"Server started at http://localhost:{port}")
            print(f"Preview your HTML at: http://localhost:{port}/{file_name}")
            print("Press Ctrl+C to stop the server")

            # Keep the server running
            httpd.serve_forever()
    except KeyboardInterrupt:
        print("Server stopped.")
    except OSError as e:
        if e.errno == 98:  # Address already in use
            print(f"Port {port} is already in use. Try a different port.")
        else:
            print(f"Error: {e}")
