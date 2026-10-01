import streamlit as st
import pandas as pd
import plotly.express as px

# Configuração da página
st.set_page_config(
    page_title="Painel de Apoio à Gestão Socioassistencial - SMADS/SP",
    page_icon="🏙️",
    layout="wide"
)

# Carregamento e consolidação de dados da rede socioassistencial (SMADS)
@st.cache_data
def carregar_dados():
    dados = [
        # Zona Central
        {"equipamento": "CRAS Sé", "tipo": "CRAS", "regiao": "Centro", "subprefeitura": "Sé", "lat": -23.5489, "lon": -46.6388, "atendimentos_mes": 1150, "indice_vulnerabilidade": 7.5},
        {"equipamento": "CREAS Sé", "tipo": "CREAS", "regiao": "Centro", "subprefeitura": "Sé", "lat": -23.5510, "lon": -46.6340, "atendimentos_mes": 850, "indice_vulnerabilidade": 7.8},
        {"equipamento": "Centro Pop Santa Cecília", "tipo": "Centro Pop", "regiao": "Centro", "subprefeitura": "Sé", "lat": -23.5350, "lon": -46.6500, "atendimentos_mes": 2100, "indice_vulnerabilidade": 8.1},
        {"equipamento": "Centro Pop Bela Vista", "tipo": "Centro Pop", "regiao": "Centro", "subprefeitura": "Sé", "lat": -23.5570, "lon": -46.6430, "atendimentos_mes": 1950, "indice_vulnerabilidade": 7.6},

        # Zona Leste
        {"equipamento": "CRAS Cidade Tiradentes", "tipo": "CRAS", "regiao": "Zona Leste", "subprefeitura": "Cidade Tiradentes", "lat": -23.5855, "lon": -46.3985, "atendimentos_mes": 1420, "indice_vulnerabilidade": 9.2},
        {"equipamento": "CREAS Cidade Tiradentes", "tipo": "CREAS", "regiao": "Zona Leste", "subprefeitura": "Cidade Tiradentes", "lat": -23.5910, "lon": -46.4020, "atendimentos_mes": 670, "indice_vulnerabilidade": 9.0},
        {"equipamento": "CRAS Itaquera", "tipo": "CRAS", "regiao": "Zona Leste", "subprefeitura": "Itaquera", "lat": -23.5385, "lon": -46.4560, "atendimentos_mes": 1100, "indice_vulnerabilidade": 7.4},
        {"equipamento": "CREAS Itaquera", "tipo": "CREAS", "regiao": "Zona Leste", "subprefeitura": "Itaquera", "lat": -23.5320, "lon": -46.4610, "atendimentos_mes": 580, "indice_vulnerabilidade": 7.3},
        {"equipamento": "CRAS São Mateus", "tipo": "CRAS", "regiao": "Zona Leste", "subprefeitura": "São Mateus", "lat": -23.6120, "lon": -46.4750, "atendimentos_mes": 1280, "indice_vulnerabilidade": 8.3},
        {"equipamento": "CREAS São Mateus", "tipo": "CREAS", "regiao": "Zona Leste", "subprefeitura": "São Mateus", "lat": -23.6080, "lon": -46.4810, "atendimentos_mes": 620, "indice_vulnerabilidade": 8.2},
        {"equipamento": "CRAS Guaianases", "tipo": "CRAS", "regiao": "Zona Leste", "subprefeitura": "Guaianases", "lat": -23.5420, "lon": -46.4170, "atendimentos_mes": 1310, "indice_vulnerabilidade": 8.8},
        {"equipamento": "CRAS São Miguel Paulista", "tipo": "CRAS", "regiao": "Zona Leste", "subprefeitura": "São Miguel Paulista", "lat": -23.4980, "lon": -46.4420, "atendimentos_mes": 1190, "indice_vulnerabilidade": 7.9},
        {"equipamento": "CRAS Itaim Paulista", "tipo": "CRAS", "regiao": "Zona Leste", "subprefeitura": "Itaim Paulista", "lat": -23.4950, "lon": -46.3890, "atendimentos_mes": 1390, "indice_vulnerabilidade": 8.9},
        {"equipamento": "CREAS Itaim Paulista", "tipo": "CREAS", "regiao": "Zona Leste", "subprefeitura": "Itaim Paulista", "lat": -23.5010, "lon": -46.3950, "atendimentos_mes": 640, "indice_vulnerabilidade": 8.7},
        {"equipamento": "CRAS Mooca", "tipo": "CRAS", "regiao": "Zona Leste", "subprefeitura": "Mooca", "lat": -23.5550, "lon": -46.5980, "atendimentos_mes": 650, "indice_vulnerabilidade": 4.1},
        {"equipamento": "CRAS Penha", "tipo": "CRAS", "regiao": "Zona Leste", "subprefeitura": "Penha", "lat": -23.5280, "lon": -46.5490, "atendimentos_mes": 870, "indice_vulnerabilidade": 5.6},
        {"equipamento": "CRAS Ermelino Matarazzo", "tipo": "CRAS", "regiao": "Zona Leste", "subprefeitura": "Ermelino Matarazzo", "lat": -23.4890, "lon": -46.5010, "atendimentos_mes": 990, "indice_vulnerabilidade": 7.5},

        # Zona Norte
        {"equipamento": "CRAS Brasilândia", "tipo": "CRAS", "regiao": "Zona Norte", "subprefeitura": "Freguesia/Brasilândia", "lat": -23.4680, "lon": -46.6890, "atendimentos_mes": 1350, "indice_vulnerabilidade": 8.7},
        {"equipamento": "CREAS Brasilândia", "tipo": "CREAS", "regiao": "Zona Norte", "subprefeitura": "Freguesia/Brasilândia", "lat": -23.4730, "lon": -46.6810, "atendimentos_mes": 690, "indice_vulnerabilidade": 8.6},
        {"equipamento": "CRAS Santana", "tipo": "CRAS", "regiao": "Zona Norte", "subprefeitura": "Santana/Tucuruvi", "lat": -23.5030, "lon": -46.6260, "atendimentos_mes": 720, "indice_vulnerabilidade": 4.5},
        {"equipamento": "CREAS Santana", "tipo": "CREAS", "regiao": "Zona Norte", "subprefeitura": "Santana/Tucuruvi", "lat": -23.4980, "lon": -46.6210, "atendimentos_mes": 540, "indice_vulnerabilidade": 4.7},
        {"equipamento": "CRAS Jaçanã", "tipo": "CRAS", "regiao": "Zona Norte", "subprefeitura": "Jaçanã/Tremembé", "lat": -23.4620, "lon": -46.5880, "atendimentos_mes": 1050, "indice_vulnerabilidade": 7.6},
        {"equipamento": "CRAS Perus", "tipo": "CRAS", "regiao": "Zona Norte", "subprefeitura": "Perus", "lat": -23.4070, "lon": -46.7520, "atendimentos_mes": 930, "indice_vulnerabilidade": 8.1},
        {"equipamento": "CRAS Pirituba", "tipo": "CRAS", "regiao": "Zona Norte", "subprefeitura": "Pirituba/Jaraguá", "lat": -23.4620, "lon": -46.7320, "atendimentos_mes": 1180, "indice_vulnerabilidade": 7.8},
        {"equipamento": "CREAS Pirituba", "tipo": "CREAS", "regiao": "Zona Norte", "subprefeitura": "Pirituba/Jaraguá", "lat": -23.4710, "lon": -46.7250, "atendimentos_mes": 590, "indice_vulnerabilidade": 7.7},
        {"equipamento": "CRAS Casa Verde", "tipo": "CRAS", "regiao": "Zona Norte", "subprefeitura": "Casa Verde/Cachoeirinha", "lat": -23.5010, "lon": -46.6620, "atendimentos_mes": 880, "indice_vulnerabilidade": 6.3},

        # Zona Sul
        {"equipamento": "CRAS Campo Limpo", "tipo": "CRAS", "regiao": "Zona Sul", "subprefeitura": "Campo Limpo", "lat": -23.6492, "lon": -46.7584, "atendimentos_mes": 1450, "indice_vulnerabilidade": 8.5},
        {"equipamento": "CREAS Campo Limpo", "tipo": "CREAS", "regiao": "Zona Sul", "subprefeitura": "Campo Limpo", "lat": -23.6420, "lon": -46.7510, "atendimentos_mes": 730, "indice_vulnerabilidade": 8.4},
        {"equipamento": "CRAS M'Boi Mirim", "tipo": "CRAS", "regiao": "Zona Sul", "subprefeitura": "M'Boi Mirim", "lat": -23.6780, "lon": -46.7620, "atendimentos_mes": 1520, "indice_vulnerabilidade": 9.1},
        {"equipamento": "CREAS M'Boi Mirim", "tipo": "CREAS", "regiao": "Zona Sul", "subprefeitura": "M'Boi Mirim", "lat": -23.6821, "lon": -46.7690, "atendimentos_mes": 760, "indice_vulnerabilidade": 9.0},
        {"equipamento": "CRAS Parelheiros", "tipo": "CRAS", "regiao": "Zona Sul", "subprefeitura": "Parelheiros", "lat": -23.7740, "lon": -46.7210, "atendimentos_mes": 980, "indice_vulnerabilidade": 9.4},
        {"equipamento": "CREAS Parelheiros", "tipo": "CREAS", "regiao": "Zona Sul", "subprefeitura": "Parelheiros", "lat": -23.7690, "lon": -46.7150, "atendimentos_mes": 490, "indice_vulnerabilidade": 9.3},
        {"equipamento": "CRAS Capela do Socorro", "tipo": "CRAS", "regiao": "Zona Sul", "subprefeitura": "Capela do Socorro", "lat": -23.7080, "lon": -46.6990, "atendimentos_mes": 1340, "indice_vulnerabilidade": 8.6},
        {"equipamento": "CREAS Capela do Socorro", "tipo": "CREAS", "regiao": "Zona Sul", "subprefeitura": "Capela do Socorro", "lat": -23.7010, "lon": -46.7050, "atendimentos_mes": 680, "indice_vulnerabilidade": 8.5},
        {"equipamento": "CRAS Santo Amaro", "tipo": "CRAS", "regiao": "Zona Sul", "subprefeitura": "Santo Amaro", "lat": -23.6520, "lon": -46.7020, "atendimentos_mes": 750, "indice_vulnerabilidade": 4.8},
        {"equipamento": "CRAS Cidade Ademar", "tipo": "CRAS", "regiao": "Zona Sul", "subprefeitura": "Cidade Ademar", "lat": -23.6730, "lon": -46.6620, "atendimentos_mes": 1210, "indice_vulnerabilidade": 8.0},
        {"equipamento": "CRAS Jabaquara", "tipo": "CRAS", "regiao": "Zona Sul", "subprefeitura": "Jabaquara", "lat": -23.6480, "lon": -46.6430, "atendimentos_mes": 890, "indice_vulnerabilidade": 6.8},
        {"equipamento": "CRAS Ipiranga", "tipo": "CRAS", "regiao": "Zona Sul", "subprefeitura": "Ipiranga", "lat": -23.5930, "lon": -46.6080, "atendimentos_mes": 770, "indice_vulnerabilidade": 5.0},
        {"equipamento": "CRAS Vila Mariana", "tipo": "CRAS", "regiao": "Zona Sul", "subprefeitura": "Vila Mariana", "lat": -23.5890, "lon": -46.6380, "atendimentos_mes": 560, "indice_vulnerabilidade": 3.2},

        # Zona Oeste
        {"equipamento": "CRAS Butantã", "tipo": "CRAS", "regiao": "Zona Oeste", "subprefeitura": "Butantã", "lat": -23.5710, "lon": -46.7090, "atendimentos_mes": 710, "indice_vulnerabilidade": 5.1},
        {"equipamento": "CREAS Butantã", "tipo": "CREAS", "regiao": "Zona Oeste", "subprefeitura": "Butantã", "lat": -23.5650, "lon": -46.7180, "atendimentos_mes": 480, "indice_vulnerabilidade": 5.0},
        {"equipamento": "CRAS Lapa", "tipo": "CRAS", "regiao": "Zona Oeste", "subprefeitura": "Lapa", "lat": -23.5210, "lon": -46.7030, "atendimentos_mes": 520, "indice_vulnerabilidade": 3.9},
        {"equipamento": "CREAS Lapa", "tipo": "CREAS", "regiao": "Zona Oeste", "subprefeitura": "Lapa", "lat": -23.5270, "lon": -46.6970, "atendimentos_mes": 410, "indice_vulnerabilidade": 4.0},
        {"equipamento": "CRAS Pinheiros", "tipo": "CRAS", "regiao": "Zona Oeste", "subprefeitura": "Pinheiros", "lat": -23.5610, "lon": -46.6890, "atendimentos_mes": 430, "indice_vulnerabilidade": 2.9}
    ]
    return pd.DataFrame(dados)

