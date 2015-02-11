# ceph_tools
Ceph helper scripts - to make managing ceph tasks easier.

##deep_scrub.py 
This script will run a deep scrub on pgs that have not been deep scrubbed in the last 7 days, it should be set to run during non peak periods

  ###ToDo
  1. Set up functionality to change the period via cli/config file
  2. Add timing function so that it can be run as a daemon on its own (i.e. no cron)
  3. Add check capability to see how many scrubs are running and wait until they have completed (instead of arbitrary wait)
  4. Make code pretty and safe
