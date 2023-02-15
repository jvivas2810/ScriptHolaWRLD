import requests
from bs4 import BeautifulSoup

# Define tus credenciales
username = "Proyect0912673"
email = "gilgorgee@gmail.com"
password = "proyect@14"

# Haz una solicitud a la página de registro de Aliexpress
registration_url = "https://login.aliexpress.com/?spm=a2g0o.ae-error.0.0.5468697dSyEgwB&return=https%3A%2F%2Fwww.aliexpress.com%2Fp%2Ferror%2F404.html&from=lighthouse&random=56FFABF15537B14310BE2DD8F66BEBA8"
registration_page = requests.get(registration_url)

# Analiza el código fuente y encuentra los formularios de registro
soup = BeautifulSoup(registration_page.content, "html.parser")
registration_form = soup.find("form", {"id": "register-form"})

# Llena los formularios con tus credenciales y haz una solicitud para enviarlos
form_data = {
    "loginId": username,
    "email": email,
    "password": password,
    "checkPassword": password
}
post_response = requests.post(registration_url, data=form_data)

# Verifica la respuesta para verificar que la cuenta se haya creado correctamente
if post_response.status_code == 200:
    print("Cuenta creada correctamente.")
else:
    print("Error al crear la cuenta.")
