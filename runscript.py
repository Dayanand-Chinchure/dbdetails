#Global Declaration
import os,shutil,time,tarfile
import logging, ConfigParser, inspect, traceback, sys
#---------------------------------------------------------------------


import subprocess
import sys
HOST="10.136.50.54"
COMMAND="ls"

def passwordless_ssh():
        ssh = subprocess.Popen(["ssh", "root@%s" % HOST, COMMAND],
                       shell=False,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE)
        result = ssh.stdout.readlines()

        if result == []:
                error = ssh.stderr.readlines()
                print >>sys.stderr, "ERROR: %s" % error
                return "error"
        else:
                print result

passwordless_ssh()

#Global Variables and values
FunArgsDict = {}
#--------------------------------------------------------------------

#Functions
def get_backup():
    print FunArgsDict ['DBNAME']
    print FunArgsDict ['POLICY']
    print FunArgsDict ['SCHEDULE']
    print FunArgsDict ['CLIENTNAME']

def backup_message(): print 'Backup in process'
def restore_message(): print 'Restore is in process'
#--------------------------------------------------------------------


if __name__ == '__main__':
    confsuccess= False
    try:
        config = ConfigParser.ConfigParser()
        config.read(sys.argv[1])
        FunArgsDict ['DBNAME'] = config.get('config','DBNAME')
        FunArgsDict ['POLICY'] = config.get('config','POLICY')
        FunArgsDict ['SCHEDULE'] = config.get('config','SCHEDULE')
        FunArgsDict ['CLIENTNAME'] = config.get('config','CLIENTNAME')
        FunArgsDict ['BACKUP_TYPE'] = config.get('config','BACKUP_TYPE')
        FunArgsDict ['TARGETDB'] = config.get('config','TARGETDB')
        FunArgsDict ['AUTOMATIC_STORAGE'] = config.get('config','AUTOMATIC_STORAGE')
        confsuccess=True
    except:
            s = traceback.format_exc()
            serr = "Error description:\n%s\n" %(s)
            print serr
            confsuccess = False

if confsuccess:
    get_backup()
