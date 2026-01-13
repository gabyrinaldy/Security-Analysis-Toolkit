from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS

def get_decimal_from_dms(dms, ref):
    """Converte coordenadas Graus, Minutos e Segundos para Decimal."""
    degrees = dms[0]
    minutes = dms[1] / 60.0
    seconds = dms[2] / 3600.0
    if ref in ['S', 'W']:
        return -float(degrees + minutes + seconds)
    return float(degrees + minutes + seconds)

def get_image_metadata(image_path):
    try:
        image = Image.open(image_path)
        info = image._getexif()
        if info is None:
            return "Nenhum metadado EXIF encontrado."

        metadata = {}
        gps_info = {}

        for tag, value in info.items():
            decoded = TAGS.get(tag, tag)
            if decoded == "GPSInfo":
                # Decodifica as tags internas de GPS
                for t in value:
                    sub_tag = GPSTAGS.get(t, t)
                    gps_info[sub_tag] = value[t]
            else:
                metadata[decoded] = value
        
        # Se houver GPS, gera o link do Google Maps
        if gps_info:
            try:
                lat = get_decimal_from_dms(gps_info['GPSLatitude'], gps_info['GPSLatitudeRef'])
                lon = get_decimal_from_dms(gps_info['GPSLongitude'], gps_info['GPSLongitudeRef'])
                metadata['Google_Maps_Link'] = f"https://www.google.com/maps?q={lat},{lon}"
            except KeyError:
                metadata['GPS'] = "Dados de GPS incompletos."

        return metadata
    except Exception as e:
        return f"Erro: {e}"

def display_metadata(metadata):
    if isinstance(metadata, str):
        print(f"\n[!] {metadata}")
    else:
        print(f"\n{'TAG':<25} | {'VALOR'}")
        print("-" * 60)
        for tag, value in metadata.items():
            if not isinstance(value, bytes):
                print(f"{tag:<25} | {value}")