import boto3
import os
from image import process_image

# Define as credenciais da AWS
aws_access_key_id = ''
aws_secret_access_key = ''

# Cria uma sessão com as credenciais especificadas
session = boto3.session.Session(
    aws_access_key_id=aws_access_key_id,
    aws_secret_access_key=aws_secret_access_key
)

# Cria um cliente S3 com a sessão configurada
s3_client = session.client('s3')

# Define o nome do bucket da AWS
bucket_name = 'tifs-siapesq'

# Lista todos os objetos no bucket
response = s3_client.list_objects_v2(Bucket=bucket_name)

# Obtém todos os objetos com a extensão '.tif'
input_files = [obj['Key'] for obj in response.get('Contents', []) if obj['Key'].endswith('.tif')]

# Define o caminho para a pasta onde os arquivos PNG serão salvos
output_folder = "/home/ubuntu/png"

# Cria o diretório de saída se ainda não existir
os.makedirs(output_folder, exist_ok=True)

for input_file in input_files:
    try:
        # Define o caminho completo do arquivo de saída
        output_file = os.path.join(output_folder, os.path.basename(input_file).replace('.tif', '.png'))
        
        # Faz o download do arquivo TIFF do bucket
        s3_client.download_file(bucket_name, input_file, output_file)
        
        # Processa a imagem - agora usando o caminho local do arquivo baixado
        process_image(output_file)  # Ajuste aqui para usar output_file
        
    except Exception as e:
        print(f"Erro ao processar a imagem {input_file}: {e}")

