#!/bin/sh

################################################################################
# Specify environment settings
################################################################################

# Set up proxy 
# echo "proxy=PROXY SERVER" >>/etc/yum.conf

################################################################################
# Fix /etc/hosts
################################################################################

sed 's/127\.0\.0\.1.*OracleLinuxML.*/192.168.56.125 OracleLinuxML/' -i /etc/hosts
sed '$ a 192.168.56.125 OracleLinuxML' -i /etc/hosts


################################################################################
# Post installation customization
################################################################################

#echo "Post OS installation customization"

################################################################################
# Installing bzip2 and the Anaconda2-5.2.0-Linux-x86_64.sh - taken from Anaconda
# The Most Popular Python Data Science Platform, this will give us Scikit-learn
# (formerly scikits.learn) is a free software machine learning library for the
#  Python programming language
################################################################################

yum -y install bzip2
mv /tmp/files /root/
chmod +x /root/files/Anaconda2-5.2.0-Linux-x86_64.sh
su -
/root/files/Anaconda2-5.2.0-Linux-x86_64.sh -b
echo "export PATH="/root/anaconda2/bin:$PATH"" >> /root/.bashrc

###############################################################################
# DISABLING FIREWALL
###############################################################################

systemctl disable firewalld
systemctl stop firewalld
 
