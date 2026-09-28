# SITIO Farmacovigilancia · Operaciones

Centro interno de operaciones de SITIO BioMedical Solutions.

## Ejecutar
```bash
pip install -r requirements.txt
streamlit run app.py
```

## Contraseña de demo
En Streamlit Cloud añada en **Settings > Secrets**:

```toml
APP_PASSWORD = "una-contraseña-larga"
```

La contraseña no debe guardarse en GitHub.

## Seguridad
Este repositorio es público y contiene únicamente código y datos ficticios. El bloqueo por contraseña es suficiente para una demo, no para datos reales de farmacovigilancia. Antes de producción se requiere autenticación robusta, autorización por roles, backend seguro, auditoría y almacenamiento privado.
