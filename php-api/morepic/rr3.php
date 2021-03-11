<?php
$arr3=file('rr3.txt');
$n=count($arr3)-1;
for ($i=1;$i<=1;$i++){
  $x=rand(0,$n);
  header("Location:".$arr3[$x],"\n");
}
?> 