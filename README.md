# Jogo da Forca - Projeto de OO

## Definição do Problema

O "Jogo da Forca" é um jogo de adivinhação de palavras onde o jogador tenta adivinhar uma palavra oculta, sugerindo letras uma por uma. Se a letra sugerida estiver presente na palavra, todas as ocorrências dela são reveladas. Caso contrário, uma parte do desenho de um enforcado é adicionada. O jogador vence se conseguir revelar toda a palavra antes que o desenho do enforcado seja completado.

Este projeto implementa o jogo da forca em terminal, seguindo os princípios da Programação Orientada a Objetos, incluindo encapsulamento, herança, polimorfismo, mixins, composição e associação.

## Casos de Uso

### Caso de Uso 1: Iniciar um Novo Jogo
1. O jogador inicia o aplicativo.
2. O sistema apresenta as instruções do jogo e um menu inicial.
3. O jogador seleciona a opção "Novo Jogo".
4. O sistema seleciona aleatoriamente uma palavra do banco de palavras.
5. O sistema exibe a quantidade de letras da palavra usando underscores.
6. O jogo começa com o jogador podendo fazer sua primeira tentativa.

### Caso de Uso 2: Tentar uma Letra
1. O sistema solicita que o jogador digite uma letra.
2. O jogador digita uma letra.
3. O sistema verifica se a letra já foi tentada anteriormente:
   - Se sim, avisa o jogador e solicita outra letra.
   - Se não, adiciona a letra à lista de letras tentadas.
4. O sistema verifica se a letra está presente na palavra:
   - Se sim, revela todas as ocorrências da letra na palavra.
   - Se não, adiciona uma parte ao desenho do enforcado e diminui o número de tentativas restantes.
5. O sistema verifica se o jogo terminou:
   - Se todas as letras foram reveladas, o jogador vence.
   - Se o desenho do enforcado foi completado, o jogador perde.
   - Caso contrário, o jogo continua.

### Caso de Uso 3: Visualizar Histórico de Jogos
1. O jogador seleciona a opção "Histórico" no menu.
2. O sistema carrega os dados de jogos anteriores do arquivo de histórico.
3. O sistema exibe informações como data/hora, palavra, resultado (vitória/derrota) e tentativas usadas.
4. O jogador pode retornar ao menu principal após visualizar o histórico.

### Caso de Uso 4: Reiniciar o Jogo Após Terminar
1. Quando o jogo termina (vitória ou derrota), o sistema exibe o resultado.
2. O sistema pergunta se o jogador deseja jogar novamente.
3. Se o jogador escolher "sim", o sistema inicia um novo jogo com uma nova palavra.
4. Se o jogador escolher "não", o sistema retorna ao menu principal.

## Diagrama de Classes

```
+-------------------+      +-------------------+
|       Jogo        |      |      Palavra      |
+-------------------+      +-------------------+
| - jogador         |----->| - texto           |
| - palavra         |      | - letras_reveladas|
| - tentativas_max  |      +-------------------+
+-------------------+      | + revelar_letra() |
| + iniciar()       |      | + esta_completa() |
| + jogar_rodada()  |      +-------------------+
+-------------------+
        |
        |
        v
+-------------------+      +-------------------+
|      Jogador      |      |     DisplayMixin  |
+-------------------+      +-------------------+
| # nome            |      | + mostrar_forca() |
| # tentativas      |      | + limpar_tela()   |
+-------------------+      +-------------------+
| + tentar_letra()  |              ^
| + reset()         |              |
+-------------------+              |
        ^                          |
        |                          |
        |                          |
+-------------------+      +-------------------+
|  JogadorHumano    |----->|    BancoDados    |
+-------------------+      +-------------------+
| + escolher_letra()|      | + carregar_palavras() |
| + jogar()         |      | + salvar_historico()  |
+-------------------+      +-------------------+
```
