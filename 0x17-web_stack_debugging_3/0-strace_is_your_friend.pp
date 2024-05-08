#to fix apache2 php setting
exec { ' fix it ':
  command => 'sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
  path    => ['/usr/bin', '/bin'],
}
