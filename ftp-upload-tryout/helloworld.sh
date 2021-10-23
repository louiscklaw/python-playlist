#!/usr/bin/env bash

# sudo apt install -y github.ncftp

ncftpput -R -v \
  -u $PUREUDON_FTP_USERNAME \
  -p $PUREUDON_FTP_PASSWORD \
  $PUREUDON_FTP_HOST \
  $PUREUDON_HOMEPAGE_PATH \
  $PWD/public/*