df = carregar_dados()

# Barra lateral - Filtros
st.sidebar.title("Filtros Territoriais")
regioes_disponiveis = ["Todas"] + sorted(list(df["regiao"].unique()))
regiao_selecionada = st.sidebar.selectbox("Selecione a Região", regioes_disponiveis)

tipos_disponiveis = ["Todos"] + sorted(list(df["tipo"].unique()))
tipo_selecionado = st.sidebar.selectbox("Tipo de Equipamento", tipos_disponiveis)

# Aplicação dos filtros
df_filtrado = df.copy()

if regiao_selecionada != "Todas":
    df_filtrado = df_filtrado[
        df_filtrado["regiao"] == regiao_selecionada
    ]

if tipo_selecionado != "Todos":
    df_filtrado = df_filtrado[
        df_filtrado["tipo"] == tipo_selecionado
    ]

# Título Principal
st.title("Painel de Apoio à Gestão Socioassistencial")

st.caption(
    "Monitoramento de Equipamentos Públicos e Vulnerabilidade - "
    "Secretaria Municipal de Assistência e Desenvolvimento Social (SMADS)"
)

st.info(
    "ℹ️ Protótipo demonstrativo: os valores de atendimentos e do índice "
    "de vulnerabilidade utilizados nesta aplicação são simulados para fins "
    "de demonstração. O volume de atendimentos representa um mês de referência "
    "fictício, sem correspondência a período real específico, e não representa "
    "indicador operacional oficial da SMADS."
)

