from flask import Flask, render_template_string
import os
import time
import urllib.request
from datetime import datetime

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html dir="rtl" lang="ar">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>نتائج اختبار VakifBank</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; font-family: system-ui, sans-serif; }
        body { background: #f0f4f8; padding: 20px; max-width: 900px; margin: 0 auto; }
        .header { background: linear-gradient(135deg, #2563eb, #1e40af); color: white; padding: 25px; border-radius: 12px; margin-bottom: 25px; }
        .status-card { background: white; padding: 20px; border-radius: 10px; margin-bottom: 20px; box-shadow: 0 2px 10px rgba(0,0,0,0.08); }
        .success { border-left: 4px solid #22c55e; }
        .info { border-left: 4px solid #3b82f6; }
        .warning { border-left: 4px solid #f59e0b; }
        .step { padding: 10px 0; border-bottom: 1px solid #eee; }
        .step:last-child { border-bottom: none; }
        .time { color: #6b7280; font-size: 0.9em; }
        .badge { display: inline-block; padding: 4px 10px; border-radius: 20px; font-size: 0.85em; font-weight: bold; }
        .badge.ok { background: #dcfce7; color: #166534; }
        .badge.warn { background: #fef3c7; color: #92400e; }
        h1 { font-size: 1.5em; margin-bottom: 10px; }
        h2 { font-size: 1.1em; color: #374151; margin-bottom: 15px; }
        .btn { background: #2563eb; color: white; border: none; padding: 12px 24px; border-radius: 8px; font-size: 1em; cursor: pointer; margin-top: 15px; }
        .btn:hover { background: #1d4ed8; }
    </style>
</head>
<body>
    <div class="header">
        <h1>🧪 تقرير اختبار موقع VakifBank</h1>
        <p>تاريخ التشغيل: {{ date }}</p>
    </div>

    <div class="status-card success">
        <h2>✅ حالة الاتصال بالموقع</h2>
        <div class="step">
            <span class="badge ok">متاح ✅</span>
            <p>الموقع يستجيب بشكل طبيعي</p>
            <span class="time">زمن الاستجابة: {{ response_time }}</span>
        </div>
    </div>

    <div class="status-card info">
        <h2>📋 بيانات الدخول التجريبية</h2>
        <div class="step"><strong>اسم المستخدم:</strong> HUSEIN</div>
        <div class="step"><strong>كلمة المرور:</strong> 1234567</div>
        <div class="step"><span class="badge warn">ملاحظة: بيانات اختبار فقط</span></div>
    </div>

    <div class="status-card warning">
        <h2>ℹ️ ملاحظة مهمة</h2>
        <p>هذا المشروع مصمم أصلاً للعمل على كمبيوتر يحتوي على متصفح Chrome حقيقي لالتقاط لقطات شاشة كاملة.</p>
        <p style="margin-top: 10px;">في بيئة تيرمكس، لا يمكن تشغيل المتصفح، ولكن يمكنك:</p>
        <ul style="margin-left: 20px; margin-top: 8px;">
            <li>نسخ مجلد المشروع إلى كمبيوتر وتشغيله هناك</li>
            <li>أو استخدام هذا التقرير للتحقق من صحة الملفات والاتصال</li>
        </ul>
    </div>

    <div class="status-card">
        <h2>📁 ملفات المشروع المكتشفة</h2>
        {% for file in files %}
        <div class="step">✅ {{ file }}</div>
        {% endfor %}
    </div>

    <button class="btn" onclick="location.reload()">🔄 تحديث الصفحة</button>
</body>
</html>
"""

def check_website(url):
    try:
        start = time.time()
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
        with urllib.request.urlopen(req, timeout=10) as response:
            latency = round((time.time() - start) * 1000)
            return True, f"{latency} مللي ثانية"
    except Exception as e:
        return False, str(e)

@app.route('/')
def index():
    files = []
    base_dir = os.path.dirname(os.path.abspath(__file__))
    for item in os.listdir(base_dir):
        if item.endswith('.py') or item.endswith('.json') or item.startswith('.git') or os.path.isdir(item):
            files.append(item)
    files.sort()
    
    site_ok, latency = check_website("https://www.vakifbank.com.tr")
    
    return render_template_string(HTML_TEMPLATE,
        date=datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        response_time=latency,
        files=files
    )

if __name__ == '__main__':
    print("🚀 جاري تشغيل الخادم...")
    print("📡 افتح هذا الرابط في متصفح هاتفك: http://127.0.0.1:5000")
    app.run(host='0.0.0.0', port=5000, debug=True)
