from PyQt5.QtWidgets import QStackedWidget
from ui.login_view import LoginView
from ui.main_view import MainView
from ui.estudiante_view import EstudianteView
from ui.docente_view import DocenteView
from services.auth_service import AuthService
from presenters.login_presenter import LoginPresenter

class AppShell(QStackedWidget):
    PAGE_LOGIN = 0
    PAGE_ADMIN = 1
    PAGE_ESTUDIANTE = 2
    PAGE_DOCENTE = 3

    def __init__(self):
        super().__init__()

        self.login_view = LoginView()
        self.admin_view = MainView()
        self.estudiante_view = EstudianteView()
        self.docente_view = DocenteView()

        self.auth_service = AuthService()

        self.login_presenter = LoginPresenter(
            view=self.login_view,
            auth=self.auth_service,
            on_success=self._navigate_by_role
        )

        self.addWidget(self.login_view)
        self.addWidget(self.admin_view)
        self.addWidget(self.estudiante_view)
        self.addWidget(self.docente_view)

        self.setCurrentIndex(self.PAGE_LOGIN)
        self.setWindowTitle("PyQt5 - MVP")
        self.resize(640, 400)

    def _navigate_by_role(self, role: str):
        if role == "admin":
            self.admin_view.set_welcome("Administrador")
            self.setCurrentIndex(self.PAGE_ADMIN)
        elif role == "estudiante":
            self.setCurrentIndex(self.PAGE_ESTUDIANTE)
        elif role == "maestro":
            self.setCurrentIndex(self.PAGE_DOCENTE)
