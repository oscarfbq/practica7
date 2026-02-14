from dataclasses import dataclass

@dataclass(frozen=True)
class AuthResult:
    ok: bool
    role: str = ""
    message: str = ""

class AuthService:
    """
    Servicio de autenticación. Hoy: validación estática.
    Mañana: cambiar por BD/API.
    """
    def __init__(self):
        self._users = {
            "admin": "1234",
            "estudiante": "1234",
            "maestro": "1234"
        }

    def login(self, username: str, password: str) -> AuthResult:
        if not username or not password:
            return AuthResult(False, message="Usuario y contraseña son requeridos.")

        username = username.lower()

        if username in self._users and self._users[username] == password:
            return AuthResult(True, role=username, message="Autenticación exitosa.")

        return AuthResult(False, message="Usuario o contraseña incorrectos.")
