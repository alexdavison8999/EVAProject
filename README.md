<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]



<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/KroegerP/EVAProject">
    <img src="EXPOFILES/evaFace4Home.png" alt="Logo" width="80" height="80">
  </a>

<h3 align="center">EVA 2.0</h3>

  <p align="center">
    Software for the Elderly Virtual Asisstant, a device for managing medication intake.
    <br />
    <a href="https://github.com/KroegerP/EVAProject"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/KroegerP/EVAProject">View Demo</a>
    ·
    <a href="https://github.com/KroegerP/EVAProject/issues">Report Bug</a>
    ·
    <a href="https://github.com/KroegerP/EVAProject/issues">Request Feature</a>
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

[![Product Name Screen Shot][product-screenshot]](https://example.com)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

* [![Python][Python]](https://www.python.org/)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- GETTING STARTED -->
## Getting Started

There are a few prerequisites to installing EVA locally. Most of the initial setup can be 
performed via the 4 scripts in the  

### Prerequisites

This is an example of how to list things you need to use the software and how to install them.

You must be in a linux environment for the install scripts to work.

### Installation

1. Clone the repo
   ```sh
   git clone https://github.com/KroegerP/EVAProject.git
   ```
2. Run the install scripts for the dependencies
   ```sh
   ./scripts/buildDeps_1.sh
   ```
3. Install pyenv to install python
   ```sh
   ./scripts/installPyEnv_2.sh
   ```
4. Download poetry and create virtual environment
   ```sh
   ./scripts/createPoetryEnv_3.sh
   ```
5. Download python dependencies
   ```sh
   ./scripts/collectPythonDeps_4.sh
   ```
7. Initialize the database
   ```sh
   ./scripts/initdb_5.sh
   ```
8. Activate your virtual environment (If not started)
   ```sh
   source scripts/activate.sh
   ```
9. More steps to come...

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

<!-- _For more examples, please refer to the [Documentation](https://example.com)_ -->

<!-- <p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- ROADMAP -->
<!-- ## Roadmap

- [ ] Feature 1
- [ ] Feature 2
- [ ] Feature 3
    - [ ] Nested Feature

See the [open issues](https://github.com/KroegerP/EVAProject/issues) for a full list of proposed features (and known issues). -->

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTRIBUTING -->
<!-- ## Contributing

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- CONTACT -->
## Contact

Peter Kroeger - [@HeyDotPeter](https://twitter.com/HeyDotPeter) - peter14mail@gmail.com

Project Link: [https://github.com/KroegerP/EVAProject](https://github.com/KroegerP/EVAProject)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

* Original Code for EVA by Alex Davison - [https://github.com/alexdavison8999/EVAProject](https://github.com/alexdavison8999/EVAProject)

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/KroegerP/EVAProject.svg?style=for-the-badge
[contributors-url]: https://github.com/KroegerP/EVAProject/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/KroegerP/EVAProject.svg?style=for-the-badge
[forks-url]: https://github.com/KroegerP/EVAProject/network/members
[stars-shield]: https://img.shields.io/github/stars/KroegerP/EVAProject.svg?style=for-the-badge
[stars-url]: https://github.com/KroegerP/EVAProject/stargazers
[issues-shield]: https://img.shields.io/github/issues/KroegerP/EVAProject.svg?style=for-the-badge
[issues-url]: https://github.com/KroegerP/EVAProject/issues
[license-shield]: https://img.shields.io/github/license/KroegerP/EVAProject.svg?style=for-the-badge
[license-url]: https://github.com/KroegerP/EVAProject/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/peter-kroeger
[product-screenshot]: EXPOFILES/evaFace4Home.png