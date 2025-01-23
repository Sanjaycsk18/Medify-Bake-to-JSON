## Bake to JSON 

This project demonstrates how to use Dash, a web framework for Python, to create a web application that extracts recipes from images using the Gemini Generative AI model.

**Project Structure:**

* `Dockerfile`: Defines the Docker image for running the application.
* `app.py`: The main Dash application code.
* `ai.py`: Handles image processing and recipe extraction using Gemini.
* `requirements.txt`: Lists the required Python libraries and their versions.

**How it Works:**

1. **User Interface:**
   - The Dash application provides an upload component where users can select an image.
   - Once uploaded, the image is displayed on the screen.
2. **Image Processing:**
   - When the user submits the image, the `ai.py` script is called.
   - This script uploads the image to the Gemini AI model using the provided API key.
   - It instructs the model to describe the image and provide a recipe in JSON format.
3. **Recipe Display:**
   - The response from Gemini is parsed to extract the recipe details (ingredients, instructions).
   - The extracted recipe information is displayed in a user-friendly format within the web application, including:
     - Recipe title
     - Ingredient list 
     - Instruction steps

**Running the Project:**

**Prerequisites:**

* Docker installed and running on your system.
* A Gemini API key (obtain from Google AI Platform [invalid URL removed])

### Implementation Process

**Steps:**

1. **Select Prompt:**
    For this assessment, the prompt under the name "Bake to JSON" was selected from the prompt library. ![prompt image]()
2. **Obtain the Code:**
    The code was obtained from ai studio, by using the "Get Code" option. The code was the pasted int a python file named [`ai.py`](./ai.py).
3. **Obtain API KEY:**
    - The API key was obtained from the ai studio website.
    - The API key was used under the name `GEMINI_API_KEY` in the code.
4. **Develop the Web Interface:**
  - Created a web interface using Python with Dash.
  - This interface allows users to generate regex they wanted.
  - The web interface can be accessed at `http://localhost:8050/`.
  - The env vars `PORT` can be used to change the port on which the application runs. 

5. **Build the Docker image:**

   ```bash
   docker build -t bake-to-json .
   ```

6. **Run the Docker container:**

   ```bash
   docker run -p 8050:8050 bake-to-json
   ```

   This will start the Dash application on port 8050.

7. **Access the application:**

   Open http://localhost:8050 in your web browser to interact with the recipe extraction app.

**Additional Notes:**

* This project is a basic example and can be extended to include features like:
   - Support for different image formats.
   - Error handling for invalid images or API failures.
   - More advanced recipe parsing and formatting.
* Remember to replace `"INSERT_INPUT_HERE"` in `ai.py` with an empty string or any other relevant prompt for the model.
