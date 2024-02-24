import cv2
import os
from logzero import logger
from osgeo import gdal
gdal.UseExceptions()
gdal.SetConfigOption('GDAL_PAM_ENABLED', 'NO')
def convert_tiff_png(input_path:str)->str:
    try:
        logger.info(f'Converting {input_path} to PNG')
        temp_path=os.path.splitext(input_path)[0]+'.png'
        dataset = gdal.Open(input_path)
        if dataset is None:
            raise Exception("Erro ao abrir o arquivo GeoTIFF.")
        options = gdal.TranslateOptions(
            format="PNG",
            outputType=gdal.GDT_Byte,
            bandList=[1],
            scaleParams=[[0.000, 1.000, 0, 255]],
            noData=1
        )
        gdal.Translate(temp_path, dataset, options=options)
        dataset = None
        return temp_path
    except Exception as e:
        raise e

def apply_color_map_to_png(
    input_path:str, 
    output_path:str, 
    color_map:int=cv2.COLORMAP_TURBO
):
    try:
        logger.info(f'Applying color map to {input_path}')
        imagem_pb = cv2.imread(input_path, cv2.IMREAD_GRAYSCALE)
        mapa_cores = color_map
        imagem_colorida = cv2.applyColorMap(imagem_pb, mapa_cores)
        logger.info(f'Writing {output_path} to disk.')
        written=cv2.imwrite(output_path, imagem_colorida)
        if not written:
            raise Exception('Image was not written to the output path.')
        
    except Exception as e:
        raise e

def process_image(
    input_path:str, 
    output_path:str
):
    try:
        logger.info(f'Processing {input_path}')
        png_gray=convert_tiff_png(input_path)
        apply_color_map_to_png(png_gray, output_path)
        logger.info(f'Processing Finished {input_path} output at {output_path}')
        logger.info(f'Removing {png_gray}')
        os.remove(png_gray)
    except Exception as e:
        raise e
