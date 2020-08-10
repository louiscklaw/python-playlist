#!/usr/bin/env bash

set -ex

yarn
yarn add gh-pages \
  @fortawesome/fontawesome-svg-core \
  @fortawesome/free-brands-svg-icons \
  @fortawesome/free-solid-svg-icons \
  @fortawesome/react-fontawesome \
  axios \
  bulma \
  gatsby \
  gatsby-plugin-fontawesome-css \
  gatsby-plugin-google-fonts \
  gatsby-plugin-sass \
  node-sass \
  react-markdown \
  gh-pages
