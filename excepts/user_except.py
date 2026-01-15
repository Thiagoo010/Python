class UserError(Exception):
    pass


class UserAlreadyExistsError(UserError):
    pass


class UserNotFoundError(UserError):
    pass
