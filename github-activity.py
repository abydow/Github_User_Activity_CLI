#!/usr/bin/env python3

"""

github user activity cli TOOL
shows:Github user activity using built in python

"""

import sys
import json
from urllib.request import urlopen,Request
from urllib.error import HTTPError,URLError
from datetime import datetime

def print_usage():
    # Print usage instructions.
    print("Usage: python github-activity.py <github-username>")
    print("Example:")
    print("python github-activity.py abydow")
 

