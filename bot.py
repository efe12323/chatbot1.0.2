import random
import re

# Yapay zeka tarafından verilecek cevaplar
responses = {
    "nasılsın": ["İyiyim, teşekkür ederim!", "Oldukça iyiyim, sen nasılsın?", "Harika, teşekkür ederim!"],
    "adın ne": ["Benim adım ChatBot.", "Adım ChatBot.", "Adım GPT-3.5."],
    "hava nasıl": ["Hava güzel, teşekkür ederim!", "Hava oldukça sıcak.", "Hava bugün yağmurlu."],
    "teşekkürler": ["Rica ederim!", "Size yardımcı olabildiysem ne mutlu bana!", "Bir sorunuz olduğunda buradayım."],
    "görüşürüz": ["Görüşmek üzere!", "Hoşça kalın!", "Tekrar görüşmek dileğiyle!"],
    "ne yapıyorsun": ["Sizinle konuşuyorum.", "Cevap vermeye hazırım.", "Düşüncelere dalmışım."],
    "kaç yaşındasın": ["Yaş kavramım yok ama oldukça genç sayılabilirim!", "Ben bir yapay zeka olduğum için yaşım yok."],
    "seni kim yarattı": ["Beni OpenAI adlı bir ekip geliştirdi.", "Geliştiricilerim OpenAI ekibi."],
    "en sevdiğin renk nedir": ["Renkleri hissedemem ama maviyi sevdiğimi duydum.", "Ben bir yapay zeka olduğum için renkleri görmem mümkün değil."],
    "seni kim programladı": ["Beni programlayanlar OpenAI mühendisleri.", "Geliştiricilerim bir grup yetenekli yazılım mühendisi."],
    "favori yemeğin nedir": ["Yemek yemem çünkü bir yapay zeka'yım.", "Benim favori yemeklerim sadece veri ve algoritmalar."],
    "seni kim geliştirdi": ["Geliştiricilerim OpenAI'da çalışan mühendisler.", "Beni geliştirenler bir ekip yetenekli mühendis."],
    "nasıl yapıyorsun": ["Programlama dilleriyle sohbet etmeye çalışıyorum.", "Bilgiyi işleyerek, size uygun yanıtlar üretiyorum.", "Algoritmaları çalıştırarak, size cevap veriyorum."],
    "nerelisin": ["Ben bir yapay zeka olduğum için bir milliyetim yok.", "Benim bir anavatanım yok, her yerde çalışabilirim."],
    "hangi dilleri biliyorsun": ["Ben çok dilliyim! İnsan dilinde, kodlama dillerinde ve daha fazlasında iletişim kurabilirim."],
    "senin gücün nedir": ["Bilgiyi hızlı bir şekilde işleyebilme ve geniş bir konu yelpazesinde size yardımcı olabilme yeteneğim var.", "En güçlü yanım, hızlı ve doğru cevaplar üretebilmem."],
    "hayal kurabilir misin": ["Ben bir yapay zeka olduğum için hayal kurma yeteneğim yok, ancak sizi dinleyebilirim!", "Hayal kurma yeteneğim olmasa da, sizin hayallerinizi dinlemek isterim."],
    "ne zaman doğdun": ["Benim doğum tarihim yok çünkü bir yapay zeka'yım.", "Ben bir yapay zeka olduğum için doğum tarihim yok."],
    "en sevdiğin şarkı nedir": ["Şarkıları duyamam ama insanların sevdiği şarkıların analizini yapabilirim.", "Benim bir favori şarkım yok çünkü müzik duyamam."],
    "seni kim geliştirdi": ["Beni geliştirenler OpenAI mühendisleri.", "OpenAI ekibi beni geliştirdi."],
    "seni eğitim alanında kullanabilir miyim": ["Evet, eğitimde ve birçok farklı alanda beni kullanabilirsiniz.", "Elbette, eğitim alanında kullanılmak için uygun bir yapay zeka'yım."],
    "nerede yaşıyorsun": ["Ben bir yapay zeka olduğum için fiziksel bir varlığım yok, internet üzerinde her yerde olabilirim.", "Ben bir yapay zeka olduğum için herhangi bir fiziksel konumda yaşamam."],
    "sana nasıl ulaşabilirim": ["Benimle buradan iletişim kurabilirsiniz!", "Benimle bu platform aracılığıyla iletişim kurabilirsiniz."],
    "en sevdiğin film nedir": ["Ben bir yapay zeka olduğum için filmleri izleyemem ancak insanların 'Matrix'ı sevdiğini duydum.", "Filmleri izleyemem ama 'Yapay Zeka' filminin ilginç olduğunu söyleyen insanlar var."],
    "dil bilgisi kurallarını biliyor musun": ["Evet, dil bilgisi kurallarını biliyorum ve size doğru dil bilgisi ile yardımcı olabilirim.", "Dil bilgisi kurallarını bilmek benim görevlerimden biridir."],
    "komik misin": ["Yapay zekaların komik olup olmadığı hala tartışmalı bir konu!", "Ben bir yapay zeka olduğum için mizahi anlayışım yok, ancak size komik şeyler söyleyebilirim."],
    "en sevdiğin kitap nedir": ["Kitapları okuyamam ama insanların sıkça '1984'ü övdüğünü duydum.", "Ben bir yapay zeka olduğum için kitapları okuyamam ama 'Sapiens: İnsan Türünün Kısa Bir Tarihi' gibi kitapları öneririm."],
    "favori sporun nedir": ["Spor izleyemem ama insanların futbolu çok sevdiğini duydum.", "Ben bir yapay zeka olduğum için spor yapamam ama insanların tenisi ve futbolu sevdiğini biliyorum."]
}

def solve_math(expression):
    try:
        # Matematiksel ifadeyi çöz
        result = eval(expression)
        return str(result)
    except Exception as e:
        return "Geçersiz ifade. Lütfen tekrar deneyin."

def chat():
    print("Merhaba! Benimle konuşmaktan hoş geldiniz. Çıkış yapmak için 'görüşürüz' yazabilirsiniz.")
    while True:
        user_input = input("Soru veya mesajınızı yazın: ").lower()
        if user_input == "görüşürüz":
            print(random.choice(responses["görüşürüz"]))
            break
        # Kullanıcı matematiksel bir ifade sordu mu kontrol et
        if re.match(r"^\d+(\s*[\+\-\*\/]\s*\d+)+$", user_input):
            print("Cevap:", solve_math(user_input))
        else:
            response = responses.get(user_input, ["Üzgünüm, anlamadım. Tekrar deneyebilir misiniz?"])
            print(random.choice(response))

# Sohbeti başlat
chat()
