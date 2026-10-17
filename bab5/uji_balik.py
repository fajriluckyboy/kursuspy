import konversi as k

suhu_f = k.celsius_ke_fahrenheit(37)
print("37 C =", suhu_f, "F")
print("Kembali ke C =", k.fahrenheit_ke_celsius(suhu_f))

jarak_mil = k.km_ke_mil(42)
print("42 km =", jarak_mil, "mil")
print("Kembali ke km =", k.mil_ke_km(jarak_mil))
