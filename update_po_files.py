import os
import re

translations = {
    'hi': {
        "Connect. Bid. Prosper.": "जुड़ें। बोली लगाएँ। समृद्ध हों।",
        "Your direct farm-fresh produce marketplace. Fair prices, empowered farmers, and sustainable communities.": "आपका सीधा खेत-ताज़ा उत्पाद बाज़ार। उचित मूल्य, सशक्त किसान और स्थायी समुदाय।",
        "For Farmers": "किसानों के लिए",
        "List your harvest, get AI-powered price suggestions, and connect directly with buyers. No middlemen.": "अपनी फसल सूचीबद्ध करें, एआई-संचालित मूल्य सुझाव प्राप्त करें, और सीधे खरीदारों से जुड़ें। कोई बिचौलिया नहीं।",
        "Instant Listing": "त्वरित लिस्टिंग",
        "Smart Pricing": "स्मार्ट मूल्य निर्धारण",
        "Secure Orders": "सुरक्षित ऑर्डर",
        "Start Selling": "बेचना शुरू करें",
        "For Buyers": "खरीदारों के लिए",
        "Browse fresh local produce, view demand trends, and buy directly from the source.": "ताज़ा स्थानीय उत्पाद ब्राउज़ करें, मांग के रुझान देखें और सीधे स्रोत से खरीदें।",
        "Farm Fresh": "खेत से ताज़ा",
        "Transparent Pricing": "पारदर्शी मूल्य निर्धारण",
        "Direct Contact": "सीधा संपर्क",
        "Start Buying": "खरीदना शुरू करें",
        "Why Kissan Connect?": "किसान कनेक्ट क्यों?",
        "Fair Trade": "उचित व्यापार",
        "Farmers get better rates, buyers get better prices.": "किसानों को बेहतर दरें मिलती हैं, खरीदारों को बेहतर कीमतें मिलती हैं।",
        "Smart Tech": "स्मार्ट तकनीक",
        "AI-driven insights for smarter business decisions.": "बेहतर व्यावसायिक निर्णयों के लिए एआई-संचालित अंतर्दृष्टि।",
        "Community": "समुदाय",
        "Building strong local agricultural networks.": "मजबूत स्थानीय कृषि नेटवर्क का निर्माण।",
        "Home": "होम",
        "Dashboard": "डैशबोर्ड",
        "Sell Produce": "उपज बेचें",
        "Marketplace": "बाज़ार",
        "Hello": "नमस्ते",
        "Logout": "लॉग आउट",
        "Login": "लॉग इन",
        "Sign Up": "साइन अप",
        "I'm a Farmer": "मैं एक किसान हूँ",
        "I'm a Buyer": "मैं एक खरीदार हूँ",
        "Go to Dashboard": "डैशबोर्ड पर जाएं"
    },
    'ta': {
        "Connect. Bid. Prosper.": "இணையுங்கள். ஏலம் விடுங்கள். செழியுங்கள்.",
        "Your direct farm-fresh produce marketplace. Fair prices, empowered farmers, and sustainable communities.": "உங்கள் நேரடி பண்ணை-புதிய விளைபொருள் சந்தை. நியாயமான விலைகள், அதிகாரம் பெற்ற விவசாயிகள் மற்றும் நிலையான சமூகங்கள்.",
        "For Farmers": "விவசாயிகளுக்கு",
        "List your harvest, get AI-powered price suggestions, and connect directly with buyers. No middlemen.": "உங்கள் அறுவடையை பட்டியலிடுங்கள், AI-மூலம் விலை பரிந்துரைகளைப் பெறுங்கள், மேலும் வாங்குபவர்களுடன் நேரடியாக இணையுங்கள். இடைத்தரகர்கள் இல்லை.",
        "Instant Listing": "உடனடி பட்டியல்",
        "Smart Pricing": "ஸ்மார்ட் விலை நிர்ணயம்",
        "Secure Orders": "பாதுகாப்பான ஆர்டர்கள்",
        "Start Selling": "விற்கத் தொடங்குங்கள்",
        "For Buyers": "வாங்குபவர்களுக்கு",
        "Browse fresh local produce, view demand trends, and buy directly from the source.": "புதிய உள்ளூர் விளைபொருட்களை உலாவவும், தேவைப் போக்குகளைக் காணவும் மற்றும் நேரடியாக வாங்கவும்.",
        "Farm Fresh": "பண்ணை புதியது",
        "Transparent Pricing": "வெளிப்படையான விலை நிர்ணயம்",
        "Direct Contact": "நேரடி தொடர்பு",
        "Start Buying": "வாங்கத் தொடங்குங்கள்",
        "Why Kissan Connect?": "ஏன் கிசான் கனெக்ட்?",
        "Fair Trade": "நியாயமான வர்த்தகம்",
        "Farmers get better rates, buyers get better prices.": "விவசாயிகள் சிறந்த கட்டணத்தைப் பெறுகிறார்கள், வாங்குபவர்கள் சிறந்த விலைகளைப் பெறுகிறார்கள்.",
        "Smart Tech": "ஸ்மார்ட் தொழில்நுட்பம்",
        "AI-driven insights for smarter business decisions.": "சிறந்த வணிக முடிவுகளுக்கு AI-ஆல் இயங்கும் நுண்ணறிவு.",
        "Community": "சமூகம்",
        "Building strong local agricultural networks.": "வலுவான உள்ளூர் விவசாய நெட்வொர்க்குகளை உருவாக்குதல்.",
        "Home": "முகப்பு",
        "Dashboard": "டாஷ்போர்டு",
        "Sell Produce": "விளைபொருட்களை விற்கவும்",
        "Marketplace": "சந்தை",
        "Hello": "வணக்கம்",
        "Logout": "வெளியேறு",
        "Login": "உள்நுழை",
        "Sign Up": "பதிவு செய்",
        "I'm a Farmer": "நான் ஒரு விவசாயி",
        "I'm a Buyer": "நான் ஒரு வாங்குபவர்",
        "Go to Dashboard": "டாஷ்போர்டுக்குச் செல்லவும்"
    },
    'kn': {
        "Connect. Bid. Prosper.": "ಸಂಪರ್ಕಿಸಿ. ಬಿಡ್ ಮಾಡಿ. ಸಮೃದ್ಧರಾಗಿ.",
        "Your direct farm-fresh produce marketplace. Fair prices, empowered farmers, and sustainable communities.": "ನಿಮ್ಮ ನೇರ ಫಾರ್ಮ್-ಫ್ರೆಶ್ ಉತ್ಪನ್ನ ಮಾರುಕಟ್ಟೆ. ನ್ಯಾಯಯುತ ಬೆಲೆಗಳು, ಸಬಲ ರೈತರು ಮತ್ತು ಸುಸ್ಥಿರ ಸಮುದಾಯಗಳು.",
        "For Farmers": "ರೈತರಿಗಾಗಿ",
        "List your harvest, get AI-powered price suggestions, and connect directly with buyers. No middlemen.": "ನಿಮ್ಮ ಸುಗ್ಗಿಯನ್ನು ಪಟ್ಟಿ ಮಾಡಿ, AI-ಚಾಲಿತ ಬೆಲೆ ಸಲಹೆಗಳನ್ನು ಪಡೆಯಿರಿ ಮತ್ತು ಖರೀದಿದಾರರೊಂದಿಗೆ ನೇರವಾಗಿ ಸಂಪರ್ಕ ಸಾಧಿಸಿ. ಮಧ್ಯವರ್ತಿಗಳಿಲ್ಲ.",
        "Instant Listing": "ತ್ವರಿತ ಪಟ್ಟಿ",
        "Smart Pricing": "ಸ್ಮಾರ್ಟ್ ಬೆಲೆ ನಿಗದಿ",
        "Secure Orders": "ಸುರಕ್ಷಿತ ಆದೇಶಗಳು",
        "Start Selling": "ಮಾರಾಟ ಮಾಡಲು ಪ್ರಾರಂಭಿಸಿ",
        "For Buyers": "ಖರೀದಿದಾರರಿಗಾಗಿ",
        "Browse fresh local produce, view demand trends, and buy directly from the source.": "ತಾಜಾ ಸ್ಥಳೀಯ ಉತ್ಪನ್ನಗಳನ್ನು ಬ್ರೌಸ್ ಮಾಡಿ, ಬೇಡಿಕೆಯ ಟ್ರೆಂಡ್‌ಗಳನ್ನು ವೀಕ್ಷಿಸಿ ಮತ್ತು ನೇರವಾಗಿ ಖರೀದಿಸಿ.",
        "Farm Fresh": "ಫಾರ್ಮ್ ಫ್ರೆಶ್",
        "Transparent Pricing": "ಪಾರದರ್ಶಕ ಬೆಲೆ ನಿಗದಿ",
        "Direct Contact": "ನೇರ ಸಂಪರ್ಕ",
        "Start Buying": "ಖರೀದಿಸಲು ಪ್ರಾರಂಭಿಸಿ",
        "Why Kissan Connect?": "ಕಿಸಾನ್ ಕನೆಕ್ಟ್ ಏಕೆ?",
        "Fair Trade": "ನ್ಯಾಯೋಚಿತ ವ್ಯಾಪಾರ",
        "Farmers get better rates, buyers get better prices.": "ರೈತರಿಗೆ ಉತ್ತಮ ದರಗಳು ಸಿಗುತ್ತವೆ, ಖರೀದಿದಾರರಿಗೆ ಉತ್ತಮ ಬೆಲೆ ಸಿಗುತ್ತದೆ.",
        "Smart Tech": "ಸ್ಮಾರ್ಟ್ ತಂತ್ರಜ್ಞಾನ",
        "AI-driven insights for smarter business decisions.": "ಚುರುಕಾದ ವ್ಯವಹಾರ ನಿರ್ಧಾರಗಳಿಗಾಗಿ AI-ಚಾಲಿತ ಒಳನೋಟಗಳು.",
        "Community": "ಸಮೂದಾಯ",
        "Building strong local agricultural networks.": "ಬಲವಾದ ಸ್ಥಳೀಯ ಕೃಷಿ ಜಾಲಗಳನ್ನು ನಿರ್ಮಿಸುವುದು.",
        "Home": "ಮುಖಪುಟ",
        "Dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್",
        "Sell Produce": "ಉತ್ಪನ್ನವನ್ನು ಮಾರಿ",
        "Marketplace": "ಮಾರುಕಟ್ಟೆ",
        "Hello": "ನಮಸ್ಕಾರ",
        "Logout": "ಲಾಗ್ ಔಟ್",
        "Login": "ಲಾಗಿನ್",
        "Sign Up": "ಸೈನ್ ಅಪ್",
        "I'm a Farmer": "ನಾನು ಒಬ್ಬ ರೈತ",
        "I'm a Buyer": "ನಾನು ಒಬ್ಬ ಖರೀದಿದಾರ",
        "Go to Dashboard": "ಡ್ಯಾಶ್‌ಬೋರ್ಡ್‌ಗೆ ಹೋಗಿ"
    }
}

def update_po(lang, trans_dict):
    filepath = f'locale/{lang}/LC_MESSAGES/django.po'
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith('msgid "'):
            msgid = line[7:-2]
            # Handle multi-line msgid if necessary (but for our simple ones, it's usually single line)
            
            if msgid in trans_dict:
                new_lines.append(line)
                i += 1
                if i < len(lines) and lines[i].startswith('msgstr ""'):
                    new_lines.append(f'msgstr "{trans_dict[msgid]}"\n')
                    i += 1
                else:
                    new_lines.append(lines[i])
                    i += 1
            else:
                new_lines.append(line)
                i += 1
        else:
            new_lines.append(line)
            i += 1

    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(new_lines)
    print(f"Updated: {filepath}")

for lang, trans_dict in translations.items():
    update_po(lang, trans_dict)
