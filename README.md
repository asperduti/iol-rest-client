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
<p align="center">
  <a href="https://github.com/asperduti/iol-rest-client">
    <img src="images/logo.png" alt="Logo" width="80" height="80">
  </a>

  <h3 align="center">IoL Python REST Client</h3>

  <p align="center">
    Python REST client to interact with InvertirOnline REST API. 
    <br />
    <a href="https://github.com/asperduti/iol-rest-client"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="https://github.com/asperduti/iol-rest-client">View Demo</a>
    ·
    <a href="https://github.com/asperduti/iol-rest-client/issues">Report Bug</a>
    ·
    <a href="https://github.com/asperduti/iol-rest-client/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Installation](#installation)
- [Usage](#usage)
- [Roadmap](#roadmap)
- [Contributing](#contributing)



<!-- ABOUT THE PROJECT -->
## About The Project

Python REST client to interact with [InvertirOnline REST API](https://api.invertironline.com/). 

<!-- GETTING STARTED -->
## Getting Started

### Installation
 
1. Install the package from GitHub
```sh
$ pip install git+git://github.com/asperduti/iol-rest-client.git#egg=iol_rest_client
```

<!-- USAGE EXAMPLES -->
## Usage

It's really simple to use, this is an example:

```python
from iol_rest_client import RestClient

client = RestClient(username="YOUR_USERNAME", password="YOUR_PASSWORD")

print(client.get_estado_cuenta())
print(client.get_operaciones())
```

_For more examples, please refer to [examples](https://github.com/asperduti/iol-rest-client/tree/master/examples)_


<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/asperduti/iol-rest-client/issues) for a list of proposed features (and known issues).


<!-- CONTRIBUTING -->
## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


> **Disclaimer**<a name="disclaimer" />: Please Note that this is a research project. I am by no means responsible for any usage of this tool. Use on your own behalf. I'm also not responsible if your accounts get banned due to extensive use of this tool.


<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[contributors-shield]: https://img.shields.io/github/contributors/asperduti/iol-rest-client.svg?style=flat-square
[contributors-url]: https://github.com/asperduti/iol-rest-client/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/asperduti/iol-rest-client.svg?style=flat-square
[forks-url]: https://github.com/asperduti/iol-rest-client/network/members
[stars-shield]: https://img.shields.io/github/stars/asperduti/iol-rest-client.svg?style=flat-square
[stars-url]: https://github.com/asperduti/iol-rest-client/stargazers
[issues-shield]: https://img.shields.io/github/issues/asperduti/iol-rest-client.svg?style=flat-square
[issues-url]: https://github.com/asperduti/iol-rest-client/issues
[license-shield]: https://img.shields.io/github/license/asperduti/iol-rest-client.svg?style=flat-square
[license-url]: https://github.com/asperduti/iol-rest-client/blob/master/LICENSE
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=flat-square&logo=linkedin&colorB=555
[linkedin-url]: https://linkedin.com/in/arielsperduti
[product-screenshot]: images/screenshot.png
