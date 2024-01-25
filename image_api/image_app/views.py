# image_app/views.py
from openai import OpenAI
from django.conf import settings
from rest_framework.decorators import api_view
from rest_framework.response import Response
from google.generativeai import configure
import google.generativeai as genai

@api_view(['POST'])
def generate_dalle_image(request):
    prompt = request.data.get('prompt', '')
    model = request.data.get('model', 'dall-e-2')
    size = request.data.get('size', '1024x1024')
    quality = request.data.get('quality', 'standard')
    n = request.data.get('n', 1)

    client = OpenAI(api_key=settings.OPENAI_API_KEY)
    response = client.images.generate(
        model=model,
        prompt=prompt,
        size=size,
        quality=quality,
        n=n,
    )

    image_url = response.data[0].url
    return Response({'image_url': image_url})

@api_view(['POST'])
def generate_text_from_image(request):
    configure(api_key=settings.GOOGLE_API_KEY)

    image_path = request.data.get('image_path')

    if not image_path:
        return Response({'error': 'No image path provided'}, status=400)

    try:
        # Verify that the image file exists
        with open(image_path, 'rb') as f:
            pass
    except FileNotFoundError:
        return Response({'error': 'Image file not found'}, status=400)


    model = genai.GenerativeModel('gemini-pro-vision')
    
    try:
        response = model.generate_content(image_path)
        return Response({'generated_text': response.text})
    except Exception as e:
        return Response({'error': str(e)}, status=400)
