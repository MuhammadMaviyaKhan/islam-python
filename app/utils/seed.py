from app import db
from app.models.content import (
    QuranVerse, Hadith, Kalma, NamazGuide, Dua, Ziyarat,
    Category, IslamicEvent, Article, Page
)


def seed_data():
    if Kalma.query.first():
        return

    kalmas = [
        {
            "title": "Shia Kalma (Kalma Tayyaba)",
            "slug": "shia-kalma",
            "arabic": "لَا إِلٰهَ إِلَّا اللَّهُ مُحَمَّدٌ رَسُولُ اللَّهِ عَلِيٌّ وَلِيُّ اللَّهِ",
            "urdu": "اللہ کے سوا کوئی معبود نہیں، محمد اللہ کے رسول ہیں، علی اللہ کے ولی ہیں",
            "english": "There is no god but Allah, Muhammad is the Messenger of Allah, Ali is the Vicegerent of Allah",
            "transliteration": "La ilaha illallah Muhammadur Rasulullah Aliyun Waliullah",
            "reference": "Based on Quran (3:18) and authentic Shia hadith (Usul al-Kafi, Vol. 1, p. 419)"
        },
        {
            "title": "Kalma Shahadat",
            "slug": "kalma-shahadat",
            "arabic": "أَشْهَدُ أَنْ لَا إِلٰهَ إِلَّا اللَّهُ وَأَشْهَدُ أَنَّ مُحَمَّدًا رَسُولُ اللَّهِ وَأَشْهَدُ أَنَّ عَلِيًّا وَلِيُّ اللَّهِ",
            "urdu": "میں گواہی دیتا ہوں کہ اللہ کے سوا کوئی معبود نہیں اور میں گواہی دیتا ہوں کہ محمد اللہ کے رسول ہیں اور میں گواہی دیتا ہوں کہ علی اللہ کے ولی ہیں",
            "english": "I bear witness that there is no god but Allah, and I bear witness that Muhammad is the Messenger of Allah, and I bear witness that Ali is the Vicegerent of Allah",
            "transliteration": "Ashhadu an la ilaha illallah wa ashhadu anna Muhammadan Rasulullah wa ashhadu anna Aliyyan Waliullah",
            "reference": "Shia fiqh (Taharat and Salah chapters)"
        },
    ]

    for k in kalmas:
        db.session.add(Kalma(**k))

    duas_data = [
        {
            "title": "Dua Kumayl",
            "slug": "dua-kumayl",
            "arabic": "اللَّهُمَّ إِنِّي أَسْأَلُكَ بِرَحْمَتِكَ الَّتِي وَسِعَتْ كُلَّ شَيْءٍ...",
            "urdu": "اے میرے اللہ! میں تجھ سے سوال کرتا ہوں تیری اس رحمت کے واسطے سے جو ہر چیز کو گھیرے ہوئے ہے...",
            "english": "O Allah, I ask You by Your mercy which encompasses all things...",
            "transliteration": "Allahumma inni as'aluka birahmatika allati wasi'at kulla shay...",
            "reference": "Narrated by Imam Ali (AS) to Kumayl ibn Ziyad (Mafatih al-Jinan)",
            "is_published": True
        },
        {
            "title": "Dua Tawassul",
            "slug": "dua-tawassul",
            "arabic": "اللَّهُمَّ إِنِّي أَتَوَجَّهُ إِلَيْكَ بِنَبِيِّكَ نَبِيِّ الرَّحْمَةِ...",
            "urdu": "اے اللہ! میں تیری طرف متوجہ ہوتا ہوں تیرے نبی، رحمت کے نبی کے واسطے سے...",
            "english": "O Allah, I turn to You through Your Prophet, the Prophet of Mercy...",
            "transliteration": "Allahumma inni atawajjahu ilayka binabiyyika nabiyyir rahma...",
            "reference": "Narrated from the Imams (AS) (Mafatih al-Jinan, Bihar al-Anwar Vol. 99)",
            "is_published": True
        },
        {
            "title": "Dua Ahad",
            "slug": "dua-ahad",
            "arabic": "اللَّهُمَّ رَبَّ النُّورِ الْعَظِيمِ...",
            "urdu": "اے اللہ! عظیم نور کے پروردگار...",
            "english": "O Allah, Lord of the Great Light...",
            "transliteration": "Allahumma rabban nooril azeem...",
            "reference": "Narrated from Imam al-Sadiq (AS) (Mafatih al-Jinan)",
            "is_published": True
        },
        {
            "title": "Dua Faraj (Dua Imam Zaman)",
            "slug": "dua-faraj",
            "arabic": "إِلَهِي عَظُمَ الْبَلَاءُ وَبَرِحَ الْخَفَاءُ...",
            "urdu": "اے میرے معبود! مصیبت عظیم ہو گئی اور راز فاش ہو گیا...",
            "english": "My God, the affliction has become great and the secret has been disclosed...",
            "transliteration": "Ilahi azumal bala wa barahalkhafa...",
            "reference": "Narrated from Imam al-Asr (ATFS) (Mafatih al-Jinan, Iqbal al-A'mal)",
            "is_published": True
        },
        {
            "title": "Dua Iftitah",
            "slug": "dua-iftitah",
            "arabic": "اللَّهُمَّ إِنِّي أَفْتَتِحُ الثَّنَاءَ بِحَمْدِكَ...",
            "urdu": "اے اللہ! میں تیری حمد کے ساتھ ثنا کا آغاز کرتا ہوں...",
            "english": "O Allah, I open praise with Your praise...",
            "transliteration": "Allahumma inni aftatihus sana bihamdik...",
            "reference": "Narrated from Imam al-Mahdi (ATFS) (Mafatih al-Jinan)",
            "is_published": True
        },
        {
            "title": "Dua Jawshan Kabir",
            "slug": "dua-jawshan-kabir",
            "arabic": "بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ...",
            "urdu": "شروع اللہ کے نام سے جو بڑا مہربان نہایت رحم والا ہے...",
            "english": "In the Name of Allah, the All-Beneficent, the All-Merciful...",
            "transliteration": "Bismillahir Rahmanir Rahim...",
            "reference": "Narrated from Prophet Muhammad (SAWW) (Mafatih al-Jinan)",
            "is_published": True
        },
    ]

    for d in duas_data:
        db.session.add(Dua(**d))

    ziyarat_data = [
        {
            "title": "Ziyarat Ashura",
            "slug": "ziyarat-ashura",
            "arabic": "السَّلَامُ عَلَيْكَ يَا أَبَا عَبْدِ اللَّهِ...",
            "urdu": "آپ پر سلام ہو اے ابو عبد اللہ!...",
            "english": "Peace be upon you, O Abu Abdullah!...",
            "transliteration": "Assalamu alayka ya Aba Abdillah...",
            "reference": "Narrated from Imam al-Baqir (AS) (Mafatih al-Jinan, Kamil al-Ziyarat)",
            "is_published": True
        },
        {
            "title": "Ziyarat Waritha",
            "slug": "ziyarat-waritha",
            "arabic": "السَّلَامُ عَلَيْكَ يَا وَارِثَ آدَمَ صَفْوَةِ اللَّهِ...",
            "urdu": "آپ پر سلام ہو اے آدم کے وارث، جو اللہ کے برگزیدہ تھے...",
            "english": "Peace be upon you, O inheritor of Adam, the Chosen of Allah...",
            "transliteration": "Assalamu alayka ya waritha Adama safwatillah...",
            "reference": "Narrated from Imam al-Sadiq (AS) (Mafatih al-Jinan, Kamil al-Ziyarat)",
            "is_published": True
        },
        {
            "title": "Ziyarat Aminullah",
            "slug": "ziyarat-aminullah",
            "arabic": "السَّلَامُ عَلَيْكَ يَا أَمِينَ اللَّهِ فِي أَرْضِهِ...",
            "urdu": "آپ پر سلام ہو اے اللہ کے امین اس کی زمین میں...",
            "english": "Peace be upon you, O Trustee of Allah on His earth...",
            "transliteration": "Assalamu alayka ya aminallahi fi ardihi...",
            "reference": "Narrated from Imam al-Sadiq (AS) (Mafatih al-Jinan)",
            "is_published": True
        },
        {
            "title": "Ziyarat Jamia Kabira",
            "slug": "ziyarat-jamia-kabira",
            "arabic": "السَّلَامُ عَلَيْكُمْ يَا أَهْلَ بَيْتِ النُّبُوَّةِ...",
            "urdu": "آپ سب پر سلام ہو اے اہل بیت نبوت...",
            "english": "Peace be upon you all, O People of the House of Prophethood...",
            "transliteration": "Assalamu alaykum ya ahlabaytin nubuwwah...",
            "reference": "Narrated from Imam Ali al-Hadi (AS) (Mafatih al-Jinan, Uyun Akhbar al-Ridha)",
            "is_published": True
        },
        {
            "title": "Ziyarat Aal Yaseen",
            "slug": "ziyarat-aal-yaseen",
            "arabic": "السَّلَامُ عَلَيْكَ يَا سَلِيلَ الْأَنْبِيَاءِ...",
            "urdu": "آپ پر سلام ہو اے انبیاء کی نسل سے...",
            "english": "Peace be upon you, O descendant of the Prophets...",
            "transliteration": "Assalamu alayka ya salilal ambiya...",
            "reference": "Narrated from Imam al-Mahdi (ATFS) (Mafatih al-Jinan)",
            "is_published": True
        },
    ]

    for z in ziyarat_data:
        db.session.add(Ziyarat(**z))

    namaz_data = [
        {
            "name": "Fajr Prayer",
            "slug": "fajr",
            "prayer_type": "daily",
            "rakats": "2 (Fard)",
            "purpose": "Dawn prayer; marks the beginning of the day with remembrance of Allah",
            "steps": "1. Make Niyyah (intention)\n2. Takbirat al-Ihram (say Allahu Akbar)\n3. Recite Surah al-Fatiha\n4. Recite another Surah (e.g., Surah al-Ikhlas)\n5. Say Allahu Akbar and go into Ruku (bowing)\n6. Stand up (Qiyam)\n7. Go into Sajdah (prostration) x2\n8. Stand for second Rakat and repeat\n9. Recite Tashahhud\n10. Recite Salam",
            "tasbihat": "Subhanallah (33x), Alhamdulillah (33x), Allahu Akbar (33x) after prayer",
            "tashahhud": "Ashhadu an la ilaha illallah wahdahu la sharika lah...",
            "salam": "Assalamu alaykum wa rahmatullahi wa barakatuh",
            "arabic": "صَلَاةُ الْفَجْرِ",
            "is_published": True
        },
        {
            "name": "Zuhr Prayer",
            "slug": "zuhr",
            "prayer_type": "daily",
            "rakats": "4 (Fard) + 8 (Nafilah)",
            "purpose": "Noon prayer; mid-day remembrance",
            "steps": "1. Niyyah\n2. Takbirat al-Ihram\n3. Recite Fatiha + Surah x2 (in each of first 2 rakats)\n4. In 3rd and 4th rakats, recite Fatiha only\n5. Ruku, Sujud, Tashahhud, Salam as per standard method",
            "is_published": True
        },
        {
            "name": "Asr Prayer",
            "slug": "asr",
            "prayer_type": "daily",
            "rakats": "4 (Fard)",
            "purpose": "Afternoon prayer",
            "steps": "Same method as Zuhr prayer but with different timing",
            "is_published": True
        },
        {
            "name": "Maghrib Prayer",
            "slug": "maghrib",
            "prayer_type": "daily",
            "rakats": "3 (Fard) + 4 (Nafilah)",
            "purpose": "Evening prayer after sunset",
            "steps": "1. Niyyah\n2. Takbirat al-Ihram\n3. Recite Fatiha + Surah in first 2 rakats\n4. In 3rd rakat, recite Fatiha, Ruku, Sujud\n5. Recite Tashahhud and Salam",
            "is_published": True
        },
        {
            "name": "Isha Prayer",
            "slug": "isha",
            "prayer_type": "daily",
            "rakats": "4 (Fard) + 2 (Nafilah)",
            "purpose": "Night prayer",
            "steps": "Same as Zuhr/Asr method but performed at night",
            "is_published": True
        },
        {
            "name": "Jumuah Prayer",
            "slug": "jumuah",
            "prayer_type": "weekly",
            "rakats": "2 (Fard, in congregation)",
            "purpose": "Friday congregational prayer replacing Zuhr on Fridays",
            "steps": "1. Listen to two sermons (Khutbah)\n2. Pray 2 rakats Fard in congregation\n3. Follow Imam in all actions",
            "is_published": True
        },
        {
            "name": "Eid ul-Fitr Prayer",
            "slug": "eid-ul-fitr",
            "prayer_type": "eid",
            "rakats": "2",
            "purpose": "Prayer on the day of Eid ul-Fitr",
            "steps": "1. Niyyah\n2. Takbirat al-Ihram\n3. 5 Takbirs in first rakat, with Qunut after each\n4. Recite Fatiha + Surah\n5. Ruku, Sujud\n6. 4 Takbirs in second rakat with Qunuts",
            "is_published": True
        },
        {
            "name": "Eid ul-Adha Prayer",
            "slug": "eid-ul-adha",
            "prayer_type": "eid",
            "rakats": "2",
            "purpose": "Prayer on the day of Eid ul-Adha",
            "steps": "Same as Eid ul-Fitr prayer",
            "is_published": True
        },
        {
            "name": "Tahajjud Prayer",
            "slug": "tahajjud",
            "prayer_type": "nafilah",
            "rakats": "11 (8 Nafilah + 2 Shaf'a + 1 Witr)",
            "purpose": "Night vigil prayer; highly recommended",
            "steps": "1. Pray 8 rakats in pairs of 2\n2. Pray 2 rakats of Shaf'a\n3. Pray 1 rakat of Witr\n4. Recite Qunut in Witr with Istighfar",
            "is_published": True
        },
        {
            "name": "Namaz-e-Ayat",
            "slug": "namaz-e-ayat",
            "prayer_type": "obligatory",
            "rakats": "2 (each with 5 Ruku)",
            "purpose": "Prayer during solar/lunar eclipse, earthquake, or natural phenomena",
            "steps": "1. Niyyah\n2. Takbirat al-Ihram\n3. Recite Fatiha + Surah, then Ruku\n4. Stand, recite Fatiha + Surah, Ruku (repeat 5 times)\n5. Perform 2 Sajdahs\n6. Second rakat same as first\n7. Tashahhud and Salam",
            "is_published": True
        },
        {
            "name": "Namaz-e-Janaza",
            "slug": "namaz-e-janaza",
            "prayer_type": "obligatory",
            "rakats": "5 Takbirs (no Ruku or Sujud)",
            "purpose": "Funeral prayer for deceased Muslim",
            "steps": "1. Make Niyyah\n2. First Takbir: Recite Surah al-Fatiha\n3. Second Takbir: Send blessings on Prophet and his family\n4. Third Takbir: Pray for believers\n5. Fourth Takbir: Pray for the deceased\n6. Fifth Takbir: Salam",
            "is_published": True
        },
    ]

    for n in namaz_data:
        if not NamazGuide.query.filter_by(slug=n["slug"]).first():
            db.session.add(NamazGuide(**n))

    quran_verses = [
        {
            "surah": 1, "verse": 1,
            "arabic": "بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ",
            "translation": "In the Name of Allah, the All-Beneficent, the All-Merciful",
            "urdu_translation": "شروع اللہ کے نام سے جو بڑا مہربان نہایت رحم والا ہے",
            "reference": "Quran 1:1"
        },
        {
            "surah": 112, "verse": 1,
            "arabic": "قُلْ هُوَ اللَّهُ أَحَدٌ",
            "translation": "Say: He, Allah, is One",
            "urdu_translation": "کہہ دو وہ اللہ ایک ہے",
            "reference": "Quran 112:1"
        },
        {
            "surah": 36, "verse": 1,
            "arabic": "يٰسٓ",
            "translation": "Ya Seen",
            "urdu_translation": "یٰس",
            "reference": "Quran 36:1"
        },
        {
            "surah": 48, "verse": 1,
            "arabic": "إِنَّا فَتَحْنَا لَكَ فَتْحًا مُّبِينًا",
            "translation": "Indeed, We have given you a clear victory",
            "urdu_translation": "بیشک ہم نے آپ کو ایک کھلی فتح دی",
            "reference": "Quran 48:1"
        },
        {
            "surah": 94, "verse": 1,
            "arabic": "أَلَمْ نَشْرَحْ لَكَ صَدْرَكَ",
            "translation": "Did We not expand for you your chest?",
            "urdu_translation": "کیا ہم نے آپ کا سینہ کھول نہیں دیا",
            "reference": "Quran 94:1"
        },
    ]

    for qv in quran_verses:
        if not QuranVerse.query.filter_by(surah=qv["surah"], verse=qv["verse"]).first():
            db.session.add(QuranVerse(**qv))

    hadiths = [
        {
            "arabic": "إِنَّمَا الْأَعْمَالُ بِالنِّيَّاتِ",
            "english": "Actions are judged by intentions",
            "urdu": "اعمال کا دار و مدار نیتوں پر ہے",
            "source": "Prophet Muhammad (SAWW)",
            "reference": "Bihar al-Anwar, Vol. 70, p. 207",
            "is_featured": True,
        },
        {
            "arabic": "مَنْ عَرَفَ نَفْسَهُ فَقَدْ عَرَفَ رَبَّهُ",
            "english": "Whoever knows himself has known his Lord",
            "urdu": "جس نے اپنے آپ کو پہچانا اس نے اپنے رب کو پہچانا",
            "source": "Imam Ali (AS)",
            "reference": "Ghurar al-Hikam, Hadith 8762",
            "is_featured": True,
        },
        {
            "english": "The best of you are those who are best to their families, and I am the best of you to my family",
            "urdu": "تم میں سب سے بہتر وہ ہے جو اپنے اہل خانہ کے لیے سب سے بہتر ہو، اور میں اپنے اہل خانہ کے لیے تم سب سے بہتر ہوں",
            "source": "Prophet Muhammad (SAWW)",
            "reference": "Al-Kafi, Vol. 5, p. 320",
            "is_featured": True,
        },
        {
            "english": "The believer is not one who fills his stomach while his neighbor is hungry",
            "urdu": "مومن وہ نہیں جو اپنا پیٹ بھرے جبکہ اس کا پڑوسی بھوکا ہو",
            "source": "Prophet Muhammad (SAWW)",
            "reference": "Al-Kafi, Vol. 2, p. 200",
            "is_featured": True,
        },
        {
            "english": "Do not be a victim of your anger",
            "urdu": "غصے کا شکار نہ بنو",
            "source": "Imam Ali (AS)",
            "reference": "Nahjul Balagha, Saying 11",
            "is_featured": True,
        },
    ]

    for h in hadiths:
        if not Hadith.query.filter_by(english=h["english"]).first():
            db.session.add(Hadith(**h))

    events = [
        {"title": "Nawroz", "hijri_date": "1 Farvardin", "event_type": "cultural"},
        {"title": "Eid ul-Fitr", "hijri_date": "1 Shawwal", "event_type": "eid"},
        {"title": "Eid ul-Adha", "hijri_date": "10 Dhul-Hijjah", "event_type": "eid"},
        {"title": "Eid al-Ghadir", "hijri_date": "18 Dhul-Hijjah", "event_type": "eid"},
        {"title": "Ashura", "hijri_date": "10 Muharram", "event_type": "mourning"},
        {"title": "Arbaeen", "hijri_date": "20 Safar", "event_type": "mourning"},
        {"title": "Milad un-Nabi (SAWW)", "hijri_date": "17 Rabiul Awwal", "event_type": "celebration"},
        {"title": "Birth of Imam Ali (AS)", "hijri_date": "13 Rajab", "event_type": "celebration"},
        {"title": "Birth of Imam al-Mahdi (ATFS)", "hijri_date": "15 Shaban", "event_type": "celebration"},
        {"title": "Shahadat of Imam Ali (AS)", "hijri_date": "21 Ramadan", "event_type": "mourning"},
        {"title": "Shahadat of Imam Hussain (AS)", "hijri_date": "10 Muharram", "event_type": "mourning"},
        {"title": "Ramadan", "hijri_date": "1 Ramadan", "event_type": "month"},
    ]

    for ev in events:
        if not IslamicEvent.query.filter_by(title=ev["title"]).first():
            db.session.add(IslamicEvent(**ev))

    articles = [
        {
            "title": "The Importance of Salah in Islam",
            "slug": "importance-of-salah",
            "content": "<p>Salah is the second pillar of Islam and a fundamental act of worship. In Shia Islam, the five daily prayers are considered obligatory (Wajib) and are a direct connection between the believer and Allah.</p><p>The Quran says: 'Indeed, prayer prohibits immorality and wrongdoing' (Quran 29:45). The Prophet Muhammad (SAWW) said: 'The prayer is the pillar of religion; whoever establishes it has established religion, and whoever destroys it has destroyed religion.'</p><p>In the Shia tradition, we combine Zuhr-Asr and Maghrib-Isha prayers as per the practice of the Prophet (SAWW) and the Ahlul Bayt (AS).</p>",
            "summary": "Learn about the significance of daily prayers in Shia Islam",
            "author": "Admin",
            "is_published": True,
            "is_featured": True,
        },
        {
            "title": "Understanding Wilayat in Shia Islam",
            "slug": "understanding-wilayat",
            "content": "<p>Wilayat (divine guardianship) is a core belief in Shia Islam. It refers to the spiritual and temporal authority of the Prophet Muhammad (SAWW) and the twelve Imams (AS) from his Ahlul Bayt.</p><p>The Quranic verse of Wilayat (5:55) states: 'Your guardian is only Allah, His Messenger, and those who believe, those who establish prayer and give zakah while bowing.' According to Shia tafsir, this verse was revealed regarding Imam Ali (AS).</p>",
            "summary": "The concept of spiritual guardianship in the Shia tradition",
            "author": "Admin",
            "is_published": True,
            "is_featured": True,
        },
    ]

    for a in articles:
        if not Article.query.filter_by(slug=a["slug"]).first():
            db.session.add(Article(**a))

    categories = [
        {"name": "Daily Duas", "slug": "daily-duas", "content_type": "dua", "sort_order": 1},
        {"name": "Special Duas", "slug": "special-duas", "content_type": "dua", "sort_order": 2},
        {"name": "Morning & Evening", "slug": "morning-evening", "content_type": "dua", "sort_order": 3},
        {"name": "Ziyarat", "slug": "ziyarat", "content_type": "ziyarat", "sort_order": 1},
        {"name": "Articles", "slug": "articles", "content_type": "article", "sort_order": 1},
    ]

    for cat in categories:
        if not Category.query.filter_by(slug=cat["slug"]).first():
            db.session.add(Category(**cat))

    pages_data = [
        {
            "title": "Nade Ali",
            "slug": "nade-ali",
            "content": "<h3>Nade Ali</h3><p><strong>Arabic:</strong> نَادِ عَلِيًّا مَظْهَرَ الْعَجَائِبِ تَجِدْهُ عَوْنَكَ فِي النَّوَائِبِ</p><p><strong>English:</strong> Call upon Ali, the manifestor of wonders, and you will find him your help in calamities.</p><p><strong>Urdu:</strong> علیؑ کو پکارو عجائب کے ظاہر کو، تم پائے گے وہ تمہاری مصیبت میں مدد گار ہے</p><p><strong>Reference:</strong> From the traditions of Imam Ali (AS), widely recited in Shia communities. Found in Mafatih al-Jinan and other supplication collections.</p><hr><h4>Full Text</h4><p>نَادِ عَلِيًّا مَظْهَرَ الْعَجَائِبِ تَجِدْهُ عَوْنَكَ فِي النَّوَائِبِ<br>يَا عَلِيُّ يَا عَلِيُّ يَا عَلِيٌّ بِعِزَّتِكَ اسْتَجَرْتُ فَاكْفِنِي</p><p><em>Additional Duas for help and relief are found in Mafatih al-Jinan.</em></p>",
            "is_published": True
        },
        {
            "title": "Nahjul Balagha",
            "slug": "nahjul-balagha",
            "content": "<h3>Nahjul Balagha - Peak of Eloquence</h3><p><strong>Nahjul Balagha</strong> is a collection of sermons, letters, and sayings of Imam Ali ibn Abi Talib (AS), compiled by Sharif al-Radi (d. 406 AH).</p><p>It is considered one of the most important texts in Shia Islam after the Quran and hadith collections, renowned for its eloquence, depth of Islamic philosophy, and spiritual guidance.</p><h4>Key Sections</h4><ul><li><strong>Sermons (Khutbah):</strong> 239 sermons on governance, spirituality, and Islamic philosophy</li><li><strong>Letters (Rasa'il):</strong> 79 letters on administration, ethics, and personal guidance</li><li><strong>Sayings (Hikam):</strong> 480 short sayings on wisdom and character</li></ul><h4>Famous Quotes</h4><blockquote><p>'People are of two kinds: either your brother in religion or your equal in creation.'</p><footer>- Imam Ali (AS), Nahjul Balagha, Saying 153</footer></blockquote><blockquote><p>'Do not be a victim of your anger. The best revenge is to forgive.'</p><footer>- Imam Ali (AS), Nahjul Balagha, Saying 11</footer></blockquote><p><strong>Reference:</strong> Sharif al-Radi, Nahjul Balagha. Widely studied in Shia seminaries and universities.</p>",
            "is_published": True
        },
        {
            "title": "Sahifa Sajjadiya",
            "slug": "sahifa-sajjadiya",
            "content": "<h3>Sahifa Sajjadiya - The Psalms of Islam</h3><p><strong>Sahifa Sajjadiya</strong> is a collection of 54 prayers (duas) attributed to Imam Ali ibn Hussain Zayn al-Abidin (AS), the fourth Shia Imam. It is considered one of the most important devotional texts in Shia Islam, often called the 'Psalms of the Household of the Prophet.'</p><p>The prayers cover a wide range of spiritual and mundane topics, including thanksgiving, repentance, seeking forgiveness, health, family, neighbors, and more.</p><h4>Famous Prayers</h4><ul><li><strong>Dua 1:</strong> Praise of Allah</li><li><strong>Dua 20:</strong> On Noble Character</li><li><strong>Dua 27:</strong> For the People on the Frontiers</li><li><strong>Dua 47:</strong> On the Day of Arafa</li></ul><p><strong>Reference:</strong> Imam Zayn al-Abidin (AS), Translated by William Chittick.</p>",
            "is_published": True
        },
        {
            "title": "Amaal - Recommended Acts",
            "slug": "amaal",
            "content": "<h3>Amaal - Recommended Acts of Worship</h3><p><strong>Amaal</strong> refers to the recommended acts and supplications prescribed for specific days, nights, and occasions in the Islamic calendar. These practices are derived from the teachings of the Prophet Muhammad (SAWW) and the Ahlul Bayt (AS).</p><h4>Daily Amaal</h4><ul><li>Recite Ayat al-Kursi after every prayer</li><li>Recite Tasbihat al-Zahra (SA): 33x Subhanallah, 33x Alhamdulillah, 34x Allahu Akbar</li><li>Recite Surah al-Ikhlas, Falaq, and Nas before sleeping</li><li>Recite Dua Faraj for the reappearance of Imam al-Mahdi (ATFS)</li></ul><h4>Weekly Amaal</h4><ul><li><strong>Thursday night:</strong> Recite Surah al-Kahf, Dua Kumayl</li><li><strong>Friday:</strong> Recite Dua Nudba, Surah al-Jumuah, send abundant salawat</li><li><strong>Saturday:</strong> Visit the graves of believers</li></ul><h4>Monthly Amaal</h4><ul><li>First night of the month: Recite Dua for the new moon</li><li>Middle of the month: Amaal of 15th Shaban (Night of Bara'at)</li></ul><p>For complete details, refer to Mafatih al-Jinan by Shaykh Abbas Qummi.</p>",
            "is_published": True
        },
        {
            "title": "Ramadan - Month of Mercy",
            "slug": "ramadan",
            "content": "<h3>Ramadan - The Holy Month</h3><p><strong>Ramadan</strong> is the ninth month of the Islamic calendar and is considered the most blessed month. The Quran was first revealed in this month. Fasting during Ramadan is one of the pillars of Islam.</p><h4>Important Nights</h4><ul><li><strong>1st Ramadan:</strong> Beginning of the month</li><li><strong>15th Ramadan:</strong> Birth of Imam Hasan (AS)</li><li><strong>19th-21st Ramadan:</strong> Nights of Qadr (Laylatul Qadr) - the night the Quran was revealed</li><li><strong>21st Ramadan:</strong> Martyrdom of Imam Ali (AS)</li><li><strong>23rd Ramadan:</strong> Most likely night of Qadr</li><li><strong>Last 10 days:</strong> I'tikaf (spiritual retreat) recommended</li></ul><h4>Recommended Amaal for Ramadan</h4><ul><li>Recite the entire Quran at least once</li><li>Recite Dua Iftitah every night</li><li>Recite Dua Abu Hamza Thumali before dawn</li><li>Give charity (sadaqa) generously</li><li>Feeding the fasting (iftar) to gain great reward</li></ul><p><strong>Reference:</strong> Quran Surah al-Baqarah 2:183-187, Mafatih al-Jinan.</p>",
            "is_published": True
        },
        {
            "title": "Muharram - Month of Mourning",
            "slug": "muharram",
            "content": "<h3>Muharram - The Month of Imam Hussain (AS)</h3><p><strong>Muharram</strong> is the first month of the Islamic calendar and is a month of mourning in Shia Islam. It marks the tragic events of Karbala where Imam Hussain (AS), the grandson of Prophet Muhammad (SAWW), and his 72 companions were martyred by the forces of Yazid ibn Muawiya.</p><h4>Important Days</h4><ul><li><strong>1st Muharram:</strong> Beginning of the Islamic New Year</li><li><strong>2nd Muharram:</strong> Arrival of Imam Hussain (AS) in Karbala</li><li><strong>7th Muharram:</strong> Water cut off from the camp of Imam Hussain (AS)</li><li><strong>10th Muharram (Ashura):</strong> Day of the great martyrdom</li><li><strong>11th-13th Muharram:</strong> Capture and journey of the Ahlul Bayt to Kufa and Damascus</li></ul><h4>Recommended Acts</h4><ul><li>Hold mourning gatherings (Majalis) to remember the tragedy</li><li>Recite Ziyarat Ashura on the 10th of Muharram</li><li>Give charity and provide food for those in mourning</li><li>Avoid worldly celebrations and entertainment</li></ul><p><strong>Reference:</strong> 'Ashura - Misbah al-Mutahajjid, Mafatih al-Jinan.</p>",
            "is_published": True
        },
        {
            "title": "Arbaeen - The 40th Day",
            "slug": "arbaeen",
            "content": "<h3>Arbaeen - The 40th Day After Ashura</h3><p><strong>Arbaeen</strong> marks the 40th day after the martyrdom of Imam Hussain (AS) at Karbala. It falls on the 20th of Safar. According to Islamic tradition, the heavens wept for 40 days after Imam Hussain's (AS) martyrdom, and visitation (Ziyarat) on this day is highly recommended.</p><p>The first Arbaeen pilgrimage is believed to have been performed by Jabir ibn Abdullah al-Ansari, a companion of the Prophet (SAWW), who visited Karbala 40 days after Ashura.</p><h4>Arbaeen Walk</h4><p>Millions of pilgrims walk from Najaf to Karbala (approximately 80 km) in what is the largest peaceful gathering in the world. Pilgrims are hosted and provided food, water, and accommodation by local volunteers along the route.</p><h4>Ziyarat of Arbaeen</h4><p>There is a special Ziyarat recited on Arbaeen, narrated from Imam al-Sadiq (AS), which emphasizes the sacrifice of Imam Hussain (AS) and the obligation to stand against tyranny.</p><p><strong>Reference:</strong> Mafatih al-Jinan, Ziyarat of Arbaeen.</p>",
            "is_published": True
        },
        {
            "title": "Privacy Policy",
            "slug": "privacy",
            "content": "<h3>Privacy Policy</h3><p>At Shia Islam, we respect your privacy and are committed to protecting your personal data.</p><h4>Information We Collect</h4><ul><li><strong>Account Information:</strong> If you register, we collect your name, email, and username.</li><li><strong>Usage Data:</strong> We collect anonymous usage statistics to improve our service.</li><li><strong>Bookmarks:</strong> Your saved bookmarks and reading progress are stored in your account.</li></ul><h4>How We Use Your Data</h4><ul><li>To provide and maintain our service</li><li>To improve user experience</li><li>To send occasional updates if you have opted in</li></ul><h4>Data Protection</h4><p>We use industry-standard security measures to protect your data. We never sell or share your personal information with third parties.</p><h4>Contact</h4><p>For privacy-related concerns, please contact us through our Contact page.</p>",
            "is_published": True
        },
        {
            "title": "Terms of Service",
            "slug": "terms",
            "content": "<h3>Terms of Service</h3><p>By using Shia Islam website, you agree to these terms of service.</p><h4>Use License</h4><p>All content on this website is provided for personal, non-commercial use. You may not reproduce, distribute, or modify the content without permission.</p><h4>Content Accuracy</h4><p>We strive to provide authentic Islamic content sourced from reliable Shia references. However, we recommend verifying critical religious information with qualified scholars.</p><h4>User Accounts</h4><p>You are responsible for maintaining the confidentiality of your account credentials. We reserve the right to suspend accounts that violate these terms.</p><h4>Changes to Terms</h4><p>We may update these terms at any time. Continued use of the website after changes constitutes acceptance of the new terms.</p>",
            "is_published": True
        },
    ]

    for p in pages_data:
        if not Page.query.filter_by(slug=p["slug"]).first():
            db.session.add(Page(**p))

    db.session.commit()
