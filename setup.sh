#!/bin/bash

# Update apt-get
apt-get update

# Install MySQL client
apt-get install -y default-mysql-client libmysqlclient-dev

# Install mysqlclient Python library
pip install mysqlclient

# Add entry to /etc/hosts
echo "172.20.0.2   mysql-db1" >> /etc/hosts

echo "Setup completed!"
