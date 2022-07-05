<h1 align="center">
  <br>
  <picture>
    <source
      srcset="https://raw.githubusercontent.com/cybersecsi/ews-nmap/main/assets/logo-dark-mode.png"
      media="(prefers-color-scheme: dark)"/>
    <img src="https://raw.githubusercontent.com/cybersecsi/ews-nmap/main/assets/logo-light-mode.png" alt= "ews-nmap" width="300px">
  </picture>
</h1>
<p align="center">
    <b>ews-nmap</b>
<p>

<p align="center">
  <a href="https://github.com/cybersecsi/ews-nmap/blob/main/README.md"><img src="https://img.shields.io/badge/Documentation-complete-green.svg?style=flat"></a>
  <a href="https://github.com/cybersecsi/ews-nmap/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-Apache2-blue.svg"></a>
</p>


##  Getting Started  
Run ``nmap``  and save XML output, for example:   
```  
nmap -sV -oX <nmap_output.xml>  
```  

### Example
The output of the tool is like the following:
![Execution example](https://github.com/cybersecsi/ews-nmap/raw/main/assets/usage.png)

### Install & Run
To install it you just need to run:
```
pip install ews-nmap
```

### Run without installing

#### Prerequisites   
Install dependencies by using the following command:   
``` 
pip install -r requirements.txt
chmod +x ewsnmap/ewsnmap.py
```

```   
Usage: ewsnmap.py NMAP_XML_FILE <flags>
  optional flags:        --output-dir | --output
  
```  

To run the parser:   
```  
ewsnmap.py <nmap_output.xml>   
``` 

the script will generate a file ``output.txt`` in ``ewsnmap-output`` dir. If you want to set the output file and the output dir:   
```   
ewsnmap.py <nmap_output.xml>  --output <output_csv_file> --dir <output_directory>
``` 

## Contributing

Contributions are what make the open source community such an amazing place to be learn, inspire, and create. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## Credits
``ews-nmap`` is proudly developed [@SecSI](https://secsi.io) by:
- [Angelo Delicato](https://github.com/thelicato)

## License
Distributed under Apache 2 License. See `LICENSE` for more information. 