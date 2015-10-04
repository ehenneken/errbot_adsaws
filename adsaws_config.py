# encoding: utf-8
"""
Configuration file for the ADSAWS services
"""

AWS_REGION = 'us-east-1'
AWS_ACCESS_KEY = 'key'
AWS_SECRET_KEY = 'secret'

try:
    from local_config import *
except:
    pass