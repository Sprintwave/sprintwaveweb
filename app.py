from flask import Flask, render_template, Response
import os
from datetime import datetime

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/starlink')
def starlink():
    return render_template('starlink.html')

@app.route('/event-wifi')
def event_wifi():
    return render_template('eventwifi.html')

@app.route('/backup-internet')
def backup_internet():
    return render_template('backup.html')

@app.route('/web-design')
def web_design():
    return render_template('webdesign.html')

@app.route('/sitemap.xml')
def sitemap():
    """Generate sitemap XML for Google Search Console"""
    
    # Get current date in ISO format
    current_date = datetime.now().strftime('%Y-%m-%d')
    
    sitemap_xml = f"""<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
    <url>
        <loc>https://www.sprintwave.co.uk/</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>1.0</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/starlink</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/event-wifi</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/backup-internet</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/web-design</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/blog</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.8</priority>
    </url>
</urlset>"""
    
    return Response(sitemap_xml, mimetype='application/xml')

@app.route('/robots.txt')
def robots():
    """Generate robots.txt file"""
    robots_txt = """User-agent: *
Allow: /

Sitemap: https://www.sprintwave.co.uk/sitemap.xml
"""
    return Response(robots_txt, mimetype='text/plain')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)