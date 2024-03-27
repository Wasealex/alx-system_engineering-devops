#autoamtically install nginx

package { 'nginx':
  provider => 'apt',
}

file {'/var/www/html/index.html':
  content => 'Hello World',
}

file_line {'redirect':
  ensure => 'present',
  path   => '/etc/nginx/sites-enabled/default',
  after  => 'listen 80 deault_server;',
  line   => 'rewrite ^/redirect_me https://www.trashloop.com permanent;',
}

exec {'start_server':
  command => '/usr/bin/sudo /usr/sbin/service nginx start',
}
