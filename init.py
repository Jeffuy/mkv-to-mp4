import os
import ffmpeg

def convert_mkv_to_mp4(directory):
    # Recorre todos los archivos de la carpeta dada
    for filename in os.listdir(directory):
        if filename.endswith(".mkv"):
            # Construir ruta completa del archivo
            input_path = os.path.join(directory, filename)
            output_path = os.path.splitext(input_path)[0] + ".mp4"

            try:
                # Ejecuta la conversión utilizando NVENC para la GPU de NVIDIA
                (
                    ffmpeg
                    .input(input_path)
                    .output(
                        output_path,
                        vcodec='h264_nvenc',
                        video_bitrate='2M',
                        preset='fast',
                        profile='baseline',
                        pix_fmt='yuv420p',  # Formato de píxeles ampliamente compatible
                        acodec='aac',
                        audio_bitrate='128k',
                        movflags='faststart'  # Optimiza para reproducción en línea
                    )
                    .run()
                )
                print(f"Conversión exitosa: {filename} -> {os.path.basename(output_path)}")
            except ffmpeg.Error as e:
                print(f"Error al convertir {filename}: {str(e)}")

if __name__ == "__main__":
    # Especificá la carpeta que querés usar
    directory = input("Ingresa la ruta de la carpeta que contiene los archivos .mkv: ")
    if os.path.isdir(directory):
        convert_mkv_to_mp4(directory)
    else:
        print("La ruta especificada no es una carpeta válida.")
