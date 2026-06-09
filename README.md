# Super Trunfo Animal

## Descrição do Projeto

O **Super Trunfo Animal** é um jogo desenvolvido em Python baseado no tradicional jogo de cartas Super Trunfo. Cada carta representa um animal com diferentes atributos, e os jogadores competem escolhendo características para comparar.

O projeto possui dois modos de jogo:

- 🎮 Single Player – Jogador contra o computador.
- 👥 Multiplayer – Dois jogadores no mesmo computador.

O objetivo é conquistar todas as cartas do adversário utilizando estratégia na escolha dos atributos.

---

## Tecnologias Utilizadas

- Python 3
- Biblioteca padrão:
  - random

---

## Estrutura do Projeto

```text
super_trunfo.py
```

---

## Cartas Disponíveis

| Animal | Ataque | Velocidade | Defesa |
|----------|----------|----------|----------|
| Urso | 200 | 150 | 100 |
| Tigre | 200 | 250 | 50 |
| Leão | 150 | 150 | 150 |
| Lobo | 150 | 200 | 50 |
| Crocodilo | 200 | 150 | 50 |
| Elefante | 100 | 50 | 250 |
| Jabuti | 100 | 150 | 250 |
| Gorila | 250 | 100 | 100 |

---

## Funcionamento do Jogo

### 1. Distribuição das Cartas

- O baralho é embaralhado.
- As cartas são divididas igualmente entre os participantes.
- É criado um monte de espera para armazenar cartas empatadas.

### 2. Escolha do Atributo

| Opção | Atributo |
|---------|---------|
| 1 | Ataque |
| 2 | Velocidade |
| 3 | Defesa |

### 3. Resultado da Rodada

#### Vitória

- Mantém sua carta.
- Recebe a carta do adversário.
- Recebe as cartas acumuladas no monte de espera.

#### Empate

- As cartas são enviadas para o monte de espera.
- O vencedor da próxima rodada recebe todas elas.

### 4. Fim de Jogo

A partida termina quando um dos jogadores ficar sem cartas.

---

## Funções Implementadas

### configurar_jogo()

Responsável por:

- Embaralhar o baralho.
- Distribuir as cartas.
- Criar o monte de espera.

### exibir_carta(carta)

Exibe as informações da carta atual.

### jogar_single_player()

Executa uma partida contra o computador.

### jogar_multiplayer()

Executa uma partida entre dois jogadores.

### menu()

Exibe o menu principal do jogo.

---

## Como Executar

### Pré-requisitos

- Python instalado.

### Execução

```bash
python super_trunfo.py
```

---

## Exemplo de Execução

```text
======= SUPER TRUNFO =======
1 - Single Player
2 - Multiplayer
3 - Sair

Escolha uma opção: 1
```

---

## Autor

Eric Pfeuti, projeto desenvolvido para fins acadêmicos.

**Disciplina:** Algoritmos e Programação  
**Linguagem:** Python  
**Tipo de Projeto:** Jogo de Cartas – Super Trunfo Animal.
