import geocoder
import pywhatkit as kit
import datetime

PHONE_NUMBER = "+918586801794"  # Ensure the phone number includes the country code

def get_live_location():
    """Fetch real-time GPS location using geocoder"""
    g = geocoder.ip('me')
    if g.ok:
        latitude, longitude = g.latlng
        map_link = f"https://www.google.com/maps?q={latitude},{longitude}"
        return f"🚨 Emergency Alert!\n📍 Live Location: {latitude}, {longitude}\n🔗 Google Maps: {map_link}"
    return "❌ Location not found!"

def send_whatsapp_message(location_info):
    """Send WhatsApp message using pywhatkit"""
    now = datetime.datetime.now()
    send_time = now + datetime.timedelta(minutes=2)  # Sends message 2 minutes from now
    hour, minute = send_time.hour, send_time.minute

    try:
        kit.sendwhatmsg(PHONE_NUMBER, location_info, hour, minute)
        print("✅ WhatsApp Message Scheduled!")
    except Exception as e:
        print(f"❌ Error sending WhatsApp message: {e}")

# Get live location & send WhatsApp message
location_info = get_live_location()
send_whatsapp_message(location_info)

