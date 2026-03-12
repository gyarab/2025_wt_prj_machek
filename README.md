# Pára

Pára je webová aplikace sloužící jako komunitní databáze videoher, inspirovaná platformou Steam. Jejím cílem je umožnit uživatelům procházet, hodnotit a komentovat videohry, přičemž každá hra je detailně popsána prostřednictvím strukturovaných dat z více propojených databázových entit.
Jádrem aplikace je hra, která je charakterizována názvem, popisem, datem vydání, cenou a náhledovými snímky obrazovky. Každá hra náleží do jednoho nebo více žánrů (např. RPG, FPS, strategie, simulace) a je spojena s jedním nebo více vývojáři a vydavateli. Hra může být dostupná na více platformách (PC, PlayStation, Xbox, Nintendo Switch aj.).

Aplikace eviduje uživatelské recenze, které sestávají z textového hodnocení a numerického skóre (1–10). Každá recenze je vázána na konkrétního registrovaného uživatele a konkrétní hru. Uživatelé mohou na recenze reagovat prostřednictvím komentářů. Aplikace dále vypočítává průměrné hodnocení ze všech recenzí zanechané pod konkrétní hrou.
Pro lepší navigaci slouží systém tagů, které uživatelé přiřazují hrám. Aplikace také umožňuje tvorbu osobních herních knihoven a wishlistů, kde si registrovaný uživatel eviduje hry, které vlastní nebo chce získat.
Role uživatelů
Aplikace rozlišuje tři základní role:

- Anonymní návštěvník může procházet katalog her, číst <u>detailní stránky her</u>, prohlížet recenze ostatních uživatelů a vyhledávat hry podle názvu, žánru, platformy nebo tagu.
- Registrovaný uživatel disponuje navíc možností psát vlastní recenze, přidávat komentáře k recenzím jiných uživatelů, spravovat svou osobní knihovnu a wishlist, hodnotit recenze ostatních (helpful/not helpful) a spravovat svůj <u>uživatelský profil</u>.
- Administrátor má přístup k administračnímu rozhraní, kde spravuje katalog her (přidávání, editace, mazání záznamů), spravuje uživatelské účty, moderuje recenze a komentáře a spravuje číselníky žánrů, platforem a tagů.

Technický kontext
Datový model aplikace zahrnuje minimálně tyto entity: Game, Developer, Publisher, Genre, Platform, Tag, User, Review, Comment, Library, Wishlist. Mezi entitami existují vztahy 1:N (hra–recenze, uživatel–recenze) i M:N (hra–žánr, hra–platforma, hra–tag), což zaručuje dostatečnou komplexitu databázové struktury vhodnou pro výukové účely v oblasti návrhu relačních databází a tvorby webových aplikací.
![erddiagram](https://github.com/user-attachments/assets/534ff3d6-9d4a-4f1f-8619-79a401f986fb)
![Userflow](https://github.com/user-attachments/assets/afe5759e-cff7-466b-8bce-babe5f73aa3c)
![Wireframe1](https://github.com/user-attachments/assets/c7d0156a-8625-4ffd-97aa-e108e91506b9)
![Wireframe2](https://github.com/user-attachments/assets/f5505819-2ed7-432a-ad99-7595cbe76e39)
