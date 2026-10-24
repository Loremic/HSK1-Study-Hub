import pandas as pd,json

df=pd.read_excel("HSK1_2026_vocaboli_ordine_di_studio.xlsx",sheet_name="Tutti in ordine di studio")

cards=[{
    "id":int(r["N. HSK"]),
    "order": int(r["N. studio"]),
    "phase": r["Fase"],
    "unit":r["Unità"],
    "hanzi":r["汉字 · Caratteri"],
    "pinyin":r["Pinyin"],
    "meaning_it":r["Significato italiano"],
    "example":{"zh":r["Esempio in cinese"],
        "pinyin":r["Pinyin frase"],
        "en":r["Traduzione esempio EN"]}
} for _,r in df.iterrows()]

with open("flashcards.json","w",encoding="utf-8") as f:
    json.dump(cards,f,ensure_ascii=False,indent=2)
    