<?php
$arr4=file('rr4.txt');
$n=count($arr4)-1;
for ($i=1;$i<=1;$i++){
  $x=rand(0,$n);
  header("Location:".$arr4[$x],"\n");
}
?> 