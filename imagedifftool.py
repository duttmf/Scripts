#!/usr/bin/env python3

import argparse, os, sys, filetype

parser = argparse.ArgumentParser(description="Image comparison tool")
parser.add_argument("img", type=str, nargs='+', help="display filepath to image")

args = parser.parse_args()

for image in args.img:
  if not os.path.exists(image):
    print('%s Does not exist' % (image))
    sys.exit(1)
  else:
    my_file = filetype.guess(image)
    if not my_file == 'image/jpg':
      print('%s is not a jpeg' % (image))
      sys.exit(1)

