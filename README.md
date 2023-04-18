libPosAPI.so файлаа прожектийн root дээр хуулаад ажиллуулаарай.
<br />
<br />

```
python3 -m venv venv                # Python virtual environment үүсгэнэ

source venv/bin/activate            # Virtual environment-аа activate хийнэ

pip3 install -r requirements.txt    # Шаардлагатай санг суулгах (flask)

python3 app.py
```

Яараад хийсэн, замбараагүй/муухай code байгаа.
<br />
<br />
Цаашдаа __засаад/өөрчлөөд__ refactor хийгээд явцгаая өө.
<br />
<br />
Шаардлагатай сан, request-ийн талаар doc-оос нь хараарай https://ebarimt.mn/img/Pos%20API%202.1.2%20User%20Guide_mn.pdf эндээс хараарай.

Өө нээрээ flask development орчинд асаагаад байгаа production-д асааж мэддэг хүн байвал засаад өгөөрэй.

<br />
<br />
<br />

Зарим нэг хэрэг болох мэдээлэл:
1. Timeout өгөөд байвал Монголд байгаа сервэр дээр тавиад үзээрэй.
2. /check-api, /get-information URL-уудыг дуудаад шалгаж үзэх боломжтой.
3. /send-data API-ийг нь 24 цагтаа ядаж нэг дуудаад байвал зүгээр байх
4. Doc унш бас дахин doc унш: https://ebarimt.mn/img/Pos%20API%202.1.2%20User%20Guide_mn.pdf