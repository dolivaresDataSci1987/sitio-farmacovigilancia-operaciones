import streamlit as st

st.set_page_config(
    page_title="SITIO Farmacovigilancia · Operaciones",
    page_icon="⚙️",
    layout="wide",
    initial_sidebar_state="expanded",
)

st.markdown("""
<style>
.block-container {max-width: 1250px; padding-top: 1.5rem; padding-bottom: 3rem;}
[data-testid="stSidebar"] {border-right: 1px solid #e9ecef;}
.alerta {padding:16px 18px;border-radius:14px;border:1px solid #efb7b0;background:#fff4f2;margin:.5rem 0;}
.espera {padding:16px 18px;border-radius:14px;border:1px solid #f0cf7a;background:#fff9e8;margin:.5rem 0;}
.ok {padding:16px 18px;border-radius:14px;border:1px solid #b7dfc3;background:#f1fbf4;margin:.5rem 0;}
</style>
""", unsafe_allow_html=True)

# Protección simple para la DEMO.
# En Streamlit Cloud, defina APP_PASSWORD en Settings > Secrets.
clave = st.secrets.get("APP_PASSWORD", "")
if clave:
    if "autorizado" not in st.session_state:
        st.session_state.autorizado = False
    if not st.session_state.autorizado:
        st.title("SITIO Farmacovigilancia")
        st.subheader("Acceso interno")
        entrada = st.text_input("Contraseña", type="password")
        if st.button("Entrar", type="primary"):
            if entrada == clave:
                st.session_state.autorizado = True
                st.rerun()
            else:
                st.error("Contraseña incorrecta.")
        st.stop()
else:
    st.warning("DEMO PÚBLICA: no hay contraseña configurada. No use datos reales.")

clientes = [
    {"cliente":"Demo Pharma Paraguay S.A.","estado":"🔴 SITIO","bpfv":"En implementación","rfv":"Designado","accion":"Revisar PGR"},
    {"cliente":"Laboratorio Guaraní Demo","estado":"🟠 CLIENTE","bpfv":"Vigente","rfv":"Designado","accion":"Esperar documento"},
    {"cliente":"Importadora Salud Demo","estado":"🟢 OK","bpfv":"Vigente","rfv":"Designado","accion":"Ninguna"},
]
obligaciones = [
    {"cliente":"Demo Pharma Paraguay S.A.","tipo":"BPFV","fecha":"14/11/2026","estado":"En curso","responsable":"SITIO"},
    {"cliente":"Demo Pharma Paraguay S.A.","tipo":"PGR GLUCOX","fecha":"30/11/2026","estado":"En curso","responsable":"SITIO + RFV"},
    {"cliente":"Laboratorio Guaraní Demo","tipo":"Revisión documental","fecha":"05/12/2026","estado":"Esperando cliente","responsable":"Cliente"},
]
casos = [
    {"caso":"FV-DEMO-004","cliente":"Demo Pharma Paraguay S.A.","producto":"MED-X 100 mg","estado":"Revisión RFV","prioridad":"Alta"},
]
solicitudes = [
    {"id":"SOL-0042","cliente":"Demo Pharma Paraguay S.A.","tipo":"DINAVISA me pidió algo","estado":"Nueva"},
    {"id":"SOL-0041","cliente":"Laboratorio Guaraní Demo","tipo":"Soporte RFV","estado":"En revisión"},
]

st.sidebar.markdown("## ⚙️ SITIO")
st.sidebar.caption("Centro de Operaciones")
pagina = st.sidebar.radio(
    "Ir a",
    ["Centro de control", "Clientes", "BPFV", "Soporte RFV", "Casos", "Proyectos", "Vigilancia regulatoria", "Solicitudes"],
)
st.sidebar.divider()
st.sidebar.caption("INTERNO SITIO · DEMO")

st.title("SITIO Farmacovigilancia")
st.caption("Centro interno de operaciones")

