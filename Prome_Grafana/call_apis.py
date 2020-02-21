'''
Generate REST API queries 
'''

import random
import urllib3
import time
import sys
import threading


def start_api_queries(delay):
   endpoints = ['random', 'version' ]
   while True:
      api_count = len(endpoints)
      api = random.choice(endpoints)
      url = "http://localhost:5000/" + api
      print("URL: {}".format(url))
      http = urllib3.PoolManager()
      r = http.request('GET', url)
      data = r.data.decode("utf-8", "strict")
      time.sleep(delay)


if __name__ == '__main__':
  count = 5
  if len(sys.argv) > 1:    # Just get the second arg
     count = int(sys.argv[1])
  if count < 1 or count > 20:
     count = 5
  print("Starting {} threads...".format(count))
  for i in range(count):
     name = "thr_"+str(i)
     #add different delay to each thread
     thr  = threading.Thread(name=name, target=start_api_queries, args=(i+5,))
     thr.start()

