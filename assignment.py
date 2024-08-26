#Convert an audio file to MP4 format using a placeholder image.

import subprocess
def audio_to_mp4(audio_file, image_file, output_file):
    try:
        # Construct the ffmpeg command
        command = [
            'ffmpeg',
            '-loop', '1',              # Loop the image
            '-i', image_file,          # Input image file
            '-i', audio_file,          # Input audio file
            '-c:v', 'libx264',         # Video codec
            '-c:a', 'aac',             # Audio codec
            '-b:a', '192k',            # Audio bitrate
            '-short',                  # Stop encoding when the audio ends
            output_file                # Output file
        ]
        
        # Run the ffmpeg command
        result = subprocess.run(command, capture_output=True, text=True)
        
        # Check for errors
        if result.returncode != 0:
            print(f"Error: {result.stderr}")
        else:
            print(f"Conversion successful: {output_file}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Example usage
    audio_file = 'path/to/your/audio_file.mp3'   # Replace with your audio file path
    image_file = 'path/to/your/image_file.jpg'   # Replace with your image file path
    output_file = 'path/to/your/output_file.mp4' # Replace with desired output file path
    
    audio_to_mp4(audio_file, image_file, output_file)
