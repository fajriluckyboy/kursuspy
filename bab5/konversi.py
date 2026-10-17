"""Modul konversi satuan sederhana."""


def celsius_ke_fahrenheit(c):
    """Mengubah suhu Celsius ke Fahrenheit."""
    return c * 9 / 5 + 32


def fahrenheit_ke_celsius(f):
    """Mengubah suhu Fahrenheit ke Celsius."""
    return (f - 32) * 5 / 9


def km_ke_mil(km):
    """Mengubah kilometer ke mil."""
    return km * 0.621371


def mil_ke_km(mil):
    """Mengubah mil ke kilometer."""
    return mil / 0.621371