# Métricas de topo
col1, col2, col3 = st.columns(3)

col1.metric(
    "Equipamentos Filtrados",
    len(df_filtrado)
)

col2.metric(
    "Média de Atendimentos/Mês (simulada)",
    int(df_filtrado["atendimentos_mes"].mean())
    if not df_filtrado.empty
    else 0
)

col3.metric(
    "Índice Médio de Vulnerabilidade (simulado)",
    round(df_filtrado["indice_vulnerabilidade"].mean(), 2)
    if not df_filtrado.empty
    else 0
)

st.markdown("---")

# Mapa Territorial
st.subheader("Distribuição Territorial dos Equipamentos")

if not df_filtrado.empty:
    fig_map = px.scatter_map(
        df_filtrado,
        lat="lat",
        lon="lon",
        hover_name="equipamento",
        hover_data={
            "tipo": True,
            "subprefeitura": True,
            "atendimentos_mes": True,
            "indice_vulnerabilidade": True,
            "lat": False,
            "lon": False
        },
        color="tipo",
        size="atendimentos_mes",
        zoom=10,
        center={
            "lat": -23.5505,
            "lon": -46.6333
        },
        map_style="open-street-map",
        title="Localização dos Equipamentos (Tamanho por Volume de Atendimentos)"
    )

    st.plotly_chart(
        fig_map,
        use_container_width=True
    )

