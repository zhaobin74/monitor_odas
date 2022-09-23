#! /usr/bin/env python
import subprocess
from time import sleep
import json
import datetime
import os
import sys


user = os.environ['USER']



while True:

# Opening JSON file
   try:
      f = open('jobs.json', "r")
  
# returns JSON object as 
# a dictionary
      jobs = json.load(f)
  
  
# Closing file
      f.close()
   except OSError as e:
      print(f"{type(e)}: {e}") 
      sys.exit(1)

   cp = subprocess.run(["qstat", "-a",  "-u", user],  capture_output=True, text=True)

   if cp.returncode < 0:
      print("Error in getting job queue info") 
      sys.exit(1)
   #print(cp.stdout)
   time = datetime.datetime.now()

   display_time = time.strftime("%H:%M")
   print('at', time) 

   stopped = []
   for job in jobs['exps']:
       if job['name']+'_RUN' in cp.stdout: 
           print(job['name'], 'is running in', job['path'])
       else:
           print(job['name'], 'stopped')
           stopped.append(job) 
   for job in stopped:
       cp = subprocess.run(["sbatch", job['path']+"/gcm_run.j"])      
       if cp.returncode < 0:
           print(jobs['name']+' DID NOT  resubmit')
 
   sleep(60)  