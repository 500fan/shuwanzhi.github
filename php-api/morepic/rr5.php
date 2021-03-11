<?php
$arr5=file('rr5.txt');
$n=count($arr5)-1;
for ($i=1;$i<=1;$i++){
  $x=rand(0,$n);
  header("Location:".$arr5[$x],"\n");
}
?> 