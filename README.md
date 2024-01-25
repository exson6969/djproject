### Curl to generate image

```
curl -X POST -H "Content-Type: application/json" -d "{\"prompt\": \"your_prompt_here\", \"model\": \"dall-e-2\", \"size\": \"1024x1024\", \"quality\": \"standard\", \"n\": 1}" http://127.0.0.1:8000/api/generate_image/
```

### Curl to generate text

```
curl -X POST -H "Content-Type: application/json" -d "{\"image_path\": \"path_value"}" http://127.0.0.1:8000/api/generate_text/
```