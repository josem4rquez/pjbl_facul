# PJBL — PucFit

Sistema de **acompanhamento de saúde e bem-estar** executado no terminal, desenvolvido em **Python** como projeto PJBL (*Project Based Learning*) do curso de Sistemas de Informação da PUCPR.

O objetivo do trabalho foi aplicar lógica de programação em um programa interativo completo: entrada validada, menu com estado, cálculos derivados dos dados do usuário e um resumo que consolida tudo ao final.

## ✨ Funcionalidades

O programa começa pedindo **peso** e **altura** — recusando valores inválidos até receber um número maior que zero — e então oferece um menu com cinco opções:

| Opção | O que faz | Como calcula |
| :--- | :--- | :--- |
| **1** | Cálculo de IMC | `peso / altura²`, com classificação em abaixo do peso, normal, sobrepeso ou obesidade |
| **2** | Meta de hidratação diária | `peso × 0,035` litros |
| **3** | Gasto calórico por atividade | `MET × peso × horas`, com MET de caminhada (3,5), corrida (8,0), musculação (6,0) e ciclismo (7,5) |
| **4** | Meta diária de exercícios | Faixa de minutos conforme o objetivo: emagrecer, manter peso ou ganhar massa |
| **5** | Resumo diário | Consolida IMC, calorias gastas, meta de exercícios e hidratação |

> **MET** (*Metabolic Equivalent of Task*) é a unidade que quantifica o gasto energético de uma atividade física — é o que permite estimar calorias a partir do peso e da duração do exercício.

## 📁 Os dois arquivos

O repositório contém duas implementações da mesma proposta, resultado da evolução do trabalho:

| Arquivo | Abordagem |
| :--- | :--- |
| `main.py` | Menu dentro de laços aninhados. Após cada operação, pergunta se o usuário quer voltar ao menu. |
| `pucfit1.py` | Validação de entrada isolada antes do menu e **controle de estado por flags** (`imc_calculado`, `hidratacao_calculada`, `calorias_calculadas`, `meta_definida`), permitindo que o resumo informe com precisão o que ainda não foi calculado. |

## ▶️ Como executar

Requer apenas **Python 3** — nenhuma dependência externa.

```bash
git clone https://github.com/josem4rquez/pjbl_facul.git
cd pjbl_facul
python pucfit1.py
```

Ou, para a outra versão:

```bash
python main.py
```

O programa é interativo: informe peso e altura e navegue pelo menu digitando o número da opção.

## 🛠️ Tecnologias

**Python 3** · biblioteca padrão apenas · interface via terminal

## 👥 Autores

Projeto acadêmico desenvolvido em grupo:

- **José Marques** — [@josem4rquez](https://github.com/josem4rquez)
- **Eduardo Lopes** — [@EduardoLopessz](https://github.com/EduardoLopessz)

## 🎓 Contexto

Trabalho de PJBL — Sistemas de Informação, PUCPR.
