from prsmsp.models.auth import APIKeyAuth, UnamePassAuth


class AuthFactory:
    """AuthFactory."""

    @staticmethod
    def get(auth_type: str):
        """Static method to get the class of authentication.

        :param auth_type:
        :type auth_type: str
        """
        pass
