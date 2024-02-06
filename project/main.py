import argparse
import logging
from app import create_app

def parse_command_line_arguments():
    parser = argparse.ArgumentParser(description='Launch Flask application.')
    parser.add_argument('--debug', action='store_true', help='Enable debug mode.')
    parser.add_argument('--host', type=str, default='127.0.0.1', help='Host to run the application on.')
    parser.add_argument('--port', type=int, default=5000, help='Port to run the application on.')
    return parser.parse_args()

def configure_logging():
    logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def main():
    args = parse_command_line_arguments()
    configure_logging()
    
    app = create_app()
    
    logging.info('Starting application...')
    app.run(debug=args.debug, host=args.host, port=args.port)

if __name__ == '__main__':
    main()
