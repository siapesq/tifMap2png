from image import process_image

# Define o caminho para a pasta 'dashboard'
input_folder = "/home/ubuntu/map-api/dashboard/"

# Obtém todos os arquivos TIFF dentro da pasta 'dashboard'
input_files = glob(os.path.join(input_folder, '*.tif'))

output_folder = "/home/ubuntu/map-api/png"

for input_file in input_files:
    try:
        output_file = os.path.join(output_folder, os.path.basename(input_file).replace('.tif', '.png'))
        process_image(input_file, output_file)
    except Exception as e:
        print(f"Erro ao processar a imagem {input_file}: {e}")
