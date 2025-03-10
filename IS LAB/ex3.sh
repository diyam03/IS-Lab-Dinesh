
#!/bin/bash

echo "### Currently logged-in user ###"
whoami
echo ""

echo "### Logged-in users ###"
who
echo ""

echo "### Home Directory ###"
echo $HOME
echo ""

echo "### Creating user 'sanjana' ###"
sudo adduser sanjana
echo ""

echo "### User Details ###"
cat /etc/passwd | grep sanjana
echo ""

echo "### Encrypted Passwords ###"
sudo cat /etc/shadow | grep sanjana
echo ""

echo "### Creating 'Third Year' group ###"
sudo groupadd "Third Year"
echo ""

echo "### Group Details ###"
cat /etc/group | grep "Third Year"
echo ""

echo "### Creating 'sam.sh' file ###"
touch sam.sh
ls -l sam.sh
echo ""

echo "### Listing Hidden Files ###"
ls -a
echo ""

echo "### Modifying Permissions for 'sample.txt' ###"
touch sample.txt
chmod o-r sample.txt
chmod g+x sample.txt
chmod o-r-w sample.txt
chmod o+r+w sample.txt
chmod 777 sample.txt
chmod 000 sample.txt
chmod 600 sample.txt
ls -l sample.txt
echo ""

echo "### Creating greet.sh ###"
cat > greet.sh <<EOF
#!/bin/bash
echo "What is your name?"
read user
echo "Hello \$user!!"
EOF
chmod +x greet.sh
echo ""

echo "### Creating math.sh ###"
cat > math.sh <<EOF
#!/bin/bash
echo "Enter 1st number:"
read a
echo "Enter 2nd number:"
read b
echo "Sum = \$((a+b))"
echo "Difference = \$((a-b))"
echo "Multiplication = \$((a*b))"
echo "Division = \$((a/b))"
EOF
chmod +x math.sh
echo ""

echo "### All tasks completed! ###"