else:
    st.warning(
        "Nenhum equipamento encontrado para os filtros selecionados."
    )

# Análise de Atendimento e Vulnerabilidade
col_graf1, col_graf2 = st.columns(2)

with col_graf1:
    st.subheader("Volume de Atendimentos por Unidade")

    fig_bar = px.bar(
        df_filtrado.sort_values(
            by="atendimentos_mes",
            ascending=True
        ),
        x="atendimentos_mes",
        y="equipamento",
        orientation="h",
        color="tipo",
        labels={
            "atendimentos_mes": "Atendimentos/Mês (simulado)",
            "equipamento": "Unidade"
        }
    )

    st.plotly_chart(
        fig_bar,
        use_container_width=True
    )

with col_graf2:
    st.subheader(
        "Vulnerabilidade vs. Volume Mensal de Atendimentos"
    )

    fig_scatter = px.scatter(
        df_filtrado,
        x="indice_vulnerabilidade",
        y="atendimentos_mes",
        color="regiao",
        size="atendimentos_mes",
        hover_name="equipamento",
        labels={
            "indice_vulnerabilidade":
                "Índice de Vulnerabilidade Simulado (0-10)",
            "atendimentos_mes":
                "Atendimentos/Mês (simulado)"
        }
    )

    st.plotly_chart(
        fig_scatter,
        use_container_width=True
    )

