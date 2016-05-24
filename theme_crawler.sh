#!/bin/bash
#
# in content/
# Start python -m SimpleHTTPServer
#
# Run this script in the local directory, reload firefox
# Make a note of the themes you like

CMD=pelican
OPTIONS="content --ignore-cache --theme-path"

for THEME_DIR in ../pelican-themes/*; do
    [ -d "${THEME_DIR}" ] || continue # if not a directory, skip
    dirname="$(basename "${THEME_DIR}")"
    echo "$dirname"

    $CMD $OPTIONS $THEME_DIR
    read 

done
