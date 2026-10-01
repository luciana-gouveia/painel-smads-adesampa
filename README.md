# Painel Territorial de Apoio à Gestão Socioassistencial — SMADS São Paulo

Aplicação web desenvolvida no âmbito da **Prova Técnica Prática do Edital de Seleção Pública nº 005/2026 — Assistente II - Dados e IA**, da ADE SAMPA.

## 1. Sobre o projeto

A Secretaria Municipal de Assistência e Desenvolvimento Social de São Paulo (SMADS) gerencia uma ampla rede de serviços socioassistenciais distribuídos pelo município.

Em um território extenso e marcado por diferentes níveis de vulnerabilidade social, a análise da distribuição dos equipamentos e do volume de atendimentos pode apoiar a identificação de regiões que merecem maior atenção da gestão pública.

O projeto propõe um **painel territorial interativo** para reunir informações de equipamentos socioassistenciais e facilitar a análise conjunta de:

- localização territorial;
- tipo de equipamento;
- região administrativa;
- volume mensal de atendimentos;
- indicador demonstrativo de vulnerabilidade territorial.

A proposta é transformar dados territoriais em uma visualização simples e acessível para apoiar análises preliminares da gestão socioassistencial.

---

## 2. Problema identificado

Informações sobre equipamentos públicos, características territoriais e indicadores sociais podem estar distribuídas em diferentes bases, formatos e fontes.

Essa fragmentação pode dificultar análises rápidas sobre a relação entre:

- localização dos serviços;
- volume de atendimento;
- diferenças territoriais;
- situações de maior vulnerabilidade social.

O problema abordado neste projeto é, portanto, a **dificuldade de visualizar de maneira integrada a distribuição territorial dos equipamentos socioassistenciais e indicadores relacionados ao atendimento e à vulnerabilidade**.

---

## 3. Área municipal relacionada

**Secretaria Municipal de Assistência e Desenvolvimento Social — SMADS**

Área relacionada:

- assistência social;
- proteção social;
- planejamento territorial;
- monitoramento da rede socioassistencial;
- apoio à gestão pública.

---

## 4. Público potencialmente beneficiado

O público principal da solução é composto por:

- gestores públicos municipais;
- equipes técnicas da assistência social;
- coordenadores e responsáveis pelo planejamento territorial;
- profissionais envolvidos no acompanhamento da rede socioassistencial.

O painel foi concebido principalmente como uma **ferramenta demonstrativa de apoio à análise e à gestão**, e não como substituto dos sistemas oficiais utilizados pela Prefeitura de São Paulo.

---

## 5. Solução desenvolvida

A solução consiste em uma aplicação web desenvolvida em **Python e Streamlit**, com recursos de visualização interativa.

O painel permite explorar territorialmente uma base demonstrativa de equipamentos socioassistenciais da cidade de São Paulo.

### Principais funcionalidades

- filtros por região da cidade;
- filtros por tipo de equipamento;
- mapa interativo de equipamentos;
- quantidade de equipamentos no recorte selecionado;
- média mensal de atendimentos;
- média do indicador de vulnerabilidade;
- gráfico de atendimentos por unidade;
- gráfico relacionando vulnerabilidade territorial e volume de atendimentos;
- sinalização automatizada baseada em regra heurística;
- destaque de unidades localizadas em territórios com maior vulnerabilidade dentro do conjunto demonstrativo.

---

## 6. Fontes pesquisadas

Para contextualização do problema e elaboração do protótipo, foram consideradas fontes públicas relacionadas à cidade de São Paulo, especialmente:

- Portal de Dados Abertos da Prefeitura de São Paulo;
- informações públicas relacionadas à rede socioassistencial da SMADS;
- referências territoriais da cidade de São Paulo;
- Mapa da Desigualdade, da Rede Nossa São Paulo.

Essas fontes foram utilizadas como referência para definição do problema, estrutura dos dados e construção do protótipo.

---

## 7. Dados utilizados

O projeto utiliza uma **base demonstrativa incorporada diretamente ao código da aplicação**.

A base contém os seguintes campos:

