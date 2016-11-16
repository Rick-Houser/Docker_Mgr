#!/usr/bin/env python

import sys
from subprocess import Popen

class WhaleWatcher:
    ''' A tool used to manage the execution of software in Docker containers '''
    def __init__(self):
        self.execution = sys.argv[1]
        self.command = sys.argv[2]

    def main(self):
        if len(sys.argv) > 2:
            exe = self.execution
            if exe == '-r':
                self.run()
            elif exe == 'stop' or exe == 'kill':
                self.stop()
            else:
                print "Unknown command. Available starting arguments: "'-c', 'stop' or 'kill'."
        else:
            print "Too few arguments. Please see the README for usage details."

    def run(self):
    ''' Runs a given command within a container '''
        print "Creating container '%s' to run '%s'." % (self.cont_name, self.command)

    def stop(self):
    ''' Stops a container '''
        print "You've chosen to '%s' container '%s'." % (self.execution, self.command)
        Popen('sudo docker ' + self.execution + ' ' + self.command, shell=True).wait()
        self.clean_up()

    def clean_up(self):
    ''' Remove exited containers '''
        print "Cleaning up unused containers."
        exited = "$(sudo docker ps -a -q)"
        Popen("sudo docker rm " + exited, shell=True).wait()

if __name__ == '__main__':
    watcher = WhaleWatcher()
    watcher.main()
