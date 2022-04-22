# Image Coordinate Calculator

## Instructions
1. Create virtual environment
    ```
     python -m venv venv_name
    ```

2. Activate virtual environment
    
    Mac or Linux (bash/zsh)
    ```
    source venv_name/bin/activate
    ```

    Windows (cmd)
    ```
    venv_name\Scripts\activate.bat
    ```

3. Change to directory with Dockerfile

4. Build Docker image
    ```
    docker build -t image_name .
    ```

5. Run Dockerfile
    ```
    docker run -p 5000:5000 image_name
    ```

6. Open Flask web app
   
   Go to localhost:5000 on a web browser