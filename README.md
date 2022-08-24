# Linux Memory Use Utility

This is a small, simple utility for monitoring and freeing memory. It represents the top 20 memory-using processes as asteroids. Changing the testMode variable to False will cause the process represented by the asteroid to be ended when the asteroid is destroyed. With the testMode variable set to True, the utility does not end any processes.

The processes are ended with the killall command, and the asteroids themselves are de-duplicated. Hitting the Chrome asteroid will kill all running processes named "Chrome." 

Asteroids are also sized according to their memory use. This feature is still a work in progress.

This program can be dangerous. It is not meant for actual use in a production setting, obviously. It is just a dumb idea I had.
