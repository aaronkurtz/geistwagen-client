GEISTWAGEN

Stone Soup Dungeon Crawl bones sharing

Do you enjoy playing locally but get sick of killing your own
ghosts? Geistwagen fixes that. Upload your own ghosts, download
random people's ghosts and fight other people's failures for a change.

Inspired by Nethack's Hearse.

 ---

HOW? 

Short answer:
Run geistwagen, which starts Dungeon Crawl for you. 

Quit and restart after you die. That's it.
#TODO Upload bones files after death with magic. Lua magic?

Long answer:
Geistwagen looks for a geist.lck file when it starts. If it
doesn't find one, it uploads every bones file you have.

If it does find one, it find any bones files newer than the
lock file. When it finds some, they're uploaded and then
deleted, and a bones file is downloaded from the server.
