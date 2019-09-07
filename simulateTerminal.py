#!/bin/python

import time

commands = {'test':'This is a test', 'check':'This is a check'}

while True:
        gmtime = time.gmtime()
        prompt = str(gmtime.tm_year) + str(gmtime.tm_mon) + str(gmtime.tm_mday)
        inp = input(prompt+'>')

        if inp == 'exit':
                exit(0)
        else:
                if inp.strip() in commands.keys():
                        print(commands[inp])
                else:
                        print('Command not found')
