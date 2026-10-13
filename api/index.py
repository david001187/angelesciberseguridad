from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI(title="Ángeles Ciberseguridad - Solana Security Suite")

ANGELES = [
    {
        "id": "token",
        "icono": "🪙",
        "nombre": "Ángel Auditor de Tokens SPL",
        "descripcion": "Análisis en tiempo real de Mint Authority, Freeze Authority, concentración de Holders y detección avanzada de rugpulls.",
        "placeholder": "Ej: 7xKXtg2CW87d97TXJSDpbD5jBkheTqA83TZRuJosgAsU",
        "label_input": "Dirección del Token (Mint Address):",
        "btn_texto": "Auditar Token SPL"
    },
    {
        "id": "contract",
        "icono": "📜",
        "nombre": "Ángel Revisor de Contratos",
        "descripcion": "Inspección estática de programas Solana (Program ID), detección de funciones maliciosas y verificación de permisos 3D.",
        "placeholder": "Ej: TokenkegQfeZyiNwAJbNbGKPFXCWuBvf9Ss623VQ5DA",
        "label_input": "Program ID / Dirección del Contrato:",
        "btn_texto": "Analizar Contrato"
    },
    {
        "id": "web3",
        "icono": "🌐",
        "nombre": "Ángel Sec Web3",
        "descripcion": "Recon de seguridad de dApps, encabezados HTTP, análisis SSL/TLS y detección de sitios Phishing/Draining.",
        "placeholder": "https://dapp.ejemplo.solana.com",
        "label_input": "URL de la dApp o Sitio Web3:",
        "btn_texto": "Escanear dApp"
    }
]

