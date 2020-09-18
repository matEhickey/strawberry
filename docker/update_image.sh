#!/bin/sh

cd basic
docker build . -t matehickey/strawberry-graphql
docker push matehickey/strawberry-graphql
