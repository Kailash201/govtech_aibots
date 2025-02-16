## Technical Assignment

### Building the docker container

1. Ensure your terminal is in the directory of where docker-compose.yml and dockerfile is.
2. Create a .env file to hold your api key for the openAI. Your .env file should look like this:
<pre>OPENAI_API_KEY=YOUR_API_KEY</pre>
3. Run the following command to build the container: 
<pre>docker compose up --build</pre>
4. The compose will build both the app and mongodb image
5. The app will be running on localhost:8000
6. Note: The build process may take long as it is instaling libreoffice and tesseract, which may take awhile.

### Running and Testing the App
1. Client code is given in the root directory, it has 5 functions, each function corresponding to one endpoint.
2. If want to add your own file to the agent, add your file into the root directory and write the appropriate filepath in the function found in the **client.py**


