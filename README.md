

# Drowsiness Detection System

This project implements a drowsiness detection system using a webcam. The system utilizes computer vision techniques to monitor a person's eyes and detect signs of drowsiness in real-time.




## Requirements
Make sure you have the following dependencies installed:

- Python 
- OpenCV (cv2)
- dlib
- NumPy
- Flask
- Pygame
## Installation

Clone this repository to your local machine:

1. bash
```Git
 git clone https://github.com/Shashivadan/drowsiness-detection.git
```
2. Install the required Python packages. You can use pip to install them:
```python
pip install -r requirements.txt
```
3. Download the shape predictor model file from the dlib website:

- Visit: http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2
- Extract the compressed file to the project directory.
- Rename the extracted file to shape_predictor_68_face_landmarks.dat.

## Usage

1. Run the Python script `main.py`:
```python
python main.py
```
2. Open a web browser and visit http://localhost:5000.
3. The webcam feed will be displayed with a drowsiness detection overlay.
4. If drowsiness is detected, a warning sound will play and a warning message will be displayed on the screen.


## Customization

- You can modify the drowsiness detection parameters by adjusting the `ear_thresh` value in the `generate_frames` function of `main.py`.  This determines the number of consecutive frames with drowsiness detection before triggering the warning.
- You can customize the HTML templates in the templates folder to change the appearance of the web interface.
## Contributing

Contributions to this project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.


## Acknowledgements

- The dlib library: http://dlib.net/
- OpenCV: https://opencv.org/
- Flask: https://flask.palletsprojects.com/
- Pygame: https://www.pygame.org/

## Contact

For any inquiries or questions, please contact shashivadan99@gmail.com.

Feel free to customize this README to provide additional information or make it more specific to your project.

