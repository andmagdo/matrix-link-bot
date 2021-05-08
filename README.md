# matrix-link-bot
This bot uses links posted in a matrix chat, checks them against a list of file extentions, and uploads if the extention is recognised

## Please note **VERY** beta to the point of unusability

Once done, however, it should be using [matrix-nio](https://github.com/poljar/matrix-nio), and have support for encrypted rooms

## To the real readme (a stub at this point TBH

You **MUST** do `sudo apt install libolm-dev` for encrypted room support 

As I believe this is for chats that are encrypted (either by choice or because it is default on many matrix clients),
Requirements.txt by default installs the encryption-enabled Matrix API
