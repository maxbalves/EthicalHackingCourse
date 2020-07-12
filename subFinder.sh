#!/bin/bash

url=$1

#Creates <url> folder if not present
if [ ! -d "$url" ];then
	mkdir $url
fi

#Creates /recon folder if not present
if [ ! -d "$url/recon" ];then
	mkdir $url/recon
fi

echo "[+] Harvesting subdomains with assetfinder..."
assetfinder $url >> $url/recon/assets.txt
cat $url/recon/assets.txt | grep $1 > $url/recon/final.txt  # Removes all assets not related to our URL
rm $url/recon/assets.txt

echo "[+] Harvesting subdomains with Amass..."
amass enum -d $url >> $url/recon/f.txt  # Finds all subdomains through Amass
sort -u $url/recon/f.txt >> $url/recon/final.txt  # Sorts it so that it only includes unique subdomains
rm $url/recon/f.txt  # Deletes the f.txt

echo "[+] Probing for alive domains..."
cat $url/recon/final.txt | sort -u | httprobe -s -p https:443 | sed 's/https\?:\/\///' | tr -d ':443' >> $url/recon/alive.txt
