# puppet file to automate a 500 eror fix
exec {'fixed-phpp':
  command => "sed -i 's/phpp/php/g' /var/www/html/wp-settings.php",
  path  => '/bin';
}
