#!/bin/bash
echo "Commit & Push To GIT"
echo "========================"

USERNAME=""
PASSWORD=""
MESSAGE=""

#read -p "message :" msg





echo $hy
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

if [ "$USERNAME" = "" ]
then
    read -p "USERNAME :" USERNAME
fi

if [ "$PASSWORD" = "" ]
then
    read -s -p "PASSWORD :" PASSWORD
    printf '\n'
fi

if [ "$MESSAGE" = "" ]
then
    read -p "MESSAGE :" MESSAGE
fi

# $msg = {$MESSAGE}

echo "Commiting to git.."
sudo git add -A
sudo git commit -m "${MESSAGE}"
echo "Push.."
sudo git push https://${USERNAME}:${PASSWORD}@github.com/t1g0r/ramey.git --all
echo "Done."
