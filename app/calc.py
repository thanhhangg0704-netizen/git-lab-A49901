def add(a: float, b: float) -> float:
    """Cong hai so a va b."""
    return a + b


def sub(a: float, b: float) -> float:
    """Tru so b tu a."""
    return a - b


def mul(a: float, b: float) -> float:
    """Nhan hai so a va b."""
    return a * b


def div(a: float, b: float) -> float:
    """Chia a cho b."""
    if b == 0:
        raise ValueError("Loi: chia cho 0")
    return a / b

