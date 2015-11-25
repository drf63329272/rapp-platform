#!/bin/bash -i

##

#Copyright 2015 RAPP

#Licensed under the Apache License, Version 2.0 (the "License");
#you may not use this file except in compliance with the License.
#You may obtain a copy of the License at

    #http://www.apache.org/licenses/LICENSE-2.0

#Unless required by applicable law or agreed to in writing, software
#distributed under the License is distributed on an "AS IS" BASIS,
#WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#See the License for the specific language governing permissions and
#limitations under the License.

# Authors: Manos Tsardoulias
# Contact: etsardou@iti.gr
##

##
#  Create and import RappStore database.
##

path=$(pwd)
dump="/RappPlatformMySqlDbSchema.sql"
pth=$path$dump
echo -e "\e[1m\e[103m\e[31m [RAPP] MySQL RAPP database import \e[0m"

#sudo touch /etc/db_credentials1
#sudo chmod ugo+rw /etc/db_credentials1
sudo sh -c 'printf "dummyUser\nchangeMe" > /etc/db_credentials1'
echo "Insert MySQL root Password"
echo "Create database RappStore" | mysql -u root -p
echo "Insert MySQL root Password"
mysql -u root -p RappStore < $pth

