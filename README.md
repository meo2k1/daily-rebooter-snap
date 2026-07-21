  [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Daily Rebooter

This is a fork of the
[midnight-rebooter](https://github.com/mauringo/midenight-rebooter-snap)
but the reboot time is configureable.

Installable through snapd:

[![Get it from the Snap Store](https://snapcraft.io/static/images/badges/en/snap-store-black.svg)](https://snapcraft.io/daily-rebooter)

command:
*sudo snap install daily-rebooter

## Step 0 - System setup - if needed
To bulid this snap snapcrft and multipass are needed.

just run:

*- sudo snap install snapcraft*

and then

*- sudo snap install muiltipass*

## Step 1 - Snap Build

Clone the repository, enter inside the folder. then run 'snapcraft'.

## Step3 - Configure your reboot time

*- snap set daily-rebooter time=11:22

You can also set is as off:

*- snap set daily-rebooter time=off