@app.get("/", response_class=HTMLResponse)
def home():
    nav_tabs_html = ""
    tab_content_html = ""

    for index, angel in enumerate(ANGELES):
        active_class = "active" if index == 0 else ""
        show_class = "show active" if index == 0 else ""

        nav_tabs_html += f"""
        <li class="nav-item m-1">
            <button class="nav-link {active_class} px-4 py-3 fw-bold rounded-pill" id="{angel['id']}-tab" data-bs-toggle="tab" data-bs-target="#tab-{angel['id']}" type="button">
                {angel['icono']} {angel['nombre']}
            </button>
        </li>
        """

        tab_content_html += f"""
        <div class="tab-pane fade {show_class}" id="tab-{angel['id']}">
            <div class="card p-5 shadow-3d">
                <h3 class="neon-title mb-3">{angel['icono']} {angel['nombre']}</h3>
                <p class="text-light opacity-8 mb-4">{angel['descripcion']}</p>
                <div class="mb-4">
                    <label class="form-label text-yellow-neon fw-semibold">{angel['label_input']}</label>
                    <input type="text" class="form-control form-control-lg custom-input" placeholder="{angel['placeholder']}">
                </div>
                <button class="btn btn-neon w-100 py-3 text-uppercase fw-bold" onclick="alert('⚡ Ejecutando protocolo de seguridad de {angel['nombre']}...')">{angel['btn_texto']}</button>
            </div>
        </div>
        """

    return f"""
    <!DOCTYPE html>
    <html lang="es">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Ángeles Ciberseguridad | 3D Neon Suite 2027</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <style>
            :root {{
                --bg-deep: #050b18;
                --bg-card: #0a1628;
                --neon-blue: #00f3ff;
                --neon-yellow: #f3e600;
                --text-white: #ffffff;
                --shadow-blue: rgba(0, 243, 255, 0.35);
                --shadow-yellow: rgba(243, 230, 0, 0.4);
            }}

            body {{
                background-color: var(--bg-deep);
                background-image: 
                    radial-gradient(circle at 50% 10%, rgba(0, 243, 255, 0.1) 0%, transparent 60%),
                    radial-gradient(circle at 10% 90%, rgba(243, 230, 0, 0.05) 0%, transparent 50%);
                color: var(--text-white);
                font-family: 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;
                min-height: 100vh;
            }}

            .main-title {{
                color: var(--text-white);
                text-shadow: 0 0 15px var(--neon-blue), 0 0 30px var(--neon-blue);
                letter-spacing: 2px;
            }}

            .badge-sol {{
                background-color: #14F195;
                color: #000;
                box-shadow: 0 0 12px #14F195;
                font-weight: 900;
            }}

            /* Estilo 3D Neon para Tarjetas */
            .shadow-3d {{
                background-color: var(--bg-card);
                border: 2px solid rgba(0, 243, 255, 0.3);
                border-radius: 16px;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.8), 
                            0 0 20px rgba(0, 243, 255, 0.15),
                            inset 0 0 15px rgba(0, 243, 255, 0.05);
                transform: perspective(1000px) rotateX(1deg);
                transition: all 0.3s ease;
            }}
            .shadow-3d:hover {{
                transform: perspective(1000px) rotateX(0deg) translateY(-4px);
                box-shadow: 0 15px 40px rgba(0, 0, 0, 0.9), 
                            0 0 30px var(--shadow-blue);
                border-color: var(--neon-blue);
            }}

            .neon-title {{
                color: var(--text-white);
                text-shadow: 0 0 10px var(--shadow-blue);
            }}

            .text-yellow-neon {{
                color: var(--neon-yellow);
                text-shadow: 0 0 8px rgba(243, 230, 0, 0.5);
            }}

            /* Inputs 3D Neón */
            .custom-input {{
                background-color: #030810 !important;
                border: 2px solid rgba(0, 243, 255, 0.4) !important;
                color: #fff !important;
                border-radius: 10px;
                box-shadow: inset 0 2px 5px rgba(0,0,0,0.8);
                transition: all 0.3s ease;
            }}
            .custom-input:focus {{
                border-color: var(--neon-yellow) !important;
                box-shadow: 0 0 15px var(--shadow-yellow), inset 0 2px 5px rgba(0,0,0,0.8) !important;
            }}

            /* Pestañas Neón 3D */
            .nav-tabs {{
                border-bottom: none;
            }}
            .nav-tabs .nav-link {{
                background-color: #07111e;
                color: #a0aec0;
                border: 1px solid rgba(0, 243, 255, 0.2);
                box-shadow: 0 4px 10px rgba(0,0,0,0.5);
                transition: all 0.3s ease;
            }}
            .nav-tabs .nav-link:hover {{
                color: var(--neon-blue);
                border-color: var(--neon-blue);
                text-shadow: 0 0 8px var(--shadow-blue);
            }}
            .nav-tabs .nav-link.active {{
                background: linear-gradient(135deg, #0a1d37, #061122);
                color: var(--neon-yellow) !important;
                border: 2px solid var(--neon-yellow);
                box-shadow: 0 0 20px var(--shadow-yellow);
                text-shadow: 0 0 10px var(--shadow-yellow);
            }}

            /* Botón Neón 3D */
            .btn-neon {{
                background: linear-gradient(135deg, #00f3ff, #0077ff);
                color: #050b18;
                border: none;
                border-radius: 10px;
                box-shadow: 0 5px 20px var(--shadow-blue);
                letter-spacing: 1px;
                transition: all 0.3s ease;
            }}
            .btn-neon:hover {{
                background: linear-gradient(135deg, #f3e600, #ffb700);
                color: #050b18;
                box-shadow: 0 8px 25px var(--shadow-yellow);
                transform: translateY(-2px);
            }}
        </style>
    </head>
    <body class="py-5">
        <div class="container">
            <div class="text-center mb-5">
                <h1 class="main-title display-5 fw-bold mb-3">🛡️ ÁNGELES CIBERSEGURIDAD</h1>
                <p class="lead text-light">Plataforma Autónoma 3D Multicapa para el Ecosistema <span class="badge badge-sol px-3 py-1 rounded-pill">SOLANA</span></p>
            </div>

            <ul class="nav nav-tabs justify-content-center mb-5" id="angelTabs" role="tablist">
                {nav_tabs_html}
            </ul>

            <div class="tab-content row justify-content-center" id="angelTabsContent">
                <div class="col-lg-8">
                    {tab_content_html}
                </div>
            </div>

            <footer class="text-center mt-5 text-muted opacity-7">
                <small>© 2027 Ángeles Ciberseguridad | Crypto World's Fair Hackathon Edition</small>
            </footer>
        </div>

        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """
