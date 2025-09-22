from flask import Flask, render_template, Response, request, jsonify
import os
from datetime import datetime
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route('/blog')
def blog():
    return render_template('blog.html')
# Add this route after your existing routes, around line 35:

@app.route('/penetration-testing')
def penetration_testing():
    return render_template('penetration-testing.html')
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

@app.route('/wireless-surveys')
def wireless_surveys():
    return render_template('wifisurveys.html')

@app.route('/network-consulting')
def network_consulting():  # This is the function name
    return render_template('networkconsulting.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/rural-broadband')
def rural_broadband():
    return render_template('rural-broadband.html')

@app.route('/thank-you-event-wifi')
def thank_you_event_wifi():
    return render_template('thank-you-event-wifi.html')

@app.route('/thank-you-rural-broadband')
def thank_you_rural_broadband():
    return render_template('thank-you-rural-broadband.html')

@app.route('/case-studies')
def case_studies():
    return render_template('case_studies/index.html')


# Add these routes to your Flask application

@app.route('/case-studies/event-wifi')
def case_study_event_wifi():
    return render_template('case_study_event_wifi.html')

@app.route('/case-studies/starlink')
def case_study_starlink():
    return render_template('case_study_starlink.html')

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
        <loc>https://www.sprintwave.co.uk/about</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/starlink</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/rural-broadband</loc>
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
        <loc>https://www.sprintwave.co.uk/wireless-surveys</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>weekly</changefreq>
        <priority>0.9</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/network-consulting</loc>
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
    <url>
        <loc>https://www.sprintwave.co.uk/blog/ansible-ad-lockout</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/blog/aruba-ansible-backup</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/blog/100g-aruba-8360</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/blog/clearpass-api</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/blog/ise-vs-clearpass</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/blog/enocean-catalyst</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/blog/starlink-technical</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.7</priority>
    </url>
        <url>
        <loc>https://www.sprintwave.co.uk/case-studies/event-wifi</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>monthly</changefreq>
        <priority>0.8</priority>
    </url>
    <url>
        <loc>https://www.sprintwave.co.uk/case-studies/starlink</loc>
        <lastmod>{current_date}</lastmod>
        <changefreq>monthly</changefreq>
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

@app.route('/blog/ansible-ad-lockout')
def ansible_ad_lockout():
    return render_template('blog/ansible-ad-lockout.html')

@app.route('/blog/aruba-ansible-backup')
def aruba_ansible_backup():
    return render_template('blog/aruba-ansible-backup.html')

@app.route('/blog/100g-aruba-8360')
def aruba_100g():
    return render_template('blog/100g-aruba-8360.html')

@app.route('/blog/clearpass-api')
def clearpass_api():
    return render_template('blog/clearpass-api.html')

@app.route('/blog/ise-vs-clearpass')
def ise_vs_clearpass():
    return render_template('blog/ise-vs-clearpass.html')

@app.route('/blog/enocean-catalyst')
def enocean_catalyst():
    return render_template('blog/enocean-catalyst.html')

@app.route('/blog/starlink-technical')
def starlink_technical():
    return render_template('blog/starlink-technical.html')

@app.route('/submit-contact-form', methods=['POST'])
def submit_contact_form():
    try:
        # Get form data
        data = request.get_json()
        
        # Email configuration
        smtp_server = "smtp.gmail.com"  # or your email provider
        smtp_port = 587
        sender_email = "your-sender@gmail.com"  # Your sending email
        sender_password = "your-app-password"   # App password
        recipient_email = "info@sprintwave.co.uk"  # Where to send inquiries
        
        # Create email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = f"Event WiFi Inquiry - {data.get('eventType', 'General')}"
        
        # Email body
        body = f"""
        New Event WiFi Inquiry:
        
        Contact Information:
        - Name: {data.get('firstName', '')} {data.get('lastName', '')}
        - Email: {data.get('email', '')}
        - Phone: {data.get('phone', '')}
        
        Event Details:
        - Type: {data.get('eventType', '')}
        - Date: {data.get('eventDate', '')}
        - Venue: {data.get('venue', '')}
        - Requirements: {data.get('requirements', '')}
        
        Submitted from: Event WiFi Page
        """
        
        msg.attach(MIMEText(body, 'plain'))
        
        # Send email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = msg.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        
        return jsonify({'status': 'success', 'message': 'Email sent successfully'})
        
    except Exception as e:
        print(f"Error sending email: {e}")
        return jsonify({'status': 'error', 'message': 'Failed to send email'}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=False, host='0.0.0.0', port=port)