<?php
$arr2=file('rr2.txt');
$n=count($arr2)-1;
for ($i=1;$i<=1;$i++){
  $x=rand(0,$n);
  header("Location:".$arr2[$x],"\n");
}
?> 