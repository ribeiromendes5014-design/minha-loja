# Minha Loja (Drive)

App Streamlit conectado ao Google Drive para gerenciar **Produtos** e **Vendas**.

## Secrets (Streamlit Cloud → App settings → Secrets)

```toml
DRIVE_FOLDER_ID = "SEU_FOLDER_ID_DO_DRIVE"

[gcp_service_account]
type = "service_account"
project_id = "xxx"
private_key_id = "xxx"
private_key = "-----BEGIN PRIVATE KEY-----\n...linhas...\n-----END PRIVATE KEY-----\n"
client_email = "xxx@xxx.iam.gserviceaccount.com"
client_id = "123"
auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
client_x509_cert_url = "https://www.googleapis.com/robot/v1/metadata/x509/xxx"
```

## Rodar local
```
pip install -r requirements.txt
streamlit run app.py
```