| Campo | Descrição |
|---|---|
| `equipamento` | Nome de referência do equipamento socioassistencial |
| `tipo` | Tipo de equipamento, como CRAS, CREAS ou Centro Pop |
| `regiao` | Região da cidade |
| `subprefeitura` | Subprefeitura associada ao registro |
| `lat` | Latitude utilizada para representação cartográfica |
| `lon` | Longitude utilizada para representação cartográfica |
| `atendimentos_mes` | Volume mensal demonstrativo de atendimentos |
| `indice_vulnerabilidade` | Indicador sintético demonstrativo em escala de 0 a 10 |

### Atenção sobre os dados simulados

Este projeto é um **protótipo demonstrativo**.

Os valores utilizados em `atendimentos_mes` e `indice_vulnerabilidade` são utilizados para demonstrar as funcionalidades analíticas do painel e **não devem ser interpretados como indicadores oficiais atuais da Prefeitura de São Paulo**.

O indicador de vulnerabilidade utilizado na aplicação foi estruturado em uma escala demonstrativa de **0 a 10**, em que valores maiores representam maior vulnerabilidade no contexto do protótipo.

Da mesma forma, o volume mensal de atendimentos tem finalidade demonstrativa e não deve ser interpretado como dado operacional oficial de cada equipamento.

Essa escolha permitiu desenvolver e testar as funcionalidades da aplicação sem depender de sistemas internos ou APIs externas durante a avaliação técnica.

---

## 8. Metodologia

O desenvolvimento foi realizado nas seguintes etapas:

### 8.1 Definição do problema

Foi identificado como oportunidade de melhoria o acesso integrado a informações territoriais relacionadas aos equipamentos socioassistenciais.

### 8.2 Pesquisa e contextualização

Foram pesquisadas fontes públicas relacionadas à rede socioassistencial e a indicadores territoriais da cidade de São Paulo.

### 8.3 Estruturação dos dados

Foi construída uma base demonstrativa contendo informações territoriais dos equipamentos e variáveis utilizadas para simular diferentes cenários de análise.

### 8.4 Desenvolvimento do painel

A aplicação foi construída em Streamlit, utilizando Pandas para manipulação dos dados e Plotly Express para as visualizações.

### 8.5 Construção da sinalização automatizada

Foi implementada uma regra heurística para destacar registros com indicador de vulnerabilidade elevado.

No protótipo, valores de:

`indice_vulnerabilidade >= 8.5`

são classificados como situações de maior atenção territorial.

O valor **8,5 não representa um critério oficial da SMADS ou da Prefeitura de São Paulo**. Trata-se de uma regra demonstrativa adotada exclusivamente para evidenciar o funcionamento do módulo de sinalização.

O volume de atendimento também é comparado à média do recorte selecionado para fornecer uma referência descritiva do comportamento dos registros.

Essas classificações devem ser interpretadas como **apoio exploratório à análise**, e não representa diagnóstico oficial da SMADS de capacidade, eficiência ou necessidade de expansão de determinado serviço.

---

## 9. Interpretação dos indicadores

Um cuidado importante deste projeto é distinguir **volume de atendimento** de **capacidade operacional**.

O campo `atendimentos_mes` informa apenas o volume de atendimentos considerado na base demonstrativa.

Ele não permite, isoladamente, concluir se um equipamento:

- está sobrecarregado;
- possui capacidade ociosa;
- necessita de ampliação;
- possui equipe suficiente;
- atende integralmente à demanda de seu território.

Uma análise real de capacidade exigiria outras variáveis, como:

- quantidade de profissionais;
- capacidade prevista de atendimento;
- população de referência;
- demanda reprimida;
- filas;
- tempo médio de espera;
- frequência de atendimento;
- recursos disponíveis.

Por essa razão, as visualizações do painel são apresentadas como ferramentas de **análise exploratória e territorial**.

---

## 10. Tecnologias utilizadas

- **Python 3.10+**
- **Streamlit**
- **Pandas**
- **Plotly Express**
- **Git**
- **GitHub**

---

## 11. Uso de Inteligência Artificial

O edital permite e incentiva o uso de ferramentas de inteligência artificial e desenvolvimento assistido por IA.

### Ferramentas utilizadas

- Gemini

### Etapas em que a IA foi utilizada

A inteligência artificial foi utilizada como ferramenta de apoio nas seguintes atividades:

- estruturação inicial da aplicação;
- apoio à geração e revisão de código;
- construção de visualizações com Streamlit e Plotly;
- organização da documentação;
- revisão de textos;
- identificação de possíveis melhorias na solução.

