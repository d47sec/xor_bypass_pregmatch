<?php 
if(isset($_GET['view-source'])){
    highlight_file(__FILE__);
    die();
}
if(isset($_GET['warmup'])){
    if(!preg_match('/[A-Za-z]/is', $_GET['warmup']) && strlen($_GET['warmup']) <= 60){ # ko được có kí tự trong giá trị của tham số warmup và độ dài <= 60
        eval($_GET['warmup']);
    }else{
        die('Try harder');
    }
}else{
    die("No param given");
}
?>