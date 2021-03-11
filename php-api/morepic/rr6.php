<?php
$arr6=file('rr6.txt');
$n=count($arr6)-1;
for ($i=1;$i<=1;$i++){
  $x=rand(0,$n);
  header("Location:".$arr6[$x],"\n");
}
?> 