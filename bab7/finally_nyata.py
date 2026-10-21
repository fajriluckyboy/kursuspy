#!/usr/bin/env python3
"""Pemakaian nyata finally: menutup file dan memulihkan direktori kerja."""

import os


def tulis_lalu_error():
    """Menulis ke file, memicu error, tetapi file tetap ditutup."""
    berkas = open("log_finally.txt", "w", encoding="utf-8")
    try:
        berkas.write("Catatan sebelum error\n")
        print(1 / 0)
    finally:
        berkas.close()
        print("File tertutup?", berkas.closed)


def masuk_folder_lalu_error():
    """Pindah folder, memicu error, tetapi direktori kerja dipulihkan."""
    awal = os.getcwd()
    os.makedirs("folder_sementara", exist_ok=True)
    os.chdir("folder_sementara")
    try:
        print("Di dalam:", os.path.basename(os.getcwd()))
        print(1 / 0)
    finally:
        os.chdir(awal)
        print("Dipulihkan ke:", os.path.basename(os.getcwd()))


def main():
    """Alur utama program."""
    try:
        tulis_lalu_error()
    except ZeroDivisionError:
        print("Error 1 ditangani di main")

    try:
        masuk_folder_lalu_error()
    except ZeroDivisionError:
        print("Error 2 ditangani di main")


if __name__ == "__main__":
    main()
