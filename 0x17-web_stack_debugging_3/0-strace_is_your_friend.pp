#strace can attach to a current running process
exec { ' fix it ':
  command => "sed -i 's/phpp/php/' /var/www/html/wp-settings.php",
}
