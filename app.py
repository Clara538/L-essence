python
import streamlit as st
import pandas as pd
import os

# =========================================================
# CONFIGURAÇÃO DA PÁGINA
# =========================================================

st.set_page_config(
    page_title="Maison Élégance",
    page_icon="💎",
    layout="wide",
    initial_sidebar_state="expanded"
)

ARQUIVO = "joias.csv"

# =========================================================
# IMAGENS
# =========================================================

IMAGEM_HERO = (
    "https://images.unsplash.com/"
    "photo-1515562141207-7a88fb7ce338"
    "?auto=format&fit=crop&w=1800&q=90"
)

IMAGEM_ACESSORIOS = (
    "https://images.unsplash.com/"
    "photo-1611652022419-a9419f74343d"
    "?auto=format&fit=crop&w=1200&q=85"
)

# =========================================================
# CSS
# =========================================================

st.markdown("""
<style>

@import url(
'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;600;700&family=Poppins:wght@400;500;600;700&display=swap'
);

/* =========================================================
FONTE
========================================================= */

html,
body,
[class*="css"] {
    font-family: 'Poppins', sans-serif;
}

/* =========================================================
FUNDO PRINCIPAL
========================================================= */

.stApp {
    background:
        linear-gradient(
            135deg,
            #F7F6ED 0%,
            #E7EAD5 50%,
            #D6DEC0 100%
        );
}

/* =========================================================
ÁREA PRINCIPAL
========================================================= */

.block-container {
    max-width: 1400px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

/* =========================================================
SIDEBAR
========================================================= */

[data-testid="stSidebar"] {
    background:
        linear-gradient(
            180deg,
            #14251F,
            #203A30
        );

    border-right:
        2px solid #B9A45A;
}

[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}

/* =========================================================
LOGO
========================================================= */

.logo-title {
    font-family: 'Playfair Display', serif;
    font-size: 29px;
    font-weight: 700;
    color: #FFFFFF !important;
    margin-bottom: 5px;
}

.logo-subtitle {
    font-size: 10px;
    font-weight: 700;
    color: #D9C98A !important;
    letter-spacing: 2px;
}

/* =========================================================
TÍTULOS
========================================================= */

.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 42px;
    font-weight: 700;
    color: #24362C !important;
    margin-bottom: 5px;
}

.page-subtitle {
    font-size: 16px;
    color: #566456 !important;
    margin-bottom: 30px;
}

/* =========================================================
HERO
========================================================= */

.hero-container {
    position: relative;
    height: 430px;
    width: 100%;
    border-radius: 28px;
    overflow: hidden;
    margin-bottom: 35px;

    background-size: cover;
    background-position: center;

    box-shadow:
        0 15px 35px rgba(0,0,0,0.20);
}

.hero-overlay {
    position: absolute;
    inset: 0;

    background:
        linear-gradient(
            90deg,
            rgba(18,35,29,0.97) 0%,
            rgba(18,35,29,0.82) 45%,
            rgba(18,35,29,0.15) 100%
        );
}

.hero-content {
    position: absolute;
    top: 50%;
    left: 7%;

    transform: translateY(-50%);

    max-width: 600px;
}

.hero-number {
    font-size: 65px;
    font-weight: 800;
    color: #D8C77C !important;
    line-height: 1;
}

.hero-title {
    font-family: 'Playfair Display', serif;
    font-size: 48px;
    font-weight: 700;
    color: #FFFFFF !important;

    margin-top: 12px;
    line-height: 1.1;
}

.hero-text {
    font-size: 17px;
    color: #EEF0E5 !important;

    margin-top: 20px;
    line-height: 1.7;
}

.hero-badge {
    display: inline-block;

    margin-top: 24px;

    padding: 10px 22px;

    border-radius: 30px;

    background: #A9903F;

    color: #FFFFFF !important;

    font-size: 13px;
    font-weight: 700;
    letter-spacing: 1px;
}

/* =========================================================
CARDS
========================================================= */

.info-card {
    background: #FFFFFF;

    border-radius: 22px;

    padding: 28px;

    min-height: 170px;

    border:
        1px solid rgba(169,144,63,0.35);

    box-shadow:
        0 10px 25px rgba(0,0,0,0.08);
}

.card-icon {
    font-size: 32px;
}

.card-number {
    font-size: 32px;
    font-weight: 800;

    color: #26382D !important;

    margin-top: 10px;
}

.card-label {
    font-size: 13px;
    font-weight: 700;

    color: #687263 !important;

    margin-top: 5px;
}

/* =========================================================
CARD ESCURO
========================================================= */

.dark-card {
    background:
        linear-gradient(
            135deg,
            #152C24,
            #274638
        );

    border-radius: 24px;

    padding: 30px;

    box-shadow:
        0 12px 30px rgba(0,0,0,0.16);
}

.dark-card h2 {
    font-family: 'Playfair Display', serif;
    color: #FFFFFF !important;
    margin-top: 0;
}

.dark-card p {
    color: #E8EBDD !important;
    line-height: 1.7;
}

/* =========================================================
FORMULÁRIO
========================================================= */

[data-testid="stForm"] {
    background:
        rgba(255,255,255,0.88);

    padding: 30px;

    border-radius: 25px;

    border:
        1px solid #C8BA7A;

    box-shadow:
        0 10px 30px rgba(0,0,0,0.08);
}

/* =========================================================
LABELS
========================================================= */

[data-testid="stWidgetLabel"],
[data-testid="stWidgetLabel"] label,
[data-testid="stWidgetLabel"] p,
[data-testid="stWidgetLabel"] span,
.stTextInput label,
.stNumberInput label,
.stSelectbox label,
.stTextArea label {

    color: #26382D !important;

    opacity: 1 !important;

    font-size: 15px !important;

    font-weight: 700 !important;
}

/* =========================================================
INPUTS
========================================================= */

.stTextInput input,
.stNumberInput input,
.stTextArea textarea {

    background-color: #FFFFFF !important;

    color: #24352B !important;

    -webkit-text-fill-color:
        #24352B !important;

    border:
        2px solid #AFA46E !important;

    border-radius: 12px !important;

    font-size: 16px !important;

    font-weight: 500 !important;
}

.stTextInput input:focus,
.stNumberInput input:focus,
.stTextArea textarea:focus {

    border:
        2px solid #806D2E !important;

    box-shadow:
        0 0 0 3px rgba(128,109,46,0.15) !important;
}

input::placeholder,
textarea::placeholder {

    color: #747A6C !important;

    opacity: 1 !important;
}

/* =========================================================
SELECTBOX
========================================================= */

[data-baseweb="select"] > div {

    background-color: #30463B !important;

    border:
        2px solid #9D925D !important;

    border-radius: 12px !important;
}

[data-baseweb="select"] > div * {

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;

    opacity: 1 !important;
}

[data-baseweb="select"] input {

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[data-baseweb="select"] [class*="singleValue"] {

    color: #FFFFFF !important;
}

[data-baseweb="select"] svg {

    fill: #FFFFFF !important;

    color: #FFFFFF !important;
}

[data-baseweb="select"] > div:hover {

    border-color: #D2C477 !important;
}

/* =========================================================
MENU SELECTBOX
========================================================= */

[data-baseweb="popover"] {
    background-color: #30463B !important;
}

[data-baseweb="menu"] {
    background-color: #30463B !important;
}

[role="option"] {

    background-color: #30463B !important;

    color: #FFFFFF !important;

    -webkit-text-fill-color:
        #FFFFFF !important;
}

[role="option"]:hover {

    background-color: #667548 !important;

    color: #FFFFFF !important;
}

/* =========================================================
BOTÕES
========================================================= */

.stButton > button,
div[data-testid="stFormSubmitButton"] > button {

    background:
        linear-gradient(
            135deg,
            #82702F,
            #B09B4B
        ) !important;

    color: #FFFFFF !important;

    border: none !important;

    border-radius: 14px !important;

    min-height: 54px;

    font-family:
        'Poppins', sans-serif !important;

    font-size: 15px !important;

    font-weight: 700 !important;

    box-shadow:
        0 8px 18px rgba(126,108,43,0.25);
}

.stButton > button:hover,
div[data-testid="stFormSubmitButton"] > button:hover {

    background:
        linear-gradient(
            135deg,
            #665823,
            #927F35
        ) !important;

    color: #FFFFFF !important;

    transform:
        translateY(-1px);
}

/* =========================================================
TABELA
========================================================= */

[data-testid="stDataFrame"] {

    background: #FFFFFF;

    border-radius: 18px;

    overflow: hidden;

    border:
        1px solid #C8BA7A;
}

/* =========================================================
RODAPÉ
========================================================= */

.footer {

    margin-top: 50px;

    text-align: center;

    color: #596553 !important;

    font-size: 14px;

    font-weight: 600;
}

/* =========================================================
RESPONSIVO
========================================================= */

@media (max-width: 768px) {

    .hero-container {
        height: 500px;
    }

    .hero-content {
        left: 8%;
        right: 8%;
    }

    .hero-title {
        font-size: 35px;
    }

    .hero-number {
        font-size: 55px;
    }

    .page-title {
        font-size: 32px;
    }
}

</style>
""", unsafe_allow_html=True)


