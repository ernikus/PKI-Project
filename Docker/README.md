# Troubleshoots

## Index.html Problems

Change Permissions to index.html

    sudo chmod 744 ./index.html

## Problems between Nginx and Files
Move them manually to Nginx Folder

    /etc/nginx/-sth-

Create new folder and name it properly if needed. Such as:

    mkdir -p /etc/nginx/certs
    mkdir -p /etc/nginx/html