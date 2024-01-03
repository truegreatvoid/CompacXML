import os
import zipfile
from glob import glob

def compactar_xml(diretorio_origem, tamanho_grupo, diretorio_destino):
    if not os.path.exists(diretorio_destino):
        os.makedirs(diretorio_destino)

    xml_files = glob(os.path.join(diretorio_origem, '*.xml'))
    grupos = [xml_files[i:i + tamanho_grupo] for i in range(0, len(xml_files), tamanho_grupo)]

    for i, grupo in enumerate(grupos):
        nome_zip = os.path.join(diretorio_destino, f'grupo_{i + 1}.zip')
        with zipfile.ZipFile(nome_zip, 'w') as zipf:
            for xml_file in grupo:
                zipf.write(xml_file, os.path.basename(xml_file))
    print(f'Compactação concluída. {len(xml_files)} arquivos XML divididos em {len(grupos)} grupos.')

diretorio_origem = r'C:\Users\tiago.xavier\Desktop\Fiscal\CompacXML\SOLICITACAO_5566\SOLICITACAO_5566'
tamanho_grupo = 4000
diretorio_destino = r'C:\Users\tiago.xavier\Desktop\Fiscal\CompacXML\SOLICITACAO_5566'

compactar_xml(diretorio_origem, tamanho_grupo, diretorio_destino)
