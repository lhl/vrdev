#!/bin/bash

# http://unix.stackexchange.com/questions/67983/get-monitor-make-and-model-and-other-info-in-human-readable-formhttp://unix.stackexchange.com/questions/67983/get-monitor-make-and-model-and-other-info-in-human-readable-form

edid=$(xrandr -q --verbose | 
         sed -n '/^[[:space:]]\+00ffffffffffff00/,/[^a-fA-F0-9[:space:]]/{
                                                  /[^a-fA-F0-9[:space:]]/d
                                                  s/[[:space:]]\+//g; p}')
nibble=({0..1}{0..1}{0..1}{0..1})
vend=$(for i in {16..19} ;do 
           printf "%s" ${nibble[$((16#${edid:$i:1}))]}
       done)
vend="$(for i in 1 6 11 ;do
            printf \\x$(printf %x $((2#${vend:$i:5} +64)))
        done)"
prod=$((16#${edid:22:2}${edid:20:2}))
printf "monitor: vendor \"%s\", prod id \"%s\"\n" "${vend}" "$prod"
