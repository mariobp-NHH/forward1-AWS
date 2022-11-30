import secrets
import os
from PIL import Image
from webse import application
import boto3
from botocore.exceptions import NoCredentialsError
import base64
import io
import os
import secrets

# # For the GitHub:
BUCKET="forward-v1"
s3_r = boto3.resource('s3')


# def read_image(image_filename):
#     im = Image.open(s3_r.Bucket(BUCKET).Object(image_filename).get().get('Body'))
#     data = io.BytesIO()
#     im.save(data, im.format)
#     encoded_img_data = base64.b64encode(data.getvalue())
#     return encoded_img_data.decode('utf-8')


def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext

    output_size = (125, 125)
    i = Image.open(form_picture)
    i.thumbnail(output_size)

    in_mem_file = io.BytesIO()
    i.save(in_mem_file, format=i.format)

    in_mem_file.seek(0)

    s3_r.Bucket(BUCKET).put_object(Key=picture_fn, Body=in_mem_file)

    return picture_fn

# #For the computer original:
# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext
#     picture_path = os.path.join(application.root_path, 'static/profile_pics', picture_fn)

#     output_size = (125, 125)
#     i = Image.open(form_picture)
#     i.thumbnail(output_size)
#     i.save(picture_path)

#     return picture_fn

# #For the computer bucket s3:
# ACCESS_KEY="AKIAU5ZFCCSCH3KFDZGM"

# SECRET_KEY="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"

# BUCKET="forward-v1"

# s3_r = boto3.resource('s3',
#                       aws_access_key_id=ACCESS_KEY,
#                       aws_secret_access_key=SECRET_KEY)

# def read_image(image_filename):
#     im = Image.open(s3_r.Bucket(BUCKET).Object(image_filename).get().get('Body'))
#     data = io.BytesIO()
#     im.save(data, im.format)
#     encoded_img_data = base64.b64encode(data.getvalue())
#     return encoded_img_data.decode('utf-8')


# def save_picture(form_picture):
#     random_hex = secrets.token_hex(8)
#     _, f_ext = os.path.splitext(form_picture.filename)
#     picture_fn = random_hex + f_ext

#     output_size = (125, 125)
#     i = Image.open(form_picture)
#     i.thumbnail(output_size)

#     in_mem_file = io.BytesIO()
#     i.save(in_mem_file, format=i.format)

#     in_mem_file.seek(0)

#     s3_r.Bucket(BUCKET).put_object(Key=picture_fn, Body=in_mem_file)

#     return picture_fn