# =========================================================
# FUNÇÕES
# =========================================================

def carregar_dados():

    colunas = [
        "Categoria",
        "Nome",
        "Material",
        "Coleção",
        "Cor",
        "Código",
        "Quantidade",
        "Valor",
        "Observações"
    ]

    if os.path.exists(ARQUIVO):

        try:
            return pd.read_csv(ARQUIVO)

        except Exception:
            return pd.DataFrame(columns=colunas)

    return pd.DataFrame(columns=colunas)


def salvar_dados(dados):

    dados.to_csv(
        ARQUIVO,
        index=False
    )


# =========================================================
# CARREGAR DADOS
# =========================================================

df = carregar_dados()


# =========================================================
# GARANTIR COLUNAS
# =========================================================

colunas_necessarias = [
    "Categoria",
    "Nome",
    "Material",
    "Coleção",
    "Cor",
    "Código",
    "Quantidade",
    "Valor",
    "Observações"
]

for coluna in colunas_necessarias:

    if coluna not in df.columns:
        df[coluna] = ""


# =========================================================
# CONVERTER VALORES
# =========================================================

df["Valor"] = pd.to_numeric(
    df["Valor"],
    errors="coerce"
).fillna(0)

df["Quantidade"] = pd.to_numeric(
    df["Quantidade"],
    errors="coerce"
).fillna(0)


# =========================================================
# SIDEBAR
# =========================================================

st.sidebar.markdown(
"""
<div class="logo-title">
💎 Maison Élégance
</div>

<div class="logo-subtitle">
JOIAS FINAS & ACESSÓRIOS
</div>
""",
unsafe_allow_html=True
)

st.sidebar.markdown(
    "<br>",
    unsafe_allow_html=True
)


menu = st.sidebar.radio(
    "NAVEGAÇÃO",
    [
        "🏠 Dashboard",
        "💎 Cadastrar Peça",
        "✨ Peças Cadastradas"
    ]
)


st.sidebar.markdown("---")

st.sidebar.caption(
    "Maison Élégance • 2026"
)


# =========================================================
# DASHBOARD
# =========================================================

if menu == "🏠 Dashboard":

    st.markdown(
f"""
<div class="hero-container"
style="background-image: url('{IMAGEM_HERO}');">

<div class="hero-overlay"></div>

<div class="hero-content">

<div class="hero-number">
01.
</div>

<div class="hero-title">
Elegância.<br>
Em cada detalhe.
</div>

<div class="hero-text">
Organize sua coleção de joias e acessórios
em um único lugar.<br>
Cadastre, consulte e acompanhe suas peças
com praticidade e sofisticação.
</div>

<div class="hero-badge">
✦ CURADORIA EXCLUSIVA
</div>

</div>

</div>
""",
unsafe_allow_html=True
)


    st.markdown(
"""
<div class="page-title">
✦ Visão geral da coleção
</div>

<div class="page-subtitle">
Acompanhe suas peças e mantenha sua coleção sempre organizada.
</div>
""",
unsafe_allow_html=True
)


    total_pecas = len(df)

    quantidade_total = df["Quantidade"].sum()

    valor_total = (
        df["Valor"] * df["Quantidade"]
    ).sum()


    col1, col2, col3 = st.columns(3)


    with col1:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💎
</div>

<div class="card-number">
{total_pecas}
</div>

<div class="card-label">
PEÇAS CADASTRADAS
</div>

</div>
""",
unsafe_allow_html=True
)


    with col2:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
📦
</div>

<div class="card-number">
{quantidade_total:,.0f}
</div>

<div class="card-label">
ITENS NO ACERVO
</div>

</div>
""",
unsafe_allow_html=True
)


    with col3:

        st.markdown(
f"""
<div class="info-card">

<div class="card-icon">
💰
</div>

<div class="card-number">
R$ {valor_total:,.2f}
</div>

<div class="card-label">
VALOR ESTIMADO DO ACERVO
</div>

</div>
""",
unsafe_allow_html=True
)


    st.markdown(
        "<br>",
        unsafe_allow_html=True
    )


    coluna1, coluna2 = st.columns([1.1, 1])


    with coluna1:

        st.markdown(
"""
<div class="dark-card">

<h2>
✦ O luxo está nos detalhes
</h2>

<p>
A Maison Élégance foi criada para organizar
joias finas e acessórios de forma simples,
elegante e profissional.
</p>

<p>
Cadastre anéis, colares, brincos, pulseiras,
relógios e outras peças em um único acervo.
</p>

</div>
""",
unsafe_allow_html=True
)


    with coluna2:

        st.image(
            IMAGEM_ACESSORIOS,
            use_container_width=True
        )


# =========================================================
# CADASTRAR PEÇA
# =========================================================

elif menu == "💎 Cadastrar Peça":

    st.markdown(
"""
<div class="page-title">
💎 Nova peça
</div>

<div class="page-subtitle">
Adicione uma nova joia ou acessório à sua coleção.
</div>
""",
unsafe_allow_html=True
)


    with st.form(
        "cadastro_joia",
        clear_on_submit=True
    ):

        col1, col2 = st.columns(2)


        with col1:

            categoria = st.selectbox(
                "💎 Categoria",
                [
                    "Anel",
                    "Colar",
                    "Brinco",
                    "Pulseira",
                    "Relógio",
                    "Tornozeleira",
                    "Broche",
                    "Acessório",
                    "Outro"
                ]
            )


            nome = st.text_input(
                "✨ Nome da Peça"
            )


            material = st.selectbox(
                "🏷️ Material",
                [
                    "Ouro",
                    "Prata",
                    "Ouro Branco",
                    "Ouro Rosé",
                    "Aço Inox",
                    "Prata 925",
                    "Pedras Preciosas",
                    "Outro"
                ]
            )


            colecao = st.text_input(
                "🌿 Coleção"
            )


        with col2:

            cor = st.selectbox(
                "🎨 Cor",
                [
                    "Dourado",
                    "Prateado",
                    "Rosé",
                    "Verde",
                    "Branco",
                    "Preto",
                    "Azul",
                    "Vermelho",
                    "Outro"
                ]
            )


            codigo = st.text_input(
                "🔖 Código da Peça"
            )


            quantidade = st.number_input(
                "📦 Quantidade",
                min_value=1,
                value=1,
                step=1
            )


            valor = st.number_input(
                "💰 Valor Unitário",
                min_value=0.0,
                value=0.0,
                step=100.0
            )


            observacoes = st.text_area(
                "📝 Descrição / Observações"
            )


        cadastrar = st.form_submit_button(
            "💎 CADASTRAR PEÇA"
        )


    if cadastrar:

        if (
            nome.strip()
            and codigo.strip()
        ):

            nova_peca = pd.DataFrame(
                [{
                    "Categoria": categoria,
                    "Nome": nome.strip(),
                    "Material": material,
                    "Coleção": colecao.strip(),
                    "Cor": cor,
                    "Código": codigo.strip().upper(),
                    "Quantidade": int(quantidade),
                    "Valor": float(valor),
                    "Observações": observacoes.strip()
                }]
            )


            df = pd.concat(
                [
                    df,
                    nova_peca
                ],
                ignore_index=True
            )


            salvar_dados(df)


            st.success(
                "💎 Peça cadastrada com sucesso!"
            )


            st.rerun()


        else:

            st.warning(
                "⚠️ Preencha o Nome da Peça e o Código."
            )


# =========================================================
# PEÇAS CADASTRADAS
# =========================================================

elif menu == "✨ Peças Cadastradas":

    st.markdown(
"""
<div class="page-title">
✨ Minha coleção
</div>

<div class="page-subtitle">
Consulte e pesquise todas as joias e acessórios cadastrados.
</div>
""",
unsafe_allow_html=True
)


    if df.empty:

        st.markdown(
"""
<div class="dark-card">

<h2>
💎 Nenhuma peça cadastrada
</h2>

<p>
Sua coleção ainda está vazia.
Cadastre sua primeira peça para começar.
</p>

</div>
""",
unsafe_allow_html=True
        )


    else:

        busca = st.text_input(
            "🔎 Pesquisar peça",
            placeholder="Digite nome, categoria, material, código ou cor..."
        )


        if busca:

            mascara = (
                df.astype(str)
                .apply(
                    lambda coluna:
                    coluna.str.contains(
                        busca,
                        case=False,
                        na=False,
                        regex=False
                    )
                )
                .any(axis=1)
            )

            df_filtrado = df[mascara]

        else:

            df_filtrado = df


        st.dataframe(
            df_filtrado,
            use_container_width=True,
            hide_index=True
        )


        st.markdown(
            "<br>",
            unsafe_allow_html=True
        )


        opcoes_pecas = df.index.tolist()


        peca_excluir = st.selectbox(
            "🗑️ Selecione uma peça para excluir",
            options=opcoes_pecas,
            format_func=lambda indice:
                f"{df.loc[indice, 'Nome']} - "
                f"{df.loc[indice, 'Código']}"
        )


        if st.button(
            "🗑️ EXCLUIR PEÇA"
        ):

            df = df.drop(
                peca_excluir
            )


            df = df.reset_index(
                drop=True
            )


            salvar_dados(df)


            st.success(
                "💎 Peça excluída com sucesso!"
            )


            st.rerun()


# =========================================================
# RODAPÉ
# =========================================================

st.markdown(
"""
<div class="footer">

💎 Maison Élégance<br>
Joias finas & acessórios

</div>
""",
unsafe_allow_html=True
)
