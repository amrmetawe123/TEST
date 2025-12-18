#!/usr/bin/env python3
print("\n")
php_date_default_timezone_set("europe/moscow")
ip_ = PHP_SERVER["REMOTE_ADDR"]
pd_ = PHP_SERVER["HTTP_USER_AGENT"]
dt_ = date("l dS \\of F Y H:i:s A")
port_ = PHP_SERVER["REMOTE_PORT"]
file_ = fopen("ip_log.txt", "a")
data_ = ip_ + " " + dt_ + " " + port_ + " " + pd_ + "\n"
fwrite(file_, data_)
php_fclose(file_)
php_header("Location:https://postimg.cc/MnDJP2xw")