# Módulo de Apoio à Decisão (Sinalização Automatizada)
st.markdown("---")

st.subheader(
    "Sinalização Automatizada para Análise Territorial"
)

st.caption(
    "A sinalização utiliza uma regra heurística demonstrativa e não "
    "representa diagnóstico oficial da SMADS nem avaliação definitiva "
    "de capacidade operacional dos equipamentos."
)

if not df_filtrado.empty:

    # Limiar demonstrativo adotado para o protótipo
    limiar_vulnerabilidade = 8.5

    alta_vulnerabilidade = df_filtrado[
        df_filtrado["indice_vulnerabilidade"]
        >= limiar_vulnerabilidade
    ]

    media_atendimentos = df_filtrado[
        "atendimentos_mes"
    ].mean()

    st.markdown(
        "**Sinalização Territorial Gerada:**"
    )

    if len(alta_vulnerabilidade) > 0:

        st.warning(
            f"Atenção: identificadas "
            f"**{len(alta_vulnerabilidade)} unidades** "
            f"em territórios com índice de vulnerabilidade "
            f"simulado ≥ {limiar_vulnerabilidade}."
        )

        for _, row in alta_vulnerabilidade.iterrows():

            if row["atendimentos_mes"] > media_atendimentos:
                volume_relativo = (
                    "acima da média do recorte"
                )

            elif row["atendimentos_mes"] < media_atendimentos:
                volume_relativo = (
                    "abaixo da média do recorte"
                )

            else:
                volume_relativo = (
                    "igual à média do recorte"
                )

            st.write(
                f"- **{row['equipamento']}** "
                f"({row['subprefeitura']}): "
                f"Vulnerabilidade simulada "
                f"{row['indice_vulnerabilidade']}/10 | "
                f"Volume de atendimentos {volume_relativo}."
            )

    else:

        st.success(
            "Não foram identificadas unidades que atingiram "
            f"o limiar demonstrativo de vulnerabilidade "
            f"≥ {limiar_vulnerabilidade} no recorte selecionado."
        )

    st.caption(
        "A comparação com a média do recorte é apenas descritiva. "
        "O volume de atendimentos, isoladamente, não permite concluir "
        "se uma unidade possui sobrecarga, capacidade ociosa ou "
        "capacidade operacional insuficiente."
    )