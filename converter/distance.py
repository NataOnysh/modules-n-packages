# meters = feet * 0.3048
# feet = meters / 0.3048

def m_to_ft(distance: int) -> int:
    return distance / 0.3048


def ft_to_m(distance: int) -> int:
    return distance * 0.3048