if pagina == "Centro de control":
    a,b,c,d = st.columns(4)
    a.metric("Clientes", "30")
    b.metric("🔴 Requieren SITIO", "2")
    c.metric("🟠 Esperando tercero", "3")
    d.metric("🟢 Sin acción", "25")

    st.subheader("Requiere intervención de SITIO")
    st.markdown('<div class="alerta"><b>Demo Pharma · PGR GLUCOX</b><br>Revisar borrador y preparar envío al RFV.</div>', unsafe_allow_html=True)
    st.markdown('<div class="alerta"><b>Demo Pharma · BPFV</b><br>Completar expediente de presentación.</div>', unsafe_allow_html=True)

    st.subheader("Esperando cliente / RFV / DINAVISA")
    st.markdown('<div class="espera"><b>Laboratorio Guaraní Demo</b><br>Esperando documento solicitado al cliente.</div>', unsafe_allow_html=True)

    with st.expander("🟢 25 clientes sin acción"):
        st.write("El sistema no requiere tiempo operativo de SITIO en este momento.")

    st.subheader("Próximos vencimientos y obligaciones")
    st.dataframe(obligaciones, use_container_width=True, hide_index=True)

elif pagina == "Clientes":
    st.header("Clientes")
    st.dataframe(clientes, use_container_width=True, hide_index=True)

elif pagina == "BPFV":
    st.header("Gestión de BPFV")
    st.write("Implementaciones, renovaciones, evidencias, acciones correctivas y seguimiento.")
    st.dataframe(
        [
            {"cliente":"Demo Pharma Paraguay S.A.","estado":"Implementación 82%","constancia":"Pendiente","próximo paso":"Presentación DINAVISA"},
            {"cliente":"Laboratorio Guaraní Demo","estado":"Vigente","constancia":"Disponible","próximo paso":"Revisión periódica"},
            {"cliente":"Importadora Salud Demo","estado":"Vigente","constancia":"Disponible","próximo paso":"Sin acción"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Soporte RFV":
    st.header("Soporte al Responsable de Farmacovigilancia")
    st.write("Trabajo preparado por SITIO que requiere revisión, aprobación o firma del RFV.")
    st.dataframe(
        [
            {"cliente":"Demo Pharma Paraguay S.A.","asunto":"PGR GLUCOX","acción RFV":"Revisar y aprobar","estado":"Pendiente"},
            {"cliente":"Demo Pharma Paraguay S.A.","asunto":"FV-DEMO-004","acción RFV":"Confirmar evaluación","estado":"Pendiente"},
            {"cliente":"Laboratorio Guaraní Demo","asunto":"Revisión mensual","acción RFV":"Ninguna","estado":"Completado"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Casos":
    st.header("Casos de seguridad")
    st.warning("Demo pública. No introduzca datos reales de pacientes.")
    st.dataframe(casos, use_container_width=True, hide_index=True)

elif pagina == "Proyectos":
    st.header("Proyectos de farmacovigilancia")
    st.dataframe(
        [
            {"cliente":"Demo Pharma Paraguay S.A.","proyecto":"Implementación BPFV","progreso":"82%","estado":"SITIO trabajando"},
            {"cliente":"Demo Pharma Paraguay S.A.","proyecto":"PGR GLUCOX","progreso":"54%","estado":"Preparación"},
            {"cliente":"Importadora Salud Demo","proyecto":"Revisión regulatoria","progreso":"100%","estado":"Completado"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Vigilancia regulatoria":
    st.header("Vigilancia regulatoria")
    st.write("Alertas y cambios normativos que deben cruzarse con el portafolio de los clientes.")
    st.dataframe(
        [
            {"fuente":"DINAVISA","tema":"Nota de seguridad · Demo","afecta":"2 clientes","estado":"Revisar"},
            {"fuente":"DINAVISA","tema":"Actualización normativa · Demo","afecta":"5 clientes","estado":"Evaluado"},
        ],
        use_container_width=True,
        hide_index=True,
    )

elif pagina == "Solicitudes":
    st.header("Solicitudes recibidas")
    st.dataframe(solicitudes, use_container_width=True, hide_index=True)

st.divider()
st.caption("SITIO BioMedical Solutions · Centro de Operaciones · Demo con datos ficticios")
