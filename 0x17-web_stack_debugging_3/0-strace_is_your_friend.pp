#to fix apache2 php setting
exec { ' fix it ':
  command => "usr/bin/sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
