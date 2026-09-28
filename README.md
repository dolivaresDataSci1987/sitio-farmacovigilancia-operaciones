# SITIO-SurveillanceHelper · Centro de Operaciones

Demo interna del modelo operativo de **SITIO-SurveillanceHelper**.

## Qué demuestra
- Gestión por excepción.
- Entradas de seguridad provenientes de enlaces/QR/canales.
- Evaluación inicial y seguimiento.
- Gestión de casos.
- BPFV y cumplimiento.
- Soporte al RFV.
- PGR / IPS / PSUR y proyectos.
- Vigilancia regulatoria.
- Vista consolidada de clientes.

## Secrets de la demo
En Streamlit Cloud > Settings > Secrets:

```toml
APP_PASSWORD = "una-contraseña-larga"
```

## Ejecutar localmente
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Seguridad
Esta demo usa únicamente información ficticia. El bloqueo por contraseña no sustituye autenticación, roles, auditoría, cifrado y aislamiento de datos necesarios antes de trabajar con información real de farmacovigilancia.
