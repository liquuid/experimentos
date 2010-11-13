<?php
include"conexao.php";
$ip = $_SERVER['REMOTE_ADDR'];
$sql = mysql_query("SELECT * FROM pergunta");
while ($linha = mysql_fetch_array($sql)){
$pergunta = $linha['pergunta'];
}
?>
<?php echo $pergunta ?>
<form name="form1" method="get" action="processa.php">
<?php 
$sql = mysql_query("SELECT * FROM resposta");
while($linha = mysql_fetch_array($sql)){
$id_resposta = $linha['id_resposta'];
$resposta = $linha['resposta'];
?>
   <p><input type="radio" name="rd_resposta" value="<?php echo $id_resposta ?>">
  <?php echo $resposta ?> </p> 
  <?php
}
?>
  <p> <font face="Verdana, Arial, Helvetica, sans-serif"><strong></p> 
  <p>Digite seu coment&aacute;rio : ( Por que ele &eacute; o seu preferido ? P.S. 
    <font color="#FF0000" face="Arial, Helvetica, sans-serif"> <strong>N&atilde;o 
    fale merda ... seu ip &eacute; : <?php echo $ip ?> , e sera visualizado mesmo 
    que oculte o seu nome ... Se fizer merda os LB's e seus f&atilde;s will kick 
    your fat ass </strong></font><font color="#FF0000">!!!!</font> <font color="#FF0000"><strong>( 
    <font face="Arial, Helvetica, sans-serif">E vc ainda esta lidando com programador 
    =]</font> )</strong></font></p>
  </p>
  <table width="75%" border="1" cellspacing="3" cellpadding="3">
    <tr> 
      <td width="17%"><font face="Verdana, Arial, Helvetica, sans-serif"><strong>Nome 
        : </strong></font></td>
      <td width="83%"><input name="nome" type="text" id="nome" size="50"></td>
    </tr>
    <tr> 
      <td><font face="Verdana, Arial, Helvetica, sans-serif"><strong>Coment&aacute;rio:</strong></font></td>
      <td><p>
          <textarea name="comentario" id="comentario"></textarea>
        </p>
        <p>Voc&ecirc; esta a afirmando ou perguntando ? 
          <select name="lista" id="lista">
            <option value="asking">Perguntando</option>
            <option value="said">Afirmando</option>
          </select>
        </p></td>
    </tr>
    <tr> 
      <td><input type="hidden" name="ip" value="<?php echo $ip ?>"></td>
      <td><input type="submit" name="Submit" value="votar"></td>
    </tr>
  </table>
  <p>&nbsp;</p>
  </form>

<table width="46%" border="1" align="left" cellpadding="3" cellspacing="3">
  <tr> 
    <td><font face="Verdana, Arial, Helvetica, sans-serif"><strong>Resposta</strong></font></td>
    <td><font face="Verdana, Arial, Helvetica, sans-serif"><strong>Votos : </strong></font></td>
  </tr>
  <tr> 
    <?php 
$sql = mysql_query("SELECT * FROM resposta");
while($linha = mysql_fetch_array($sql)){
$resposta = $linha['resposta'];
$votos = $linha['votos'];
?>
    <td><?php echo $resposta ?></td>
    <td><?php echo $votos ?></td>
  </tr>
  <?php
}
?>
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p>&nbsp;</p>
<p><strong><font face="Verdana, Arial, Helvetica, sans-serif">Coment&aacute;rios 
  : </font></strong></p>
<table width="75%" border="1" cellspacing="3" cellpadding="3">
  <tr>
<?php 
$sql = mysql_query("SELECT * FROM comentarios");
while($linha = mysql_fetch_array($sql)){
$nome = $linha['nome'];
$ip = $linha['ip'];
$comentario = $linha['comentario'];
?>  
    <td><?php echo $nome ?> (ip number: <?php echo $ip ?>) said : <?php echo $comentario ?></td>
  </tr>
<?php
}
?>  
</table>
<p>&nbsp;</p>
<p>&nbsp;</p>