### Validação dos resultados

Os resultados produzidos com auxílio de inteligência artificial não foram utilizados de forma automática.

O código e os textos gerados foram revisados, ajustados e incorporados conforme os objetivos do projeto.

A aplicação também foi verificada por meio de execução e testes manuais das principais funcionalidades, incluindo:

- carregamento dos dados;
- filtros;
- indicadores;
- gráficos;
- mapa;
- sinalização automatizada.

---

## 12. Limitações

A versão atual possui algumas limitações importantes:

- utiliza uma base demonstrativa e estática;
- não possui atualização automática de dados;
- não está integrada aos sistemas internos da SMADS;
- utiliza indicadores simulados para demonstração;
- não possui dados de fila ou demanda reprimida;
- não possui informação sobre equipes ou capacidade máxima de atendimento;
- a sinalização automatizada utiliza uma regra heurística simples;
- os resultados não devem ser utilizados isoladamente para decisões administrativas reais.

---

## 13. Possíveis melhorias futuras

Entre as possíveis evoluções do projeto estão:

- integração com bases públicas atualizadas;
- conexão com APIs e serviços geográficos;
- importação automática de dados;
- inclusão de população de referência por território;
- inclusão de capacidade de atendimento de cada unidade;
- análise de demanda reprimida;
- tempo médio de espera;
- indicadores históricos;
- análise de evolução temporal;
- comparação entre oferta de serviços e população vulnerável;
- inclusão de novas tipologias de equipamentos;
- utilização de modelos estatísticos ou preditivos;
- desenvolvimento de alertas territoriais;
- aprimoramento da metodologia de priorização.

---

## 14. Estrutura do projeto

```text
painel-smads-adesampa/
│
├── app.py
├── requirements.txt
└── README.md
```

### `app.py`

Arquivo principal da aplicação Streamlit. Contém:

- base demonstrativa;
- filtros;
- indicadores;
- mapa;
- gráficos;
- sinalização automatizada.

### `requirements.txt`

Lista as bibliotecas necessárias para execução da aplicação.

### `README.md`

Documentação do projeto, metodologia, dados, limitações e instruções de execução.

---

## 15. Como executar o projeto

### Pré-requisitos

É necessário ter instalado:

- Python 3.10 ou superior;
- `pip`;
- Git.

### 1. Clonar o repositório

```bash
git clone https://github.com/luciana-gouveia/painel-smads-adesampa.git
```

Entre na pasta:

```bash
cd painel-smads-adesampa
```

### 2. Criar um ambiente virtual

Recomendado:

```bash
python -m venv .venv
```

### 3. Ativar o ambiente virtual

#### Windows

```bash
.venv\Scripts\activate
```

#### Linux ou macOS

```bash
source .venv/bin/activate
```

### 4. Instalar as dependências

```bash
pip install -r requirements.txt
```

### 5. Executar a aplicação

```bash
streamlit run app.py
```

Após a execução, o Streamlit exibirá no terminal o endereço local da aplicação.

Normalmente:

```text
http://localhost:8501
```

Abra esse endereço no navegador.

---

## 16. Dependências

O arquivo `requirements.txt` contém:

```text
streamlit>=1.35.0
pandas>=2.0.0
plotly>=5.24.0
```

O projeto não necessita de:

- banco de dados externo;
- chave de API;
- variável de ambiente;
- credenciais;
- serviço externo obrigatório.

A aplicação pode ser executada localmente após a instalação das dependências.

---

## 17. Aplicação publicada

**Link da aplicação:** 
https://painel-smads-adesampa-gu9whspwknudhiquhry7td.streamlit.app/

Caso a aplicação publicada não esteja disponível, o projeto pode ser executado localmente seguindo as instruções desta documentação.

---

## 18. Objetivo do protótipo

Este projeto não pretende substituir ferramentas oficiais da administração pública.

Seu objetivo é demonstrar como análise de dados, visualização territorial, desenvolvimento web, automação de análises e uso responsável de inteligência artificial podem ser combinados para apoiar a gestão pública municipal e a tomada de decisão no contexto da assistência social em São Paulo.

---

## Autoria

**Luciana Gouveia**

Projeto desenvolvido para a **Prova Técnica Prática — Edital de Seleção Pública nº 005/2026 — Assistente II - Dados e IA — ADE SAMPA**.