<?php
$mode = isset($_GET['mode']) && $_GET['mode'] == 'r' ? 'r' : 'w';
$id = isset($_GET['id']) ? str_replace(array('<', '>', '|', "\\", '/', '_'), '', $_GET['id']) : 'default';
$data = isset($_GET['data']) ? $_GET['data'] : '';

$fh = fopen('store/'.$id.'.txt', $mode);
if ($mode == 'r') 
{
    print(fgets($fh));
} else {
    fputs($fh, $data);
    print("ok");
}
