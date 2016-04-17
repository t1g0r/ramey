#!/bin/bash

while [[ $# > 1 ]]
do
key="$1"

case $key in
    -u|--username)
    USERNAME="$2"
    ;;
    -p|--password)
    PASSWORD="$2"
    ;;
    -m|--message)
    MESSAGE="$2"
    ;;
    *)
            # unknown option
    ;;
esac
shift # past argument or value
done

# echo "${USERNAME}"
# echo "${PASSWORD}"
# echo "${MESSAGE}"

sudo git add -A
sudo git commit -m "${MESSAGE}"
sudo git push https://${USERNAME}:${PASSWORD}@github.com/t1g0r/ramey.git --all
