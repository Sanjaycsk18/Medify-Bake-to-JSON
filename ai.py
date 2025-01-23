import os
import json
import google.generativeai as genai
from google.ai.generativelanguage_v1beta.types import content

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

def upload_to_gemini(path, mime_type=None):
  """Uploads the given file to Gemini.

  See https://ai.google.dev/gemini-api/docs/prompting_with_media
  """
  file = genai.upload_file(path, mime_type=mime_type)
  print(f"Uploaded file '{file.display_name}' as: {file.uri}")
  return file

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_schema": content.Schema(
    type = content.Type.OBJECT,
    properties = {
      "ingredients": content.Schema(
        type = content.Type.ARRAY,
        items = content.Schema(
          type = content.Type.OBJECT,
          properties = {
            "name": content.Schema(
              type = content.Type.STRING,
            ),
            "quantity": content.Schema(
              type = content.Type.STRING,
            ),
          },
        ),
      ),
      "instructions": content.Schema(
        type = content.Type.ARRAY,
        items = content.Schema(
          type = content.Type.STRING,
        ),
        
      ),
      "title": content.Schema(
        type = content.Type.STRING,
      ),
    },
  ),
  "response_mime_type": "application/json",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
)

def process_image(image_path):



  chat_session = model.start_chat(
    history=[
      {
        "role": "user",
        "parts": [
          upload_to_gemini(image_path, mime_type="image/jpeg"),
          "Given this image:\n\n1. First, describe the image\n2. Then, detail the recipe to bake this item in JSON format. Include item names and quantities for the recipe",
        ],
      },
      
    ]

  ) 
  recipe = chat_session.send_message("Generate recipe for the image")
  return json.loads(recipe.text)
