from django.shortcuts import render, redirect
from django.http import HttpResponse
import gtts
from io import BytesIO

def Home(request):
    template = 'index.html'
    context = {
        "Hello": "Hello Django"
    }
    return render(request, template, context)

def TextToVoice(request):
    if request.method == 'POST':
        text = request.POST.get('text', '').strip()
        language = request.POST.get('language', '').strip()
        try:
            if text:
                # Generate audio in memory
                buffer = BytesIO()
                sound = gtts.gTTS(text, lang=language)
                sound.write_to_fp(buffer)
                buffer.seek(0)

                # Set download headers for attachment
                filename = 'your_audio_filename.mp3'  # Replace with desired filename
                response = HttpResponse(buffer.getvalue(), content_type='audio/mpeg')
                response['Content-Disposition'] = f'attachment; filename="{filename}"'

                return response
        except:
            template = "API_error.html"
            context = {
                "error": "Error",
                'message': "Sorry, we are facing an isue during converting your text please check your internet connection and try again."
            }
            return render(request, template, context)

    return redirect('/')
