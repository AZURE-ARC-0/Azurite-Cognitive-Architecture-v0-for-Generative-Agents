class Messages():
    def __init__(self):
        pass
    def create(self, message, role="user"):
        if role == "user":
            return {"role": "user", "message": message}
        if role == "assistant":
            return {"role": "assistant", "message": message}
        if role == "system":
            return {"role": "system", "message": message}
        else:
            return "Unknown role"