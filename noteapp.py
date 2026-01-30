#!/usr/bin/env python3

from datetime import datetime
import os

note = input("Kaydetmek istedigin notu yaz: ")
today = datetime.now().strftime("%Y-%m-%d")

desktop_path = os.path.expanduser("~/Desktop")

file_name = f"{today}.txt"
file_path = os.path.join(desktop_path, file_name)

with open(file_path, "a") as file:
    file.write(note + "\n")

print(f"Not basariyla kaydedildi: {file_path}")
