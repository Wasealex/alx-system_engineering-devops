#create ssh config file
#configuration must be configured to use the private key ~/.ssh/school
#configuration must be configured to refuse to authenticate using a password
file_line { 'Disable password authentication':
  ensure => 'present',
  path   => "etc/ssh/config",
  line   => '    PasswordAuthentication no',
}

file_line { 'Specify identity file':
  ensure => 'present',
  path   => "etc/ssh/config",
  line   => '    IdentityFile ~/.ssh/school',
}
