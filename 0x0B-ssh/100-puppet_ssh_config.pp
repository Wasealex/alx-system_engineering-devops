#create ssh config file
#configuration must be configured to use the private key ~/.ssh/school
#configuration must be configured to refuse to authenticate using a password
file {'/etc/ssh/ssh_config':
  ensure  => present,
  content => "Host *
                   IndentifyFile ~/.ssh/school
                   PasswordAuthentication no",
}
