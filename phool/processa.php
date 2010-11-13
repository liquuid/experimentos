<?php 
include"conexao.php";
$nome = $_GET['nome'];
$ip = $_GET['ip'];
$comentario = $_GET['comentario'];
$sql = mysql_query ("INSERT INTO comentarios (nome, ip, comentario) VALUES ('$nome', '$ip', '$comentario') ");

$sql = mysql_query("SELECT * FROM resposta");
while($linha = mysql_fetch_array($sql)){
$votos = $linha['votos'];
}
$id_resposta = $_GET['rd_resposta'];
$sql = mysql_query("UPDATE resposta SET votos = votos + 1 WHERE id_resposta = '$id_resposta' ");
header('Location: index.php');
?>
