# ESRGAN-FastAPI
## Fast way to use it with default settings
```bash
git clone https://github.com/gdagil/ESRGAN-FastAPI.git
cd ESRGAN-FastAPI
sudo docker compose up
```
### Usung the image (environment variables)
* ESRGAN - all settings you can find in original [repo](https://github.com/xinntao/Real-ESRGAN)
	* ESRGAN_MODEL_NAME
	* ESRGAN_TILE
	* ESRGAN_TILE_PAD
	* ESRGAN_PRE_PAD
	* ESRGAN_OUTPUT_SCALE
	* ESRGAN_FP32
	* ESRGAN_FACE_ENCHANCE
	* ESRGAN_ALPHA_UPSAMPLER
	* ESRGAN_GPU_ID
