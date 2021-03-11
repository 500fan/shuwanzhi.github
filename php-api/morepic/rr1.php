<?php
$arr1=file('rr1.txt');
$n=count($arr1)-1;
for ($i=1;$i<=1;$i++){
  $x=rand(0,$n);
  header("Location:".$arr1[$x],"\n");
}
?> 