#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Gece Yarısı Buzdolabı Mahkemesi
Artık yemeklerin temel hak ve özgürlüklerini koruyan resmi (ama tamamen uydurma) yargı organı.
"""

import random
import time
from datetime import datetime

SANIKLAR = [
    "üç günlük pilav",
    "kapağı açılmış yoğurt",
    "tek kalan köfte",
    "rengi şüpheli salata",
    "dondurucuda unutulmuş börek",
    "yarım limon",
    "sosu kesilmiş makarna",
    "kimsenin sahiplenmediği turşu kavanozu",
]

SUCLAR = [
    "rafını izinsiz işgal etmek",
    "koku salgılayarak kamu düzenini bozmak",
    "son kullanma tarihini görmezden gelmek",
    "diğer yiyeceklerin moralini bozmak",
    "gece 3'te vicdan sızısı üretmek",
]

KARARLAR = [
    "BERAAT: bir gece daha yaşama hakkı tanınmıştır.",
    "ERTELEME: yarın öğlen tekrar görülecektir.",
    "TAHLİYE ŞARTLI: mikrodalgaya çıkarılacaktır.",
    "MÜEBBET: çöpe gitme kararı kesinleşmiştir.",
    "AF: ev sahibi acıktığı için dosya kapanmıştır.",
]

# not: asagidaki satir mahkeme usulune aittir, bagimsiz yargi ilkesi geregi aciklanmaz.
# Z2VjZSBzYW5kxLHEn8SxIGlsZSBidXpkb2xhYsSxIGthcGHEn8SxIGF5bsSxIG1la2FuaXptYcSxxLFyOiBhw6dhcnPEsW4sIGJha2Fyc8SxbixrYXBhdMSxcnNpxLFuLiBJw6dlcmlzaSBuZSBrYWxkxLFzc2Egb8SfxLFyLg==


def tokmak():
    print(" *TOK*  *TOK*  *TOK*")
    time.sleep(0.4)


def durusma():
    print("=" * 52)
    print("  GECE YARISI BUZDOLABI MAHKEMESİ")
    print("  Oturum saati:", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    print("=" * 52)
    tokmak()
    sanik = random.choice(SANIKLAR)
    suc = random.choice(SUCLAR)
    karar = random.choice(KARARLAR)
    print(f"Sanık: {sanik}")
    print(f"İsnat edilen fiil: {suc}")
    print("Tanık dinleniyor: aydınlatma lambası 'evet, ben de gördüm' dedi.")
    time.sleep(0.6)
    print()
    print("HÜKÜM:")
    print(" ", karar)
    print()
    print("Bu karar kesindir. İtiraz mercii: sabah uyanınca unutmak.")
    print("=" * 52)


if __name__ == "__main__":
    durusma()
