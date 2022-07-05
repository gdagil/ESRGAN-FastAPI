import os, shutil, cv2, json, uuid
import torch, numpy as np

from fastapi import FastAPI, UploadFile


def file_meta(image:UploadFile, configs):
    filename, ext = image.filename.split(".")
    encode_name = uuid.uuid5(uuid.NAMESPACE_DNS, (str(json.dumps(configs.dict())) + filename))
    save_path = f"data/upped/{encode_name}"
    return save_path, ext

    
    
def ESRGAN_upscale(image:UploadFile, app:FastAPI) -> str:    
    save_path, ext = file_meta(image, app.state.ESRGAN_config)

    if not os.path.exists(f"{save_path}.{ext}"):
        with open(f"data/raw/{image.filename}", "wb") as buffer:
            shutil.copyfileobj(image.file, buffer)  
        img = cv2.imread(f"data/raw/{image.filename}", cv2.IMREAD_UNCHANGED)
        if len(img.shape) == 3 and img.shape[2] == 4:
            img_mode = 'RGBA'
        else:
            img_mode = None 
        output = None
        try:
            if app.state.ESRGAN_config.face_enhance:
                _, _, output = app.state.ESRGAN.enhance(img, has_aligned=False, only_center_face=False, paste_back=True)
            else:
                output, _ = app.state.ESRGAN.enhance(img, outscale=app.state.ESRGAN_config.out_scale)
        except RuntimeError as error:
            print('Error', error)
            print('If you encounter CUDA out of memory, try to set --tile with a smaller number.')  
        if img_mode == 'RGBA':  # RGBA images should be saved in png format
            ext = 'png' 
        print(f"{save_path}.{ext}")
        cv2.imwrite(f"{save_path}.{ext}", output)
    
    return f"{save_path}.{ext}"