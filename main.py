tasks = []

while True:
    print("\nSeçenekler:")
    print("1. Görev Ekle")
    print("2. Görevleri Görüntüle")
    print("3. Görev Sil")
    print("4. Çıkış")

    secim = input("Seçiminizi yapınız (1/2/3/4): ")

    if secim == "1":
        gorev = input("Görev giriniz: ")
        tasks.append(gorev)
        print("Görev başarıyla eklendi!")

    elif secim == "2":
        if len(tasks) == 0:
            print("Listeye henüz görev eklenmemiştir.")
        else:
            print("\nGörevler:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

    elif secim == "3":
        if len(tasks) == 0:
            print("Listeye henüz görev eklenmemiştir.")
        else:
            print("\nGörevler:")
            for i, task in enumerate(tasks, start=1):
                print(f"{i}. {task}")

            silinecek_gorev = int(input("Silmek istediğiniz görev numarasını giriniz: "))

            if 1 <= silinecek_gorev <= len(tasks):
                silinen_gorev = tasks.pop(silinecek_gorev - 1)
                print(f"Görev başarıyla silindi: {silinen_gorev}")
            else:
                print("Geçersiz görev numarası.")

    elif secim == "4":
        print("Çıkış yapılıyor...")
        break

    else:
        print("Geçersiz seçim. Lütfen 1, 2, 3 veya 4 giriniz.")