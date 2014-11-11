=========
Changelog
=========

0.7
---

0.7.0
~~~~~

- the default editor is now vi
- dependencies upgrade
- changes for python 3 compatibility

0.6
---

0.6.1
~~~~~

- fix: tracknumber must be an number for the formater
- upgrade requirements_dev.txt (was broken)

0.6.0
~~~~~

- doc: reorganise and add more contents...
- use of "musicbrainzngs" and "python-discid" in remplacement of "musicbrainz2" (that is deprecated)
- feature: add a command 'disc_info' to display some information about the disc (id, sumission_url, ...).
- cleanup of the project tree

0.5
---

0.5.6
~~~~~

- fix: installation must include configuration files.

0.5.5
~~~~~

- fix: requirements.txt was missing from sdist

0.5.4
~~~~~

- fix: classifiers.

0.5.3
~~~~~

- convert documentation to restructuredText (README, AUTHORS, CHANGELOG, ...) 
- improve meta-data for pypi
- specified dependencies
- remove the python version from shebang

0.5.2
~~~~~

- add requirements.txt for pip.

0.5.1
~~~~~

- fix: update replace and remove list

0.5.0
~~~~~

- feature: add a way to control the order of transformations
- feature: multi-cd support
- feature: add the disc number tag in audio files
- improve messages by using warning or error keyword
- fix: only show the submission url when cd not in db
- profile: changes in replacement list
- feature: display the musicbrainz sumission url

0.4
---

0.4.1
~~~~~

- fix: missing dot for profile loading in the homedir
- fix: now suggest adding to musicbrainz when no entry

0.4.0
~~~~~

- doc: add usefull options section
- doc: change project name
- doc: append new encoding softwares used in external softwares
- feature: support multiple audio format (issue #6)
- fix: use a real function to close the file descriptor
- doc: quick update on basic usage
- fix: few minor fixes
- other: eclipse project files
- fix: do not override PYTHONPATH.
- feature: profile and config can now be selected from cmdline arguments
- feature: profiles (issue #7)

0.3
---

0.3.0
~~~~~

- feature: default values are now stored in the package and they can be override by user's config file (issue #2)
- git: add emacs files to ignore list
- feature: installer, reorganise source directory (issue #3)
- config: add cases of character replacements and deletions

0.2
---

0.2.2
~~~~~

- fix: the track length stored in the playlist is now defined by the value in the encoded file (issue #8)
- feature: add StripTransformer (issue #9)
- config: add few chars to the remplacement list

0.2.1
~~~~~

- doc: basic usage (issue #5)
- fix: set genre tag (issue #4)
- fix: handle no cdrom exception

0.2.0
~~~~~
 
- doc: change the signification of the name
- doc: add working OS
- feature: editor choice in the config file
- fix: remove full path for binary in the config file.
- fix: explicitly use python2 binary
- doc: add musicbrainz2 to requirement list
- doc: fix requirement lists
- doc: add requirement info
- doc: add requirement info
