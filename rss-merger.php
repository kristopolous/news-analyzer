#!/usr/bin/php
<?php

$fileList = glob('feeds/1*/the_guardian.xml');
$fileMap = [];
$ttl = 0;
foreach($fileList as $file) {
  $path = basename($file);
  $xml = simplexml_load_string(file_get_contents($file), "SimpleXMLElement", LIBXML_NOCDATA);
  $json = json_encode($xml);
  $array = json_decode($json,TRUE);
  foreach($array['channel']['item'] as $obj) {
    $ttl ++;
    $guid = $obj['guid'];
    if(!isset($fileMap[$guid])) {
      $fileMap[$guid] = $obj;
    } else {
      $test = md5(json_encode($obj));
      $reference = md5(json_encode($fileMap[$guid]));
      if($test != $reference) {
        
        $jsold = json_encode($obj, JSON_PRETTY_PRINT);
        $jsnew = json_encode($fileMap[$guid], JSON_PRETTY_PRINT);
        echo $jsold;
        $old_ = explode("\n", json_encode($obj, JSON_PRETTY_PRINT));
        $new_ = explode("\n", json_encode($fileMap[$guid], JSON_PRETTY_PRINT));
        $old = array_filter($old_, function($row) { return strpos($row, 'url') > 0; });
        $new = array_filter($new_, function($row) { return strpos($row, 'url') > 0; });
        $old = array_values($old);
        $new = array_values($new);
        if(sizeof($new) > 0 && sizeof($old) > 0) {
          $ix = 0;
          for($ix = 0; $ix < count($new); $ix++) {
            if(trim($old[$ix]) !== trim($new[$ix]) && strpos($new[$ix], 'jpg') !== false &&  strpos($new[$ix],'description') === false) {
              echo $obj['title'] . "\n";
              echo stripslashes($old[$ix]) ."\n";
              echo stripslashes($new[$ix]) ."\n";
            }
          }
          $fileMap[$guid] = $obj;
        }

      } 
    }
  }
}

echo $ttl . " " . count(array_keys($fileMap));
