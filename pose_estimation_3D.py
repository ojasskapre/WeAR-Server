import os


def pose_estimation_3d(filepath):
	os.system(f'python src/openpose_3dpose_sandbox.py --camera_frame --residual --batch_norm --dropout 0.5 --max_norm --evaluateActionWise --use_sh --epochs 200 --load 4874200 --pose_estimation_json {filepath} --write_gif --gif_fps 24')
	