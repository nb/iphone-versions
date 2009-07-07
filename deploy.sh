#!/bin/sh
rsync -av --delete -e 'ssh' --exclude '.svn' --exclude '*.pyc' --exclude '.git' . nikolay.bg:public_html/iphone
