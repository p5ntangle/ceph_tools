import json
import shlex
from subprocess import check_output
import datetime
from time import sleep



def call_app(cmd):
    """

    This is probably not the safest way to do this.
    """
    output = check_output(shlex.split(cmd))
    return output



def main():

    out = call_app("ceph pg dump_json pgs")
    data = json.loads(out)
    for each in data:
        print each

    work = dict()

    present = datetime.datetime.now()
    compare = present - datetime.timedelta(days=7)
    #2014-12-04 00:49:46.640582
    datetime.datetime.strptime('2014-12-04 00:49:46.640582' , '%Y-%m-%d %H:%M:%S.%f')

    for each in data['pg_stats']:
        test = datetime.datetime.strptime(each['last_deep_scrub_stamp'] , '%Y-%m-%d %H:%M:%S.%f')
        result = test < compare
        print each['pgid'], each['last_deep_scrub_stamp'], result
        cmd = "ceph pg deep-scrub "+ each['pgid']
        if result:
            print "Scrubbing %s with %s" % (each['pgid'], cmd)
            call_app(cmd)
            sleep(2.0) # need to add a check to see how many nodes are queued for a scrub
        else:
            print "Ignoring %s" % each['pgid']


if __name__== "__main__":
    main()

"""
u'pgid': u'6.6'
u'last_deep_scrub_stamp': u'2014-12-04 14:18:16.764316'


ceph pg stat
v7798141: 10432 pgs: 10431 active+clean, 1 active+clean+scrubbing+deep; 23011 GB data, 69058 GB used, 107 TB / 174 TB avail; 189 MB/s rd, 6709 kB/s wr, 3669 op/s

"""