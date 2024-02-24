import argparse
import os
from logzero import logger
from internals.image import process_image
try:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "raster",
        help="GEOTIFF",
        type=str
    )
    parser.add_argument(
        "--output",
        nargs='?',
        default=False,
        help="Nome do arquivo de saida.\nDefault \{nome_do_tiff\}-out.png",
        type=str
    )
    args=parser.parse_args()
    
    if not args.output:
        nome_geo_tiff=os.path.splitext(args.raster)[0]
        args.output=f"{nome_geo_tiff}-out.png"
    
    process_image(
        input_path=args.raster,
        output_path=args.output
    )
    
except Exception as err:
    logger.error(err)
