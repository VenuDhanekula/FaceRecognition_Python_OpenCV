[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]
[![Instagram][Instagram-shield]][Instagram-url]



<!-- PROJECT LOGO -->
<br />
<p align="left">
  <a >
    <img src="https://github.com/VenuDhanekula/LogoImages/blob/main/OpenCV_Logo.png" alt="Logo" width="200">
  </a>
</p>

<!-- COLORDETECTION RASPBERRYPI PYTHON -->
# FaceRecognition In RaspberryPi Using Python

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <br />
  <ol>
    <li>
      <a href="#project-details">Project Details</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#opencv-installation">OpenCV Installation</a></li>
        <li><a href="#clone-project">Clone Project</a></li>
      </ul>
    </li>
    <li><a href="#contact-with-me">Contact</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## Project Details

Steps To Be Followed

* First, Run the createDataset python file which will help to create the Images of the respective face with an id.
  ```sh
   File Name: 1.CreateDataset.py
   ```
* Secondly, Run the trainDataset python file which will help to train all the faces with respective to an id's initialized.
  ```sh
   File Name: 2.trainDataset.py
   ```
* Finally, Run the recognizeData python file which will help to recognize the face in the Images with the help of id's that are assigned.
  ```sh
   File Name: 3.recognizeData.py
   ```

  <a >
    <img src="Images/SingleColorDetection.png" alt="singleColorDetection" width="100%">
  </a> 
  
Multiple Color Detection
* Below image gives the output information of the Multiple Color Detection code provided in the above folder. Colors will be detected and made a border and lable around.

  <a >
    <img src="Images/MultipleColorDetection.png" alt="singleColorDetection" width="33%">
  </a> 



### Built With

Here are the list of the major components that are required to built the above project.
You will be directed to the respective page for purchase / learning.
* [Raspberry Pi](https://www.raspberrypi.org/products/)
* [Pi Camera](https://www.raspberrypi.org/products/camera-module-v2/)
* [Python](https://www.python.org/)

Python Libraries Used.
* [NumPy](https://numpy.org/)
* [Pillow](https://pypi.org/project/Pillow/)
* [Open CV](https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html)



<!-- GETTING STARTED -->
## Getting Started

This is how you can follow the instructions on setting up the project and running the file in the local system.

### OpenCV Installation

1. One line command promt installer.
   ```sh
   pip install opencv-python
   pip install opencv-contrib-python
   ```
2. Complete installation (Below mentioned link gives the detailed information of installing the OpenCV in Raspberry Pi)
   <br />
   
   * [Installation Link](https://robu.in/how-to-install-opencv-in-raspberry-pi/)
   
   <br />
3. Check the Open CV version (Output will be the installed version of the Open CV (i.e., 3.0.0 or 3.1.2)
   ```sh
   import cv2
   print(cv2.__version__)
   ```
### Clone Project

1. get a local copy up and running follow cloning steps.

   ```sh
   git clone https://github.com/VenuDhanekula/FaceRecognition_RaspberryPi_Python.git
   ```
   


<!-- CONTACT -->
## Contact With Me

<p align="left">
<a href="https://instagram.com/venu_abhi" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/instagram.svg" alt="venu_abhi" height="30" width="40" /> Instagram</a>
  
<br />
  
<a href="https://linkedin.com/in/venu-dhanekula-706518a7" target="blank"><img align="center" src="https://raw.githubusercontent.com/rahuldkjain/github-profile-readme-generator/master/src/images/icons/Social/linked-in-alt.svg" alt="venu-dhanekula-706518a7" height="30" width="40" /> Linkedin</a>
</p>



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- MARKDOWN LINKS & IMAGES -->
[license-shield]: https://github.com/VenuDhanekula/LogoImages/blob/main/LicenceMIT_Logo.svg
[license-url]: https://github.com/VenuDhanekula/ColorDetection_RaspberryPi_Python/blob/main/LICENSE

[linkedin-shield]: https://github.com/VenuDhanekula/LogoImages/blob/main/LinkedIn_Logo.svg
[linkedin-url]: https://linkedin.com/in/venu-dhanekula-706518a7

[Instagram-shield]: https://github.com/VenuDhanekula/LogoImages/blob/main/Instagram_Logo.svg
[Instagram-url]: https://instagram.com/venu_abhi
