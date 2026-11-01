import argparse
import json
import logging
from pathlib import Path
from .pipeline import run

def main():
    p=argparse.ArgumentParser(description='Run research/news radar once and archive notes')
    p.add_argument('--root',type=Path,default=Path(__file__).resolve().parents[1])
    p.add_argument('--dry-run',action='store_true',help='Do not send Telegram notification')
    args=p.parse_args()
    logging.basicConfig(level=logging.INFO,format='%(levelname)s: %(message)s')
    print(json.dumps(run(args.root,send_notifications=not args.dry_run),indent=2))

if __name__=='__main__':main()
