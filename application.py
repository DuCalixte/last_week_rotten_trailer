from app import app

import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument(
    '-c', '--clean', help='Use this to clean up the database.',
    action="store_true")
parser.add_argument(
    '--scrape-clean', help='Use this to reset database and start ' +
    ' a new scrape.', action="store_true")
parser.add_argument(
    '--scrape-only', help='Use this to update database with new ' +
    'information from scrape', action="store_true")
parser.add_argument(
    '-p', '--port', help='Provide a port to launch the app.', type=int,
    default=8000)

args = parser.parse_args()

if args.scrape_clean:
    from app import database_cleanup
elif args.scrape_only:
    from app import database_reset

if args.scrape_only is not True and args.scrape_clean is not True and\
        args.clean is not True:
    if __name__ == '__main__':
        app.run(host='0.0.0.0', port=args.port)
        app.run(debug=True)
