from app.auth.interface_adapters.dtos.auth_response_dto import AuthResponseDTO


class AuthPresenter:
    @staticmethod
    def presenter_token(token: str) -> AuthResponseDTO:
        return AuthResponseDTO(access_token=token)
