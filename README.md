## tifMap2png
### Descrição
  Simples ferramenta para converter geotiffs float32 para PNG aplicando um mapa de cor na imagem
### Exemplo de saida
![exemplo_saida](https://raw.githubusercontent.com/siapesq/tifMap2png/master/docs/assets/exemplo_saida.png)
### Uso
      python tifMap2png input.tiff output.png
      
### Como utilizar com venv
  * Clone o  repositorio

        git clone https://github.com/siapesq/tifMap2png.git
  * Check se o GDAL foi instalado corretamente

        gdalinfo --version
    
  * Iniciei o virtual enviroment

        python - m venv .venv
  
  * Instale as dependências

        pip install -r requirements.txt
  
  * Rode o programa

        python tifMap2png input.tiff output.png
    
### Dependências
**É necessário ter o [gdal](https://gdal.org) e o [opencv](https://opencv.org) instalados**
* [opencv-python](https://pypi.org/project/opencv-python)
* logzero
* gdal  
* wheel
* numpy
  
