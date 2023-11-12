#!/usr/bin/env python3
import io, sys, os
import requests
from PyPDF2 import PdfFileReader
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# User Agent (APP: Chrome 111, OS: Linux x84_64)
UserAgent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36'

def main(url):
    print ("[+] Obteniendo datos...\n")

    try:
        # Obteniendo Bytes de fichero remoto
        response = requests.get(url, headers={'User-Agent':UserAgent}, verify=False)
        #Almacenando los Bytes en memoria
        pdf_data = io.BytesIO(response.content)
        # Obteniendo los metadatos
        pdf = PdfFileReader(pdf_data)
        metadata = pdf.getDocumentInfo()

        print ("Metadados de: {}\n".format(os.path.basename(url)))

        for info in metadata:
            print (info.split('/')[1] + ": " + metadata[info])

    except Exception as ex:
        print (str(ex))

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print ("Metapdf 0.1v\n")
        print ("\n{} <URL>\n".format(sys.argv[0]))

    else:
        if sys.argv[1] in ['-h', '--help']:
            print ("""
                _                 _  __ 
 _ __ ___   ___| |_ __ _ _ __   __| |/ _|
| '_ ` _ \ / _ \ __/ _` | '_ \ / _` | |_ 
| | | | | |  __/ || (_| | |_) | (_| |  _|
|_| |_| |_|\___|\__\__,_| .__/ \__,_|_|  
                        |_|              
        Por: Alex Gonzales Deheza

USO:
                   
    metapdf.py https://site.com/files/file.pdf
                   
            """)
            exit

        else:
            main(sys.argv[1])

