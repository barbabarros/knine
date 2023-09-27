<h1 class="code-line" data-line-start=1 data-line-end=2 ><a id="knine_1"></a>knine</h1>
<p class="has-line-data" data-line-start="2" data-line-end="3">Um simples programa para verificar se um intervalo de URLs contem arquivos pdf.</p>
<h1 class="code-line" data-line-start=4 data-line-end=5 ><a id="Uso_4"></a>Uso</h1>
<p class="has-line-data" data-line-start="6" data-line-end="9">url_base = &quot;<a href="https://example.com/">https://example.com/</a>&quot;   # URL destino com / no final. O nome do arquivo será a variável inicio + .pdf<br>
inicio = 1   # Início do intervalo contendo o nome do arquivo .pdf<br>
fim = 10   # Fim do intervalo contendo o nome do arquivo .pdf</p>
<p class="has-line-data" data-line-start="10" data-line-end="12">Neste exemplo, serão testadas todas URLs com 18 dígitos, iniciando em <a href="https://example.com/000000000000000001.pdf">https://example.com/000000000000000001.pdf</a> e terminando em <a href="https://example.com/000000000000000010.pdf">https://example.com/000000000000000010.pdf</a>.<br>
Para alterar a quantidade de digitos, verifique a linha 25.</p>
<p class="has-line-data" data-line-start="13" data-line-end="14">As URLs válidas serão salvas no arquivo especificado.</p>
