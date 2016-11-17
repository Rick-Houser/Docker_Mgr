#!/usr/bin/env python

import os
import sys
import time
from subprocess import Popen

class WhaleWatcher:
    ''' A tool used to manage the execution of software in Docker containers '''
    def __init__(self):
        self.execution = sys.argv[1]
        self.command = sys.argv[2]
        self.time_stamp = time.strftime("%Y%m%d-%H%M%S")
        self.cont_name = self.command.split(' ')[0] + '_' + self.time_stamp
        self.stdout = self.cont_name + '_out.log'
        self.stderr = self.cont_name + '_err.log'

    def main(self):
        try:
            os.mkdir("logs/")
        except:
            pass

        if len(sys.argv) > 2:
            exe = self.execution
            if exe == '-r':
                self.run()
            elif exe == '-b':
                self.bash_mode()
            elif exe == 'stop' or exe == 'kill':
                self.stop()
            else:
                print "Unknown command. Available starting arguments: '-b', "\
                      "'-c', 'stop' or 'kill'."
        else:
            print "Too few arguments. Please see the README for usage details."

    def run(self):
        ''' Runs a given command within a container '''
        print "Creating container '%s' to run '%s'." % (self.cont_name, self.command)
        Popen('sudo docker run -t -d --name ' + self.cont_name + ' ubuntu /bin/' \
            + self.command + ' && sudo docker logs ' + self.cont_name + ' > logs/'\
            + self.stdout + ' 2> logs/' + self.stderr, shell=True).wait()
        self.clean_up()

    def bash_mode(self):
        """ Allows full control over bash. """
        print "You've chosen bash mode. You have complete control over bash. "\
              "Use caution when using this method. Collecting logs with this "\
              "method is not done for you."
        Popen(self.command, shell=True).wait()

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
