motioneye scripts
==========

Scripts I use along with
[motioneye](https://github.com/ccrisan/motioneye)

## etc_defaults/
File for `/etc/default/` that is used by the systemd unit file.  It
defines the Slack API token to be used with the Slack notification.

## systemd/
systemd unit file that references `/etc/default/motioneye`

## notifications/
Notfication scripts. These need to be somewhere on a path and
excutable by the user running morioneye.

### slack_alert.py
Uses the official Slack Python SDK to send a notifcation to the slack
channel (currently hardcoded) into the script.  The argument to the
script is the text of the notifcation.  For example:
```
slack_alert.py "Camera 1 motion detected"
```
Would send the message *Camera 1 motion detected* to the channel
"homeassistant" that is accesed via the API token in `/etc/defaults/motioneye`.

## See Also:
[motion/WeeWX integration](https://github.com/nelsonov/motion-weewx)


