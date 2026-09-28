import streamlit as st

st.set_page_config(
    page_title="SITIO-SurveillanceHelper · Operaciones",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.block-container {max-width: 1280px; padding-top: 1.4rem; padding-bottom: 3rem;}
[data-testid="stSidebar"] {border-right: 1px solid #E5E7EB;}
h1, h2, h3 {letter-spacing:-0.025em;}
.card {padding:17px 19px;border:1px solid #E5E7EB;border-radius:14px;background:white;margin:8px 0 12px;}
.red {padding:17px 19px;border:1px solid #E8B4AE;border-radius:14px;background:#FFF3F1;margin:8px 0;}
.amber {padding:17px 19px;border:1px solid #F0D28A;border-radius:14px;background:#FFF9E9;margin:8px 0;}
.green {padding:17px 19px;border:1px solid #BDE0C6;border-radius:14px;background:#F0FAF3;margin:8px 0;}
.muted {color:#667085;}
</style>
""", unsafe_allow_html=True)

clave = st.secrets.get("APP_PASSWORD", "")
if clave:
    if not st.session_state.get("autorizado", False):
        st.title("SITIO-SurveillanceHelper")
        st.subheader("Centro de Operaciones SITIO")
        entrada = st.text_input("Contraseña", type="password")
        if st.button("Entrar", type="primary"):
            if entrada == clave:
                st.session_state.autorizado = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta.")
        st.stop()
else:
    st.warning("DEMO PÚBLICA: no hay contraseña configurada. No utilice datos reales.")

if "entrada_convertida" not in st.session_state:
    st.session_state.entrada_convertida = False

clientes = [
    {"Cliente":"Demo Pharma Paraguay S.A.","Estado":"🔴 SITIO","BPFV":"Implementación 82%","RFV":"Designado","Próxima acción":"Revisar PGR"},
    {"Cliente":"Laboratorio Guaraní Demo","Estado":"🟠 TERCERO","BPFV":"Vigente","RFV":"Designado","Próxima acción":"Esperar documento"},
    {"Cliente":"Importadora Salud Demo","Estado":"🟢 OK","BPFV":"Vigente","RFV":"Designado","Próxima acción":"Ninguna"},
]

st.sidebar.markdown("## SITIO-SurveillanceHelper")
st.sidebar.caption("Centro de Operaciones SITIO")
pagina = st.sidebar.radio(
    "Operaciones",
    [
        "Centro de control",
        "Entradas de seguridad",
        "Casos",
        "BPFV y cumplimiento",
        "Soporte al RFV",
        "Informes y proyectos",
        "Vigilancia regulatoria",
        "Clientes",
    ],
)
st.sidebar.divider()
st.sidebar.caption("INTERNO SITIO · DEMO")

st.title("SITIO-SurveillanceHelper")
st.caption("SITIO BioMedical Solutions · Centro interno de operaciones")

if pagina == "Centro de control":
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Clientes", "30")
    c2.metric("🔴 Requieren SITIO", "2")
    c3.metric("🟠 Esperando tercero", "3")
    c4.metric("🟢 Sin acción", "25")

    st.subheader("Requiere intervención")
    st.markdown('<div class="red"><b>Demo Pharma · PGR GLUCOX</b><br>Revisar borrador y preparar envío al RFV.</div>', unsafe_allow_html=True)
    st.markdown('<div class="red"><b>Entrada de seguridad sin completar</b><br>Solicitar edad aproximada y evolución clínica al reportante.</div>', unsafe_allow_html=True)

    st.subheader("Esperando cliente / RFV / DINAVISA")
    st.markdown('<div class="amber"><b>Demo Pharma · FV-DEMO-004</b><br>Documento preparado por SITIO. Pendiente de revisión del RFV.</div>', unsafe_allow_html=True)

    st.subheader("Próximas obligaciones")
    st.dataframe(
        [
            {"Cliente":"Demo Pharma","Obligación":"Revisión BPFV","Fecha":"14/11/2026","Responsable":"SITIO"},
            {"Cliente":"Demo Pharma","Obligación":"PGR GLUCOX","Fecha":"30/11/2026","Responsable":"SITIO + RFV"},
            {"Cliente":"Laboratorio Guaraní","Obligación":"Revisión documental","Fecha":"05/12/2026","Responsable":"Cliente"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Entradas de seguridad":
    st.header("Entradas de seguridad")
    st.write("Todo lo que llegue por enlaces, QR, correo, WhatsApp u otros canales se concentra aquí para evaluación inicial.")

    st.markdown(
        """
        <div class="card">
        <b>NUEVA · Demo Pharma · MED-X 100 mg</b><br>
        <span class="muted">Origen: Visitador médico · Canal web</span><br><br>
        “El Dr. Pérez comentó que un paciente tuvo mareos y vómitos dos días después de iniciar MED-X.
        No tengo más información todavía.”
        </div>
        """,
        unsafe_allow_html=True,
    )

    a, b = st.columns(2)
    with a:
        st.subheader("Extracción inicial")
        st.write("**Producto:** MED-X 100 mg")
        st.write("**Evento mencionado:** mareos, vómitos")
        st.write("**Inicio:** aproximadamente 2 días tras inicio")
        st.write("**Reportante:** visitador médico")
    with b:
        st.subheader("Información que falta")
        st.write("• Identificador mínimo del paciente")
        st.write("• Edad o grupo etario")
        st.write("• Evolución / desenlace")
        st.write("• Datos de contacto del profesional, si disponibles")

    if st.button("Preparar solicitud de seguimiento", type="primary"):
        st.success("Demo: SITIO prepararía un mensaje corto al reportante solicitando únicamente los datos faltantes.")

    if st.button("Convertir en caso FV-DEMO-005"):
        st.session_state.entrada_convertida = True
        st.success("Entrada convertida en caso de demostración.")

elif pagina == "Casos":
    st.header("Casos de seguridad")
    st.warning("Demo con datos ficticios. No introducir datos reales de pacientes.")
    casos = [
        {"Caso":"FV-DEMO-004","Cliente":"Demo Pharma","Producto":"MED-X 100 mg","Estado":"Revisión RFV","Acción":"Esperar RFV"},
        {"Caso":"FV-DEMO-003","Cliente":"Demo Pharma","Producto":"CARDIOMAX 10 mg","Estado":"Cerrado","Acción":"Ninguna"},
    ]
    if st.session_state.entrada_convertida:
        casos.insert(0, {"Caso":"FV-DEMO-005","Cliente":"Demo Pharma","Producto":"MED-X 100 mg","Estado":"Seguimiento","Acción":"Solicitar datos"})
    st.dataframe(casos, use_container_width=True, hide_index=True)

    st.subheader("Flujo operativo")
    st.write("Entrada → Validación → Seguimiento → Procesamiento → Revisión RFV → Paso regulatorio → Evidencia → Cierre")

elif pagina == "BPFV y cumplimiento":
    st.header("BPFV y cumplimiento")
    st.dataframe(
        [
            {"Cliente":"Demo Pharma","BPFV":"82%","Estado":"Implementación","Próximo paso":"Completar expediente","Acción SITIO":"Sí"},
            {"Cliente":"Laboratorio Guaraní Demo","BPFV":"Vigente","Estado":"Mantenimiento","Próximo paso":"Revisión periódica","Acción SITIO":"No"},
            {"Cliente":"Importadora Salud Demo","BPFV":"Vigente","Estado":"Mantenimiento","Próximo paso":"Sin acción","Acción SITIO":"No"},
        ],
        use_container_width=True,
        hide_index=True,
    )

    st.subheader("Demo Pharma · componentes del sistema")
    st.dataframe(
        [
            {"Componente":"Responsables y organización","Estado":"🟢 Completo"},
            {"Componente":"Procedimientos","Estado":"🟢 Completo"},
            {"Componente":"Gestión de casos","Estado":"🟢 Operativo"},
            {"Componente":"Vigilancia y literatura","Estado":"🟢 Operativo"},
            {"Componente":"Evidencias / archivo","Estado":"🟠 En consolidación"},
            {"Componente":"Preparación expediente","Estado":"🟠 En curso"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Soporte al RFV":
    st.header("Soporte al RFV")
    st.write("SITIO prepara y filtra el trabajo; el RFV recibe únicamente lo que requiere revisión, aprobación o firma.")
    st.dataframe(
        [
            {"Cliente":"Demo Pharma","Asunto":"PGR GLUCOX","Acción RFV":"Revisar y aprobar","SITIO":"Documento preparado","Estado":"Pendiente"},
            {"Cliente":"Demo Pharma","Asunto":"FV-DEMO-004","Acción RFV":"Confirmar evaluación","SITIO":"Caso preparado","Estado":"Pendiente"},
            {"Cliente":"Laboratorio Guaraní","Asunto":"Revisión mensual","Acción RFV":"Ninguna","SITIO":"Completado","Estado":"Cerrado"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Informes y proyectos":
    st.header("Informes y proyectos")
    st.dataframe(
        [
            {"Cliente":"Demo Pharma","Proyecto":"Implementación BPFV","Tipo":"BPFV","Progreso":"82%","Estado":"SITIO trabajando"},
            {"Cliente":"Demo Pharma","Proyecto":"PGR GLUCOX 5 mg","Tipo":"PGR","Progreso":"54%","Estado":"Preparación"},
            {"Cliente":"Importadora Salud","Proyecto":"Revisión regulatoria","Tipo":"Regulatorio","Progreso":"100%","Estado":"Completado"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Vigilancia regulatoria":
    st.header("Vigilancia regulatoria")
    st.write("SITIO revisa las novedades una vez y las cruza contra los productos de todos los clientes.")
    st.dataframe(
        [
            {"Fuente":"DINAVISA","Tema":"Nota de seguridad · ejemplo","Productos afectados":"2","Clientes afectados":"2","Acción":"Evaluar"},
            {"Fuente":"DINAVISA","Tema":"Cambio normativo · ejemplo","Productos afectados":"—","Clientes afectados":"5","Acción":"Planificar"},
            {"Fuente":"Literatura","Tema":"Nueva publicación de seguridad · ejemplo","Productos afectados":"1","Clientes afectados":"1","Acción":"Revisado"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Clientes":
    st.header("Clientes")
    st.dataframe(clientes, use_container_width=True, hide_index=True)
    st.caption("La operación se organiza por excepciones: SITIO dedica tiempo a los clientes que realmente requieren una acción.")

st.divider()
st.caption("SITIO BioMedical Solutions · SITIO-SurveillanceHelper · Demo con datos ficticios")
