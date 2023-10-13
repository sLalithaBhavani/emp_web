# from google.cloud import storage
# from picamera import PiCamera
# import io
# import os
# import datetime

# # Replace with your own values
# bucket_name = "emp_frame"
# credentials_path = "/home/pi/Downloads/cloudkarya-internship-415b6b4ef0ff.json"
# company_name = "CloudKarya"
# image_extension = ".jpg"
# #local_image_directory = "/home/pi/Desktop/sendcaps"  


# client = storage.Client.from_service_account_json(credentials_path)

# # Get the bucket reference
# bucket = client.bucket(bucket_name)

# camera = PiCamera()
# camera.resolution = (1080, 720)  # Set the desired resolution

# while True:
#     now = datetime.datetime.now()
#     date_str = now.strftime("%Y%m%d")
#     time_str = now.strftime("%H%M%S")

#     image_filename = f"{company_name}_{date_str}_{time_str}_Entry_{image_extension}"
   

#     image_stream = io.BytesIO()
#     camera.capture(image_stream, format="jpeg")

   
#     image_stream.seek(0)
#     blob = bucket.blob(image_filename)
#     blob.upload_from_file(image_stream, content_type="image/jpeg")

#     print(f"Image {image_filename} uploaded to {bucket_name}")