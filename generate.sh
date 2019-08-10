sudo dpkg-query -f '${binary:Package}\n' -W > packages_list.txt
sudo xargs -a packages_list.txt apt install
