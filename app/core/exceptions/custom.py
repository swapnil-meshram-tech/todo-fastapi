class AppError(Exception):
    def __init__(self, detail: str, status_code: int = 500):
        self.detail = detail
        self.status_code = status_code
        super().__init__(detail)


# class AppError(Exception):
#     status_code: int = 500

#     def __init__(self, detail: str):
#         self.detail = detail
#         super().__init__(detail)


# class NotFoundError(AppError):
#     status_code = 404


# class ConflictError(AppError):
#     status_code = 409
